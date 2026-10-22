// Exercise the real application module with a small DOM adapter. No user storage
// or running browser is touched; only fixture progress is supplied.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import vm from 'node:vm';

const raw=JSON.parse(await fs.readFile(new URL('../dist/data.json',import.meta.url),'utf8'));
const app=await fs.readFile(new URL('../dist/app.js',import.meta.url),'utf8');
const oldKey='dai-cuong-cnxh-v1';
const byId=Object.fromEntries(raw.questions.map(q=>[q.id,q]));

async function boot(initial={}, {mobile=false,course='cnxh',data=raw}={}){
 const memory=new Map(Object.entries(initial));
 let html='',buttons=[],panels={};
 const events={};
 const window={location:{search:course==='bank'?'?course=hcm&track=bank':course==='hcm'?'?course=hcm':''},scrollX:0,scrollY:0,scrollTo({left=0,top=0}){this.scrollX=left;this.scrollY=Math.max(0,top);}};
 const inert={scrollIntoView(){},focus(){},showModal(){}};
 const root={get innerHTML(){return html;},set innerHTML(value){
  html=value;buttons=[];
  panels=Object.fromEntries(['.main','.sidebar','.evidence','.number-grid'].map(selector=>[selector,{scrollTop:0,scrollLeft:0,scrollHeight:2000,clientHeight:mobile?2000:700,
   getBoundingClientRect(){return {top:mobile?200-window.scrollY:64};}}]));
  for(const match of html.matchAll(/<button\b([^>]*)>/g)){
   const dataset={};
   for(const attr of match[1].matchAll(/\bdata-([a-z-]+)(?:="([^"]*)")?/g)){
    dataset[attr[1].replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase())]=attr[2]??'';
   }
   buttons.push({dataset,disabled:/\bdisabled\b/.test(match[1])});
  }
 }};
 const document={activeElement:null,addEventListener(name,handler){events[name]=handler;},
  querySelector(selector){
   if(selector==='#app')return root;
   if(selector==='.search')return null;
   if(panels[selector])return panels[selector];
   if(selector==='.question-card')return html.includes('class="question-card')?{...inert,getBoundingClientRect(){return {top:mobile?1064-window.scrollY:364-panels['.main'].scrollTop};}}:null;
   if(selector==='.exam-top')return html.includes('class="exam-top"')?{offsetHeight:58,getBoundingClientRect(){return {top:92,bottom:150};}}:null;
   return inert;
  },
  querySelectorAll(selector){
   const name=selector.match(/^\[data-([a-z-]+)\]$/)?.[1];
   if(!name)return [];
   const key=name.replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase());
   return buttons.filter(button=>Object.hasOwn(button.dataset,key));
  }
 };
 const context=vm.createContext({document,window,
  localStorage:{getItem:key=>memory.get(key)??null,setItem:(key,value)=>memory.set(key,value)},
  fetch:async url=>{assert.equal(url,course==='bank'?'/hcm-bank-data.json':course==='hcm'?'/hcm-data.json':'/data.json');return {ok:true,json:async()=>structuredClone(data)};},setInterval(){},
 });
 const module=new vm.SourceTextModule(app+'\nexport {state,render,current,visibleQuestions,storageKey,previousExamScores};',{context});
 await module.link(()=>{throw Error('Unexpected import');});await module.evaluate();
 return {api:module.namespace,memory,document,window,get html(){return html;},
  key(key){let prevented=false;events.keydown({key,preventDefault(){prevented=true;}});return prevented;},
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
page.document.querySelector('.main').scrollTop=210;
page.document.querySelector('.sidebar').scrollTop=130;
page.document.querySelector('.number-grid').scrollTop=95;
page.click('[data-answer]',wrong);
assert.equal(page.document.querySelector('.main').scrollTop,210,'Answer preserves main scroll after DOM replacement');
assert.equal(page.document.querySelector('.sidebar').scrollTop,130,'Answer preserves sidebar scroll');
assert.equal(page.document.querySelector('.number-grid').scrollTop,95,'Answer preserves number grid scroll');
assert(page.html.includes('answer-box error'));
assert(page.html.includes(byId['doc-031'].explanation));
assert(page.html.includes('evidence-card focused'));
page.click('[data-nav]','1');
assert.equal(page.document.querySelector('.question-card').getBoundingClientRect().top,76,'Next question aligns inside main panel');
assert.equal(page.document.querySelector('.sidebar').scrollTop,130);
page.document.querySelector('.main').scrollTop=240;
assert(page.key('1'));
assert.equal(page.document.querySelector('.main').scrollTop,240,'Keyboard answer preserves scroll');
assert(page.key('ArrowRight'));
assert.equal(page.document.querySelector('.question-card').getBoundingClientRect().top,76,'Keyboard navigation matches buttons');
page.click('[data-mode]','exam');
assert(page.html.includes('Trước biên tập · Cao nhất: 30/30'));
assert.equal(page.document.querySelectorAll('[data-exam-start]').length,8);
page.click('[data-exam-start]','midterm-8');
assert(page.html.includes('15:00'));
assert.equal(page.document.querySelector('.question-card').getBoundingClientRect().top,162,'Exam anchor leaves room for sticky timer and panel padding');
const form=raw.examForms[7],qid=form.questionIds[0];
page.document.querySelector('.main').scrollTop=260;
page.click('[data-exam-choice]',String(byId[qid].answer));
assert.equal(page.document.querySelector('.main').scrollTop,260,'Exam selection preserves scroll');
assert(!page.html.includes('answer-box'));
const reloaded=await boot(Object.fromEntries(page.memory));
assert.equal(reloaded.api.state.examAttempts[form.id].answers[qid],byId[qid].answer);
assert(!reloaded.html.includes('Bộ câu hỏi đã được biên tập lại'));
reloaded.click('[data-exam-submit]');reloaded.click('[data-exam-confirm]');
assert(reloaded.html.includes('1/30 câu đúng'));
assert(reloaded.html.includes(byId[qid].explanation));
assert(reloaded.html.includes(byId[qid].source.kind==='slide'?'data-slide-open':'evidence-card focused'));
assert.equal(reloaded.memory.get(oldKey),legacyJSON);
const fresh=await boot();
assert.equal(fresh.api.state.reviewNotice,false);
assert.equal(Object.keys(fresh.api.state.answers).length,0);
await boot({[oldKey]:'invalid json'});
const mobilePage=await boot({}, {mobile:true});
mobilePage.window.scrollY=720;
mobilePage.click('[data-answer]','0');
assert.equal(mobilePage.window.scrollY,720,'Mobile selection preserves page scroll');
mobilePage.click('[data-nav]','1');
assert.equal(mobilePage.document.querySelector('.question-card').getBoundingClientRect().top,12,'Mobile navigation aligns the question in the viewport');
const revisionKey=`dai-cuong-cnxh-${raw.questionRevision}`;
const retryFixture={source:'doc',chapter:0,index:0,mode:'quiz',reviewNoticeDismissed:true,
 answers:{'doc-001':(byId['doc-001'].answer+1)%4,'doc-002':(byId['doc-002'].answer+1)%4,'doc-003':byId['doc-003'].answer,'slide-001':byId['slide-001'].answer},
 bookmarks:['doc-001'],examHistory:{'midterm-1':[{score:23,submittedAt:5}]}};
const retryPage=await boot({[revisionKey]:JSON.stringify(retryFixture)});
assert.equal(retryPage.api.current().id,'doc-001');
assert(retryPage.html.includes('answer-box error'),'Old-schema completed items remain reviewable');
retryPage.click('[data-practice-retry]','question');
assert.equal(Object.keys(retryPage.api.state.answers).length,4,'Retry never clears completion');
assert.equal(retryPage.api.state.practiceAnswers['doc-001'],undefined);
assert(!retryPage.html.includes('answer-box'));
assert(!retryPage.html.includes('evidence-card focused'),'Retry hides source as well as answer');
const retryReload=await boot(Object.fromEntries(retryPage.memory));
assert.equal(retryReload.api.state.practiceAnswers['doc-001'],undefined,'Reload does not restore feedback during retry');
retryReload.click('[data-answer]',String(byId['doc-001'].answer));
assert.equal(retryReload.api.state.answers['doc-001'],byId['doc-001'].answer,'Latest result updates on retry');
assert.equal(Object.keys(retryReload.api.state.answers).length,4);
retryReload.click('[data-review]','wrong');
assert.deepEqual(retryReload.api.visibleQuestions().map(q=>q.id),['doc-002']);
retryReload.click('[data-practice-retry]','wrong');
assert.equal(retryReload.api.state.practiceAnswers['doc-002'],undefined);
assert.equal(Object.keys(retryReload.api.state.answers).length,4);
retryReload.click('[data-answer]',String(byId['doc-002'].answer));
assert.equal(retryReload.api.current().id,'doc-002','Corrected question stays visible for feedback');
assert(retryReload.html.includes(byId['doc-002'].explanation));
assert(retryReload.html.includes('1/1 đã sửa đúng'));
retryReload.click('[data-review]','wrong');
assert.equal(retryReload.api.visibleQuestions().length,0,'Refreshing wrong filter excludes corrected items');
retryReload.click('[data-review]','all');
retryReload.click('[data-practice-retry]','visible');
assert.equal(Object.keys(retryReload.api.state.answers).length,4,'Whole-group retry keeps lifetime completion');
assert.equal(retryReload.api.state.practiceAnswers['doc-003'],undefined,'Correct questions can also be retried');
assert.equal(retryReload.api.state.practiceAnswers['slide-001'],byId['slide-001'].answer,'Other source is unaffected');
assert.deepEqual([...retryReload.api.state.bookmarks],['doc-001']);
assert.equal(retryReload.api.state.examHistory['midterm-1'][0].score,23);
const slidePractice=await boot();
slidePractice.click('[data-source]','slide');
const slideQuestion=slidePractice.api.current(),pageKey=`${slideQuestion.source.file}::${slideQuestion.source.page}`;
assert(!slidePractice.html.includes('data-slide-open'),'Unanswered question does not expose slide image');
slidePractice.click('[data-answer]',String(slideQuestion.answer));
assert(slidePractice.html.includes(`src="${slideQuestion.source.image}"`),'Evidence image matches the referenced page');
assert(slidePractice.html.includes('Xem văn bản trích xuất'));
slidePractice.click('[data-slide-open]',pageKey);
assert(slidePractice.html.includes('id="slide-viewer"'));
assert(slidePractice.html.includes(`Trang ${slideQuestion.source.page}/`));
assert(slidePractice.key('ArrowRight'));
assert.equal(slidePractice.api.current().id,slideQuestion.id,'Viewer arrows change slides, not quiz questions');
assert(slidePractice.html.includes(`Trang ${slideQuestion.source.page+1}/`));
slidePractice.click('[data-slide-zoom]');
assert(slidePractice.html.includes('width:160%'));
slidePractice.click('[data-slide-close]');
assert(!slidePractice.html.includes('id="slide-viewer"'));
slidePractice.click('[data-practice-retry]','question');
assert(!slidePractice.html.includes('data-slide-open'),'Retry hides source images again');
slidePractice.click('[data-mode]','reader');
assert.equal(slidePractice.document.querySelectorAll('[data-slide-open]').length,125,'Reader includes every original slide');
console.log('PASS: progress, exams, scrolling, retries, image visibility, source mapping, viewer navigation/zoom and all 125 reader slides');

const hcm=JSON.parse(await fs.readFile(new URL('../dist/hcm-data.json',import.meta.url),'utf8'));
const emptyHcm={...hcm,questions:[],examForms:[],studySections:[]};
const existingKey=`dai-cuong-cnxh-${raw.questionRevision}`;
const existingWork=JSON.stringify({answers:{'doc-001':0},bookmarks:['doc-001']});
const hcmPage=await boot({[oldKey]:legacyJSON,[existingKey]:existingWork},{course:'hcm',data:emptyHcm});
assert.equal(hcmPage.api.storageKey,'dai-cuong-hcm-v1');
assert.equal(hcmPage.memory.get(existingKey),existingWork,'Opening HCM preserves current CNXH progress');
assert.equal(hcmPage.memory.get(oldKey),legacyJSON,'HCM cannot migrate legacy CNXH state');
assert.equal(Object.keys(hcmPage.api.state.answers).length,0);
assert(!hcmPage.html.includes('NaN')&&!hcmPage.html.includes('0/0'));
assert(hcmPage.html.includes('Khung ôn tập đã sẵn sàng'));
assert(hcmPage.html.includes('href="/"')&&hcmPage.html.includes('href="/?course=hcm" aria-current="page"'));
hcmPage.click('[data-chapter]','2');
assert(hcmPage.html.includes('Phạm vi chương 2'));
hcmPage.click('[data-mode]','reader');
assert(hcmPage.html.includes('Học liệu sẽ được bổ sung theo từng chương'));
hcmPage.click('[data-mode]','exam');
assert(hcmPage.html.includes('Đề luyện tập sẽ được mở sau khi có câu hỏi'));
assert(!hcmPage.html.includes('data-exam-start'));

// Synthetic fixture, never published: the same interface must accept text-only
// questions and source sections when the user supplies the actual material.
const future=structuredClone(emptyHcm);
future.studySections=[{id:'fixture-section',chapter:1,title:'Mục kiểm thử',text:'Nội dung gốc <fixture> & đối chiếu.'}];
future.questions=[{id:'hcm-fixture',chapter:1,question:'Câu hỏi kiểm thử?',choices:['A','B','C','D'],answer:2,explanation:'Giải thích kiểm thử.',source:{kind:'text',sectionId:'fixture-section',label:'Chương 1 · Mục kiểm thử',evidence:future.studySections[0].text}}];
const futurePage=await boot({[existingKey]:existingWork},{course:'hcm',data:future});
assert(!futurePage.html.includes('Nội dung gốc &lt;fixture&gt;'));
futurePage.click('[data-answer]','2');
assert(futurePage.html.includes('Nội dung gốc &lt;fixture&gt; &amp; đối chiếu.'));
assert(!futurePage.html.includes('undefined'));
futurePage.click('[data-practice-retry]','question');
assert.equal(futurePage.api.state.answers['hcm-fixture'],2);
assert(!futurePage.html.includes('Nội dung gốc &lt;fixture&gt;'));
futurePage.click('[data-mode]','reader');
assert(futurePage.html.includes('Nội dung gốc &lt;fixture&gt; &amp; đối chiếu.'));
assert.equal(futurePage.memory.get(existingKey),existingWork);
console.log('PASS: HCM empty states, chapters, course routes, isolated progress and future text-only questions/reader/retries');

const liveHcm=await boot({[existingKey]:existingWork},{course:'hcm',data:hcm});
assert.equal(liveHcm.api.visibleQuestions().length,120);
assert.equal(liveHcm.api.current().chapter,1);
assert(!liveHcm.html.includes('Chờ nội dung'));
liveHcm.click('[data-chapter]','2');
assert.equal(liveHcm.api.visibleQuestions().length,90);
const target=liveHcm.api.current();
assert(!liveHcm.html.includes('evidence-card focused'));
liveHcm.click('[data-answer]',String((target.answer+1)%4));
assert(liveHcm.html.includes(target.explanation.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;')));
liveHcm.click('[data-review]','wrong');
liveHcm.click('[data-practice-retry]','wrong');
assert.equal(liveHcm.api.current().id,target.id);
assert(!liveHcm.html.includes('evidence-card focused'));
liveHcm.click('[data-answer]',String(target.answer));
assert.equal(liveHcm.api.state.answers[target.id],target.answer);
liveHcm.click('[data-mode]','reader');
assert.equal([...liveHcm.html.matchAll(/class="reader-item"/g)].length,54,'Chapter 2 reader includes all supplied pages');
liveHcm.click('[data-chapter]','0');
liveHcm.click('[data-mode]','reader');
assert.equal([...liveHcm.html.matchAll(/class="reader-item"/g)].length,62,'Reader preserves all supplied text pages');
liveHcm.click('[data-mode]','exam');
assert.equal(liveHcm.document.querySelectorAll('[data-exam-start]').length,4);
const hcmForm=hcm.examForms[0];
liveHcm.click('[data-exam-start]',hcmForm.id);
assert(!liveHcm.html.includes('evidence-card focused'),'Unsubmitted HCM exam keeps source hidden');
const hcmById=Object.fromEntries(hcm.questions.map(q=>[q.id,q]));
for(let index=0;index<30;index++){
 liveHcm.click('[data-exam-index]',String(index));
 liveHcm.click('[data-exam-choice]',String(hcmById[hcmForm.questionIds[index]].answer));
}
liveHcm.click('[data-exam-submit]');liveHcm.click('[data-exam-confirm]');
assert(liveHcm.html.includes('30/30 câu đúng'));
assert(liveHcm.html.includes('evidence-card focused'),'Submitted HCM exam reveals its text source');
assert.equal(liveHcm.memory.get(existingKey),existingWork,'Practice and exams do not alter CNXH progress');
console.log('PASS: actual HCM bank, chapter filtering, source reveal, wrong-answer retry, all 62 source pages and 30-question grading');

const bank=JSON.parse(await fs.readFile(new URL('../dist/hcm-bank-data.json',import.meta.url),'utf8'));
const slideProgress=JSON.stringify({answers:{[hcm.questions[0].id]:hcm.questions[0].answer},bookmarks:[hcm.questions[0].id]});
const bankPage=await boot({[existingKey]:existingWork,'dai-cuong-hcm-v1':slideProgress},{course:'bank',data:bank});
assert.equal(bankPage.api.storageKey,'dai-cuong-hcm-bank-v1');
assert.equal(bankPage.api.visibleQuestions().length,139);
assert(!bankPage.html.includes('Chương 0'));
assert(bankPage.html.includes('139 mục không lặp'));
assert(!bankPage.html.includes('data-mode="exam"'));
const firstBank=bankPage.api.current();
assert(!bankPage.html.includes('bank-source-occurrence'));
bankPage.click('[data-answer]',String(firstBank.answer));
assert(bankPage.html.includes('bank-source-occurrence'));
assert(bankPage.html.includes('Đáp án đúng có trong nguồn'));
bankPage.click('[data-bank-set]','tap-3');
assert.equal(bankPage.api.current().id,firstBank.id);
assert(bankPage.html.includes('answer-box'),'Shared question progress is visible in another set');
bankPage.click('[data-practice-retry]','question');
assert(!bankPage.html.includes('bank-source-occurrence'));
assert.equal(bankPage.api.state.answers[firstBank.id],firstBank.answer);
bankPage.click('[data-answer]',String((firstBank.answer+1)%4));
bankPage.click('[data-review]','wrong');
bankPage.click('[data-practice-retry]','wrong');
bankPage.click('[data-answer]',String(firstBank.answer));
assert.equal(bankPage.api.current().id,firstBank.id);
bankPage.click('[data-bank-set]','tap-2-g2');
assert(bankPage.api.visibleQuestions().every(q=>q.groupIds.includes('tap-2-g2')));
assert.equal(bankPage.api.current().id,'bank-departure-year','Each group follows original source numbering, including question 00');
bankPage.click('[data-bank-set]','all');
bankPage.click('[data-bank-kind]','pending');
assert.equal(bankPage.api.visibleQuestions().length,4);
assert(!bankPage.html.includes('data-answer'));
const countBefore=Object.keys(bankPage.api.state.answers).length;
bankPage.key('1');
assert.equal(Object.keys(bankPage.api.state.answers).length,countBefore,'Unresolved question cannot be graded by keyboard');
bankPage.click('[data-bank-reveal]');
assert(bankPage.html.includes('Chưa có đủ căn cứ'));
bankPage.click('[data-bank-kind]','essay');
assert.equal(bankPage.api.visibleQuestions().length,2);
bankPage.click('[data-bank-reveal]');
assert(bankPage.html.includes('Gợi ý:'));
assert.equal(Object.keys(bankPage.api.state.answers).length,countBefore,'Essay reveal is not a correct quiz answer');
bankPage.click('[data-bank-kind]','all');
bankPage.click('[data-mode]','reader');
assert.equal([...bankPage.html.matchAll(/class="reader-item"/g)].length,139);
assert.equal([...bankPage.html.matchAll(/class="bank-source-title"/g)].length,261,'Every original source occurrence is readable after deduplication');
assert.equal(bankPage.memory.get('dai-cuong-hcm-v1'),slideProgress);
assert.equal(bankPage.memory.get(existingKey),existingWork);
const reloadedBank=await boot(Object.fromEntries(bankPage.memory),{course:'bank',data:bank});
assert.equal(reloadedBank.api.state.answers[firstBank.id],firstBank.answer);
console.log('PASS: bank deduplication, six sets/subgroups, shared retries, read-only pending/essay items, 261 source occurrences and three isolated progress stores');
