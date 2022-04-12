// Sidebar
$(document).ready(function () {
    $("#sidebarCollapse").on("click", function() {
        $("#sidebar").addClass("active");
    });

    $("#sidebarCollapseX").on("click", function() {
        $("#sidebar").removeClass("active");
    });

    $("#sidebarCollapse").on("click", function() {
        if ($("#sidebar").hasClass("active")) {
        $(".overlay").addClass("visible");
        }
    });

    $("#sidebarCollapseX").on("click", function() {
        $(".overlay").removeClass("visible");
    });

    $('.toast').toast('show');

    $(window).ready(function () {
        $(".load-spinner").fadeOut("slow")
        $(".load-spinner2").fadeOut("fast");
    });
});

// Automatic footer fixed to bottom
$(document).ready(function() {
    setInterval(function() {
        var docHeight = $(window).height();
        var footerHeight = $('#footer').height();
        var footerTop = $('#footer').position().top + footerHeight;
        var marginTop = (docHeight - footerTop + 10);

        if (footerTop < docHeight)
            $('#footer').css('margin-top', marginTop + 'px'); // padding of 30 on footer
        else
            $('#footer').css('margin-top', '0px');
    }, 250);
    
});

