$(function(){
    $('#create_department').focus(function(){
        var height = $(document.body).outerWidth(true);
        $('#custom-layer-display').css({"display":"block","height":height});
        $('#custom-float-display').css("display","block");
    });
})