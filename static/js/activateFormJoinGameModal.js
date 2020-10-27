$(function init() {
    jQuery("#createBtn").prop('disabled', true);

    var toValidate = jQuery('#gameCode'),
    valid = false;
    toValidate.keyup(function () {
        if (jQuery(this).val().length > 0) {
            jQuery(this).data('valid', true);
        } else {
            jQuery(this).data('valid', false);
        }
        toValidate.each(function () {
            if (jQuery(this).data('valid') == true) {
                valid = true;
            } else {
                valid = false;
            }
        });
        if (valid === true) {
            jQuery("#createBtn").prop('disabled', false);
        } else {
            jQuery("#createBtn").prop('disabled', true);
        }
    });

    jQuery("#createBtnCharacter").prop('disabled', true);

    var toValidateJoinCharacter = jQuery('#characterName,#moveStat');
    validJoinCharacter = false;
    toValidateJoinCharacter.change(function () {
        if (jQuery(this).val().length > 0) {
            jQuery(this).data('valid', true);
        } else {
            jQuery(this).data('valid', false);
        }
        toValidateJoinCharacter.each(function () {
            if (jQuery(this).data('valid') == true) {
                validJoinCharacter = true;
            } else {
                validJoinCharacter = false;
            }
        });
        if (validJoinCharacter === true) {
            jQuery("#createBtnCharacter").prop('disabled', false);
            $('.select2-container--default .select2-selection--single').css('border-color','#4e73df');
            $('.select2-selection__rendered').css('color','#000');
        } else {
            jQuery("#createBtnCharacter").prop('disabled', true);
            $('.select2-container--default .select2-selection--single').css('border-color','#ccc');
            $('.select2-selection__rendered').css('color','#7d7d7d');
        }
    });


    jQuery("#createBtnGames").prop('disabled', true);

    var toValidateGames = jQuery('#gameList'),
    validGame = false;
    toValidateGames.change(function () {
        if (jQuery(this).val().length > 0) {
            jQuery(this).data('valid', true);
        } else {
            jQuery(this).data('valid', false);
        }
        toValidateGames.each(function () {
            if (jQuery(this).data('valid') == true) {
                validGame = true;
            } else {
                validGame = false;
            }
        });
        if (validGame === true) {
            jQuery("#createBtnGames").prop('disabled', false);
            $('.select2-container--default .select2-selection--single').css('border-color','#4e73df');
            $('.select2-selection__rendered').css('color','#000');
        } else {
            jQuery("#createBtnGames").prop('disabled', true);
            $('.select2-container--default .select2-selection--single').css('border-color','#ccc');
            $('.select2-selection__rendered').css('color','#7d7d7d');
        }
    });

    jQuery("#createBtnCreateGame").prop('disabled', true);

    var toValidateCreateGame = jQuery('#mapId,#gameName');
    validCreateGame = false;
    toValidateCreateGame.change(function () {
        if (jQuery(this).val().length > 0) {
            jQuery(this).data('valid', true);
        } else {
            jQuery(this).data('valid', false);
        }
        toValidateCreateGame.each(function () {
            if (jQuery(this).data('valid') == true) {
                validCreateGame = true;
            } else {
                validCreateGame = false;
            }
        });
        if (validCreateGame === true) {
            jQuery("#createBtnCreateGame").prop('disabled', false);
            $('.select2-container--default .select2-selection--single').css('border-color','#4e73df');
            $('.select2-selection__rendered').css('color','#000');
        } else {
            jQuery("#createBtnCreateGame").prop('disabled', true);
            $('.select2-container--default .select2-selection--single').css('border-color','#ccc');
            $('.select2-selection__rendered').css('color','#7d7d7d');
        }
    });



    $('#gameList').on("change", function () {
        $('#ModalMyGamesForm').attr("action", '/game/'+ $('#gameList').val())
    });

    $(document).ready(function() {
        $('.modal-select').select2();
    });

    $('#ModalJoinForm').submit(function (event) {
        event.preventDefault();
        var modalJoinForm = $(this);
        let gameCode = event.currentTarget[1].value;
        joinGameModal({"gameCode":gameCode})

    })

    $('#ModalJoinCharacterForm').submit(function (event) {
        event.preventDefault();
        var modalJoinForm = $(this);
        let gameId = event.currentTarget[1].value;
        let characterMove = event.currentTarget[3].value;
        let characterName = event.currentTarget[5].value;
        joinGameCharacterModal({"gameId":gameId, "characterName":characterName, "characterMove":characterMove})

    })

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
        url: "http://127.0.0.1:8000/mainMenu/joinGameModal/",
        //headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: JSON.stringify(data),
        type: "POST",
        success: function (response) {
            console.log(response);
            jsonData = JSON.parse(response);
            console.log(jsonData.gameCode);

            if (jsonData.gameExist) {
                $('#error-div').remove();
                if (jsonData.isNewUser) {
                    $('#joinGameCharacter').fadeIn("slow", function () {
                        $('#joinGameCharacter').modal('show');
                    });
                    $('#joinGame').fadeOut("slow", function () {
                        $('#joinGame').modal('hide');
                    });
                    $('#gameId').attr("value", jsonData.gameId);
                } else {
                    $(".loader-wrapper").fadeIn("slow");
                    var loc = window.location;
                    var origin = loc.origin;
                    let url = origin + "/game/" + jsonData.gameId;
                    $(".loader-wrapper").fadeIn("slow");
                    $(location).prop('href', url);
                }
            } else {
                $('#error-div').remove();
                $('#modal-body-join').append("<div class=\"alert alert-danger alert-dismissible\" id=\"error-div\" role=\"alert\">\n" +
                    "    <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                    "      <span aria-hidden=\"true\">×</span>\n" +
                    "    </button>\n" +
                    "    The game with code " + jsonData.gameCode + " doesn't exist.\n" +
                    "  </div>")
            }


        },
        error: function (response) {
            console.log(response);
        },
        async: true,
        contentType: "application/json; charset=utf-8",
        dataType: "text"
    });
}

function joinGameCharacterModal(data) {

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
        url: "http://127.0.0.1:8000/mainMenu/JoinGameCharacterModal/",
        //headers: { "X-CSFRToken": getCookie("csrftoken")},
        data: JSON.stringify(data),
        type: "POST",
        success: function (response) {
            console.log(response);
            jsonData = JSON.parse(response);
            if (jsonData.isMaximumUsersReached) {
                $('#error-div').remove();
                $('#modal-body-joinCharacter').append("<div class=\"alert alert-danger alert-dismissible\" id=\"error-div\" role=\"alert\">\n" +
                    "    <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                    "      <span aria-hidden=\"true\">×</span>\n" +
                    "    </button>\n" +
                    "    The game has reached the maximum number of users\n" +
                    "  </div>")
            }else{
                $(".loader-wrapper").fadeIn("slow");
                $('#error-div').remove();
                var loc = window.location;
                var origin = loc.origin;
                let url = origin+"/game/"+jsonData.gameId;
                $(location).prop('href', url);
            }
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
