const $ = (s, root = document) => root.querySelector(s);
const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const chapterNames = {1:'Nhập môn chủ nghĩa xã hội khoa học',2:'Sứ mệnh lịch sử của giai cấp công nhân',3:'Chủ nghĩa xã hội và thời kỳ quá độ',4:'Dân chủ và nhà nước xã hội chủ nghĩa'};
const letters = ['A','B','C','D'];
const raw = await fetch('/data.json').then(r => { if(!r.ok) throw Error('Không tải được học liệu'); return r.json(); });
const all = raw.questions;
const byId = Object.fromEntries(all.map(q => [q.id, q]));
const examForms = raw.examForms || [];
const storageKey = `dai-cuong-cnxh-${raw.questionRevision || 'v1'}`;
let stored = {}, previous = {};
try { stored = JSON.parse(localStorage.getItem(storageKey)) || {}; } catch {}
try { previous = JSON.parse(localStorage.getItem('dai-cuong-cnxh-v1')) || {}; } catch {}
const previousExamScores = Object.fromEntries(examForms.map(form=>{
 const attempt=previous.examAttempts?.[form.id],scores=(previous.examHistory?.[form.id]||[]).map(item=>item.score);
 if(attempt?.submittedAt)scores.push(form.questionIds.reduce((n,id)=>n+(attempt.answers?.[id]===byId[id].answer),0));
 return [form.id,scores.length?Math.max(...scores):null];
}));
const hasPreviousWork=Object.keys(previous.answers||{}).length>0||Object.keys(previous.examAttempts||{}).length>0||Object.keys(previous.examHistory||{}).length>0;
const state = {source:stored.source || previous.source || 'doc',chapter:stored.chapter ?? previous.chapter ?? 0,mode:stored.mode==='exam'?'exam':'quiz',search:'',index:stored.index || 0,answers:stored.answers || {},bookmarks:(stored.bookmarks ?? previous.bookmarks ?? []).filter(id=>byId[id]),review:'all',examId:stored.examId || null,examAttempts:stored.examAttempts || {},examHistory:stored.examHistory || {},confirmSubmit:false,reviewNotice:hasPreviousWork&&!stored.reviewNoticeDismissed};
function save(){localStorage.setItem(storageKey,JSON.stringify({source:state.source,chapter:state.chapter,index:state.index,answers:state.answers,bookmarks:state.bookmarks,mode:state.mode,examId:state.examId,examAttempts:state.examAttempts,examHistory:state.examHistory,reviewNoticeDismissed:!state.reviewNotice}));}
function sourceQuestions(){return all.filter(q => q.source.kind === state.source);}
function visibleQuestions(){return sourceQuestions().filter(q => (!state.chapter || q.chapter===state.chapter) && (!state.search || (q.question+' '+q.choices.join(' ')).toLocaleLowerCase('vi').includes(state.search.toLocaleLowerCase('vi'))) && (state.review==='all' || state.review==='wrong' && state.answers[q.id]!==undefined && state.answers[q.id]!==q.answer || state.review==='saved' && state.bookmarks.includes(q.id)));}
function current(){const qs=visibleQuestions();state.index=Math.max(0,Math.min(state.index,qs.length-1));return qs[state.index];}
function totals(kind){const qs=all.filter(q=>q.source.kind===kind);return {all:qs.length,answered:qs.filter(q=>state.answers[q.id]!==undefined).length};}
function overall(){return Object.keys(state.answers).length;}
function evidenceText(q){return q.source.evidence.replace(/^VỞ\s*│\s*|^SLIDE\s*│\s*/,'').trim();}
function activeForm(){return examForms.find(form=>form.id===state.examId);}
function activeAttempt(){return state.examAttempts[state.examId];}
function examQuestions(form){return form.questionIds.map(id=>byId[id]);}
function timeLeft(form,attempt){return Math.max(0,form.durationSeconds-Math.floor((Date.now()-attempt.startedAt)/1000));}
function clockText(seconds){return `${String(Math.floor(seconds/60)).padStart(2,'0')}:${String(seconds%60).padStart(2,'0')}`;}
function submitExam(reason='manual'){const attempt=activeAttempt();if(!attempt||attempt.submittedAt)return;attempt.submittedAt=Date.now();attempt.reason=reason;state.confirmSubmit=false;render();}
function examCurrent(){const form=activeForm(),attempt=activeAttempt();if(!form||!attempt)return null;attempt.current=Math.max(0,Math.min(attempt.current,form.questionIds.length-1));return byId[form.questionIds[attempt.current]];}
function render(){
 const q=current(),qs=visibleQuestions(),dt=totals('doc'),st=totals('slide'),done=overall();
 const sourceName=state.source==='doc'?'Ghi chú':'Slide';
 const form=activeForm(),attempt=activeAttempt(),eq=state.mode==='exam'?examCurrent():null;
 if(state.mode==='exam'&&form&&attempt&&!attempt.submittedAt&&timeLeft(form,attempt)===0){attempt.submittedAt=Date.now();attempt.reason='time';}
 $('#app').innerHTML=`<div class="app">
  <header class="topbar"><div><span class="brand"><span class="brand-mark">Đ</span>Đại cương</span><span class="course-name">/ Chủ nghĩa xã hội khoa học</span></div><div class="header-right"><span>${done}/${all.length} đã làm</span><span class="top-progress"><span style="width:${done/all.length*100}%"></span></span></div></header>
  <aside class="sidebar"><div class="side-head">Lộ trình học</div><div class="source-row">
   <button class="source-card ${state.mode!=='exam'&&state.source==='doc'?'active':''}" data-source="doc"><span><strong>01 · Ghi chú</strong><small>Học trước, theo từng ý</small></span><span class="count">${dt.answered}/${dt.all}</span></button>
   <button class="source-card ${state.mode!=='exam'&&state.source==='slide'?'active':''}" data-source="slide"><span><strong>02 · Slide bài giảng</strong><small>Ôn toàn bộ ý chính</small></span><span class="count">${st.answered}/${st.all}</span></button></div>
   <div class="side-divider"></div><div class="side-head">Chương</div><div class="chapter-list">
   <button class="chapter-btn ${state.chapter===0?'active':''}" data-chapter="0"><span>Tất cả chương</span><span>${sourceQuestions().length}</span></button>
   ${Object.entries(chapterNames).map(([k,v])=>`<button class="chapter-btn ${state.chapter===Number(k)?'active':''}" data-chapter="${k}"><span>${k}. ${escapeHtml(v)}</span><span>${sourceQuestions().filter(x=>x.chapter===Number(k)).length}</span></button>`).join('')}</div>
   <div class="side-divider"></div><div class="side-head">Tìm câu hỏi</div><input class="search" type="search" placeholder="Nhập từ khóa..." value="${escapeHtml(state.search)}" aria-label="Tìm câu hỏi">
   <p class="side-note">Làm hết phần ghi chú trước khi chuyển sang slide. Tám đề giữa kỳ có đồng hồ 15 phút và chấm sau khi nộp.</p>
  </aside>
  <main class="main"><div class="eyebrow">Ôn thi giữa kỳ · Trắc nghiệm</div><h1 class="page-title">${state.mode==='exam'?'Đề giữa kỳ':sourceName}</h1><p class="intro">${state.mode==='exam'?'Tám đề 30 câu, 15 phút mỗi đề. Đáp án và nguồn chỉ hiện sau khi nộp bài.':state.source==='doc'?'Ưu tiên toàn bộ nội dung tài liệu ghi chú. Mỗi đáp án đều có đoạn nguồn đối chiếu.':'Các ý chính từ bốn bộ slide, gồm cả những nội dung đã gặp trong ghi chú để luyện thêm một lượt.'}</p>
   <div class="toolbar"><button class="tab ${state.mode==='quiz'?'active':''}" data-mode="quiz">Làm câu hỏi</button><button class="tab ${state.mode==='reader'?'active':''}" data-mode="reader">Đọc học liệu</button><button class="tab ${state.mode==='exam'?'active':''}" data-mode="exam">Đề 30 câu · 15 phút</button>${state.mode==='quiz'?'<span class="toolbar-spacer"></span><button class="outline-button" data-review="all">Tất cả</button><button class="outline-button" data-review="wrong">Làm sai</button><button class="outline-button" data-review="saved">Đã lưu</button>':''}</div>
   ${state.reviewNotice?'<div class="review-notice" role="status"><div><strong>Bộ câu hỏi đã được biên tập lại</strong><p>Bạn bắt đầu lượt luyện mới với các phương án đã sửa. Câu đã lưu và điểm đề trước biên tập vẫn được giữ riêng trên thiết bị này.</p></div><button class="outline-button" data-review-notice-close>Đã hiểu</button></div>':''}
   ${state.mode==='quiz'?renderQuiz(q,qs):state.mode==='reader'?renderReader():renderExam()}
  </main>
  <aside class="evidence" id="evidence"><div class="evidence-head"><h2>Đối chiếu học liệu</h2><span class="muted" style="font-size:11px">${state.mode==='exam'&&attempt&&!attempt.submittedAt?'Sau khi nộp bài':q&&state.mode==='quiz'?'Nguồn gốc':''}</span></div>
   ${state.mode==='exam'?eq&&attempt?.submittedAt?renderEvidence(eq,true):'<div class="evidence-placeholder">Trong lúc làm đề, nội dung nguồn được ẩn. Nộp bài để xem đáp án và đối chiếu từng câu.</div>':state.mode==='quiz'&&q?renderEvidence(q):'<div class="evidence-placeholder">Chọn một câu hỏi để xem đoạn kiến thức tương ứng tại đây.</div>'}
  </aside></div>`;
 bind();
 save();
}
function renderQuiz(q,qs){
 if(!q)return '<div class="empty">Không có câu hỏi phù hợp. Hãy đổi từ khóa hoặc bộ lọc.</div>';
 const selected=state.answers[q.id],answered=selected!==undefined;
 return `<article class="question-card"><div class="question-meta"><div class="meta-left"><span class="badge">Câu ${state.index+1} / ${qs.length}</span><span class="badge neutral">Chương ${q.chapter}</span><span class="badge neutral">${q.source.kind==='doc'?'Ghi chú':'Slide'}</span></div><button class="outline-button ${state.bookmarks.includes(q.id)?'saved':''}" data-bookmark="${q.id}" aria-label="${state.bookmarks.includes(q.id)?'Bỏ lưu':'Lưu'} câu hỏi">${state.bookmarks.includes(q.id)?'★ Đã lưu':'☆ Lưu câu'}</button></div>
  <h2 class="question-title">${escapeHtml(q.question)}</h2><div class="options">${q.choices.map((choice,i)=>`<button class="option ${answered?(i===q.answer?'correct':i===selected?'wrong':'dim'):''}" data-answer="${i}" ${answered?'disabled':''}><span class="option-letter">${letters[i]}</span><span>${escapeHtml(choice)}</span></button>`).join('')}</div>
  ${answered?`<div class="answer-box ${selected===q.answer?'':'error'}"><strong>${selected===q.answer?'Chính xác':'Chưa đúng'} · Đáp án ${letters[q.answer]}</strong>${escapeHtml(q.explanation)}</div>`:''}
  <div class="question-footer"><button class="nav-button" data-nav="-1" ${state.index===0?'disabled':''}>← Câu trước</button><div class="progress-copy">${answered?'Đã trả lời':'Chọn một đáp án để mở phần đối chiếu'}<br>Dùng phím ← → để chuyển câu</div><button class="nav-button primary" data-nav="1" ${state.index===qs.length-1?'disabled':''}>Câu tiếp theo →</button></div>
 </article><section class="grid-section"><div class="grid-heading"><span>Danh sách câu hỏi</span><span>${qs.filter(x=>state.answers[x.id]!==undefined).length} / ${qs.length} đã làm</span></div><div class="number-grid">${qs.map((item,i)=>`<button data-index="${i}" class="${i===state.index?'current':''} ${state.answers[item.id]===undefined?'':state.answers[item.id]===item.answer?'done':'failed'}" aria-label="Câu ${i+1}">${i+1}</button>`).join('')}</div></section>`;
}
function renderEvidence(q,examReview=false){
 const answered=examReview||state.answers[q.id]!==undefined;
 return `<span class="evidence-label">${escapeHtml(q.source.label)}</span>${answered?`<div class="evidence-card focused" tabindex="-1" id="evidence-content">${escapeHtml(evidenceText(q))}</div>`:'<div class="evidence-placeholder">Chọn đáp án để mở đoạn kiến thức tương ứng. Đáp án và nguồn sẽ hiện cùng lúc.</div>'}
 ${q.source.kind==='doc'? `<a class="source-link" href="${escapeHtml(q.source.url)}" target="_blank" rel="noopener noreferrer">Mở Google Docs ↗</a>` : `<div class="source-caption">Tệp gốc: ${escapeHtml(q.source.file)}, trang ${q.source.page}. Toàn bộ văn bản slide nằm trong mục Đọc học liệu.</div>`}
 ${answered?'<p class="source-caption">Phần này được trích từ tài liệu bạn cung cấp để kiểm tra lại cách diễn đạt của câu hỏi.</p>':''}`;
}
function renderReader(){
 const items=state.source==='doc'?raw.docLines.map((text,i)=>({label:`Dòng ${i+1}`,text})).filter(x=>x.text.trim()):raw.slidePages.map(s=>({label:`${s.file} · trang ${s.slide}`,text:s.text})).filter(x=>x.text.trim());
 return `<div class="reader-list">${items.map(item=>`<details class="reader-item"><summary><small>${escapeHtml(item.label)}</small>${escapeHtml(item.text.replace(/^VỞ\s*│\s*|^SLIDE\s*│\s*/,'').slice(0,100).replace(/\n/g,' · '))}</summary><p>${escapeHtml(item.text)}</p></details>`).join('')}</div>`;
}
function renderExam(){
 const form=activeForm(),attempt=activeAttempt();
 if(!form||!attempt)return `<div class="exam-list">${examForms.map((item,i)=>{
   const previous=state.examAttempts[item.id],completed=previous?.submittedAt;
   const score=completed?item.questionIds.reduce((n,id)=>n+(previous.answers[id]===byId[id].answer),0):null;
   const historical=state.examHistory[item.id]||[],best=Math.max(score??0,...historical.map(a=>a.score));
   const oldScore=previousExamScores[item.id];
   return `<article class="exam-card"><div class="exam-num">Đề ${String(i+1).padStart(2,'0')} · 30 câu · 15 phút</div><h2>${escapeHtml(item.title)}</h2><p>${escapeHtml(item.focus)}</p><div class="exam-card-footer"><span>${completed?`Lần gần nhất: ${score}/30 · Cao nhất: ${best}/30`:previous?`${Object.keys(previous.answers).length}/30 đã chọn`:'Chưa làm'}${oldScore!==null?`<small class="legacy-score">Trước biên tập · Cao nhất: ${oldScore}/30</small>`:''}</span><div>${previous?`<button class="outline-button" data-exam-open="${item.id}">${completed?'Xem lại':'Tiếp tục'}</button>`:''}<button class="nav-button primary" data-exam-start="${item.id}">${previous?'Làm lại':'Bắt đầu'}</button></div></div></article>`;
 }).join('')}</div>`;
 const q=examCurrent(),submitted=!!attempt.submittedAt,selected=attempt.answers[q.id];
 const answered=selected!==undefined,position=attempt.current,answeredCount=Object.keys(attempt.answers).length;
 const score=submitted?form.questionIds.reduce((n,id)=>n+(attempt.answers[id]===byId[id].answer),0):0;
 return `<div class="exam-top"><button class="outline-button" data-exam-back>← Danh sách đề</button><strong>${escapeHtml(form.title)}</strong><span class="exam-timer ${!submitted&&timeLeft(form,attempt)<120?'urgent':''}" id="exam-timer">${submitted?'Đã nộp':clockText(timeLeft(form,attempt))}</span></div>
 ${submitted?`<section class="exam-result"><div><span class="eyebrow">${attempt.reason==='time'?'Hết giờ · Bài đã tự nộp':'Kết quả bài làm'}</span><h2>${score}/30 câu đúng</h2><p>Tương đương ${(score/3).toFixed(1)}/10 điểm. Chọn số câu bên dưới để xem đáp án, giải thích và đoạn nguồn.</p></div><div class="exam-result-count">${30-answeredCount} câu bỏ trống</div></section>`:`<div class="exam-progress"><span>${answeredCount}/30 đã chọn</span><span>Đáp án được giữ kín đến khi nộp</span></div>`}
 <article class="question-card exam-question"><div class="question-meta"><div class="meta-left"><span class="badge">Câu ${position+1} / 30</span><span class="badge neutral">Chương ${q.chapter}</span><span class="badge neutral">${q.source.kind==='doc'?'Ghi chú':'Slide'}</span></div></div><h2 class="question-title">${escapeHtml(q.question)}</h2>
 <div class="options">${q.choices.map((choice,i)=>`<button class="option ${submitted?(i===q.answer?'correct':i===selected?'wrong':'dim'):i===selected?'selected':''}" data-exam-choice="${i}" ${submitted?'disabled':''}><span class="option-letter">${letters[i]}</span><span>${escapeHtml(choice)}</span></button>`).join('')}</div>
 ${submitted?`<div class="answer-box ${selected===q.answer?'':'error'}"><strong>${selected===q.answer?'Chính xác':answered?'Chưa đúng':'Chưa trả lời'} · Đáp án ${letters[q.answer]}</strong>${escapeHtml(q.explanation)}</div>`:''}
 <div class="question-footer"><button class="nav-button" data-exam-nav="-1" ${position===0?'disabled':''}>← Câu trước</button><div class="progress-copy">${submitted?'Xem đoạn nguồn bên cạnh':answered?'Đã chọn '+letters[selected]:'Chưa chọn đáp án'}</div><button class="nav-button primary" data-exam-nav="1" ${position===29?'disabled':''}>Câu tiếp theo →</button></div></article>
 <section class="grid-section"><div class="grid-heading"><span>30 câu trong đề</span><span>${answeredCount}/30 đã chọn</span></div><div class="number-grid exam-grid">${form.questionIds.map((id,i)=>{
  const given=attempt.answers[id],item=byId[id],className=submitted?(given===undefined?'skipped':given===item.answer?'done':'failed'):given===undefined?'':'selected';
  return `<button data-exam-index="${i}" class="${i===position?'current':''} ${className}" aria-label="Câu ${i+1}">${i+1}</button>`;
 }).join('')}</div></section>
 ${submitted?'':state.confirmSubmit?`<div class="submit-confirm"><strong>Nộp bài ngay?</strong><span>${30-answeredCount} câu chưa chọn sẽ tính là sai. Sau khi nộp, bạn có thể xem lại hoặc làm đề mới.</span><div><button class="outline-button" data-exam-cancel>Tiếp tục làm</button><button class="nav-button primary" data-exam-confirm>Xác nhận nộp</button></div></div>`:`<div class="submit-row"><button class="nav-button primary" data-exam-submit>Nộp bài và xem kết quả</button></div>`}`;
}
function bind(){
 document.querySelectorAll('[data-review-notice-close]').forEach(el=>el.onclick=()=>{state.reviewNotice=false;render();});
 document.querySelectorAll('[data-source]').forEach(el=>el.onclick=()=>{state.source=el.dataset.source;state.mode='quiz';state.chapter=0;state.index=0;state.search='';state.review='all';render();});
 document.querySelectorAll('[data-chapter]').forEach(el=>el.onclick=()=>{state.mode='quiz';state.chapter=Number(el.dataset.chapter);state.index=0;render();});
 document.querySelectorAll('[data-mode]').forEach(el=>el.onclick=()=>{state.mode=el.dataset.mode;state.confirmSubmit=false;render();});
 document.querySelectorAll('[data-review]').forEach(el=>el.onclick=()=>{state.review=el.dataset.review;state.index=0;render();});
 const search=$('.search'); if(search)search.oninput=e=>{const pos=e.target.selectionStart;state.mode='quiz';state.search=e.target.value;state.index=0;render();const fresh=$('.search');fresh.focus();fresh.setSelectionRange(pos,pos);};
 document.querySelectorAll('[data-answer]').forEach(el=>el.onclick=()=>{const q=current();if(!q||state.answers[q.id]!==undefined)return;state.answers[q.id]=Number(el.dataset.answer);render();const pane=$('#evidence-content');if(pane){pane.scrollIntoView({behavior:'smooth',block:'nearest'});pane.focus({preventScroll:true});}});
 document.querySelectorAll('[data-nav]').forEach(el=>el.onclick=()=>{state.index+=Number(el.dataset.nav);render();$('.question-card')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-index]').forEach(el=>el.onclick=()=>{state.index=Number(el.dataset.index);render();$('.question-card')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-bookmark]').forEach(el=>el.onclick=()=>{const id=el.dataset.bookmark;state.bookmarks=state.bookmarks.includes(id)?state.bookmarks.filter(x=>x!==id):[...state.bookmarks,id];render();});
 document.querySelectorAll('[data-exam-start]').forEach(el=>el.onclick=()=>{const id=el.dataset.examStart,old=state.examAttempts[id],selected=examForms.find(form=>form.id===id);if(old?.submittedAt){const score=selected.questionIds.reduce((n,qid)=>n+(old.answers[qid]===byId[qid].answer),0);(state.examHistory[id]??=[]).push({score,submittedAt:old.submittedAt});}state.examAttempts[id]={startedAt:Date.now(),answers:{},current:0,submittedAt:null};state.examId=id;state.confirmSubmit=false;render();});
 document.querySelectorAll('[data-exam-open]').forEach(el=>el.onclick=()=>{state.examId=el.dataset.examOpen;state.confirmSubmit=false;render();});
 document.querySelectorAll('[data-exam-back]').forEach(el=>el.onclick=()=>{state.examId=null;state.confirmSubmit=false;render();});
 document.querySelectorAll('[data-exam-choice]').forEach(el=>el.onclick=()=>{const q=examCurrent(),attempt=activeAttempt();if(!q||attempt.submittedAt)return;if(timeLeft(activeForm(),attempt)===0){submitExam('time');return;}attempt.answers[q.id]=Number(el.dataset.examChoice);render();});
 document.querySelectorAll('[data-exam-nav]').forEach(el=>el.onclick=()=>{activeAttempt().current+=Number(el.dataset.examNav);render();$('.exam-question')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-exam-index]').forEach(el=>el.onclick=()=>{activeAttempt().current=Number(el.dataset.examIndex);render();$('.exam-question')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-exam-submit]').forEach(el=>el.onclick=()=>{state.confirmSubmit=true;render();$('.submit-confirm')?.scrollIntoView({block:'nearest',behavior:'smooth'});});
 document.querySelectorAll('[data-exam-cancel]').forEach(el=>el.onclick=()=>{state.confirmSubmit=false;render();});
 document.querySelectorAll('[data-exam-confirm]').forEach(el=>el.onclick=()=>submitExam());
}
document.addEventListener('keydown',e=>{
 if(['INPUT','TEXTAREA'].includes(document.activeElement?.tagName))return;
 if(state.mode==='quiz'){
  if(e.key==='ArrowRight'&&state.index<visibleQuestions().length-1){state.index++;render();}
  if(e.key==='ArrowLeft'&&state.index>0){state.index--;render();}
  if(['1','2','3','4'].includes(e.key)){const q=current();if(q&&state.answers[q.id]===undefined){state.answers[q.id]=Number(e.key)-1;render();$('#evidence-content')?.focus();}}
 }
 if(state.mode==='exam'&&activeAttempt()&&!activeAttempt().submittedAt){
  if(e.key==='ArrowRight'&&activeAttempt().current<29){activeAttempt().current++;render();}
  if(e.key==='ArrowLeft'&&activeAttempt().current>0){activeAttempt().current--;render();}
  if(['1','2','3','4'].includes(e.key)){if(timeLeft(activeForm(),activeAttempt())===0){submitExam('time');return;}activeAttempt().answers[examCurrent().id]=Number(e.key)-1;render();}
 }
});
setInterval(()=>{if(state.mode!=='exam')return;const form=activeForm(),attempt=activeAttempt();if(!form||!attempt||attempt.submittedAt)return;const remaining=timeLeft(form,attempt);if(remaining===0){submitExam('time');return;}const timer=$('#exam-timer');if(timer){timer.textContent=clockText(remaining);timer.classList.toggle('urgent',remaining<120);}},1000);
document.addEventListener('visibilitychange',()=>{if(!document.hidden&&state.mode==='exam')render();});
render();
