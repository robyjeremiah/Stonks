$(document).ready(function () {
    validatePassword();
})

function validatePassword() {
    // Shows the required field when password is focused on
    $('#password').focus(function () {
        $('.required').show();
    })
    // Hides the required field for when password is not focused on
    $('#password').blur(function () {
        $('.required').hide();
    })

    // Requirement #1 - Starts with a capitalized letter
    $('#password').keyup(function () {
        var value = this.value;
        var uppercase = /[A-Z]/g;
        if (uppercase.test(value.charAt(0))) {
            console.log('success1');
            $('#capital').removeClass('invalid');
            $('#capital').addClass('valid');
        } else {
            $('#capital').removeClass('valid');
            $('#capital').addClass('invalid');
        }


    })

    // Requirement #2 - At least 8 characters
    $('#password').keyup(function () {
        var value = this.value;
        if (value.length >= 8) {
            console.log('success2');
            $('#length').removeClass('invalid');
            $('#length').addClass('valid');
        } else {
            $('#length').removeClass('valid');
            $('#length').addClass('invalid');
        }
    })

    // Requirement #3 - At least one letter, number, and special character is used
    $("#password").keyup(function () {
        var value = this.value;
        var lowercase = /[a-z]/g;
        var numbers = /[0-9]/g;
        var specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

        if (lowercase.test(value) && numbers.test(value) && specialChars.test(value)) {
            console.log('success3');
            $('#mixed').removeClass('invalid');
            $('#mixed').addClass('valid');
        } else {
            $('#mixed').removeClass('valid');
            $('#mixed').addClass('invalid');
        }

    })
}