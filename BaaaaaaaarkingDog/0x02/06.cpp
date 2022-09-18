// 9489 시험성적
#include <iostream>
int main(void) {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int score;
    std::cin >> score;
    if (90 <= score) {
        std::cout << "A";
    }
    else if (80 <= score) {
        std::cout << "B";
    }
    else if (70 <= score) {
        std::cout << "C";
    }
    else if (60 <= score) {
        std::cout << "D";
    }
    else {
        std::cout << "F";
    }
}