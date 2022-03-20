let BackgroundBlack = document.getElementById("BackgroundBlack");
let MouseOverForm = false;
let RegistrationActive = document.getElementById("RegistrationActive");

function ShowWindowRegistration() {
  document.getElementById("RegistrationActive").style.display = "block";
  document.getElementById("BackgroundBlack").style.display = "block";
}

let x = document.getElementById("RegistrationActive");
if(x){
  x.addEventListener("focus", myFocusFunction, true);
  x.addEventListener("blur", myBlurFunction, true);
}
function myFocusFunction() {
    document.getElementById("RegistrationActive").style.display = "block";
}
function myBlurFunction() {
    document.getElementById("RegistrationActive").style.display = "block";
}
function CloseWindowRegistration() {
  document.getElementById('RegistrationActive').style.display = "none";
  document.getElementById("BackgroundBlack").style.display = "none";
}
BackgroundBlack.addEventListener('click', function (){
    if (!MouseOverForm){
        BackgroundBlack.style.display = "none";
    }
});
RegistrationActive.addEventListener('mouseover', function (){
    MouseOverForm = true;
});
RegistrationActive.addEventListener('mouseout', function (){
    MouseOverForm = false;
});


