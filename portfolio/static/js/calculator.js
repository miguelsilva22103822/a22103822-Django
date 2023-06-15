const calculator = document.querySelector('.calculator')
const keys = calculator.querySelector('#calculator-buttons')
const screen = document.getElementById('screen');

keys.addEventListener('click', e => {
 if (e.target.matches('button, i')) {
    const key = e.target
    const action = key.dataset.action

    if (!action) {
        screen.innerHTML += key.innerHTML;
    }

    if (
        action === 'add' ||
        action === 'subtract' ||
        action === 'multiply' ||
        action === 'divide' ||
        action === 'sqrt' ||
        action === 'percent'
      ) {
        switch(action) {
            case 'add':
                screen.innerHTML += "+";
                break;
            case 'subtract':
                screen.innerHTML += "-";
                break;
            case 'multiply':
                screen.innerHTML += "*";
                break;
            case 'divide':
                screen.innerHTML += "/";
                break;
        }
    }

    if (action === 'decimal') {
        screen.innerHTML += "."
    }
      
    if (action === 'clear') {
        screen.innerHTML = "";
    }
      
    if (action === 'calculate') {
        screen.innerHTML = eval(screen.innerHTML);
    }

    if(screen.innerHTML.length > 10 || screen.innerHTML === "undefined") {
        screen.innerHTML = "";
    }
 }
})