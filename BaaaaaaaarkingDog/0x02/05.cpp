// 10869 사칙연산
#include <iostream>
int main(void) {
    int A, B, addtion, subtraction, multiplication, division, mod;
    std::cin >> A >> B;
    addtion = A + B;
    subtraction = A - B;
    multiplication = A * B;
    division = A / B;
    mod = A % B;
    std::cout << addtion << "\n";
    std::cout << subtraction << "\n";
    std::cout << multiplication << "\n";
    std::cout << division << "\n";
    std::cout << mod << "\n";
}