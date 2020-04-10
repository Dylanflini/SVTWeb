$('.navbar a').on('click', function(e) {
    if (this.hash !== '') {
        e.preventDefault();
        const hash = this.hash;

        $('html, body').animate({
            scrollTop: $(hash).offset().top - $(".navbar a").height()
        }, 800);
    }
});

$('.view a').on('click', function(e) {
    if (this.hash !== '') {
        e.preventDefault();
        const hash = this.hash;

        $('html, body').animate({
            scrollTop: $(hash).offset().top - $(".navbar a").height()
        }, 800);
    }
});