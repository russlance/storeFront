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
    $.ajax({
        url: "/navbar",
        method: "get",
        success: function(data){
            var html_str=""
            html_str+= data
            document.getElementById("top_navbar").innerHTML= html_str
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

    $(document).on("submit", '#loginform', function(event){
        event.preventDefault();
        var data = {
            user_email: $('#user_email').val(),
            user_password: $("#user_password").val(),
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').attr('value')
        }
        var route = "/users/login"
        $.ajax({
            url:route,
            type: "post",
            data: data,
            success: function(data){
                $("#login_modal").modal('hide')
                var html_str=""
                html_str+= data
                document.getElementById("top_navbar").innerHTML= html_str
            }
        })
    })
    
    $(document).on("submit", '#registerform', function(event){
        event.preventDefault();
        var data = {
            user_first_name:$('user_first_name').val(),
            user_last_name:$("user_last_name").val(),
            user_email: $('#user_email').val(),
            user_password: $("#user_password").val(),
            user_password_conf:$("user_password_conf").val(),
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').attr('value')
        }
        var route = "/users/login"
        $.ajax({
            url:route,
            type: "post",
            data: data,
            success: function(data){
                $("#register_modal").modal('hide')
                var html_str=""
                html_str+= data
                document.getElementById("top_navbar").innerHTML= html_str
            }
        })
    })
})
// Navbar Methods

function display_events()
{
    $.ajax({
        url: "/events",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
}

function display_directions()
{
    $.ajax({
        url: "/directions",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
}

function display_cart()
{
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
}
function display_news()
{
    $.ajax({
        url: "/news",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
}
function display_home()
{
    $.ajax({
        url: "/home",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
}
// Product browsing methods
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

function show_product(id)
{
    $.ajax({
        url:"/products/"+id,
        method: "get",
        success: function(data){
            var html_str = ""
            html_str += data
            console.log(html_str)
            document.getElementById("content").innerHTML = html_str;
        }
    })
}

// Checkout Methods
function update_quantity(id)
{
    var data= {
        item_quantity:$("input[name='item_quantity]").val()
    }
    $.ajax({
        url:"/products/update_quantity/"+id,
        type: "post",
        data: data,
        success: function(data){
            var html_str=""
            html_str+=data
            document.getElementById("content").innerHTML= html_str
        }
    })
}
