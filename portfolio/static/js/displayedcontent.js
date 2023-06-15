const calculatorPage = document.getElementById("calculator-page");
const introductionPage = document.getElementById("introduction-page")
const playgroundPage = document.getElementById("playground-page")

calculatorPage.style.display = "none";
introductionPage.style.display = "none";
playgroundPage.style.display = "none";

document.getElementById("calculator").addEventListener("click", function () {
    calculatorPage.style.display = "flex";
    introductionPage.style.display = "none";
    playgroundPage.style.display = "none";
});

document.getElementById("introduction").addEventListener("click", function () {
    calculatorPage.style.display = "none";
    introductionPage.style.display = "flex";
    playgroundPage.style.display = "none";
});

document.getElementById("playground").addEventListener("click", function () {
    calculatorPage.style.display = "none";
    introductionPage.style.display = "none";
    playgroundPage.style.display = "flex";
});