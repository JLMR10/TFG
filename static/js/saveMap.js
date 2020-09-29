


$(function init() {

    $(".save-map").click(function () {
        let baseTiles = [];
        let baseChips = [];
        let baseCharacters = [];
        tilesArr.forEach(e => baseTiles[baseTiles.length] = e.img);
        chipsArr.forEach(e => baseChips[baseChips.length] = e.img);
        charactersArr.forEach(e => baseCharacters[baseCharacters.length] = e.img);
        let data = {
            CSRF: csrftoken,
            tiles: baseTiles,
            chips: baseChips,
            characters: baseCharacters,
        }
        edit(data, csrftoken);
    });


});

function edit(data, csrftoken) {
    $.ajaxSetup({
        url: "",
        headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: data,
        type: "POST",
        success: function (response) {
            console.log(response);
        },
        error: function (response) {
            console.log(response);
        },
        async: true,
        contentType: "application/json; charset=utf-8",
        dataType: "json"
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
