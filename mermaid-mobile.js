(function () {
  var mq = window.matchMedia('(max-width: 639px)');
  function fit() {
    document.querySelectorAll('.mermaid svg[viewBox]').forEach(function (svg) {
      var vb = svg.getAttribute('viewBox').split(/\s+/).map(Number);
      var natural = Math.min(vb[2], 760);
      var box = svg.closest('.mermaid');
      if (mq.matches && natural > box.parentElement.clientWidth * 1.15) {
        svg.style.width = natural + 'px';
        svg.style.maxWidth = 'none';
        box.parentElement.style.overflowX = 'auto';
      } else {
        svg.style.width = '';
        svg.style.maxWidth = vb[2] + 'px';
        box.parentElement.style.overflowX = '';
      }
    });
  }
  new MutationObserver(function () { window.requestAnimationFrame(fit); })
    .observe(document.documentElement, { childList: true, subtree: true });
  mq.addEventListener('change', fit);
  fit();
})();
