var canvas;
var c;
var tilesArr = [];
var mouse = {
    x: undefined,
    y: undefined
};

$(function init() {
    canvas = document.querySelector('canvas');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    c = canvas.getContext('2d');

    window.addEventListener('click', function (event) {
        mouse.x = event.x;
        mouse.y = event.y;
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
        c.drawImage(this.img ,this.x, this.y, this.h, this.w);
        c.fillStyle = this.color;
        c.strokeStyle = 'black';
        c.stroke();
    };
    this.update = function () {
        if(mouse.x != undefined && Math.abs(mouse.x - this.x) < this.w/2 && Math.abs(mouse.y - this.y) < this.h/2) {
        //if(mouse.x - this.x < this.x/2 && this.x - mouse.x > -this.x/2 && mouse.y - this.y < this.y/2 && this.y - mouse.y > -this.y/2) {
            this.color = getRandomColor();
            mouse.x = undefined;
            mouse.y = undefined;
        }
        this.draw();
    };

}

function initTiles() {
    var initial = Math.floor(innerWidth / 4);
    var x = 0;
    var y = 0;
    var w = initial;
    var h = initial;
    var img = new Image();
    img.src = 'Zaen.jpg';
    for(var i=0;i<4;i++){
        for(var j = 0; j < 4; j++){
            tilesArr.push(new Tile(img, x, y, h, w));
            x += initial;
        }
        x = 0;
        y += initial;
    }
}

function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0,0,innerWidth,innerHeight);
    tilesArr.forEach(tile => {
        tile.draw();
    })

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