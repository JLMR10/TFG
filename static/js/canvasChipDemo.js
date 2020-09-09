var chipCanvas;
var chipContext;
var chipsArr = [];
var mouse = {
    x: undefined,
    y: undefined
};
var selectedChip;
var initial;
const maxSize = 50;

$(function init() {
    chipCanvas = document.querySelector('#chipMap');

    chipCanvas.width = window.innerWidth/2;
    chipCanvas.height =  chipCanvas.width*0.75;

    chipContext = chipCanvas.getContext('2d');

    chipCanvas.addEventListener("mousedown", function(event){
        mouse.x = event.x - $("canvas").position().left;
        mouse.y = event.y - $("canvas").position().top;

        chipCanvas.onmousemove = function(event) {
            mouse.x = event.x - $("canvas").position().left;
            mouse.y = event.y - $("canvas").position().top;
        }
    });
    chipCanvas.addEventListener("mouseup", function(e){
        mouse.x = undefined;
        mouse.y = undefined;
        chipCanvas.onmousemove = null
    });
    chipCanvas.addEventListener("mouseleave", function(e){
        mouse.x = undefined;
        mouse.y = undefined;
        chipCanvas.onmousemove = null
    });

    $('img.menu-img').click(function() {
        if(selectedChip == this.src) {
            $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            selectedChip = undefined;
        }else{
            mouse.x = undefined;
            mouse.y = undefined;
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }
            this.classList.add("menu-img-selected");
            selectedChip = this.src;
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
                moveChips(0,3);
                break;
            case 'move-left':
                moveChips(3,0);
                break;
            case 'move-right':
                moveChips(-3,0);
                break;
            case 'move-down':
                moveChips(0,-3);
                break;
        }
    });
    initChips();
    animateChip();
})

function moveChips(x, y) {
    chipsArr.forEach(tile => {
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
    //this.color = getRandomColor();
    this.draw = function () {
        //c.fillRect(this.x, this.y, this.h, this.w);
        var htmlImg = new Image();
        htmlImg.src = this.img;
        chipContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        chipContext.strokeStyle = 'black';
        chipContext.stroke();
    };
    this.update = function () {
        if(selectedChip != undefined && mouse.x != undefined && this.x + this.w > mouse.x && this.x < mouse.x  && this.y + this.h > mouse.y && this.y < mouse.y) {
        //if(mouse.x != undefined && Math.abs(mouse.x - this.x) < this.w/2 && Math.abs(mouse.y - this.y) < this.h/2) {
        //if(mouse.x - this.x < this.x/2 && this.x - mouse.x > -this.x/2 && mouse.y - this.y < this.y/2 && this.y - mouse.y > -this.y/2) {
            //this.color = getRandomColor();
            this.img = selectedChip;
            mouse.x = undefined;
            mouse.y = undefined;
        }
        this.draw();
    };

}

function initChips() {
    var rowTiles = 32;
    var cubeSize = Math.floor(innerWidth / rowTiles);
    var x = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
    var y = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
    var w = cubeSize;
    var h = cubeSize;
    var img = '/static/Media/grass.jpg';


    for(var i=0;i<maxSize;i++){
        for(var j = 0; j < maxSize; j++){
            chipsArr.push(new Tile(x, y, h, w, img));
            x += cubeSize;
        }
        x = (-1 * maxSize/2 + rowTiles/2) * cubeSize;
        y += cubeSize;
    }
}
function animateChip() {
    requestAnimationFrame(animateChip);
    if(initial == undefined) {
        initial=1
        chipContext.clearRect(0,0,innerWidth,innerHeight);
        chipsArr.forEach(tile => {
            tile.draw();
        })
    }else{
        initial=1
        chipContext.clearRect(0,0,innerWidth,innerHeight);
        chipsArr.forEach(tile => {
            tile.update();
        })
    }
}


