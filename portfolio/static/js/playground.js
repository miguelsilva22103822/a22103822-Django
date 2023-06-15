const inputText = document.getElementById('meme-text-input');
const outputTexts = document.querySelectorAll('.meme-text');

inputText.addEventListener('input', () => {
    const text = inputText.value;

    outputTexts.forEach((outputText) => {
        outputText.textContent = text;
    });
});

const img1 = document.getElementById('meme1');
const img2 = document.getElementById('meme2');
const img3 = document.getElementById('meme3');
const container = document.getElementById('imgwithtextover');

const namea = document.getElementById('name-input');
const memeAuthor = document.getElementById('meme-author');

container.style.background = "url(media/shreksmol.png)";
container.style.backgroundRepeat = "no-repeat";
container.style.backgroundPosition = "center";


img1.addEventListener('click', () => {
    container.style.background = "url(media/dog.png)";
    container.style.backgroundRepeat = "no-repeat";
    container.style.backgroundPosition = "center";
});

img2.addEventListener('click', () => {
    container.style.background = "url(media/shreksmol.png)";
    container.style.backgroundRepeat = "no-repeat";
    container.style.backgroundPosition = "center";
});

img3.addEventListener('click', () => {
    container.style.background = "url(media/cj.png)";
    container.style.backgroundRepeat = "no-repeat";
    container.style.backgroundPosition = "center";
});

img3.addEventListener('click', () => {
    container.style.background = "url(media/cj.png)";
    container.style.backgroundRepeat = "no-repeat";
    container.style.backgroundPosition = "center";
});

namea.addEventListener('input', () => {
    memeAuthor.innerHTML = "Made by: " + namea.value;
    if(memeAuthor.innerHTML === "Made by: ") {
        memeAuthor.innerHTML = "";
    }
});