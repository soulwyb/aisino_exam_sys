$(function () {
    // $.ajaxSetup({
    //     beforeSend: function(xhr, settings){
    //         var csrftoken = $.cookie('csrftoken');
    //         xhr.setRequestHeader("X-CSRFToken");
    //     }
    // });
    $('#custom-add-groups').click(function(){
        var type = $('input:radio[name="r1"]:checked').attr("group-values");
        var value = $(".custom-add-margin > input").val();
        var father_group = $("#custom-float-add .custom-pop-title").text().split(" - ")[1];

        if (value == '') {
            alert("亲，名称不能为空哦~");
        }
        else {
            $.ajax({
                cache:false,
                type: "POST",
                url: "{% url 'question_bank' %}",
                data: { 'group_name' : father_group, 'type': type, 'name' : value },
                async: true,
                beforeSend: function(xhr, settings){
                    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
                },
                success: function(data){
                    if(data.status == 'fail'){
                        alert('fail');
                    }
                    else {
                        alert(data.msg);
                    }
                },
            });
                //             alert("success");
                // $('.custom-div-hidden').css("display", "none");
                // $('#custom-layer-display').css("display", "none");
                // $('#custom-tree-js').fresh();
        }
    });
})