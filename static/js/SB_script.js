function isClick(id) {
    var main = document.getElementById("main");
    var contax = document.getElementById("contax");
    var PI = document.getElementById("PI");
    var docs = document.getElementById("docs");
    var other1 = document.getElementById("other1");
    var other2 = document.getElementById("other2");
    var other3 = document.getElementById("other3");
    var other4 = document.getElementById("other4");
    var other5 = document.getElementById("other5");

    if (PI.style.top == main.style.top) {
        PI.style.top = "212px";
        contax.style.top = "300px";
        docs.style.top = "212px";


        PI.style.right = "212px";
        docs.style.left = "212px";

        // other1.style.right = "300px";
        // other2.style.right = "212px";
        // other2.style.top = "-212px";
        // other3.style.top = "-300px";
        // other4.style.top = "-212px";
        // other4.style.right = "-212px";
        // other5.style.right = "-300px";
        // main.style.height = "150px";
        // main.style.width = "150px";
    }
    else {
        PI.style.top = main.style.top;
        contax.style.top = main.style.top;
        docs.style.top = main.style.top;
        PI.style.right = main.style.right;
        docs.style.left = main.style.left;

        // other1.style.right = main.style.left;
        // other2.style.right = main.style.left;
        // other4.style.right = main.style.left;
        // other5.style.right = main.style.left;
        // other2.style.top = main.style.top;
        // other3.style.top = main.style.top;
        // other4.style.top = main.style.top;
        // main.style.height = "100px";
        // main.style.width = "100px";
    }
}

$(document).ready(function () {
    $(".dropdown-toggle-js").dropdown();
});


function Menu(id) {
    var ONE = document.getElementById("ONE");
    var TWO = document.getElementById("TWO");
    var THREE = document.getElementById("THREE");
    var FOUR = document.getElementById("FOUR");
    if ((isNaN(parseInt(TWO.style.top))) || (TWO.style.top == "0px")) {

        TWO.style.top = "220px";
        FOUR.style.top = "-220px";

    }

    else {
        TWO.style.top = "0px";
        FOUR.style.top = "0px";
    }

}