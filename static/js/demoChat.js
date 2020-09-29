
var loc = window.location;
var formData = $("#formChat");
var msgInput = $("#id_message");
var chatHolder = $("#chat-messages");
var me = $("#myUsernameId").val();

var wsStart = "ws://";
if (loc.protocol == "https:"){
    wsStart = "wss://";
}
var endpoint = wsStart + loc.host + loc.pathname;
var socket = new ReconnectingWebSocket(endpoint);
//socket.binaryType = "arraybuffer";

socket.onmessage = function(e){
    //console.log("message", e);
    var jsonData = JSON.parse(e.data);
    if(jsonData.message == undefined){
        if(jsonData.sender != me){
            updateTilesArrAsyc(jsonData.canvasArray);
        }
    }else {
        chatHolder.append("<li><b>"+ jsonData.username +"</b>: " + jsonData.message + "</li>");
    }
};
socket.onopen = function(e){
    //console.log("open", e);
    formData.submit(function (event) {
        event.preventDefault();
        var msgText = msgInput.val();
        //chatHolder.append("<li>" + msgText + " via " + me + "</li>")
        //var formDataSerialized = formData.serialize()
        var finalData = {
            "message": msgText
        }
        socket.send(JSON.stringify(finalData));
        //msgInput.val("");
        formData[0].reset();
    });
};
socket.onerror = function(e){
    //console.log("error", e)
};
socket.onclose = function(e){
    //console.log("close", e)
};