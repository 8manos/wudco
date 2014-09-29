$(document).on('ready', function(){
	$('nav .icon-menu').on('click', function(){
		$('.menu').addClass('is-visible');
	});
	$(document).on('click', function(e){
		if(!$(e.target).is('nav .icon-menu, nav .menu, nav .menu *')){
			$('.menu').removeClass('is-visible');
		}
	});
});