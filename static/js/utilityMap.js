


$(function init() {
    var toValidate = $('#mapName'),
    valid = false;
    toValidate.keyup(function () {
        if ($(this).val().length > 0) {
            $(this).data('valid', true);
        } else {
            $(this).data('valid', false);
        }
        toValidate.each(function () {
            if ($(this).data('valid') == true) {
                valid = true;
            } else {
                valid = false;
            }
        });
        if (valid === true) {
            $("#createBtnSavePrevious").prop('disabled', false);
        } else {
            $("#createBtnSavePrevious").prop('disabled', true);
        }
    });

    $("#versionOrders").on('change', function() {
        $(".loader-wrapper").fadeIn("slow");
        let selector = document.getElementById("versionOrders");
        let actualOrder = parseInt(selector.options[selector.selectedIndex].text.split('_')[1]);
        let data = {
            mapId: mapId,
            order: actualOrder
        }
        changeVersion(data);
    });

    $(".save-map").click(function () {
        let baseTiles = [];
        let baseChips = [];
        let baseCharacters = [];
        let selector = document.getElementById("versionOrders");
        let actualOrder = parseInt(selector.options[selector.selectedIndex].text.split('_')[1]);
        let isPrevious = actualOrder < maxOrder;


        tilesArr.forEach(function (e){
            baseTiles[baseTiles.length] = e.id
        });
        chipsArr.forEach(function (e){
            baseChips[baseChips.length] = e.id
        });
        charactersArr.forEach(function (e){
            baseCharacters[baseCharacters.length] = e.id
        });

        if(isPrevious){
            $("#mapId")[0].value = mapId;
            $("#order")[0].value = actualOrder;
            $("#tiles")[0].value = JSON.stringify(baseTiles);
            $("#chips")[0].value = JSON.stringify(baseChips);
            $("#characters")[0].value = JSON.stringify(baseCharacters);
            $('#savePreviousModal').fadeIn(1, function () {
                $('#savePreviousModal').modal('show');
            });
        }else{
            $(".loader-wrapper").fadeIn("slow");

            let data = {
                mapId: mapId,
                mapName: mapName,
                order: actualOrder,
                tiles: baseTiles,
                chips: baseChips,
                characters: baseCharacters,
            }
            saveMap(data);
        }

    });

    $(document).ready(function() {
        $('.selectVersion').select2();
    });
});


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function changeVersion(data) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        url: "http://127.0.0.1:8000/myMaps/editMap/changeVersion/",
        //headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: JSON.stringify(data),
        type: "POST",
        success: function (response) {
            response = JSON.parse(response);
            tilesArr = [];
            chipsArr = [];
            charactersArr = [];
            pythonTiles = response.mapTiles;
            pythonChips = response.mapChips;
            pythonCharacters = response.mapCharacters;
            initTiles();
            initChips();
            initCharacters();
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

function saveMap(data) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        url: "http://127.0.0.1:8000/myMaps/editMap/saveMap/",
        //headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: JSON.stringify(data),
        type: "POST",
        success: function (response) {
            response = JSON.parse(response);
            maxOrder = response.newOrder;
            fillVersionOrder([response.newOrder])
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
        document.getElementById(id).appendChild(elem);
    }
}

function fillVersionOrder(versionOrders) {
    var sel = document.getElementById('versionOrders');
    var fragment = document.createDocumentFragment();

    versionOrders.forEach(function(versionOrder, index) {
        var opt = document.createElement('option');
        opt.innerHTML = 'Version_' + versionOrder;
        opt.value = versionOrder;
        if(index == (versionOrders.length - 1)){
            opt.selected = true;
        }
        fragment.appendChild(opt);

    });
    sel.appendChild(fragment);
}