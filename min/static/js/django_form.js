

const form = document.getElementById("Form");



//Getting values from input fields using ID or name
var firstname = document.getElementById("firstName");
var phonenumber = document.getElementById("mob");
var email = document.getElementById("email");
var gender = document.getElementsByName('gender');
const givenDateField = document.getElementById("date");
var jobRole = document.getElementById("role");
var experience = document.getElementById("experience");

//onsubmit validation
form.addEventListener('submit', (event) => {

    validateFirstName(event);
    validatePhone(event);
    validateEmail(event);
    validateDate(event);
    validateGender(event);
    validateJobRole(event);
    validateExperience(event);

});



// First name validation
function validateFirstName(event) {
    if (firstname.value.trim() === "") {
        document.getElementById("validFirstName").innerHTML = "Name can not be empty";
        event.preventDefault();
        return false;
    }
    if ((firstname.value.trim().length < 3) || (firstname.value.trim().length > 25)) {
        document.getElementById("validFirstName").innerHTML = "Number of letters must be between 3 and 25";
        event.preventDefault();
        return false;
    }

    else {
        document.getElementById("validFirstName").innerHTML = "";
        return true
    }

}

//calling onchange event for firstname validation
firstname.addEventListener('change', (event) => {
    validateFirstName(event);

});


// Phone number validation
function validatePhone(event) {
    const regexmob = /^\d{10}$/;
    if (phonenumber.value.trim() === "") {
        document.getElementById("validateNumber").innerHTML = "Number can not be empty";
        event.preventDefault();
        return false;
    }
    if (!regexmob.test(phonenumber.value.trim())) {
        document.getElementById("validateNumber").innerHTML = "Phone number is invalid";
        event.preventDefault();
        return false;
    }
    else {
        document.getElementById("validateNumber").innerHTML = "";
        return true;
    }
}

//calling onchange event for phone validation
phonenumber.addEventListener('change', (event) => {
    validatePhone(event);

});

// Email validation
function validateEmail(event) {
    const regexemail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.value.trim() === "") {
        document.getElementById("validateEmail").innerHTML = "Email can not be empty";
        event.preventDefault();
        return false;
    }
    if (!regexemail.test(email.value.trim())) {
        document.getElementById("validateEmail").innerHTML = "Email format is invalid";
        event.preventDefault();
        return false;
    }
    else {
        document.getElementById("validateEmail").innerHTML = "";
        return true;
    }
}

//calling onchange event for email validation
email.addEventListener('change', (event) => {
    validateEmail(event);

});

// Gender validation
 function validateGender(event) {

    var genderFlag = false;
    for (var i = 0; i < gender.length; i++) {
        if (gender[i].checked) {
            genderFlag = true;
            document.getElementById('validateGender').innerHTML = "";
            break;
        }
    }
    if (genderFlag == false) {
        document.getElementById('validateGender').innerHTML = "Choose any one option";
        return false;
    }
    return genderFlag;
}

// gender.addEventListener('change', (event) => {
//     validateGender(event);

// });

// Date validation
function validateDate(event) {
    const givenDate = document.getElementById("date").value;
    console.log("givendate=", givenDate);
    const date1 = new Date();
    console.log("date1=", date1);
    const date2 = new Date(givenDate);
    console.log("date2=", date2);
    const timeDiff = (date1 - date2) / (1000 * 60 * 60 * 24 * 365.25);
    if (timeDiff >= 18) {
        document.getElementById("validateDate").innerHTML = "";
        return true;
    }
    else {
        document.getElementById("validateDate").innerHTML = "Below 18 years";
        event.preventDefault();
        return false;
    }
}

//calling onchange event for date of birth validation
givenDateField.addEventListener('change', (event) => {
    validateDate(event);

});

//Job role validation
function validateJobRole(event) {

    if (jobRole.value == "" || jobRole.value == null) {
        document.getElementById("validateJobRole").innerHTML = "Can not be empty";
        event.preventDefault();
        return false;
    }
    else if ((jobRole.value == "Developer") || (jobRole.value == "Testing") || (jobRole.value == "Devops") || (jobRole.value == "Operations") || (jobRole.value == "Accounting")) {
        document.getElementById("validateJobRole").innerHTML = "";
        return true;
    }
}

//calling onchange event for job role validation
jobRole.addEventListener('change', (event) => {
    validateJobRole(event);

});

//Experience validation
function validateExperience(event) {

    if (experience.value == "" || experience.value == null) {
        document.getElementById("validateExperience").innerHTML = "Can not be empty";
        event.preventDefault();
        return false;
    }
    else {
        document.getElementById("validateExperience").innerHTML = "";
        return true;
    }
}

//calling onchange event for experience validation
experience.addEventListener('change', (event) => {
    validateExperience(event);

});


//Disabling the back button
function preventbackbutton() { window.history.forward(); }
setTimeout("preventbackbutton()", 0);
window.onunload = function () { null };


