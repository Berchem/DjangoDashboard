$(document).ready(function(){
    $('#battery_status').click(function(){
        $.getJSON("/system/battery_status",function(ret){
        	document.getElementById('battery_status_value').innerHTML = ret["battery_status"] + " %";
        	document.getElementById('battery_status_progress').style.width = ret["battery_status"] + "%";
        })
    })
});

$(document).ready(function(){
    $('#cpu_percent').click(function(){
        $.getJSON("/system/cpu_percent",function(ret){
        	document.getElementById('cpu_percent_value').innerHTML = ret["cpu_percent"] + " %";
        	document.getElementById('cpu_percent_progress').style.width = ret["cpu_percent"] + "%";
        })
    })
});

$(document).ready(function(){
    $('#memory_percent').click(function(){
        $.getJSON("/system/memory_percent",function(ret){
        	document.getElementById('memory_percent_value').innerHTML = ret["memory_percent"] + " %";
        	document.getElementById('memory_percent_progress').style.width = ret["memory_percent"] + "%";
        })
    })
});

$(document).ready(function(){
    $('#recv_speed').click(function(){
        $.getJSON("/system/recv_speed",function(ret){
        	document.getElementById('recv_speed_value').innerHTML = ret["recv_speed"] + " Mbps";
        	document.getElementById('recv_speed_progress').style.width = ret["recv_rate"] + "%";
        })
    })
});

function load(){
    document.getElementById('battery_status').click();
    document.getElementById('cpu_percent').click();
    document.getElementById('memory_percent').click();
    document.getElementById('recv_speed').click();
}

setInterval("load()","1000");
