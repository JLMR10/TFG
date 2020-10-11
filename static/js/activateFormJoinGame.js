$(function init() {
    jQuery("#createBtn").prop('disabled', true);

    var toValidate = jQuery('#characterName, #moveStat'),
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
});



