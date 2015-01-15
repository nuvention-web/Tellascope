$(document).ready(function (){
  function scrollTo(section) {
    var sticky_nav = $('.main-nav').outerHeight();
    $('html,body').animate({scrollTop: $(section).offset().top - sticky_nav}, 800);
  }
  // sticky nav
  var mn = $(".main-nav");
    mns = "main-nav-scrolled";
    var sticky_navigation_offset_top = $('.main-nav').offset().top;

  $('#link-about').on('click', function(e) {
    e.preventDefault();
    scrollTo('#about');
  });

  $('#link-learn').on('click', function(e) {
    e.preventDefault();
    scrollTo('#learn');
  });

  $('#link-team').on('click', function(e) {
    e.preventDefault();
    scrollTo('#team');
  });
  
  $(window).scroll(function() {
    if( $(this).scrollTop() > sticky_navigation_offset_top ) {
      mn.addClass(mns);
    } else {
      mn.removeClass(mns);
    }
  });
});