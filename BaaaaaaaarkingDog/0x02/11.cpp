// 2576 홀수
#include <iostream>
int main(void) {
    int num = 0;
    int odd_sum = 0;
    int odd_min = 0;

    for (int i = 0; i < 7; i++) {
        std::cin >> num;
        if (num % 2 != 0) {
            odd_sum += num;
            if (odd_min) {
                if (num < odd_min){
                    odd_min = num;
                }
            }
            else {
                odd_min = num;
            }
        }
    }
    if (odd_sum) {
        std::cout << odd_sum << "\n" << odd_min;
    }
    else {
        std::cout << -1;
    }
}