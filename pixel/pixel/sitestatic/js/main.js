$("nav>li>a").click(function(){
	$("*").removeClass("active");
    $(this).addClass("active");
});