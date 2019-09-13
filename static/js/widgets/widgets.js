var system_status = setInterval("load('system_status')","3000");
var chat_status = setInterval("load('chat_status')","1500");
var timeout;

$(".dropdown").on("click", function(){
    clearInterval(system_status)
    clearInterval(chat_status)
    setTimeout(function(){
        system_status = setInterval("load('system_status')","3000");
        chat_status = setInterval("load('chat_status')","1500");
    }, 10000)
})