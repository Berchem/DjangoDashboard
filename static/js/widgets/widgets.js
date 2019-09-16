
var system_status_update_period = "3000"
var system_status = setInterval("load('system_status')", system_status_update_period);

var chat_status_update_period = "1500"
var chat_status = setInterval("load('chat_status')", chat_status_update_period);
var timeout;

$(".dropdown").on("click", function(){
    clearInterval(system_status)
    clearInterval(chat_status)
    clearTimeout(timeout)

    timeout = setTimeout(function(){
        system_status = setInterval("load('system_status')", system_status_update_period);
        chat_status = setInterval("load('chat_status')", chat_status_update_period);
    }, 8000)
})

