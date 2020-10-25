var chipCanvas;
var chipContext;
var chipsArr = [];
var chipMouse = {
    x: undefined,
    y: undefined
};
var selectedChip;
var initialC;
const maxSizeChip = 50;

$(function init() {
    chipCanvas = document.querySelector('#chipMap');

    chipCanvas.width = window.innerWidth/2;
    chipCanvas.height =  chipCanvas.width*0.75;

    chipContext = chipCanvas.getContext('2d');

    $('img.menu-chip').click(function() {
        if(selectedChip == this.getAttribute('src')) {
            if($('img.menu-chip-selected')[0] != undefined) {
                $('img.menu-chip-selected')[0].classList.remove("menu-chip-selected");
            }
            selectedChip = undefined;
        }else{
            chipMouse.x = undefined;
            chipMouse.y = undefined;
            if($('img.menu-img-selected')[0] != undefined) {
                $('img.menu-img-selected')[0].classList.remove("menu-img-selected");
            }if($('img.menu-chip-selected')[0] != undefined) {
                $('img.menu-chip-selected')[0].classList.remove("menu-chip-selected");
            }if($('img.menu-character-selected')[0] != undefined) {
                $('img.menu-character-selected')[0].classList.remove("menu-character-selected");
            }
            this.classList.add("menu-chip-selected");
            selectedChip = this.getAttribute('src');
            selectedImg = undefined;
            selectedCharacter = undefined;
            draggedCharacter = undefined;
        }
    });
    $('img.menu-chip, img.move-down, img.move-left, img.move-right, img.move-up').mouseover(function() {
        this.classList.add("menu-chip-over");
    });
    $('img.menu-chip, img.move-down, img.move-left, img.move-right, img.move-up').mouseleave(function() {
        this.classList.remove("menu-chip-over");
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

function Chip(x, y, h, w, img, id = undefined) {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;
    this.img = img;
    this.color = 'black';
    this.id = id;
    this.draw = function () {
        chipContext.strokeStyle = 'black';
        chipContext.strokeRect(this.x, this.y, this.h, this.w);
        if(this.img != undefined){
            var htmlImg = new Image();
            htmlImg.src = this.img;
            chipContext.drawImage(htmlImg ,this.x, this.y, this.h, this.w);
        }
    };
    this.update = function () {
        if(selectedChip != undefined && chipMouse.x != undefined && this.x + this.w > chipMouse.x && this.x < chipMouse.x  && this.y + this.h > chipMouse.y && this.y < chipMouse.y) {
            if(selectedChip.includes('trash')){
                this.img = undefined;
                this.id = "Empty";
            }else{
                this.img = selectedChip;
                this.id = $("img[src$='" + selectedChip + "']")[0].id;
            }
            chipMouse.x = undefined;
            chipMouse.y = undefined;
        }
        this.draw();
    };

}

function initChips() {
    var rowTiles = 32;
    var cubeSize = Math.floor(innerWidth / rowTiles);
    var x = (-1 * maxSizeChip/2 + rowTiles/2) * cubeSize;
    var y = (-1 * maxSizeChip/2 + rowTiles/2) * cubeSize;
    var w = cubeSize;
    var h = cubeSize;
    var img = undefined;
    let responseKeys = Object.keys(pythonChips);


    for(var i=0; i<maxSizeChip; i++){
        for(var j = 0; j < maxSizeChip; j++){
            let index = i * maxSizeMap + j;
            if(responseKeys.includes(index.toString())) {
                chipsArr.push(new Chip(x, y, h, w, $("#" + pythonChips[index]).attr('src'), pythonChips[index] ));
            }else{
                chipsArr.push(new Chip(x, y, h, w, img));
            }
            x += cubeSize;
        }
        x = (-1 * maxSizeChip/2 + rowTiles/2) * cubeSize;
        y += cubeSize;
    }
}
function animateChip() {
    requestAnimationFrame(animateChip);
    if(initialC == undefined) {
        initialC=1
        chipContext.clearRect(0,0,innerWidth,innerHeight);
        chipsArr.forEach(tile => {
            tile.draw();
        })
    }else{
        initialC=1
        chipContext.clearRect(0,0,innerWidth,innerHeight);
        chipsArr.forEach(tile => {
            tile.update();
        })
    }
}


