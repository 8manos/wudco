var imgOrientation = function($pic){
	var w = $pic.innerWidth();
	var h = $pic.innerHeight();

	if(w > h){
		return 'horizontal';
	}
	else if(w < h){
		return 'vertical';
	}
	else if(w == h){
		return 'square';
	}
}

var adjustImgs = function($carousel){
	$carousel.find('img').each(function(){
		if(imgOrientation($(this)) == 'horizontal'){
			$(this).css({
				'height': 'auto',
				'width': '100%'
			});
		}
		else if(imgOrientation($(this)) == 'vertical'){
			$(this).css({
				'height': '100%',
				'width': 'auto'
			});
		}

		if($(this).innerHeight() > $(this).parent().innerHeight()){
			$(this).css({
				'height': '100%',
				'width': 'auto'
			});
		}

		else if($(this).innerWidth() > $(this).parent().innerWidth()){
			$(this).css({
				'height': 'auto',
				'width': '100%'
			});
		}
	});
}

$(window).on('load', function(){
	if($('.owl-carousel').length > 0){
		var $carousel = $('.owl-carousel').owlCarousel({
			dots: false,
			fluidSpeed: true,
			items: 1,
			loop: true,
			nav: true,
			navContainer: '.carousel-controls',
			navText: ['<i class="icon-prev"></i>', '<i class="icon-next"></i>']
		});
		adjustImgs($carousel);
	}
});

$(window).on('resize', function(){
	if($('.owl-carousel').length > 0){
		adjustImgs($('.owl-carousel'));
	}
});

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