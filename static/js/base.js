(function(){
  var wrapper = document.querySelector('.cols');
  
  wrapper.style.height = window.innerHeight + 'px';
  
  var cols = document.querySelectorAll('.col');
  window.colWidth = getColWidth(cols);
  
  [].forEach.call(cols, function(col){
    bindEvents.call(col);
    col.style.width = colWidth + 'px';
  });
  
  window.addEventListener('resize', function(e) {
    colWidth = getColWidth(cols);
    [].forEach.call(cols, function(col){handleMouseOut.call(col)});
    wrapper.style.height = window.innerHeight + "px";
  });
})();

function getColWidth(cols) {
  return window.innerWidth / cols.length;
}

function bindEvents() {
  this.addEventListener('mouseover', handleMouseOver.bind(this));
  this.addEventListener('mouseout', handleMouseOut.bind(this));
}

function handleMouseOver() {
  TweenLite.to(this, 0.3, {css: {width: colWidth + 250 + "px"}, ease: Quad.easeOut});
}

function handleMouseOut() {
  TweenLite.to(this, 0.3, {css: {width: colWidth + "px"}, ease: Quad.easeIn});
}