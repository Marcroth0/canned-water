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

        $('.AddToWishlist').click(function (e) {
            e.preventDefault();

            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
        
            $.ajax({
                method: "POST",
                url: "/add_to_wish_list/",
                data: {
                    'product_id': product_id,
                },
                headers: { 'X-CSRFToken' : token },
                success: function (request) {
                    
                    alert(request.responseText);
                }
            });
        });
    });

