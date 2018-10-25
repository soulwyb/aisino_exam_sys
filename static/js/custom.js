$(function(){
    var flag = 0;
    $('#create_department').click(function(){
        var height = $(window).outerWidth(true);
        var title = $('[id="custom-active"]').children('a').text();
        $('#custom-layer-display').css({"display":"block","height":height});
        $('#custom-float-display').css("display","block");
        $('#custom-pop-box-title').text("题库添加 - " + title);
        flag=1;
    });
    $('.custom-tree-selected').click(function(){
        $("#custom-tree-js").find(".custom-tree-selected").removeAttr('id');
        $(this).attr("id","custom-active");
    });
})