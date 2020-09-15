var characterCanvas;
var characterContext;
var charactersArr = [];
var characterMouse = {
    x: undefined,
    y: undefined
};
var selectedCharacter;
var initialChar;
const maxSizeCharacter = 50;

$(function init() {
    characterCanvas = document.querySelector('#characterMap');

    characterCanvas.width = window.innerWidth/2;
    characterCanvas.height =  characterCanvas.width*0.75;

    characterContext = characterCanvas.getContext('2d');

    characterCanvas.addEventListener("mousedown", function(event){
        if(selectedCharacter != undefined){
            characterMouse.x = event.x - $("canvas").position().left;
            characterMouse.y = event.y - $("canvas").position().top;

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
        if(selectedCharacter != undefined) {
            characterMouse.x = undefined;
            characterMouse.y = undefined;
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
        if(selectedCharacter != undefined) {
            characterMouse.x = undefined;
            characterMouse.y = undefined;
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
        if(selectedCharacter == this.src) {
            //$("#backMap").css("z-index",0);
            //$("#chipMap").css("z-index",100);
            if($('img.menu-character-selected')[0] != undefined) {
                $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
            }
            selectedCharacter = undefined;
        }else{
            //$("#backMap").css("z-index",0);
            //$("#chipMap").css("z-index",100);
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
            selectedCharacter = this.src;
            selectedImg = undefined;
            selectedChip = undefined;
        }
    });
    $('img.menu-character, img.move-down, img.move-left, img.move-right, img.move-up').mouseover(function() {
        this.classList.add("menu-character-over");
    });
    $('img.menu-character, img.move-down, img.move-left, img.move-right, img.move-up').mouseleave(function() {
        this.classList.remove("menu-character-over");
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

function Character(x, y, h, w, img) {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;
    this.img = img;
    this.color = 'black';
    this.draw = function () {
        characterContext.strokeStyle = 'black';
        characterContext.strokeRect(this.x, this.y, this.h, this.w);
        if(this.img != undefined){
            var htmlImg = new Image();
            htmlImg.src = this.img;
            characterContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        }
    };
    this.update = function () {
        if(selectedCharacter != undefined && characterMouse.x != undefined && this.x + this.w > characterMouse.x && this.x < characterMouse.x  && this.y + this.h > characterMouse.y && this.y < characterMouse.y) {
            if(selectedCharacter.includes('trash.png')){
                this.img = undefined;
            }else{
                this.img = selectedCharacter;
            }
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


    for(var i=0; i<maxSizeCharacter; i++){
        for(var j = 0; j < maxSizeCharacter; j++){
            charactersArr.push(new Character(x, y, h, w, img));
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
        initialChar=1
        characterContext.clearRect(0,0,innerWidth,innerHeight);
        charactersArr.forEach(tile => {
            tile.update();
        })
    }
}


