#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <regex>
#include <cassert>
#include <set>
#include <algorithm>

using namespace std;

map<string, int> tests = {
    {"1+2*3", 7},
    {"1*2+3", 5},
    {"1+2+3", 6},
    {"1*2*3", 6},
    {"1-2-3", -4},
    {"4*2/2", 4},
    {"231*13-34*34", 1847}
};

vector<string> equationOrder ={
    "+",
    "-",
    "*",
    "/"
};

int multiply(int a, int b) {
    return a * b;
};

int divide(int a, int b) {
    return a / b;
};

int add(int a, int b) {
    return a + b;
};

int subtract(int a, int b) {
    return a - b;
};

int calculate(vector<string> equation)
{
    for (const auto& symbol: equationOrder) {
        auto it = find(equation.begin(), equation.end(), symbol);
        while (it != equation.end()) {
            auto num1_it = std::prev(it);
            auto num2_it = std::next(it);
            int num1 = std::stoi(*num1_it);
            int num2 = std::stoi(*num2_it);
            int result = 0;
            switch(symbol[0]) {
                case '*':
                    result = multiply(num1, num2);
                    break;
                case '/':
                    result = divide(num1, num2);
                    break;
                case '+':
                    result = add(num1, num2);
                    break;
                case '-':
                    result = subtract(num1, num2);
                    break;
            }
            *num1_it = std::to_string(result);
            it = equation.erase(it);
            it = equation.erase(it);

            it = std::find(equation.begin(), equation.end(), symbol);
        }
    }
    return std::stoi(equation.front());
}; 

vector<string> splitEquation(string equation) {
    regex re(R"(\d+|[+\-*/])");
    sregex_token_iterator it(equation.begin(), equation.end(), re);
    sregex_token_iterator reg_end;
    vector<string> result;
    for (; it != reg_end; ++it) {
        result.push_back(it->str());
    }
    return result;
};

void test_equations(bool timing = false) {
    for (auto test:tests) {
        cout << calculate(splitEquation(test.first)) << "\n";
        bool match = calculate(splitEquation(test.first)) == test.second; 
        cout << "Testing: " << test.first << " = " << test.second << "\n" << (match ? "PASS" : "FAIL") << "\n";
    }

};


int main()
{
    bool testing = true;
    string equation;
    if (testing) {
        test_equations();
    } else {
        cout << "\nGive an equation: ";
        cin >> equation;
        cout << "You entered: " << equation << "\n";
    }
};