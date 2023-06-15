const lightOn = new Audio("media/lightOn.mp3");
const lightOff = new Audio("media/lightOff.mp3");

const sun = "<i class=\"fa-solid fa-sun fa-3x\"></i>";
const moon = "<i class=\"fa-solid fa-moon fa-3x\"></i>";

var backgroundColor = "rgb(0, 0, 0)";
var transparentBg = "rgba(0, 0, 0, 0.3)";
var transparentBg2 = "rgba(0, 0, 0, 0.7)";
var color = "rgb(255, 255, 255)";
var accentColor = "rgb(0, 200, 0)";
var accentColor2 = "rgb(175, 240, 0)";
var elementBackgroundColor = "rgb(76, 76, 76)";
setProperties();
document.getElementById("themetoggle").innerHTML = moon;
var currentTheme = "dark";

document.getElementById("themetoggle").onclick = function() {
    if (currentTheme === "dark") {
        setLightTheme();
    } else if (currentTheme === "light") {
        setDarkTheme();
    }
}

function setDarkTheme() {
    lightOff.play();

    backgroundColor = "rgb(0, 0, 0)";
    transparentBg = "rgba(0, 0, 0, 0.3)";
    transparentBg2 = "rgba(0, 0, 0, 0.7)";
    color = "rgb(255, 255, 255)";
    elementBackgroundColor = "rgb(76, 76, 76)";

    setProperties();
    document.getElementById("themetoggle").innerHTML = moon;
    currentTheme = "dark";
}

function setLightTheme() {
    lightOn.play();

    backgroundColor = "rgb(255, 255, 255)";
    transparentBg = "rgba(255, 255, 255, 0.3)";
    transparentBg2 = "rgba(255, 255, 255, 0.7)";
    color = "rgb(0, 0, 0)";
    elementBackgroundColor = "rgb(179, 179, 179)";

    setProperties();
    document.getElementById("themetoggle").innerHTML = sun;
    currentTheme = "light";
}

function setProperties() {
    document.documentElement.style.setProperty('--backgroundColor', backgroundColor);
    document.documentElement.style.setProperty('--transparentBg', transparentBg);
    document.documentElement.style.setProperty('--transparentBg2', transparentBg2);
    document.documentElement.style.setProperty('--color', color);
    document.documentElement.style.setProperty('--accentColor', accentColor);
    document.documentElement.style.setProperty('--accentColor2', accentColor2);
    document.documentElement.style.setProperty('--elementBackgroundColor', elementBackgroundColor);
}