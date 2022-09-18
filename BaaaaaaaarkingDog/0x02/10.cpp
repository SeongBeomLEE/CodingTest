// 2490 윳놀이
#include <iostream>
int main(void) {
    int A, B, C, D, sum;
    for (int i = 0; i < 3; i++) {
        std::cin >> A >> B >> C >> D;
        sum = A + B + C + D;
        if (sum == 4) {
            std::cout << "E" << "\n";
        }
        else if (sum == 0) {
            std::cout << "D" << "\n";
        }
        else if (sum == 1) {
            std::cout << "C" << "\n";
        }
        else if (sum == 2) {
            std::cout << "B" << "\n";
        }
        else if (sum == 3) {
            std::cout << "A" << "\n";
        }
    }
}