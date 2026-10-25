(() => {
  const mk=(x,y,w,h,c,t)=>{const d=document.createElement('div');Object.assign(d.style,{position:'absolute',left:x+'px',top:y+'px',width:w+'px',height:h+'px',background:c,zIndex:99,display:'flex',alignItems:'center',justifyContent:'center',font:'700 11px Inter,sans-serif',color:'#fff'});d.textContent=t;document.body.appendChild(d);};
  const R=e=>{const r=e.getBoundingClientRect();return {t:r.top+scrollY,b:r.bottom+scrollY,l:r.left,r:r.right};};
  document.body.style.position='relative';
  // big gaps between top-level blocks
  const blocks=[...document.querySelectorAll('[data-spec]')].filter(e=>e.offsetParent!==null);
  for(let i=0;i<blocks.length-1;i++){const a=R(blocks[i]),b=R(blocks[i+1]);const g=Math.round(b.t-a.b);if(g>0&&g<200)mk(a.l+40,a.b,64,g,'rgba(219,39,119,.85)',g+'px');}
  // small gaps inside sections
  document.querySelectorAll('.main > section').forEach(s=>{if(s.offsetParent===null)return;const k=[...s.children].filter(e=>e.offsetParent!==null);for(let i=0;i<k.length-1;i++){const a=R(k[i]),b=R(k[i+1]);const g=Math.round(b.t-a.b);if(g>0)mk(a.r-60,a.b,44,g,'rgba(14,116,144,.85)',g);}});
  // side margin
  const m=document.querySelector('.main');if(m){const r=R(m);mk(0,r.t+120,r.l,18,'rgba(124,58,237,.85)',Math.round(r.l)+'');}
})();
