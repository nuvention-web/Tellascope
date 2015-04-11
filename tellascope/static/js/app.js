var tellascope = tellascope || {};
tellascope.post = tellascope.post || {};
var user_id;
var opened = false;

tellascope.post.init = function(opts) {
  options = opts;
  user_id = options.user_id;
};


// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$(document).ready(function (){

  // pocket form
  $('label').hide();
  $('.filter-form p:first').prepend('I feel like reading a ');
  $('.filter-form p:first').append(' minute article ');
  $('.filter-form p:nth-child(2)').prepend('that is ');

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

  // SHARE CONTAINER FUNCTIONALITY
  $('.open-share-button').click(function(e) {
    console.log(this);
    $(this).children().hide();
    itemId = $(this).data('itemId');
    $shareContainer = $('#uar-' + itemId + ' .article-share-container');
    $shareContainer.addClass('opened');
    opened = true;
    e.stopPropagation();
    e.preventDefault();
    $('#form-' + itemId).focus();
  });

  function closeShareContainer(itemId) {
    $shareContainer = $('#uar-' + itemId + ' .article-share-container');
    $shareContainer.removeClass('opened');
  }

  $(".share-uar textarea").bind('keypress', function(e) {
    if ((e.keyCode || e.which) == 13) {
      if (!opened) {
        return false;
      }
      $(this).parents('.grid-item').addClass('public')
      $(this).parents('form').submit();
      return false;
    }
  });

  $('.share-uar input[type="submit"]').on('click', function(e) {
    $(this).parents('.grid-item').addClass('public')
    $(this).parents('form').submit();
    return false;
  });

  $('.fa-close').on('click', function() {
    console.log(this);
    itemId = $(this).parent().next().data('itemId');
    closeShareContainer(itemId);
    // get share to show up if person x'ed out of it
    var share_icon = $(this).parent().parent().prev().children().children().children();
    console.log(share_icon);
    share_icon.show();
  });

  $('.share-uar').submit(function(e){

    e.preventDefault();

    if (!opened) { return false; }
    console.log(e);
    window.e = e;

    itemId = $(e.target).data('itemId');

    var $form = $('#form-' + itemId);

    var values = {};
    var inputs = $form.serializeArray();
    $.each(inputs, function (i, input) {
        values[input.name] = input.value;
    });

    console.log(values);
    window.v = values;

    $.ajax({
      type: "POST",
      url: "/api/uar/post/makepublic/",
      data: $form.serializeArray(),
      complete: function(data) { console.log(data); },
      success: function(data) { console.log(data); },
      error: function(data) { console.log(data); }
    });

    opened = false;
    closeShareContainer(itemId);
  });

  $('.article-share-container').click(function(e){
    e.stopPropagation();
    e.preventDefault();
  });

  $('.update-pocket').click(function(e) {
    // show spinner
    
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/api/user/post/refreshpocket/",
      complete: function(data) {
        // hide spinner 
        console.log(data); 
      },
      success: function(data) { console.log(data); },
      error: function(data) { console.log(data); }
    });
  })

  $('#youTab').on('click', function() {
    $("#youTab").css("color","white");
    $("#youTab").css("background-color","black");
    $("#tellascopeTab").css("color","black");
    $("#tellascopeTab").css("background-color","white");
  });

  $('#tellascopeTab').on('click', function() {
    $("#youTab").css("color","black");
    $("#youTab").css("background-color","white");
    $("#tellascopeTab").css("color","white");
    $("#tellascopeTab").css("background-color","black");
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
