$(document).ready(function() {
    if ($('#agreement_check').is(':checked')) {
        //Enable the submit button.
        $('#submit_button').attr("disabled", false);
    } else {
        //If it is not checked, disable the button.
        $('#submit_button').attr("disabled", true);
    }
});

$('#agreement_check').click(function() {
    //If the checkbox is checked.
    if ($('#agreement_check').is(':checked')) {
        //Enable the submit button.
        $('#submit_button').attr("disabled", false);
    } else {
        //If it is not checked, disable the button.
        $('#submit_button').attr("disabled", true);
    }
});