// Get reference to the element to be faded
var fadeElement = document.getElementById("fade-element");

// Add scroll event listener
window.addEventListener("scroll", function () {
    // Calculate scroll progress (value between 0 and 1)
    var scrollProgress = window.pageYOffset / (document.documentElement.scrollHeight - window.innerHeight);

    // Set opacity of the element to be faded based on scroll progress
    fadeElement.style.opacity = 1 - scrollProgress * 3; // Fade out element as scroll progresses
    fadeElement.style.height = 80 - scrollProgress * 160 + "%";
});

// Smooth scrolling with speed curve
document.getElementById("arrow-down").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = window.innerHeight * 1; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

document.getElementById("calculator").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = window.innerHeight * 2; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

document.getElementById("introduction").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = window.innerHeight * 2; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

document.getElementById("playground").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = window.innerHeight * 2; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

document.getElementById("arrow-up").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = 0; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

document.getElementById("arrow-up-low").addEventListener("click", function () {
    // Set target scroll position (adjust as needed)
    var targetScrollPos = window.innerHeight * 1; // Scroll down by 500 pixels

    // Call custom smooth scroll function with speed curve
    smoothScrollTo(targetScrollPos, 1000, "easeInOutQuad"); // Adjust duration and timing function as needed
});

function smoothScrollTo(targetPosition, duration, timingFunction) {
    var startPosition = window.pageYOffset;
    var startTime = performance.now();

    // Timing functions
    var timingFunctions = {
        linear: function (timeFraction) {
            return timeFraction;
        },
        easeInOutQuad: function (timeFraction) {
            return timeFraction < 0.5 ? 2 * timeFraction * timeFraction : 1 - Math.pow(-2 * timeFraction + 2, 2) / 2;
        },
        // Add more timing functions as needed
    };

    // Animation loop
    function animate(currentTime) {
        var timeElapsed = currentTime - startTime;
        var timeFraction = timeElapsed / duration;

        if (timeFraction > 1) {
            timeFraction = 1;
        }

        var progress = timingFunctions[timingFunction](timeFraction);
        var currentScrollPos = startPosition + (targetPosition - startPosition) * progress;
        window.scrollTo(0, currentScrollPos);

        if (timeFraction < 1) {
            requestAnimationFrame(animate);
        }
    }

    requestAnimationFrame(animate);
}