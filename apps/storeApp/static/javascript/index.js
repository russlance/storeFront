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
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("top_navbar").innerHTML = html_str
        }
    })
    $('.toast').toast({
        autohide: false
    })
    $(".toast").toast("show")
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

    $(document).on("submit", '#loginform', function(event) {
        event.preventDefault();
        var data = {
            login_email: $('#login_email').val(),
            login_password: $("#login_password").val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
        }
        var route = "/users/login"
        $.ajax({
            url: route,
            type: "post",
            data: data,
            success: function(data) {
                $("#login_modal").modal('hide')
                var html_str = ""
                html_str += data
                document.getElementById("top_navbar").innerHTML = html_str
            }
        })
    })

})

$(document).on("submit", '#registerform', function(event) {
    event.preventDefault();
    var data = {
        user_first_name: $('#user_first_name').val(),
        user_last_name: $("#user_last_name").val(),
        user_email: $('#user_email').val(),
        user_password: $("#user_password").val(),
        user_password_conf: $("#user_password_conf").val(),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
    }
    var route = "/users/register"
    $.ajax({
        url: route,
        type: "post",
        data: data,
        success: function(data) {
            $("#register_modal").modal('hide')
            var html_str = ""
            html_str += data
            document.getElementById("top_navbar").innerHTML = html_str

        }
    })
})
$(document).on("submit", "#add_product_form", function(event) {
        event.preventDefault();
        var data = {
            product_id: $("input[name='product_id']").val(),
            product_quantity: $("input[name='product_quantity']").val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
        }
        var route = "/products/add_to_cart"
        $.ajax({
            url: route,
            type: "post",
            data: data,
            success: function(data) {
                $.ajax({
                    url: "/navbar",
                    type: "get",
                    success: function(data) {
                        var html_str = ""
                        html_str += data
                        document.getElementById("top_navbar").innerHTML = html_str
                    }
                })
                var html_str = ""
                html_str += data
                document.getElementById("content").innerHTML = html_str
            }
        })
    })
    // Navbar Methods

function display_events() {
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

function display_directions() {
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

function display_cart() {
    $.ajax({
        url: "/cart",
        method: 'get',
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
            var slicey = document.getElementsByClassName("price")
            var quantums = document.getElementsByClassName("quantity")
            var totos = document.getElementsByClassName("total")
            for (var i = 0; i < slicey.length; i++) {
                var price = Number.parseFloat(slicey[i].innerHTML.slice(1))
                var quantity = Number.parseFloat(quantums[i].placeholder)
                totos[i].innerHTML = "$" + price * quantity
            }
        }
    })
}

function display_news() {
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

function display_home() {
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
            document.getElementById("content").innerHTML = html_str;
        }
    })
}

function show_product(id) {
    $.ajax({
        url: "/products/" + id,
        method: "get",
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str;
        }
    })
}




// Checkout Methods
function update_quantity(id) {
    var data = {
        item_quantity: Math.abs($(".number_" + id).val()),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
    }
    $.ajax({
        url: "/products/update_quantity/" + id,
        type: "post",
        data: data,
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str
        }
    })
}

function remove_item(id) {
    var data = {
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
    }
    $.ajax({
        url: "/products/remove_from_cart/" + id,
        type: 'post',
        data: data,
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str
            $.ajax({
                url: "/navbar",
                type: "get",
                success: function(data) {
                    var html_str = ""
                    html_str += data
                    document.getElementById("top_navbar").innerHTML = html_str
                }
            })
        }
    })
}

function empty_cart() {
    data = {
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
    }
    $.ajax({
        url: "/products/empty_cart",
        type: "post",
        data: data,
        success: function(data) {
            var html_str = ""
            html_str += data
            document.getElementById("content").innerHTML = html_str
            $.ajax({
                url: "/navbar",
                type: "get",
                success: function(data) {
                    var html_str = ""
                    html_str += data
                    document.getElementById("top_navbar").innerHTML = html_str
                }
            })
        }
    })
}

// admin methods
function delete_product(id) {
    data = {
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value'),
    }
    $.ajax({
        url: "/products/delete_product/" + id,
        data: data,
        type: "post",
    })
}

function delete_user(id) {
    data = {
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value'),
    }
    $.ajax({
        url: 'users/delete_user/' + id,
        data: data,
        type: "post",
    })
}