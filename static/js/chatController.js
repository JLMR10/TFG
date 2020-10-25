
var loc = window.location;
var formData = $("#formChat");
var msgInput = $("#id_message");
var chatHolder = $("#chat-messages");
var me = $("#myUsernameId").val();
var meName = $("#myUsername").val();

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
    if(jsonData.message == undefined && jsonData.pythonUsersTurns == undefined){
        if(jsonData.sender != me){
            updateTilesArrAsyc(jsonData.canvasArray);
            updateChipsArrAsyc(jsonData.chipsArray);
            updateCharactersArrAsyc(jsonData.charactersArray);
        }
    }else if(jsonData.pythonUsersTurns != undefined){
        pythonUsersTurns = jsonData.pythonUsersTurns;
        var userTurnName = jsonData.userTurn;
        listUsersTurns = Object.keys(jsonData.pythonUsersTurns);
        listUsersTurns.forEach(function (e) {
            if(pythonUsersTurns[e]!=0){
                $("#"+e+"_turn").css({"background-color":"aliceblue"});
            }else{
                $("#"+e+"_turn").css({"background-color":"white"});
            }
        });
        if(jsonData.endTurn){
            chatHolder.append("<div class='message py2'><span class='otherMessages card border-left-secondary'>"+userTurnName+" has moved</span></div>");
        }else{
            chatHolder.append("<div class='message py2'><span class='otherMessages card border-left-secondary'>"+userTurnName+" is ready to move</span></div>");
        }
        chatHolder[0].scrollTop = chatHolder[0].scrollHeight

    }else {
        if (jsonData.senderID != me) {
            chatHolder.append("<div class='message py2'><span class='otherMessages card border-left-secondary'><b>" + jsonData.username + ":</b> " + jsonData.message + "</span></div>");
            chatHolder[0].scrollTop = chatHolder[0].scrollHeight
        }
    }
};
socket.onopen = function(e){
    //console.log("open", e);
    formData.submit(function (event) {
        event.preventDefault();
        var msgText = msgInput.val();
        chatHolder.append("<div class='message py2'><span class='myMessages card border-right-primary'>" + msgText + "</span></div>");
        chatHolder[0].scrollTop = chatHolder[0].scrollHeight
        var finalData = {
            "message": msgText
        };
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

$("#send-message").click(function () {
    formData.submit();
});

