$(document).ready(function(){
    $('#system_status').on("click", function(){
        $.getJSON("/widgets/system/status", function(ret){
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

function load(id){
    document.getElementById(id).click();
}
