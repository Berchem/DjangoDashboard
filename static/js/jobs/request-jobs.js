function kill_job(id){
    $.get("/jobs/kill/" + id, function(ret){
        $("#job-" + id).attr("status", ret["status"])
        $("#job-panel-" + id).removeClass("bg-info")
        $("#job-panel-" + id).addClass(ret["status_bg"])

        text = '<em class="fa fa-lg fa-' + ret["status_icon"] + '">&nbsp;</em>' + ret["status"]
        $("#job-panel-" + id).html(text)
    })
}

function show_request_jobs(){
    $(".request-jobs").filter(function(i, item){
        return true
    }).show()
}

$("#dur-30min").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
    	submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60
        return (dur > 30) & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-1hr").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60
        return (dur > 1) & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-2hr").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60
        return dur > 2 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-3hr").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60
        return dur > 3 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-6hr").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60
        return dur > 6 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-12hr").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60
        return dur > 12 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-1day").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60 / 24
        return dur > 1 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-7day").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60 / 24
        return dur > 7 & (status != 'RUNNING')
    }).css("display", "none")
})

$("#dur-30day").on("click", function(){
    show_request_jobs()
    $(".request-jobs").filter(function(i, item){
        status = $(item).attr("status")
        submit_time = new Date($(item).attr("timestamp"))
    	now = Date.now()
    	dur = (now - submit_time) / 1000 / 60 / 60 / 24
        return dur > 30 & (status != 'RUNNING')
    }).css("display", "none")
})