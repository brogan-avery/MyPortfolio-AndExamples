function compareNumbers() {
  let value1 = document.querySelector("#value1").value;
  let value2 = document.querySelector("#value2").value;

  if (value1 == value2) {
    result = "Equal";
  }
  else if (value1 > value2) {
    result = ("Larger Number: " + value1);
  }
  else if (value2 > value1) {
    result = ("Larger Number: " + value2);
  }
  document.querySelector(".displayResult").innerHTML = result;
}

function resetForm() {
  document.querySelector(".displayResult").innerHTML = " ";
}


function JcompareNumbers() {
  let value1 = document.querySelector("#Jvalue1").value;
  let value2 = document.querySelector("#Jvalue2").value;

    if(validateNumbers(value1) == false){
          if (value1.trim() == ""){
            err1 = "Input required";
          }
          else{
            err1 = "Invalid content";
          }
     }
     else{
          err1 = ""
     }

    if(validateNumbers(value2) == false){
         if (value2.trim() == ""){
           err2 = "Input required";
         }
         else{
           err2 = "Invalid content";
         }
     }
    else{
         err2 = ""
    }

if(validateNumbers(value1) == true && validateNumbers(value2) == true){
  if (value1 == value2) {
    result = "Equal";
  }
  else if (value1 > value2) {
    result = ("Larger Number: " + value1);
  }
  else if (value2 > value1) {
    result = ("Larger Number: " + value2);
  }
}
else{
     result = "Cannot process form";
}
  document.querySelector(".JdisplayResult").innerHTML = result;
  document.querySelector(".displayErr1").innerHTML = err1;
  document.querySelector(".displayErr2").innerHTML = err2;
}

function validateNumbers(value){
     isValid = true;
     if (value.length > 100 || value < 0 || value == "") {
          isValid = false;
     }
     for (var i = 0; i < value.length; i++) {
          if (value.charAt(i).match(/\D/) || value.charAt(i).match(/\s/)){
          isValid = false;
     }
     }
     return isValid;
}


function JresetForm() {
  document.querySelector(".JdisplayResult").innerHTML = " ";
  document.querySelector(".displayErr1").innerHTML = "";
  document.querySelector(".displayErr2").innerHTML = "";
}
