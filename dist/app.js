const $ = (s, root = document) => root.querySelector(s);
const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const chapterNames = {1:'Nhập môn chủ nghĩa xã hội khoa học',2:'Sứ mệnh lịch sử của giai cấp công nhân',3:'Chủ nghĩa xã hội và thời kỳ quá độ',4:'Dân chủ và nhà nước xã hội chủ nghĩa'};
const letters = ['A','B','C','D'];
const raw = await fetch('/data.json').then(r => { if(!r.ok) throw Error('Không tải được học liệu'); return r.json(); });
const all = raw.questions;
const storageKey = 'dai-cuong-cnxh-v1';
let stored = {};
try { stored = JSON.parse(localStorage.getItem(storageKey)) || {}; } catch {}
const state = {source:stored.source || 'doc',chapter:stored.chapter || 0,mode:'quiz',search:'',index:stored.index || 0,answers:stored.answers || {},bookmarks:stored.bookmarks || [],review:'all'};
function save(){localStorage.setItem(storageKey,JSON.stringify({source:state.source,chapter:state.chapter,index:state.index,answers:state.answers,bookmarks:state.bookmarks}));}
function sourceQuestions(){return all.filter(q => q.source.kind === state.source);}
function visibleQuestions(){return sourceQuestions().filter(q => (!state.chapter || q.chapter===state.chapter) && (!state.search || (q.question+' '+q.choices.join(' ')).toLocaleLowerCase('vi').includes(state.search.toLocaleLowerCase('vi'))) && (state.review==='all' || state.review==='wrong' && state.answers[q.id]!==undefined && state.answers[q.id]!==q.answer || state.review==='saved' && state.bookmarks.includes(q.id)));}
function current(){const qs=visibleQuestions();state.index=Math.max(0,Math.min(state.index,qs.length-1));return qs[state.index];}
function totals(kind){const qs=all.filter(q=>q.source.kind===kind);return {all:qs.length,answered:qs.filter(q=>state.answers[q.id]!==undefined).length};}
function overall(){return Object.keys(state.answers).length;}
function evidenceText(q){return q.source.evidence.replace(/^VỞ\s*│\s*|^SLIDE\s*│\s*/,'').trim();}
function render(){
 const q=current(),qs=visibleQuestions(),dt=totals('doc'),st=totals('slide'),done=overall();
 const sourceName=state.source==='doc'?'Ghi chú':'Slide';
 $('#app').innerHTML=`<div class="app">
  <header class="topbar"><div><span class="brand"><span class="brand-mark">Đ</span>Đại cương</span><span class="course-name">/ Chủ nghĩa xã hội khoa học</span></div><div class="header-right"><span>${done}/${all.length} đã làm</span><span class="top-progress"><span style="width:${done/all.length*100}%"></span></span></div></header>
  <aside class="sidebar"><div class="side-head">Lộ trình học</div><div class="source-row">
   <button class="source-card ${state.source==='doc'?'active':''}" data-source="doc"><span><strong>01 · Ghi chú</strong><small>Học trước, theo từng ý</small></span><span class="count">${dt.answered}/${dt.all}</span></button>
   <button class="source-card ${state.source==='slide'?'active':''}" data-source="slide"><span><strong>02 · Slide bài giảng</strong><small>Ôn toàn bộ ý chính</small></span><span class="count">${st.answered}/${st.all}</span></button></div>
   <div class="side-divider"></div><div class="side-head">Chương</div><div class="chapter-list">
   <button class="chapter-btn ${state.chapter===0?'active':''}" data-chapter="0"><span>Tất cả chương</span><span>${sourceQuestions().length}</span></button>
   ${Object.entries(chapterNames).map(([k,v])=>`<button class="chapter-btn ${state.chapter===Number(k)?'active':''}" data-chapter="${k}"><span>${k}. ${escapeHtml(v)}</span><span>${sourceQuestions().filter(x=>x.chapter===Number(k)).length}</span></button>`).join('')}</div>
   <div class="side-divider"></div><div class="side-head">Tìm câu hỏi</div><input class="search" type="search" placeholder="Nhập từ khóa..." value="${escapeHtml(state.search)}" aria-label="Tìm câu hỏi">
   <p class="side-note">Làm hết phần ghi chú trước khi chuyển sang slide. Tiến độ được lưu trên trình duyệt này.</p>
  </aside>
  <main class="main"><div class="eyebrow">Ôn thi giữa kỳ · Trắc nghiệm</div><h1 class="page-title">${sourceName}</h1><p class="intro">${state.source==='doc'?'Ưu tiên toàn bộ nội dung tài liệu ghi chú. Mỗi đáp án đều có đoạn nguồn đối chiếu.':'Các ý chính từ bốn bộ slide, gồm cả những nội dung đã gặp trong ghi chú để luyện thêm một lượt.'}</p>
   <div class="toolbar"><button class="tab ${state.mode==='quiz'?'active':''}" data-mode="quiz">Làm câu hỏi</button><button class="tab ${state.mode==='reader'?'active':''}" data-mode="reader">Đọc học liệu</button>${state.mode==='quiz'?'<span class="toolbar-spacer"></span><button class="outline-button" data-review="all">Tất cả</button><button class="outline-button" data-review="wrong">Làm sai</button><button class="outline-button" data-review="saved">Đã lưu</button>':''}</div>
   ${state.mode==='quiz'?renderQuiz(q,qs):renderReader()}
  </main>
  <aside class="evidence" id="evidence"><div class="evidence-head"><h2>Đối chiếu học liệu</h2><span class="muted" style="font-size:11px">${q&&state.mode==='quiz'?'Nguồn gốc':''}</span></div>
   ${state.mode==='quiz'&&q?renderEvidence(q):'<div class="evidence-placeholder">Chọn một câu hỏi để xem đoạn kiến thức tương ứng tại đây.</div>'}
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
function renderEvidence(q){
 const answered=state.answers[q.id]!==undefined;
 return `<span class="evidence-label">${escapeHtml(q.source.label)}</span>${answered?`<div class="evidence-card focused" tabindex="-1" id="evidence-content">${escapeHtml(evidenceText(q))}</div>`:'<div class="evidence-placeholder">Chọn đáp án để mở đoạn kiến thức tương ứng. Đáp án và nguồn sẽ hiện cùng lúc.</div>'}
 ${q.source.kind==='doc'? `<a class="source-link" href="${escapeHtml(q.source.url)}" target="_blank" rel="noopener noreferrer">Mở Google Docs ↗</a>` : `<div class="source-caption">Tệp gốc: ${escapeHtml(q.source.file)}, trang ${q.source.page}. Toàn bộ văn bản slide nằm trong mục Đọc học liệu.</div>`}
 ${answered?'<p class="source-caption">Phần này được trích từ tài liệu bạn cung cấp để kiểm tra lại cách diễn đạt của câu hỏi.</p>':''}`;
}
function renderReader(){
 const items=state.source==='doc'?raw.docLines.map((text,i)=>({label:`Dòng ${i+1}`,text})).filter(x=>x.text.trim()):raw.slidePages.map(s=>({label:`${s.file} · trang ${s.slide}`,text:s.text})).filter(x=>x.text.trim());
 return `<div class="reader-list">${items.map(item=>`<details class="reader-item"><summary><small>${escapeHtml(item.label)}</small>${escapeHtml(item.text.replace(/^VỞ\s*│\s*|^SLIDE\s*│\s*/,'').slice(0,100).replace(/\n/g,' · '))}</summary><p>${escapeHtml(item.text)}</p></details>`).join('')}</div>`;
}
function bind(){
 document.querySelectorAll('[data-source]').forEach(el=>el.onclick=()=>{state.source=el.dataset.source;state.chapter=0;state.index=0;state.search='';state.review='all';render();});
 document.querySelectorAll('[data-chapter]').forEach(el=>el.onclick=()=>{state.chapter=Number(el.dataset.chapter);state.index=0;render();});
 document.querySelectorAll('[data-mode]').forEach(el=>el.onclick=()=>{state.mode=el.dataset.mode;render();});
 document.querySelectorAll('[data-review]').forEach(el=>el.onclick=()=>{state.review=el.dataset.review;state.index=0;render();});
 const search=$('.search'); if(search)search.oninput=e=>{const pos=e.target.selectionStart;state.search=e.target.value;state.index=0;render();const fresh=$('.search');fresh.focus();fresh.setSelectionRange(pos,pos);};
 document.querySelectorAll('[data-answer]').forEach(el=>el.onclick=()=>{const q=current();if(!q||state.answers[q.id]!==undefined)return;state.answers[q.id]=Number(el.dataset.answer);render();const pane=$('#evidence-content');if(pane){pane.scrollIntoView({behavior:'smooth',block:'nearest'});pane.focus({preventScroll:true});}});
 document.querySelectorAll('[data-nav]').forEach(el=>el.onclick=()=>{state.index+=Number(el.dataset.nav);render();$('.question-card')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-index]').forEach(el=>el.onclick=()=>{state.index=Number(el.dataset.index);render();$('.question-card')?.scrollIntoView({block:'start',behavior:'smooth'});});
 document.querySelectorAll('[data-bookmark]').forEach(el=>el.onclick=()=>{const id=el.dataset.bookmark;state.bookmarks=state.bookmarks.includes(id)?state.bookmarks.filter(x=>x!==id):[...state.bookmarks,id];render();});
}
document.addEventListener('keydown',e=>{if(state.mode!=='quiz'||['INPUT','TEXTAREA'].includes(document.activeElement?.tagName))return;if(e.key==='ArrowRight'&&state.index<visibleQuestions().length-1){state.index++;render();}if(e.key==='ArrowLeft'&&state.index>0){state.index--;render();}if(['1','2','3','4'].includes(e.key)){const q=current();if(q&&state.answers[q.id]===undefined){state.answers[q.id]=Number(e.key)-1;render();$('#evidence-content')?.focus();}}});
render();
