const soundOn = "<i class=\"fa-solid fa-volume-low fa-3x\"></i>";
const soundOff = "<i class=\"fa-solid fa-volume-xmark fa-3x\"></i>";

const buttonSfx = new Audio("media/buttonSfx.mp3");

document.getElementById("mutetoggle").innerHTML = soundOn;

const piano = new Audio("media/piano.mp3");

piano.loop = true;
piano.play();
var mute = false;

document.getElementById("mutetoggle").onclick = function() {
    if (mute) {
        document.getElementById("mutetoggle").innerHTML = soundOn;
        buttonSfx.play();
        piano
    .play();
        mute = false;
    } else {
        document.getElementById("mutetoggle").innerHTML = soundOff;
        buttonSfx.play();
        piano
    .pause();
        mute = true;
    }
}