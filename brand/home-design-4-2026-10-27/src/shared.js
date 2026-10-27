// Shared pieces: phone status bar, bottom tab bar (filled icons), view switch.
const ICON = {
  today: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.6"/><path d="M12 1.5l1.3 3.4h-2.6zM12 22.5l-1.3-3.4h2.6zM1.5 12l3.4-1.3v2.6zM22.5 12l-3.4 1.3v-2.6zM4.6 4.6l3.3 1.5-1.8 1.8zM19.4 19.4l-3.3-1.5 1.8-1.8zM4.6 19.4l1.5-3.3 1.8 1.8zM19.4 4.6l-1.5 3.3-1.8-1.8z"/></svg>',
  ask: '<svg viewBox="0 0 24 24"><path d="M4 3h16a2.5 2.5 0 0 1 2.5 2.5v10A2.5 2.5 0 0 1 20 18H10l-5.2 3.9c-.5.4-1.3 0-1.3-.6V18A2.5 2.5 0 0 1 1.5 15.5v-10A2.5 2.5 0 0 1 4 3z"/></svg>',
  pujas: '<svg viewBox="0 0 24 24"><path d="M12 2c1.9 2.6 2.6 4.4 2.6 5.7A2.6 2.6 0 0 1 12 10.3a2.6 2.6 0 0 1-2.6-2.6C9.4 6.4 10.1 4.6 12 2z"/><path d="M2 12.5h20c-.6 4.4-4.8 7.5-10 7.5S2.6 16.9 2 12.5z"/><rect x="8" y="20.5" width="8" height="2" rx="1"/></svg>',
  tools: '<svg viewBox="0 0 24 24"><rect x="2" y="2" width="9" height="9" rx="2.4"/><rect x="13" y="2" width="9" height="9" rx="2.4"/><rect x="2" y="13" width="9" height="9" rx="2.4"/><rect x="13" y="13" width="9" height="9" rx="4.5"/></svg>',
  me: '<svg viewBox="0 0 24 24"><circle cx="12" cy="7.5" r="5"/><path d="M2.5 22c.6-5 4.6-8 9.5-8s8.9 3 9.5 8z"/></svg>',
};
function tabbar(dark) {
  const t = [['today', 'Today'], ['ask', 'Ask'], ['pujas', 'Pujas'], ['tools', 'Tools'], ['me', 'Me']];
  return `<nav class="tabbar${dark ? ' dark' : ''}">` + t.map(([k, l], i) =>
    `<a href="${['/', '/ask', '/alchemies/category/pujas', '/tools', '/profile'][i]}" class="${i === 0 ? 'on' : ''}">${ICON[k]}<span>${l}</span></a>`).join('') + '</nav>';
}
function statusbar(color, time) {
  return `<div class="status" style="color:${color}"><span>${time || '9:32'}</span><span class="r">
    <svg width="18" height="12" viewBox="0 0 18 12" fill="${color}"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>
    <svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="${color}" opacity=".5"/><rect x="2" y="2" width="16" height="8" rx="2" fill="${color}"/><rect x="24" y="4" width="2" height="4" rx="1" fill="${color}" opacity=".5"/></svg></span></div>`;
}
// ?v=phone (default) or ?v=desktop
const VIEW = new URLSearchParams(location.search).get('v') || 'phone';
document.documentElement.dataset.view = VIEW;
