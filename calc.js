
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

tests = {
    "1+2*3": 7,
    "1*2+3": 5,
    "1+2+3": 6,
    "1*2*3": 6,
    "1-2-3": -4,
    "4*2/2": 4,
    "231*13-34*34": 1847
}

equationOrder = [
    "*",
    "/",
    "+",
    "-"
]   

const testEquations = (timing = false) => {
    for (let [equation, expectedResult] of Object.entries(tests)) {
        if (expectedResult == calculate(splitEquation(equation))) {
            if(!timing)
                console.log("Passed ", equation)
        }
        else {
            if(!timing){
            console.log("Failed ", equation)
            console.log("Expected: ", expectedResult)
            console.log("Result: ", calculate(splitEquation(equation)))
            console.log("Result: ", expectedResult == calculate(splitEquation(equation)))
        }}
    }
}

const multiply = (num1, num2) => {
    return num1 * num2
}

const divide = (num1, num2) => {
    return num1 / num2
}

const add = (num1, num2) => {
    return num1 + num2
}

const subtract = (num1, num2) => {
    return num1 - num2
}

const splitEquation = (equation) => {
    return equation.match(/\d+|[+\-*/]/g)
}


const calculate = (equation) => {
    for(symbol of equationOrder) {
        while (equation.includes(symbol)) {
            let index = equation.indexOf(symbol)
            let result = 0
            let num1 = parseInt(equation[index-1])
            let num2 = parseInt(equation[index+1])
            switch (symbol) {
                case "*":
                    result = multiply(num1, num2)
                    break;
                case "/":
                    result = divide(num1, num2)
                    break;
                case "+":
                    result = add(num1, num2)
                    break
                case "-":
                    result = subtract(num1, num2)
                    break
            }
            equation.splice(index-1, 3, result)
        }
    }
    return equation[0]
}

const testing = true

console.log("Testing mode set to :", testing, "\n")


function run(fn, count, ...args) {
    const start = performance.now()
    for (let i = 0; i < count; i++) {
        fn.apply(null, args, false)
    }
    return performance.now() - start
}

function timeTestEquations() {
    [1, 10, 100, 1000, 10000, 100000].forEach(count => {
        console.log(`Times(ms) for ${count} runs: `, run(testEquations, count, true))
    })
}


if (testing) {
    testEquations()
    timeTestEquations()
    readline.close()
} else {
    readline.question('Enter your equation: ', equation => {
        console.log("Result: ", calculate(splitEquation(equation)))
        readline.close()
    });
}