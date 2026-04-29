// MathJax v3 configuration for the OPM Flow Reference Manual.
// Renders $...$ for inline math and $$...$$ for display math, matching
// the LaTeX produced by the FODT MathML → LaTeX converter.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise();
  }
});
