
$(function(){
    var flag = 0;
    var title = '';
    // 点击按钮 根据条件出现遮罩层
    function pop_label (label_name, label_title){
        var height = $(document).outerWidth(true);
        if (title == ''){
            $('#custom-layer-display').css({"display":"block","height":height});
            $('#custom-warning-pop').fadeIn('fast').css("display","block");
        }
        else {
            $('#custom-layer-display').css({"display":"block","height":height});
            $(label_name).css("display","block");
            $('.custom-pop-title').text(label_title + " - " + title);
            flag=1;
        }
    };
    $('#create_department').click(function(){
        pop_label('#custom-float-add', '题库添加');
    });

    $('#edit_department').click(function(){
        pop_label('#custom-float-edit', '题库编辑');
        $('#custom-input-value').attr("value",title);
    });

    $('#del_department').click(function(){
        if(confirm('您确认要删除该题库或部门么(该题库下的考题或部门下的题库将全部删除!)?')) {
            pass;
        };
    });

    $('#input_department').click(function(){
        pop_label('#custom-float-input', '题库导入');
    });

    $('.custom-tree-selected').click(function(){
        $("#custom-tree-js").find(".custom-tree-selected").removeAttr('id');
        $("#custom-tree-js").parents(".custom-tree-selected").removeAttr('id');
        $(this).attr("id","custom-active");
        // alert($(this).html());
        title = $('#custom-active').text();
    });
    $('.close').click(function(){
        $('#custom-warning-pop').css("display","none");
        $('#custom-layer-display').css("display","none");
    });

    $('#custom-pop-close').click(function(){
        $('#custom-layer-display').css("display","none");
        $('#custom-float-display').css("display","none");
    });
})