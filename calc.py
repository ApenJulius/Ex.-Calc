import re
import time

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

def time_test_equations():
    for count in [1, 10, 100, 1000, 10000, 100000]:
        print(f'Time(ms) for {count} runs: {run(test_equations, count, True)*1000}')


def run(fn, count, *args):
    start = time.perf_counter()
    for _ in range(count):
        fn(*args)
    end = time.perf_counter()
    return end - start

def test_equations(timing = False):
    for equation, expectedResult in tests.items():
        assert calculate(splitEquation(equation)) == expectedResult
        if not timing:
            print("Passed ", equation)

def splitEquation(equation):
    return re.findall(r'\d+|[+\-*/]', equation)

def calculate(equation):
    for symbol in equationOrder:
        while symbol in equation:
            index = equation.index(symbol)
            num1 = int(equation[index - 1])
            num2 = int(equation[index + 1])
            if symbol == "*":
                equation[index - 1] = multiply(num1, num2)
            elif symbol == "/":
                equation[index - 1] = divide(num1, num2)
            elif symbol == "+":
                equation[index - 1] = add(num1, num2)
            elif symbol == "-":
                equation[index - 1] = subtract(num1, num2)
            equation.pop(index)
            equation.pop(index)
    return equation[0]


def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


if __name__ == "__main__":
    testing = True
    print("testing mode set to :", testing)
    if testing:
        test_equations()
        time_test_equations()
    else:
        equation = input("\nGive an equation:")
        result = calculate(splitEquation(equation))
        print(f"The result is: {result}")



