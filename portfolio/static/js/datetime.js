const dateElement = document.getElementById("date");
const timeElement = document.getElementById("time");
const fullDateElement = document.getElementById("datetime")

const date = new Date();

const timeOptions = {
    hour: "2-digit",
    minute: "2-digit",
    hourCycle: "h23"
};

const dateOptions = {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
}

const formattedDate = date.toLocaleString("pt-PT", dateOptions);
const formattedTime = date.toLocaleString("pt-PT", timeOptions);

dateElement.innerHTML = formattedDate;
timeElement.innerHTML = formattedTime;
fullDateElement.innerHTML += formattedDate + " - " + formattedTime;