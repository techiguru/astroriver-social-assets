// Shared by render.js and audit.js.
// Large text: body text x1.3, tapering to x1.0 for display type of 40px and up; app chrome keeps its size, as on iOS.
const LARGE = () => {
  for (const el of document.querySelectorAll('body *')) {
    if (el.closest('.top,.tabbar,.status,.dm')) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const k = fs <= 18 ? 1.3 : fs >= 40 ? 1 : 1.3 - 0.3 * (fs - 18) / 22;
    el.dataset.fs = fs * k;
  }
  for (const el of document.querySelectorAll('[data-fs]')) el.style.fontSize = el.dataset.fs + 'px';
};
module.exports = { LARGE };
