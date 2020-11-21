$(document).ready(function() {
    $.ajax({
        url: "/home",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
    $("#AboutUs").click(function() {
        $.ajax({
            url: "/about_us",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#home").click(function() {
        $.ajax({
            url: "/home",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#profile-tab").click(function() {
        $.ajax({
            url: "/news",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#directions").click(function() {
        $.ajax({
            url: "/directions",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#contactUs").click(function() {
        $.ajax({
            url: "/contact_us",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#events").click(function() {
        $.ajax({
            url: "/events",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })
    $("#cart").click(function() {
        $.ajax({
            url: "/cart",
            method: 'get',
            success: function(data) {
                var html_str = ""
                html_str += data
                console.log(html_str)
                document.getElementById("content").innerHTML = html_str;
            }
        })
    })

    // Do not use this until render route to new navbar.html created
    
    // $(document).on("submit", '#loginform', function(event){
    //     event.preventDefault();
    //     var data = {
    //         user_email: $('#user_email').val(),
    //         user_password: $("#user_password").val()
    //     }
    //     var token = $('input[name="csrfToken"]').attr('value')
    //     $.ajaxSetup({
    //         beforeSend: function(xhr){
    //             xhr.setRequestHeader('Csrf-Token', token)
    //         }
    //     });
    //     var route = "/user/login"
    //     $.ajax({
    //         url:route,
    //         type: "post",
    //         data: data,
    //         success: function(data){
    //             var html_str=""
    //             html_str+= data
    //             document.getElementById("top_navbar").innerHTML= html_str
    //         }
    //     })
    // })
})
function loadCategory(id) {
    $.ajax({
        url: "/category/" + id,
        method: "get",
        success: function(data) {
            var html_str = ""
            html_str += data
            console.log(html_str)
            document.getElementById("content").innerHTML = html_str;
        }
    })
}

