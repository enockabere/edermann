$(document).ready(function () {
    $("#reg").click(function (e) {
        e.preventDefault();
        $("#a-right").hide();
        $("#n-right2").show();
    })
    $("#log").click(function (e) {
        e.preventDefault();
        $("#n-right2").hide();
        $("#a-right").show();
    })
})
$(document).ready(function () {
    $("#cards1").hover(function (e) {
        e.preventDefault();
        $("#btn1").css({
            'color': 'black',
            'border-color': 'red'
        })
    })
})
$(document).ready(function () {
    $("#cards2").hover(function (e) {
        e.preventDefault();
        $("#btn2").css({
            'color': 'black',
            'border-color': 'red'
        })
    })
})
$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('color')
        }
        if ($(this).scrollTop() < 50) {
            $('.navbar').removeClass('color')
        }
    });
});
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
