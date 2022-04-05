$(document).ready(function () {

        $(document).ready(function() {
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
    });

        $('.toast').toast('show');
    
        $(window).ready(function () {
            $(".load-spinner").fadeOut("slow")
            $(".load-spinner2").fadeOut("fast");
    });
});
