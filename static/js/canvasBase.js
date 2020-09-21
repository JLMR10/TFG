var mapCanvas;
var mapContext;
var tilesArr = [];
var mapMouse = {
    x: undefined,
    y: undefined
};
var selectedImg;
var initialM;
const maxSizeMap = 50;

$(function init() {
    mapCanvas = document.querySelector('#backMap');

    mapCanvas.width = window.innerWidth/2;
    mapCanvas.height =  mapCanvas.width*0.75;

    mapContext = mapCanvas.getContext('2d');

    $('img.menu-img').click(function() {
        if(selectedImg == this.src) {
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }
            selectedImg = undefined;
        }else{
            mapMouse.x = undefined;
            mapMouse.y = undefined;
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }if($('img.menu-chip-selected')[0] != undefined) {
                $('img.menu-chip-selected')[0].classList.remove("menu-chip-selected");
            }if($('img.menu-character-selected')[0] != undefined) {
                $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
            }
            this.classList.add("menu-img-selected");
            selectedImg = this.src;
            selectedChip = undefined;
            selectedCharacter = undefined;
            draggedCharacter = undefined;
        }
    });
    $('img.menu-img, img.move-down, img.move-left, img.move-right, img.move-up').mouseover(function() {
        this.classList.add("menu-img-over");
    });
    $('img.menu-img, img.move-down, img.move-left, img.move-right, img.move-up').mouseleave(function() {
        this.classList.remove("menu-img-over");
    });
    $('img.move-down, img.move-left, img.move-right, img.move-up').click(function() {
        switch (this.classList[0]){
            case 'move-up':
                move(0,3);
                break;
            case 'move-left':
                move(3,0);
                break;
            case 'move-right':
                move(-3,0);
                break;
            case 'move-down':
                move(0,-3);
                break;
        }
    });
    initTiles();
    animate();
})

function move(x, y) {
    tilesArr.forEach(tile => {
        tile.x += tile.w * x;
        tile.y += tile.h * y;
    });
}

function Tile(x, y, h, w, img) {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;
    this.img = img;
    this.color = 'white';
    this.draw = function () {
        mapContext.strokeStyle = 'black';
        mapContext.fillStyle = this.color;
        mapContext.strokeRect(this.x, this.y, this.h, this.w);
        if(this.img != undefined){
            var htmlImg = new Image();
            htmlImg.src = this.img;
            mapContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        }
    };
    this.update = function () {
        if(selectedImg != undefined && mapMouse.x != undefined && this.x + this.w > mapMouse.x && this.x < mapMouse.x  && this.y + this.h > mapMouse.y && this.y < mapMouse.y) {
            if(selectedImg.includes('trash')){
                this.img = undefined;
            }else{
                this.img = selectedImg;
            }
            mapMouse.x = undefined;
            mapMouse.y = undefined;
        }
        this.draw();
    };
}

function initTiles() {
    var rowTiles = 32;
    var cubeSize = Math.floor(innerWidth / rowTiles);
    var x = (-1 * maxSizeMap/2 + rowTiles/2) * cubeSize;
    var y = (-1 * maxSizeMap/2 + rowTiles/2) * cubeSize;
    var w = cubeSize;
    var h = cubeSize;
    var img = undefined;//'/static/Media/grass.jpg';


    for(var i=0; i<maxSizeMap; i++){
        for(var j = 0; j < maxSizeMap; j++){
            tilesArr.push(new Tile(x, y, h, w, img));
            x += cubeSize;
        }
        x = (-1 * maxSizeMap/2 + rowTiles/2) * cubeSize;
        y += cubeSize;
    }
}
function animate() {
    requestAnimationFrame(animate);
    if(initialM == undefined) {
        initialM=1
        mapContext.clearRect(0,0,innerWidth,innerHeight);
        tilesArr.forEach(tile => {
            tile.draw();
        })
    }else{
        initialM=1
        mapContext.clearRect(0,0,innerWidth,innerHeight);
        tilesArr.forEach(tile => {
            tile.update();
        })
    }
}

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
