$(document).ready(function() {
	// Homepage Slideshow
	$('#rotator').cycle({
		fx: 'fade'
	});


    $(".fancied").fancybox({
		'transitionIn'		: 'none',
		'transitionOut'		: 'none',
		'titlePosition' 	: 'over',
		'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
			return '<span id="fancybox-title-over"></span>';
		}
	});

	$('#nav li a[href^=' + location.pathname + ']').addClass('active');

});	