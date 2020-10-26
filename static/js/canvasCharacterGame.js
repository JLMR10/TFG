var characterCanvas;
var characterContext;
var charactersArr = [];
var characterMouse = {
    x: undefined,
    y: undefined
};
var selectedCharacter;
var draggedCharacter;
var initialChar;
const maxSizeCharacter = 50;
var sendCharacter = false;

$(function init() {
    characterCanvas = document.querySelector('#characterMap');

    characterCanvas.width = window.innerWidth/2;
    characterCanvas.height =  characterCanvas.width*0.75;

    characterContext = characterCanvas.getContext('2d');

    characterCanvas.addEventListener("mousedown", function(event){
        characterMouse.x = event.x - $("canvas").position().left;
        characterMouse.y = event.y - $("canvas").position().top;

        if(selectedCharacter != undefined && selectedCharacter.img != undefined){
            characterCanvas.onmousemove = function(event) {
                characterMouse.x = event.x - $("canvas").position().left;
                characterMouse.y = event.y - $("canvas").position().top;
            }
        }else if(selectedChip != undefined){
            chipMouse.x = event.x - $("canvas").position().left;
            chipMouse.y = event.y - $("canvas").position().top;

            characterCanvas.onmousemove = function(event) {
                chipMouse.x = event.x - $("canvas").position().left;
                chipMouse.y = event.y - $("canvas").position().top;
            }
        }if(selectedImg != undefined){
            mapMouse.x = event.x - $("canvas").position().left;
            mapMouse.y = event.y - $("canvas").position().top;

            characterCanvas.onmousemove = function(event) {
                mapMouse.x = event.x - $("canvas").position().left;
                mapMouse.y = event.y - $("canvas").position().top;
            }
        }
    });
    characterCanvas.addEventListener("mouseup", function(e){
        characterMouse.x = undefined;
        characterMouse.y = undefined;

        if(selectedCharacter != undefined && selectedCharacter.img != undefined) {
            characterCanvas.onmousemove = null
        }else if(selectedChip != undefined) {
            chipMouse.x = undefined;
            chipMouse.y = undefined;
            characterCanvas.onmousemove = null
        }if(selectedImg != undefined){
            mapMouse.x = undefined;
            mapMouse.y = undefined;
            characterCanvas.onmousemove = null
        }
    });
    characterCanvas.addEventListener("mouseleave", function(e){
        characterMouse.x = undefined;
        characterMouse.y = undefined;

        if(selectedCharacter != undefined && selectedCharacter.img != undefined) {
            characterCanvas.onmousemove = null
        }else if(selectedChip != undefined) {
            chipMouse.x = undefined;
            chipMouse.y = undefined;
            characterCanvas.onmousemove = null
        }if(selectedImg != undefined){
            mapMouse.x = undefined;
            mapMouse.y = undefined;
            characterCanvas.onmousemove = null
        }
    });

    $('img.menu-character').click(function() {
        if(selectedCharacter == this.getAttribute('src')) {
            if($('img.menu-character-selected')[0] != undefined) {
                $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
            }
            selectedCharacter = undefined;
        }else if(!this.classList.contains('disabled-char')){
            characterMouse.x = undefined;
            characterMouse.y = undefined;
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }if($('img.menu-chip-selected')[0] != undefined) {
                $('img.menu-chip-selected')[0].classList.remove("menu-chip-selected");
            }if($('img.menu-character-selected')[0] != undefined) {
                $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
            }
            this.classList.add("menu-character-selected");
            selectedCharacter = this.getAttribute('src');
            selectedImg = undefined;
            selectedChip = undefined;
            draggedCharacter = undefined;
        }
    });
    $('img.menu-character, img.move-down, img.move-left, img.move-right, img.move-up').mouseover(function() {
        if(!this.classList.contains('disabled-char')) {
            this.classList.add("menu-character-over");
        }
    });
    $('img.menu-character, img.move-down, img.move-left, img.move-right, img.move-up').mouseleave(function() {
        if(!this.classList.contains('disabled-char')) {
            this.classList.remove("menu-character-over");
        }
    });
    $('img.move-down, img.move-left, img.move-right, img.move-up').click(function() {
        switch (this.classList[0]){
            case 'move-up':
                moveCharacters(0,3);
                break;
            case 'move-left':
                moveCharacters(3,0);
                break;
            case 'move-right':
                moveCharacters(-3,0);
                break;
            case 'move-down':
                moveCharacters(0,-3);
                break;
        }
    });

    initCharacters();
    animateCharacter();
})

function moveCharacters(x, y) {
    charactersArr.forEach(tile => {
        tile.x += tile.w * x;
        tile.y += tile.h * y;
    });
}

function Character(x, y, h, w, img, color = 'black', maxMove = undefined, id = undefined, isUser = "false") {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;
    this.img = img;
    this.color = color;
    this.maxMove = maxMove;
    this.id = id;
    this.isUser = isUser;
    this.draw = function () {
        if(draggedCharacter != undefined &&
            this.x >= draggedCharacter.x - draggedCharacter.maxMove * draggedCharacter.w && this.x <= draggedCharacter.x + draggedCharacter.maxMove *draggedCharacter.w &&
            this.y >= draggedCharacter.y - draggedCharacter.maxMove * draggedCharacter.h && this.y <= draggedCharacter.y + draggedCharacter.maxMove *draggedCharacter.h
        ){
            this.color = 'gold';
        }else {
            this.color = 'black';
        }
        characterContext.strokeStyle = this.color;
        characterContext.strokeRect(this.x, this.y, this.h, this.w);
        if(this.img != undefined){
            var htmlImg = new Image();
            htmlImg.src = this.img;
            characterContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        }
    };
    this.update = function () {
        if(selectedCharacter != undefined && characterMouse.x != undefined && this.x + this.w > characterMouse.x && this.x < characterMouse.x  && this.y + this.h > characterMouse.y && this.y < characterMouse.y) {
            if(selectedCharacter.includes('trash')){
                if(this.isUser == "true"){
                    $("img[src$='" + this.img + "']").removeClass('disabled-char');
                }
                this.img = undefined;
                this.maxMove = undefined;
                this.id = "Empty";
                this.isUser = "false";
            }else{
                this.img = selectedCharacter;
                this.maxMove = parseInt($("img[src$='" + selectedCharacter + "']").attr('movement'));
                this.id = $("img[src$='" + selectedCharacter + "']")[0].id;
                this.isUser = $("img[src$='" + selectedCharacter + "']").attr('isuser');
                if(this.isUser == "true"){
                    $("img[src$='" + selectedCharacter + "']").addClass('disabled-char');
                    $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
                    selectedCharacter = undefined;
                }
            }
            sendCharacter = true;
            characterMouse.x = undefined;
            characterMouse.y = undefined;
        }else if(characterMouse.x != undefined && this.x + this.w > characterMouse.x && this.x < characterMouse.x  && this.y + this.h > characterMouse.y && this.y < characterMouse.y){
            if(draggedCharacter == undefined && selectedImg == undefined && selectedChip == undefined && this.img != undefined) {
                if(isMaster == "True" || (pythonUsersTurns[this.id] == 1 && this.id==me)){
                    draggedCharacter = this;
                }
            }else if(this.color == 'gold'){
                var auxImg = draggedCharacter.img;
                var auxMaxMove = draggedCharacter.maxMove;
                var auxId = draggedCharacter.id;
                var auxIndex = charactersArr.indexOf(draggedCharacter);
                var auxIsUser = draggedCharacter.isUser;
                charactersArr[auxIndex].img = undefined;
                charactersArr[auxIndex].maxMove = undefined;
                charactersArr[auxIndex].id = "Empty";
                charactersArr[auxIndex].isUser = "false";
                if(this.isUser == "true"){
                    $("img[src$='" + this.img + "']").removeClass('disabled-char');
                }
                this.img = auxImg;
                this.maxMove = auxMaxMove;
                this.id = auxId;
                this.isUser = auxIsUser;
                draggedCharacter = undefined;
                if(isMaster=="False"){
                    endTurn(this.id);
                }
            }else{
                draggedCharacter = undefined;
            }
            sendCharacter = true;
            characterMouse.x = undefined;
            characterMouse.y = undefined;
        }
        this.draw();
    };

}

function initCharacters() {
    var rowTiles = 32;
    var cubeSize = Math.floor(innerWidth / rowTiles);
    var x = (-1 * maxSizeCharacter/2 + rowTiles/2) * cubeSize;
    var y = (-1 * maxSizeCharacter/2 + rowTiles/2) * cubeSize;
    var w = cubeSize;
    var h = cubeSize;
    var img = undefined;
    let responseKeys = Object.keys(pythonCharacters);
    let userPositions = [];
    if (pythonUserCharacters){
        Object.keys(pythonUserCharacters).forEach(function (e) {
            userPositions.push(pythonUserCharacters[e].Position);
        })
    }




    for(var i=0; i<maxSizeCharacter; i++){
        for(var j = 0; j < maxSizeCharacter; j++){
            let index = i * maxSizeMap + j;
            if(userPositions.includes(index)) {
                let subIndex = userPositions.indexOf(index);
                $("img[src$='/static/Media/" + subIndex + "_character.png']").addClass('disabled-char');
                charactersArr.push(new Character(x, y, h, w, "/static/Media/" + subIndex + '_character.png', 'black',pythonUserCharacters[subIndex + "_"].Move, pythonUserCharacters[subIndex + "_"].User, "true"));
            }else if(responseKeys.includes(index.toString())){
                charactersArr.push(new Character(x, y, h, w, $("#" + pythonCharacters[index]).attr('src'), 'black',3, pythonCharacters[index] ));
            }else{
                charactersArr.push(new Character(x, y, h, w, img));
            }
            x += cubeSize;
        }
        x = (-1 * maxSizeCharacter/2 + rowTiles/2) * cubeSize;
        y += cubeSize;
    }
}
function animateCharacter() {
    requestAnimationFrame(animateCharacter);
    if(initialChar == undefined) {
        initialChar=1
        characterContext.clearRect(0,0,innerWidth,innerHeight);
        charactersArr.forEach(tile => {
            tile.draw();
        })
    }else{
        initialChar+=1
        characterContext.clearRect(0,0,innerWidth,innerHeight);
        charactersArr.forEach(tile => {
            tile.update();
        })
        if(initialChar >= 100 && sendCharacter){
            sendCharactersArrayToSocket();
            initialChar = 1;
        }
    }
}

function sendCharactersArrayToSocket(){
    socket.send(JSON.stringify({"charactersArray": charactersArr }));
    sendCharacter = false;
}

function updateCharactersArrAsyc(socketArr) {
    if(socketArr){
        socketArr.forEach(function(e, i){
            charactersArr[i].img = e.img;
            charactersArr[i].isUser = e.isUser;
            charactersArr[i].maxMove = e.maxMove;
            charactersArr[i].id = e.id;
        });
    }
}