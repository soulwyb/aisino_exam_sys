
$(function(){
    var flag = 0;
    var title = '';
    var is_question_bank = false;
    var height = $(document).outerWidth(true);

// 点击按钮 根据条件出现遮罩层
    function pop_label (label_name, label_title){
        if (title == ''){
            $('#custom-layer-display').css({"display":"block","height":height});
            $("#custom-warning-pop span").text("亲，您没有选择任何组织或部门哦~");
            $('#custom-warning-pop').fadeIn('fast').css("display","block");
        }
        else {
            $('#custom-layer-display').css({"display":"block","height":height});
            $(label_name).css("display","block");
            $('.custom-pop-title').text(label_title + " - " + title);
            flag=1;
        }
    };


    $("#custom-tree-header").click(function () {
        title = "";
    })

// 题库或组织添加
    $('#create_department').click(function(){
        if (is_question_bank){
            $("#custom-warning-pop span").text("亲，不要选择题库哦~");
            $('#custom-layer-display').css({"display":"block","height":height});
            $("#custom-warning-pop").css("display", "block");
        }
        else {
            pop_label('#custom-float-add', '题库添加');
        }
    });

// 题库或组织编辑
    $('#edit_department').click(function(){
        pop_label('#custom-float-edit', '题库编辑');
        $('#custom-input-value').attr("value",title);
    });

// 删除部门或题库
    $('#del_department').click(function(){
        if(confirm('您确认要删除该题库或部门么(该题库下的考题或部门下的题库将全部删除!)?')) {
            pass;
        };
    });

// 导入题库
    $('#input_department').click(function(){
        pop_label('#custom-float-input', '题库导入');
    });

// 组织部门树形菜单已点击标记
    $('.custom-tree-selected').click(function(){
        $("#custom-tree-js").find(".custom-tree-selected").removeAttr('id');
        $("#custom-tree-js").parents(".custom-tree-selected").removeAttr('id');
        $(this).attr("id","custom-active");
        if($(this).attr("type") == "question_bank"){
            is_question_bank = true;
        }
        else{
            is_question_bank = false;
        }
        title = $('#custom-active').text();
    });

// 警告框关闭
    $('.close').click(function(){
        $('#custom-warning-pop').css("display","none");
        $('#custom-layer-display').css("display","none");
    });

// 弹出窗取消按钮
    $('.custom-close-btn').click(function(){
        $('.custom-div-hidden').css("display", "none");
        $('#custom-layer-display').css("display", "none");
    });
})