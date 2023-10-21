

const form = document.getElementById("Form");

//Onsubmit validation
function validateForm(event){
    validateFirstName();
    validateEmail();
    validateDate();
    validatePhone();
    validateJobRole();
    validateGender();
    validateExperience();
    if (validateFirstName() && validatePhone() && validateEmail() && validateJobRole() && validateGender() && validateExperience() && validateDate() === true){
        console.log("submitted");
        event.submit();    
    }
    else{
        event.preventDefault(); 
        return;
    }
}

// First name validation
function validateFirstName(event){
    var firstname = document.getElementById("firstName").value.trim();
    
    
        if(firstname===""){
            document.getElementById("validFirstName").innerHTML="Name can not be empty"; 
            return false;
        }
        if((firstname.length<3) || (firstname.length>25)){
            document.getElementById("validFirstName").innerHTML="Number of letters must be between 3 and 25";
            return false;
        }
        
        else{
            document.getElementById("validFirstName").innerHTML="";    
            return true
        }
    
}



// Last name validation
// function validateLastName(event){
//     var lastname = document.getElementById("lastName").value.trim();
//     if(lastname===""){
//         document.getElementById("validLastName").innerHTML="Name can not be empty";
//         // console.log("121");
//         return false;
//     }
//     if((lastname.length<1) || (lastname.length>25)){
//         document.getElementById("validLastName").innerHTML="Number of letters must be between 1 and 25";
//         return false;
//     }
//     else{
//         document.getElementById("validLastName").innerHTML="";
//         return true;
//     }
// }




// Phone number validation
function validatePhone(event){
    var phonenumber = document.getElementById("mob").value.trim();
    const regexmob = /^\d{10}$/;
    if(phonenumber===""){
        document.getElementById("validateNumber").innerHTML="Number can not be empty";
        return false;
    }
    if(!regexmob.test(phonenumber)){
        document.getElementById("validateNumber").innerHTML="Phone number is invalid";
        return false;
    }
    else{
        document.getElementById("validateNumber").innerHTML="";     
        return true;
    }
}

// Email validation
function validateEmail(event){
    var email = document.getElementById("email").value.trim();
    const regexemail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if(email===""){
        document.getElementById("validateEmail").innerHTML="Email can not be empty";
        return false;
    }
    if(!regexemail.test(email)){
        document.getElementById("validateEmail").innerHTML="Email format is invalid";    
        return false;
    }
    else{
        document.getElementById("validateEmail").innerHTML="";     
        return true;
    }
}

// Gender validation
function validateGender(event){
    var gender=document.getElementsByName('gender');
    var genderFlag = false;
    for(var i=0;i<gender.length;i++){
        if(gender[i].checked){
            genderFlag = true;
            document.getElementById('validateGender').innerHTML="";
            break;    
        }    
    }
    if(genderFlag == false){
        document.getElementById('validateGender').innerHTML="Choose any one option";   
        return false;
    }
    return genderFlag;
}

// Date validation
function validateDate(event){ 
    const givenDate = document.getElementById("date").value;
    console.log("givendate=",givenDate);
    const date1 = new Date();
    console.log("date1=",date1);
    const date2 = new Date(givenDate);
    console.log("date2=",date2);
    const timeDiff = (date1-date2)/(1000*60*60*24*365.25);
    if (timeDiff>=18){
        document.getElementById("validateDate").innerHTML="";
        return true;
    }
    else{
        document.getElementById("validateDate").innerHTML="Below 18 years";     
        return false;
    }
}

//Job role validation
function validateJobRole(event){
    var jobRole = document.getElementById("role").value;
    if (jobRole == "" || jobRole == null){
        document.getElementById("validateJobRole").innerHTML="Can not be empty";
        return false;
    }
    else if((jobRole == "Developer") || (jobRole == "Testing") || (jobRole == "Devops") || (jobRole == "Operations") || (jobRole == "Accounting")){
        document.getElementById("validateJobRole").innerHTML="";    
        return true;
    }
}

//Experience validation
function validateExperience(event){
    var experience = document.getElementById("experience").value;
    if(experience == "" || experience == null ){
        document.getElementById("validateExperience").innerHTML="Can not be empty";
        return false;
    }
    else{
        document.getElementById("validateExperience").innerHTML="";
        return true;
    }
}


//Disabling the back button
function preventbackbutton(){window.history.forward();}
setTimeout("preventbackbutton()", 0);
window.onunload=function(){null};