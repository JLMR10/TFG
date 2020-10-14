


$(function init() {

    $(".save-map").click(function () {
        let baseTiles = [];
        let baseChips = [];
        let baseCharacters = [];
        tilesArr.forEach(e => baseTiles[baseTiles.length] = e.img);
        chipsArr.forEach(e => baseChips[baseChips.length] = e.img);
        charactersArr.forEach(e => baseCharacters[baseCharacters.length] = e.img);
        let data = {
            tiles: baseTiles,
            chips: baseChips,
            characters: baseCharacters,
        }
        edit(data);
    });


});

function joinGameModal(data) {

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
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
            console.log(response);
        },
        error: function (response) {
            console.log(response);
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
