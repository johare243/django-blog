$(function() {
    console.log("ready")
        $("#header-btn").on('click', function(e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $("#main-categories").offset().top +40
            }, 500);
        })
});
