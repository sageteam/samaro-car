
$(window).on('load', function () {
    $('#btn-goTop').hide();
    $('.loader').fadeOut();
    $('.container-loader').css('background-color', 'transparent');
    $('#preload').fadeIn();
});

$("#btn-goTop").click(function () {
    var body = $("html, body");
    body.stop().animate({
        scrollTop: 0
    }, 500, 'swing', function () {
        
    });
});

$(document).ready(function() {
    scrollIsTop(); 
    $(window).scroll(scrollIsTop);
});

function scrollIsTop() { 
    var scrollPos = window.pageYOffset || document.documentElement.scrollTop; 
    if (scrollPos > 300) { 
        $('#btn-goTop').fadeIn(300); 
    } else { 
        $('#btn-goTop').fadeOut(300); 
    } 
} 

$("#btn-goTop").on({
    mouseenter: function () {
        $(this).children().animate({
            marginBottom: '-=8px'
        });
    },
    mouseleave: function () {
        $(this).children().animate({
            marginBottom: '+=8px'
        });
    },
});

$('.has-icon').mouseover(function () {
    $(this).html(
        'خروج <img class="icon" src="../../assets/img/dashboard/icons/nav/exit-yellow.svg" alt="">'
    )
}).mouseout(function () {
    $(this).html('خروج <img class="icon" src="../../assets/img/dashboard/icons/nav/exit.svg" alt="">')
});


$('.closeSideNav').click(function () {
    $('#sidenav_id').hide("fast");
    $('.main').css('margin-right', '0px');
    $('.navbar-collapse').css('margin-right', '20px');
    $('#btn-goTop').css('right', '20px');
});
$('.openSideNav').click(function () {
    $('#sidenav_id').show("fast");
    $('.main').css('margin-right', '250px');
    $('.navbar-collapse').css('margin-right', '250px');
    $('#btn-goTop').css('right', '280px');
});


$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});

$(document).ready(function () {
    $('#origin').click(function (event) {
        $('#chb-origin').toggle("slow", "linear");
    });

    $('#origin').focusout(function () {
        $('#chb-origin').hide("fast");
    });

    $('#origin').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-origin a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-origin a').click(function () {
        $('#origin').val($(this).text())
    });
});

$(document).ready(function () {
    $('#origin-region').click(function (event) {
        $('#chb-origin-region').toggle("slow", "linear");
    });

    $('#origin-region').focusout(function () {
        $('#chb-origin-region').hide("fast");
    });

    $('#origin-region').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-origin-region a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-origin-region a').click(function () {
        $('#origin-region').val($(this).text())
    });
});

$(document).ready(function () {
    $('#destination').click(function (event) {
        $('#chb-destination').toggle("slow", "linear");
    });

    $('#destination').focusout(function () {
        $('#chb-destination').hide("fast");
    });

    $('#destination').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-destination a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-destination-region a').click(function () {
        $('#destination-region').val($(this).text())
    });
});

$(document).ready(function () {
    $('#destination-region').click(function (event) {
        $('#chb-destination-region').toggle("slow", "linear");
    });

    $('#destination-region').focusout(function () {
        $('#chb-destination-region').hide("fast");
    });

    $('#destination-region').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-destination-region a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });
});

$(document).ready(function () {
    $('#bag-status').click(function (event) {
        $('#chb-bag-status').toggle("slow", "linear");
    });

    $('#bag-status').focusout(function () {
        $('#chb-bag-status').hide("fast");
    });

    $('#bag-status').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-bag-status a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-bag-status a').click(function () {
        $('#bag-status').val($(this).text())
    });
});


$(document).ready(function () {
    $('#date').click(function (event) {
        $('#chb-date').toggle("slow", "linear");
    });

    $('#date').focusout(function () {
        $('#chb-date').hide("fast");
    });

    $('#date').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-date a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-date a').click(function () {
        $('#date').val($(this).text())
    });
});


$(document).ready(function () {
    $('#day').click(function (event) {
        $('#chb-day').toggle("slow", "linear");
    });

    $('#day').focusout(function () {
        $('#chb-day').hide("fast");
    });

    $('#day').on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#chb-day a").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $('#chb-day a').click(function () {
        $('#day').val($(this).text())
    });
});

$(document).ready(function () {
    var state = 0;
    $('.accor-item .content').click(function () {
        if (state == 0) {
            state = 1
            $(this).next().html('<i class="fa fa-chevron-up"></i>')
        } else if (state == 1) {
            state = 0
            $(this).next().html('<i class="fa fa-chevron-down"></i>')
        }
    });
});

$('#owl-one').owlCarousel({
  rtl: true,
  loop: true,
  margin: 10,
  nav: true,
  autoplay: true,
  autoplayTimeout: 10000,
  smartSpeed: 900,
  navText: ["<i class='fa fa-chevron-right'></i>", "<i class='fa fa-chevron-left'></i>"],
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 1
    },
    1000: {
      items: 2
    }
  }
});

$(document).ready(function () {
  $(".navbar").sticky({
    topSpacing: 0
  });
});
