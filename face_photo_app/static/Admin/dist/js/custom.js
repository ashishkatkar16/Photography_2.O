$(function () {
	$(".sidebar-dropdown > a").click(function() {
		$(".sidebar-submenu").slideUp(200);
		if ($(this).parent().hasClass("active")) {
			$(".sidebar-dropdown").removeClass("active");
			$(this).parent().removeClass("active");
		} else {
			$(".sidebar-dropdown").removeClass("active");
			$(this).next(".sidebar-submenu").slideDown(200);
			$(this).parent().addClass("active");
		}
	});

	$("#close-sidebar").click(function() {
		$(".page-wrapper").removeClass("toggled");
	});

	$("#show-sidebar").click(function() {
		$(".page-wrapper").addClass("toggled");
	});
});

$(document).ready(function() {
    if($(window).width() < 767)
    {	
        $(".page-wrapper").removeClass('toggled');
    } else {
        $(".page-wrapper").addClass('toggled');
    }
});
$(".inputfile").change(function (e) {
  $(this).parents(".uploadFile").find(".filename").text(e.target.files[0].name);
});

$(document).ready(function(){
	$('.show').change(function(){
		if($(this).is(':checked')){
			$('.org').show();
		} else {
			$('.org').hide();
		}
	});
});