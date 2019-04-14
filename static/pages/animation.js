$(function() {
    console.log("ready")
        $("#header-btn").on('click', function(e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $(".main-mid-container").offset().top -140
            }, 500);
        })
        
        window.onscroll = function() { stickyHeader() };
        var navbar = document.getElementById("navbar");
        console.log(navbar);
        var sticky = navbar.offsetTop;
        function stickyHeader() {
                if (window.pageYOffset > sticky) {
                        navbar.classList.add("sticky");
                } else {
                        navbar.classList.remove("sticky");
                }
        }
});

