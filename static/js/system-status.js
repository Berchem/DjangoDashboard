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

function load(){
    document.getElementById('system_status').click();
}

//setInterval("load()","6000");

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
}


