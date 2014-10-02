$(document).on('ready', function(){
	$('nav .icon-menu').on('click', function(){
		$('.menu').addClass('is-visible');
	});
	$(document).on('click', function(e){
		if(!$(e.target).is('nav .icon-menu, nav .menu, nav .menu *')){
			$('.menu').removeClass('is-visible');
		}
	});

	var scrollTimeout;

	$(window).scroll(function () {
		if (scrollTimeout) {
			clearTimeout(scrollTimeout);
			scrollTimeout = null;
		}
		scrollTimeout = setTimeout(fixNav, 100);
	});

	fixNav = function(){
		var ScrollTop = $(window).scrollTop();
		if(ScrollTop >= $('.nav-container').offset().top){
			$('nav').addClass('is-fixed');
			var nav_height = $('nav').innerHeight();
			$('header').css('margin-bottom', nav_height);
		}
		else{
			$('nav').removeClass('is-fixed');
			$('header').css('margin-bottom', 0);
		}
	};

	$('.video a').asyncml();
});