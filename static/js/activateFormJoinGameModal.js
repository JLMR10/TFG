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
        } else {
            jQuery("#createBtnGames").prop('disabled', true);
        }
    });

    $('#gameList').on("change", function () {
        $('#ModalMyGamesForm').attr("action", '/game/'+ $('#gameList').val())
    })

});