function re_data(data,csrf_token){
    res_data={
        'csrfmiddlewaretoken':csrf_token,
        'data':data
    };
    return res_data
}
function onprogress(evt){
  var loaded = evt.loaded;     //已经上传大小情况
  var tot = evt.total;      //附件总大小
  var per = Math.floor(100*loaded/tot);  //已经上传的百分比
  console.log(per)
  }
function my_ajax(url,type,data,func,obj,len){
    //打包ajax函数
    var res;
    if(obj){
        $.ajax({
            'url':url,
            'type':type,
            'data':data,
            'processData': false,
             'contentType': false,
            'dataType':'json',
            // 'async':false,
            xhr:function(){
                var xhr = $.ajaxSettings.xhr();
                if (xhr.upload) {
                    xhr.upload.addEventListener('progress', function(e) {
                    }, false);
                }
                return xhr;
            }
        }).then(function(data){
                res =  data;
                if(len){
                    now++;
                    progress_bar($('.progress-bar'),len);
                }
                func(res);

            console.log(data)
        });

    }else{
        $.ajax({
            'url':url,
            'type':type,
            'data':data,
            'dataType':'json',
            // 'async':false,
            'success':function (data) {
                res =  data;

                func(res)


            }
        });
    }

    return res
}

//对输入进来的参数进行判断
function check_log(name,phone,password){
    if(name.length>=20 || name.length <=5){
        post_error.name_error = '姓名长度错误';
        console.log('姓名长度错误');
        return false
    }
    if(phone.length!==11){
        post_error.phone_error = '手机号长度错误';
        console.log('手机号长度错误');
        return false
    }
    if(password.length>=20 || password.length <=8){
        post_error.password_error = '密码长度错误';
        console.log('密码长度错误');
        return false
    }
    return true

}
function wrappers_load(){
    var my_input = $('.input-wrapper input');
    var save_input = $('.pro_save input');
    save_input.on('blur',function(){
        var val = this.value;
        if (this.name === 'pro_name') {
            if (val.length === 0) {
                post_error.pro_name_error = '请输入产品名';
            }
        }
        if (this.name === 'pro_num'){
            if(val.length ===0){
                post_error.pro_num_error = '请输入产品编号';
            }
        }
        if(this.name === 'pro_price'){
            if(val.length ===0){
                post_error.pro_price_error = '请输入产品价格';
            }
        }
        if(this.name === 'pro_units'){
            if(val.length ===0){
                post_error.pro_units_error = '请输入产品单位';
            }
        }
        if(this.name==='pro_stock'){

            if(val.length ===0){
                post_error.pro_stock_error = '请输入产品数量';
            }
        }
    });
    save_input.on('focus',function(){
        if (this.name === 'pro_name'){
            post_error.pro_name_error = '';

        }
        if (this.name === 'pro_num'){
            post_error.pro_num_error = '';

        }
        if(this.name === 'pro_price'){
            post_error.pro_price_error = '';

        }
        if(this.name === 'pro_units'){
            post_error.pro_units_error = '';

        }
        if(this.name==='pro_stock'){
            post_error.pro_stock_error = '';
        }
    });
    my_input.on('blur',function(){
        var val = this.value;
        if(val.length ===0){
                post_error.name_error = '请填写姓名';
        }else if (this.name === 'user_name'){
            if(val.length>=20 || val.length <=5){
                post_error.name_error = '请填写正确的姓名';
            }
        }
        if (this.name === 'login_user_name'){
            if(val.length ===0){
                post_error.login_name_error = '请填写姓名';
            }else if(val.length>=20 || val.length <=5){
                post_error.login_name_error = '请填写正确的姓名';
            }
        }
        if(this.name === 'pass_word'){
            if(val.length ===0){
                post_error.password_error = '请填写密码';
            }else if(val.length>=20 || val.length <=8){
                post_error.password_error = '密码长度错误';
            }
        }
        if(this.name === 'login_pass_word'){

            if(val.length ===0){
                post_error.login_password_error = '请填写密码';
            }else if(val.length>=20 || val.length <=8){
                post_error.login_password_error = '请正确的密码';
            }
        }
        if(this.name==='phone_num'){

            if(val.length ===0){
                post_error.phone_error = '请填写手机号';
            }else if(val.length!==11){
                post_error.phone_error = '请填写正确手机号';

            }
        }
    });
    my_input.on('focus',function(){
        if (this.name === 'user_name'){
            post_error.name_error = '';

        }
        if (this.name === 'login_user_name'){
            post_error.name_error = '';

        }
        if(this.name === 'pass_word'){
            post_error.password_error = '';

        }
        if(this.name === 'login_pass_word'){
            post_error.password_error = '';

        }
        if(this.name==='phone_num'){
            post_error.phone_error = '';
        }
    });


}

function progress_bar(obj,len){
    obj.css('width',parseInt((now/len)*100)+'%');
    obj.html(parseInt((now/len)*100)+'%');
}
function progress_bat_re(obj){
    obj.width(0);
    obj.html('');
}

//获取数据
function pagination(limit,lens){
    if (lens < limit){
        return 0
    }else if(lens>limit){
        return parseInt(lens/limit)+1
    }

}

function initial(obj){
    var file = obj ;
        file.after(file.clone().val(""));
        file.remove();

}
function decodeUnicode(str) {
    str = str.replace(/\\/g, "%");
    return decodeURI(str);
}