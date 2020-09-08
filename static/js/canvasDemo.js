var canvas;
var c;
var tilesArr = [];
var mouse = {
    x: undefined,
    y: undefined
};
var selectedImg;

$(function init() {
    canvas = document.querySelector('canvas');

    canvas.width = window.innerWidth/2;
    canvas.height =  canvas.width/2;

    c = canvas.getContext('2d');

    canvas.addEventListener('click', function (event) {
        mouse.x = event.x - $("canvas").position().left;
        mouse.y = event.y - $("canvas").position().top;

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
    $('img.menu-img').mouseover(function() {
        this.classList.add("menu-img-over");
    });
    $('img.menu-img').mouseleave(function() {
        this.classList.remove("menu-img-over");
    });
    initTiles();
    animate();
})

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
        c.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        c.fillStyle = this.color;
        c.strokeStyle = 'black';
        c.stroke();
    };
    this.update = function () {
        if(selectedImg != undefined && mouse.x != undefined && Math.abs(this.x + this.w) > mouse.x && this.x < mouse.x  && Math.abs(this.y + this.h) > mouse.y && this.y < mouse.y) {
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
    var initial = Math.floor(innerWidth / rowTiles);
    var x = 0;
    var y = 0;
    var w = initial;
    var h = initial;
    var img = '/static/Media/grass.jpg';


    for(var i=0;i<rowTiles/4;i++){
        for(var j = 0; j < rowTiles/2; j++){
            tilesArr.push(new Tile(x, y, h, w, img));
            x += initial;
        }
        x = 0;
        y += initial;
    }
}
var i;
function animate() {
    requestAnimationFrame(animate);
    if(i == undefined) {
        i=1
        c.clearRect(0,0,innerWidth,innerHeight);
        tilesArr.forEach(tile => {
            tile.draw();
        })
    }else{
        i=1
        c.clearRect(0,0,innerWidth,innerHeight);
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
    c.fillStyle = 'blue';
    c.fillRect(100,100,100,100);
    c.fillStyle = 'pink';
    c.fillRect(500,500,100,100);

    //Line
    c.beginPath();
    c.moveTo(50, 300);
    c.lineTo(300, 100);
    c.lineTo(400, 300);
    c.strokeStyle = 'red';
    c.stroke();

    c.beginPath();
    c.moveTo(500, 600);
    c.lineTo(700, 200);
    c.strokeStyle = 'blue';
    c.stroke();

    // Arc / Circle
    c.beginPath();
    c.arc(300,300,30,Math.PI * 2, false);
    c.strokeStyle = 'purple';
    c.stroke();

}