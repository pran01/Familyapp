const profileBtn=document.querySelector('#profile-btn');
const arrow=document.querySelector('#arrow');
const menu = document.querySelector(".home-menu");


function changeArrow() {
    if (arrow.className === 'fas fa-angle-double-down') {
        arrow.className = 'fas fa-angle-double-up';
        moveDown();
    }
    else{
        arrow.className = 'fas fa-angle-double-down';
        moveUp();
    }
};

profileBtn.addEventListener('click',changeArrow);

function moveDown() {
  var pos = 0;
  var id = setInterval(frame1, 1);
  function frame1() {
    if (pos === 85) {
      clearInterval(id);
    } else {
      pos++;
      menu.style.marginTop = pos + 'px';
    }
  }
};

function moveUp() {
  var pos = 85;
  var id = setInterval(frame2, 1);
  function frame2() {
    if (pos === 0) {
      clearInterval(id);
    } else {
      pos--;
      menu.style.marginTop = pos + 'px';
    }
  }
};