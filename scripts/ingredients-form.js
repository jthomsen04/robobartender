$(document).ready(function() {
	$('.drink-type-header').click(function() {
		var siblings = $(this).siblings('drink-list');
		siblings.css('display', 'block');
		
	});
});

