$(document).ready(function(){
    $('#system_status').click(function(){
        $.getJSON("/system/status",function(ret){
            // cpu
            document.getElementById('cpu_percent_value').innerHTML =  ret["cpu_percent"] + " %";
        	document.getElementById('cpu_percent_progress').style.width = ret["cpu_percent"] + "%";
        	// memory
            document.getElementById('memory_percent_value').innerHTML = ret["memory_percent"] + " %";
        	document.getElementById('memory_percent_progress').style.width = ret["memory_percent"] + "%";
        	// receive
        	document.getElementById('recv_speed_value').innerHTML = ret["receive_speed"] + " Mbps";
        	document.getElementById('recv_speed_progress').style.width = ret["receive_rate"] + "%";
        	// sent
        	document.getElementById('sent_speed_value').innerHTML = ret["sent_speed"] + " Mbps";
        	document.getElementById('sent_speed_progress').style.width = ret["sent_rate"] + "%";
        	// battery
            document.getElementById('battery_status_value').innerHTML = (ret["battery_low"]) ? "Battery Low. Shutdown in 1 Minute " : ret["battery_status"] + " %";
        	document.getElementById('battery_status_progress').style.width = ret["battery_status"] + "%";
        })
    })
});

$(document).ready(function(){
    $('#chat_status').click(function(){
        $.getJSON("./chat/status",function(ret){
            $(".chat-list").empty()
            for (var i = 0; i < ret.length; i++){
                $(".chat-list").append(ret[i])
            }
        })
//        $('.chat-list').slideToggle();
        $('.panel-body').animate({
//            scrollTop: $('.panel-body').height()
            scrollTop: 10000
        }, 100);
    })
});

function load(id){
    document.getElementById(id).click();
}

setInterval("load('system_status')","5000");
setInterval("load('chat_status')","5000");

function update_to_do_status(id){
    var index = id.split("-")[1]
    $.get("./to_do/update/" + index, function(ret){
        document.getElementById(id).checked = (ret["status"] == 1) ? false : true
    })
}

function delete_to_do_item(id){
    var index = id.split("-")[1]
    $.get("./to_do/delete/" + index, function(ret){
        document.getElementById(id).style.display = ret["display"]
    })
}

function insert_to_do_list(id){
    todo_input = document.getElementById(id)
    $.get("./to_do/insert/" + todo_input.value, function(ret){
        $(".todo-list").append(ret["list_item"])
    })
    todo_input.value = ""
}

// Execute a function when the user releases a key on the keyboard
$("#todo-input").on('keypress',function(e) {
  if (e.which == 13) {  // Number 13 is the "Enter" key on the keyboard
    document.getElementById("btn-todo").click();
  }
});

function insert_message(id){
    new_msg = document.getElementById(id)
    $.get("./chat/insert/" + new_msg.value, function(ret){
        $(".chat-list").append(ret["list_item"])
    })
    new_msg.value = ""
}

// Execute a function when the user releases a key on the keyboard
$("#chat-input").on('keypress',function(e) {
  if (e.which == 13) {  // Number 13 is the "Enter" key on the keyboard
    document.getElementById("btn-chat").click();
  }
});
