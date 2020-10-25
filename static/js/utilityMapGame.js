


$(function init() {

    $(".save-map").click(function () {
        $(".loader-wrapper").fadeIn("slow");
        let baseTiles = [];
        let baseChips = [];
        let baseCharacters = [];
        let userCharacters = [];

        tilesArr.forEach(function (e){
            baseTiles[baseTiles.length] = e.id
        });
        chipsArr.forEach(function (e){
            baseChips[baseChips.length] = e.id
        });
        charactersArr.forEach(function (e){
            if(e.isUser == "false") {
                baseCharacters[baseCharacters.length] = e.id
            }else{
                baseCharacters[baseCharacters.length] = undefined;
            }
        });
        charactersArr.forEach(function (e){
            if(e.isUser == "true") {
                userCharacters[userCharacters.length] = e.img.split('/')[3].split('_')[0] + '_';
            }else{
                userCharacters[userCharacters.length] = undefined;
            }
        });

        let data = {
            gameId: gameId,
            mapId: mapId,
            mapName: mapName,
            order: maxOrder,
            tiles: baseTiles,
            chips: baseChips,
            characters: baseCharacters,
            userCharacters: userCharacters,
        }
        saveGame(data);
    });
});


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function saveGame(data) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        url: "http://127.0.0.1:8000/game/saveGame/",
        //headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: JSON.stringify(data),
        type: "POST",
        success: function (response) {
            response = JSON.parse(response);
            maxOrder = response.newOrder;
            $(".loader-wrapper").fadeOut("slow");
        },
        error: function (response) {
            console.log(response);
            $(".loader-wrapper").fadeOut("slow");
        },
        async: true,
        contentType: "application/json; charset=utf-8",
        dataType: "text"
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function renderMenu(menuTiles, menuChips, menuCharacter) {
    createMenuImg("Tiles", "menu-img", menuTiles);
    createMenuImg("Chips", "menu-chip", menuChips);
    createMenuImg("Characters", "menu-character", menuCharacter);
}

function createMenuImg(id, css, array) {
    for(let index in array) {
        let elem = document.createElement("img");
        elem.src = "/static/Media/" + array[index][1];
        elem.id = array[index][0];
        elem.classList.add(css);
        if(id == 'Characters'){
            elem.setAttribute( "movement", 3 );
            elem.setAttribute( "isuser", false );
        }
        document.getElementById(id).appendChild(elem);
    }
}


function giveTurn(character){
    $("#"+character.id).css({"background-color":"aliceblue"});
    user = character.id.split("_")[0];
    pythonUsersTurns[user] = 1;
    socket.send(JSON.stringify({"pythonUsersTurns": pythonUsersTurns , "userTurn": character.text}));
}

function endTurn(id){
    $("#"+id+"_turn").css({"background-color":"white"});
    user = id;
    pythonUsersTurns[user] = 0;
    let userTurnName = $("#"+id+"_turn").text();
    socket.send(JSON.stringify({"pythonUsersTurns": pythonUsersTurns,"userTurn":userTurnName,"endTurn":true}));
}

function rolldice(number) {
    let randomNumber = Math.ceil(Math.random()*number);
    chatHolder.append("<div class='message py2'><span class='myMessages card border-right-primary'>You rolled a " + randomNumber + " with a d"+number + "</span></div>");
    chatHolder[0].scrollTop = chatHolder[0].scrollHeight;
    if(isMaster=="False"){
        socket.send(JSON.stringify({"message": "Has rolled a " + randomNumber + " with a d"+number}))
    }
}