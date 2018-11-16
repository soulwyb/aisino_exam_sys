$(function(){

    // 新建题库或者组织
     $('#custom-add-groups').click(function(){
        var input_type = $('input:radio[name="r1"]:checked').attr("group-values");
        var name = $("#custom-name").val();
        var father_group = $("#custom-float-add .custom-pop-title").text().split(" - ")[1];
        var is_question = $('.custom-float-add custom-pop-title').attr('id');
        var name_id = $('#custom-active > i').attr('id')
         if(!name){
             alert('亲，名称不能为空哦~');
         }else if(is_question == 'question'){
             alert('亲，题库下面不能再增加东西咯哦~');
         }else{
             $.ajax({
                cache:false,
                type: "POST",
                url: create_urls,
                data: { 'input_type' : input_type, 'name' : name, 'father_group': father_group, 'name_id': name_id},
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
     });

     // 编辑题库或组织
    $('#custom-edit-groups').click(function(){
        var new_name = $("#custom-input-value").val();
        var old_name = $("#custom-float-edit .custom-pop-title").text().split(" - ")[1];
        var old_name_id = $('#custom-active > i').attr('id')
        if(!name) {
            alert('亲，名称不能为空哦~');
        }else{
            $.ajax({
                cache:false,
                type: "POST",
                url: edit_urls,
                data: { 'new_name' : new_name, 'old_name': old_name, 'old_name_id': old_name_id },
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

    // 删除部门或题库
    $('#del_department').click(function(){
        var name_id = $('#custom-active > i').attr('id')
        if(confirm('您确认要删除该题库或部门么(该题库下的考题或部门下的题库将全部删除!)?')) {
            $.ajax({
                cache: false,
                type: "POST",
                url: del_urls,
                data: {'name': title, 'name_id':name_id},
                async: false,
                beforeSend: function(xhr, settings){
                    xhr.setRequestHeader("X-CSRFToken", $('#csrf_token').val());
                },
                success: function(data){
                    if(data.status == 'success'){
                        alert('删除成功。');
                        location.reload();
                    }
                    else if(data.status == "fail"){
                        alert(data.msg);
                    }
                }
            })
        };
    });

    // 上传考题
    $('#custom_upload_file').click(function(){
            var form_data = new FormData();
            var file_info = $('#file')[0].files[0];
            form_data.append(file, file_info);
            $.ajax({
                url: "",
                type: 'POST',
                async: false,
                data: form_data,
                processData: false,
                contentType: false,
                success: function(data){
                    if(data.status == 'success'){
                        pass
                    }else if(data.status == 'fail'){
                        pass
                    }
                }
            })
    });

})