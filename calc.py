import re

tests = {
    "1+2*3": 7,
    "1*2+3": 5,
    "1+2+3": 6,
    "1*2*3": 6,
    "1-2-3": -4,
    "4*2/2": 4,
    "231*13-34*34": 1847
}



def splitEquation(equation):
    return re.findall(r'\d+|[+\-*/]', equation)


equationOrder = [
    "*",
    "/",
    "+",
    "-"
]   


def checkEquation(equation):
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
    testing = False
    print("testing mode set to :", testing)
    if testing:
        for equation, result in tests.items():
            print(f"Testing {equation}...")
            assert checkEquation(splitEquation(equation)) == result
            print("Passed as", result)
    else:
        equation = input("\nGive an equation:")
        result = checkEquation(splitEquation(equation))
        print(f"The result is: {result}")