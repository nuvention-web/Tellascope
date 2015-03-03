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

  // search bar
  $('input').keypress(function(e) {
    if (e.which == 13) {
      $('form').submit();
    }
  });

  function arraysAreIdentical(arr1, arr2){
    if (arr1.length !== arr2.length) return false;
    for (var i = 0, len = arr1.length; i < len; i++){
        if (arr1[i] !== arr2[i]){
            return false;
        }
    }
    return true; 
  }

  var old_tags = $('input').val().split(',');
  // refresh form when user backspaces and deletes tags in search bar
  $('input').keyup(function(e) {
    if (e.which == 8) {
      new_tags = $('input').val().split(',');
      if (arraysAreIdentical(old_tags, new_tags) == false) {
        $('form').submit();
      }
      // console.log(new_tags);
      // console.log(arraysAreIdentical(old_tags, new_tags));
    }
  });

  // refresh form when clicking to delete tags in search bar
  $('.tag a').on('click', function(event) {
    event.preventDefault();
    $('form').submit();
  });

  $('.fa-share').on('click', function(e){
    e.preventDefault();
    id = this.id;
    var inst = $.remodal.lookup[$('[data-remodal-id='+id+']').data('remodal')];
    inst.open();
    e.stopPropagation();
  });
});

$(document).on('click', '.article-tag', function(event) {
  event.preventDefault();
  var tag = $(this).text();

  if ($('#id_tags').val().length == 0) {
    $('#id_tags').val( $('#id_tags').val() + tag );
  } else {
    $('#id_tags').val( $('#id_tags').val() + ',' + tag );
  }

  $('<span class="tag"><span>' + tag + '&nbsp;&nbsp;</span><a href="#" title="Removing tag">x</a></span>').appendTo('#id_tags_addTag');
  $('form').submit();
});