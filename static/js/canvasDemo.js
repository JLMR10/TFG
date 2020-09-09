var mapCanvas;
var mapContext;
var tilesArr = [];
var mouse = {
    x: undefined,
    y: undefined
};
var selectedImg;
var initial;
const maxSize = 50;

$(function init() {
    mapCanvas = document.querySelector('#backMap');

    mapCanvas.width = window.innerWidth/2;
    mapCanvas.height =  mapCanvas.width*0.75;

    mapContext = mapCanvas.getContext('2d');

    mapCanvas.addEventListener("mousedown", function(event){
        mouse.x = event.x - $("canvas").position().left;
        mouse.y = event.y - $("canvas").position().top;

        mapCanvas.onmousemove = function(event) {
            mouse.x = event.x - $("canvas").position().left;
            mouse.y = event.y - $("canvas").position().top;
        }
    });
    mapCanvas.addEventListener("mouseup", function(e){
        mouse.x = undefined;
        mouse.y = undefined;
        mapCanvas.onmousemove = null
    });
    mapCanvas.addEventListener("mouseleave", function(e){
        mouse.x = undefined;
        mouse.y = undefined;
        mapCanvas.onmousemove = null
    });

    $('img.menu-img').click(function() {
        if(selectedImg == this.src) {
            $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            selectedImg = undefined;
        }else{
            mouse.x = undefined;
            mouse.y = undefined;
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }
            this.classList.add("menu-img-selected");
            selectedImg = this.src;
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
    this.color = getRandomColor();
    this.draw = function () {
        //c.fillRect(this.x, this.y, this.h, this.w);
        var htmlImg = new Image();
        htmlImg.src = this.img;
        mapContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        mapContext.fillStyle = this.color;
        mapContext.strokeStyle = 'black';
        mapContext.stroke();
    };
    this.update = function () {
        if(selectedImg != undefined && mouse.x != undefined && this.x + this.w > mouse.x && this.x < mouse.x  && this.y + this.h > mouse.y && this.y < mouse.y) {
        //if(mouse.x != undefined && Math.abs(mouse.x - this.x) < this.w/2 && Math.abs(mouse.y - this.y) < this.h/2) {
        //if(mouse.x - this.x < this.x/2 && this.x - mouse.x > -this.x/2 && mouse.y - this.y < this.y/2 && this.y - mouse.y > -this.y/2) {
            //this.color = getRandomColor();
            this.img = selectedImg;
            mouse.x = undefined;
            mouse.y = undefined;
        }
        this.draw();
    };

}

function initTiles() {
    var rowTiles = 32;
    var cubeSize = Math.floor(innerWidth / rowTiles);
    var x = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
    var y = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
    var w = cubeSize;
    var h = cubeSize;
    var img = '/static/Media/grass.jpg';


    for(var i=0;i<maxSize;i++){
        for(var j = 0; j < maxSize; j++){
            tilesArr.push(new Tile(x, y, h, w, img));
            x += cubeSize;
        }
        x = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
        y += cubeSize;
    }
}
function animate() {
    requestAnimationFrame(animate);
    if(initial == undefined) {
        initial=1
        mapContext.clearRect(0,0,innerWidth,innerHeight);
        tilesArr.forEach(tile => {
            tile.draw();
        })
    }else{
        initial=1
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




function createCanvas() {

    // Rectangle
    mapContext.fillStyle = 'blue';
    mapContext.fillRect(100,100,100,100);
    mapContext.fillStyle = 'pink';
    mapContext.fillRect(500,500,100,100);

    //Line
    mapContext.beginPath();
    mapContext.moveTo(50, 300);
    mapContext.lineTo(300, 100);
    mapContext.lineTo(400, 300);
    mapContext.strokeStyle = 'red';
    mapContext.stroke();

    mapContext.beginPath();
    mapContext.moveTo(500, 600);
    mapContext.lineTo(700, 200);
    mapContext.strokeStyle = 'blue';
    mapContext.stroke();

    // Arc / Circle
    mapContext.beginPath();
    mapContext.arc(300,300,30,Math.PI * 2, false);
    mapContext.strokeStyle = 'purple';
    mapContext.stroke();

}