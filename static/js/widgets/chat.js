function insert_message(id){
    new_msg = document.getElementById(id)
    $.get("./chat/insert/" + new_msg.value, function(ret){
        $(".chat-list").append(ret["list_item"])
    })
    new_msg.value = ""
}

function load(id){
    document.getElementById(id).click();
}

// Execute a function when the user releases a key on the keyboard
$("#chat-input").on('keypress',function(e) {
  if (e.which == 13) {  // Number 13 is the "Enter" key on the keyboard
    document.getElementById("btn-chat").click();
  }
  $('.panel-body').animate({scrollTop: $('.chat-list').height()}, 100);
});

$(document).ready(function(){
    $('#chat_status').click(function(){
        $.getJSON("./chat/status",function(ret){
            $(".chat-list").empty()
            for (var i = 0; i < ret.length; i++){
                $(".chat-list").append(ret[i])
            }
        })
    })
});

$(document).ready(function(){
    $('#chat-input-group').on("mouseover touchstart", function(){
        $('.panel-body').animate(
            {scrollTop: $('.chat-list').height()}, 100);
    })
})

$(document).ready(function(){
    $('#btn-chat').on("mouseover click", function(){
        $('.panel-body').animate(
            {scrollTop: $('.chat-list').height()}, 100);
    })
})

$('.panel-body').animate({scrollTop: $('.chat-list').height()}, 100);