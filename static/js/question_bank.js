$(function(){

    // 新建题库或者组织
     $('#custom-add-groups').click(function(){
        var input_type = $('input:radio[name="r1"]:checked').attr("group-values");
        var name = $("#custom-name").val();
        var father_group = $("#custom-float-add .custom-pop-title").text().split(" - ")[1];
        var is_question = $('.custom-float-add custom-pop-title').attr('id');
         if(!name){
             alert('亲，名称不能为空哦~');
         }else if(is_question == 'question'){
             alert('亲，题库下面不能再增加东西咯哦~');
         }else{
             $.ajax({
                cache:false,
                type: "POST",
                url: urls,
                data: { 'input_type' : input_type, 'name' : name, 'father_group': father_group },
                async: false,
                beforeSend: function(xhr, settings){
                    xhr.setRequestHeader("X-CSRFToken", $('#csrf_token').val());
                },
                success: function(data){
                    if(data.status == 'fail'){
                        alert(data.msg);
                    } else if(data.status == 'success'){
                        alert(data.msg);
                        location.reload();
                    }
                },
            });
         }
     })
})