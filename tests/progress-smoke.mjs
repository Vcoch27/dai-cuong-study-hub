// Exercise the real application module with a small DOM adapter. No user storage
// or running browser is touched; only fixture progress is supplied.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import vm from 'node:vm';

const raw=JSON.parse(await fs.readFile(new URL('../dist/data.json',import.meta.url),'utf8'));
const app=await fs.readFile(new URL('../dist/app.js',import.meta.url),'utf8');
const oldKey='dai-cuong-cnxh-v1';
const byId=Object.fromEntries(raw.questions.map(q=>[q.id,q]));

async function boot(initial={}){
 const memory=new Map(Object.entries(initial));
 let html='',buttons=[];
 const inert={scrollIntoView(){},focus(){}};
 const root={get innerHTML(){return html;},set innerHTML(value){
  html=value;buttons=[];
  for(const match of html.matchAll(/<button\b([^>]*)>/g)){
   const dataset={};
   for(const attr of match[1].matchAll(/\bdata-([a-z-]+)(?:="([^"]*)")?/g)){
    dataset[attr[1].replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase())]=attr[2]??'';
   }
   buttons.push({dataset,disabled:/\bdisabled\b/.test(match[1])});
  }
 }};
 const document={activeElement:null,addEventListener(){},
  querySelector(selector){return selector==='#app'?root:selector==='.search'?null:inert;},
  querySelectorAll(selector){
   const name=selector.match(/^\[data-([a-z-]+)\]$/)?.[1];
   if(!name)return [];
   const key=name.replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase());
   return buttons.filter(button=>Object.hasOwn(button.dataset,key));
  }
 };
 const context=vm.createContext({document,
  localStorage:{getItem:key=>memory.get(key)??null,setItem:(key,value)=>memory.set(key,value)},
  fetch:async()=>({ok:true,json:async()=>structuredClone(raw)}),setInterval(){},
 });
 const module=new vm.SourceTextModule(app+'\nexport {state,render,current,visibleQuestions,storageKey,previousExamScores};',{context});
 await module.link(()=>{throw Error('Unexpected import');});await module.evaluate();
 return {api:module.namespace,memory,document,get html(){return html;},
  click(selector,value){
   const found=document.querySelectorAll(selector).find(button=>value===undefined||Object.values(button.dataset).includes(value));
   assert(found&&!found.disabled,`Enabled button ${selector} ${value??''}`);found.onclick();
  }};
}

const first=raw.examForms[0];
const legacy={source:'doc',chapter:3,answers:{'doc-031':byId['doc-031'].answer},
 bookmarks:['doc-031','unknown-id'],mode:'exam',examId:'midterm-4',
 examAttempts:{[first.id]:{answers:Object.fromEntries(first.questionIds.map(id=>[id,byId[id].answer])),submittedAt:123},
 'midterm-4':{startedAt:Date.now(),answers:{},current:0,submittedAt:null}},
 examHistory:{[first.id]:[{score:20,submittedAt:100}]}};
const legacyJSON=JSON.stringify(legacy);
const page=await boot({[oldKey]:legacyJSON});
assert.equal(page.memory.get(oldKey),legacyJSON,'Original progress remains untouched');
assert.equal(Object.keys(page.api.state.answers).length,0,'Revised items start unanswered');
assert.equal(Object.keys(page.api.state.examAttempts).length,0,'Old attempts cannot continue with changed choices');
assert.deepEqual([...page.api.state.bookmarks],['doc-031']);
assert.equal(page.api.previousExamScores[first.id],30);
assert(page.html.includes('Bộ câu hỏi đã được biên tập lại'));
page.click('[data-review-notice-close]');
page.api.state.index=page.api.visibleQuestions().findIndex(q=>q.id==='doc-031');page.api.render();
assert(page.html.includes('Cải cách nghị trường'));
assert(!page.html.includes('answer-box'));
const wrong=String((byId['doc-031'].answer+1)%4);
page.click('[data-answer]',wrong);
assert(page.html.includes('answer-box error'));
assert(page.html.includes(byId['doc-031'].explanation));
assert(page.html.includes('evidence-card focused'));
page.click('[data-mode]','exam');
assert(page.html.includes('Trước biên tập · Cao nhất: 30/30'));
assert.equal(page.document.querySelectorAll('[data-exam-start]').length,8);
page.click('[data-exam-start]','midterm-8');
assert(page.html.includes('15:00'));
const form=raw.examForms[7],qid=form.questionIds[0];
page.click('[data-exam-choice]',String(byId[qid].answer));
assert(!page.html.includes('answer-box'));
const reloaded=await boot(Object.fromEntries(page.memory));
assert.equal(reloaded.api.state.examAttempts[form.id].answers[qid],byId[qid].answer);
assert(!reloaded.html.includes('Bộ câu hỏi đã được biên tập lại'));
reloaded.click('[data-exam-submit]');reloaded.click('[data-exam-confirm]');
assert(reloaded.html.includes('1/30 câu đúng'));
assert(reloaded.html.includes(byId[qid].explanation));
assert(reloaded.html.includes('evidence-card focused'));
assert.equal(reloaded.memory.get(oldKey),legacyJSON);
const fresh=await boot();
assert.equal(fresh.api.state.reviewNotice,false);
assert.equal(Object.keys(fresh.api.state.answers).length,0);
await boot({[oldKey]:'invalid json'});
console.log('PASS: legacy progress retained; revised practice, feedback, eight forms, timer, reload, submission and source review work');
