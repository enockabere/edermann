$(document).ready(function(){
    $("#reg").click(function(e){
        e.preventDefault();
        $("#a-right").hide();
        $("#n-right2").show();
    })
    $("#log").click(function(e){
        e.preventDefault();
        $("#n-right2").hide();
        $("#a-right").show();
    })
})
$(document).ready(function(){
    $("#cards1").hover(function(e){
        e.preventDefault();
        $("#btn1").css({'color':'black','border-color':'red'})
    })
})
$(document).ready(function(){
    $("#cards2").hover(function(e){
        e.preventDefault();
        $("#btn2").css({'color':'black','border-color':'red'})
    })
})
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});