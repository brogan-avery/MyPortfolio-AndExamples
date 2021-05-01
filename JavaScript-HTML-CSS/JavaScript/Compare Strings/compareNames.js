function compareNames() {
  let value1 = document.querySelector("#value1").value;
  let value2 = document.querySelector("#value2").value;

  if (validateName(value1) == false){
     if (value1.trim() == ""){
       err1 = "Input required";
     }
     else{
       err1 = "Invalid content";
     }
  }
  else{
    err1 = "";
  }

if (validateName(value2) == false){
   if (value2.trim() == ""){
     err2 = "Input required";
   }
   else{
     err2 = "Invalid content";
   }
}
else{
  err2 = "";
}

if (validateName(value1) == true && validateName(value2) == true){
   if (value1 == value2) {
     message = "same";
   }
   else {
     message = "different";
   }
 }
 else{
   message = "Cannot process invalid input";
 }

  document.querySelector(".displayErr1").innerHTML = err1;
  document.querySelector(".displayErr2").innerHTML = err2;
  document.querySelector(".displayMsg").innerHTML = message;
}

function validateName(inputText) {
  isValid = true;
    var alphaCount = 0;
    var invalidCharCount = 0;
    if(inputText.length > 100){
        isValid = false;
     }
     for (var i = 0; i < inputText.length; i++) {
       if (inputText.charAt(i).match(/[A-Za-z]/)){
            alphaCount++;
       }
        if (inputText.charAt(i).match("/")){
            invalidCharCount++;
     }
        if (inputText.charAt(i).match(/\\/)){
            invalidCharCount++;
     }
     if (inputText.charAt(i).match(/'/)){
         invalidCharCount++;
  }
  if (inputText.charAt(i).match(/"/)){
      invalidCharCount++;
}
   }
     if(alphaCount == 0 ){
       isValid = false;
     }
     if(invalidCharCount > 0){
       isValid = false;
     }
     return isValid
}

function restart() {
  document.querySelector(".displayMsg").innerHTML = " ";
  document.querySelector(".displayErr1").innerHTML = "";
  document.querySelector(".displayErr2").innerHTML = "";

}
