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
