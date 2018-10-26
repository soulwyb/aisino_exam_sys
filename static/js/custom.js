$(function(){
    var flag = 0;
    $('#create_department').click(function(){
        var height = $(document).outerWidth(true);
        var title = $('[id="custom-active"]').children('a').text();
        if (title == ''){
            $('#custom-layer-display').css({"display":"block","height":height});
            $('#custom-warning-pop').fadeIn('fast').css("display","block");
        }
        else {
            $('#custom-layer-display').css({"display":"block","height":height});
            $('#custom-float-display').css("display","block");
            $('#custom-pop-box-title').text("题库添加 - " + title);
            flag=1;
        }
    });
    $('.custom-tree-selected').click(function(){
        $("#custom-tree-js").find(".custom-tree-selected").removeAttr('id');
        $(this).attr("id","custom-active");
    });
    $('.close').click(function(){
        $('#custom-warning-pop').css("display","none");
        $('#custom-layer-display').css("display","none");
    })
})