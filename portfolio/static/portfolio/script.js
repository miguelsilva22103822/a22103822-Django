showMenu = function () {
    var bar1 = document.querySelector(".bar1");
    var bar2 = document.querySelector(".bar2");
    var bar3 = document.querySelector(".bar3");

    if (document.getElementsByClassName('menu-container')[0].style.visibility === "visible") {
        document.getElementsByClassName('menu-container')[0].style.visibility = "hidden";
        bar1.classList.remove("change");
        bar2.classList.remove("change");
        bar3.classList.remove("change");
    }
    else {
        document.getElementsByClassName('menu-container')[0].style.visibility = "visible";
        bar1.classList.add("change");
        bar2.classList.add("change");
        bar3.classList.add("change");
    }
}


const display = document.querySelector(".display")
const buttons = document.querySelectorAll("button")

buttons.forEach((button) => {
    button.addEventListener("click", () => {
    console.log(button.value)

        if (button.value === "C") {
            display.innerText = "";
        }
        else if (button.value === "=") {
            display.innerText = eval(display.innerText) ;
        }
        else {
            display.innerText += button.value;
        }
        console.log(display.value)
    })})

const data = document.querySelector(".date")
const date = new Date()
const meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
data.innerText = date.getDate() + " de " + meses[date.getMonth()] + " , " + date.getFullYear();


function playgroundText() {
    console.log("a");
    const opiniao = document.getElementById("opiniao").value
    document.querySelector("p.p-opiniao").innerHTML = opiniao;
    const nome = document.getElementById("nomes").value
    document.querySelectorAll(".nomes p").forEach(n => n.innerHTML = nome)
    return true;
}

function lightMode() {
    var body = document.querySelector("body");
    var bar1 = document.querySelector(".bar1");
    var bar2 = document.querySelector(".bar2");
    var bar3 = document.querySelector(".bar3");
    var data = document.querySelector(".date");
    var calculator = document.querySelector(".calculator");
    var display = document.querySelector(".display");
    var textPlayground = document.querySelector(".text-playground");

    if(body.style.backgroundColor !==  "rgb(224, 224, 224)") {
        body.style.backgroundColor =  "#E0e0e0";
        bar1.style.backgroundColor =  "black";
        bar2.style.backgroundColor =  "black";
        bar3.style.backgroundColor =  "black";
        data.style.color = "black";
        calculator.style.border = "black 5px solid";
        display.style.border = "black 4px solid";
        textPlayground.style.color = "black";
    }
    else {
        console.log("a");
        body.style.backgroundColor = "rgb(25, 25, 25)";
        bar1.style.backgroundColor =  "white";
        bar2.style.backgroundColor =  "white";
        bar3.style.backgroundColor =  "white";
        data.style.color = "white";
        calculator.style.border = "white 3px solid";
        display.style.border = "white 3px solid";
        textPlayground.style.color = "white";
    }
}

function mudaCorInput(input) {
    input.style.backgroundColor = "rgb(95, 5, 122)";
}

function tiraCorInput(input) {
    input.style.backgroundColor = "#414249";
}

async function aumentaLike(id) {
    await fetch("addLike/" + id)
}

async function diminuiLike(id) {
    await fetch("diminuiLike/" + id)
}
