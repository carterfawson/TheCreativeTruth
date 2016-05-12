$(document).ready(function() {

    $(".hide-search").hide();
    $(".nav-drop").click(function() {
        $(".hide-search").toggle("fast");
        $(".nav-hide").toggle("slow");
    })

});
