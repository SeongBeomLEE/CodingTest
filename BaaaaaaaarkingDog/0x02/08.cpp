// 2753 윤년
#include <iostream>
int main(void) {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int year;
    std::cin >> year;

    if (year % 4 == 0){
        if ((year % 400 == 0) || (year % 100 != 0)) {
            std::cout << 1;
        }
        else {
            std::cout << 0;
        }
    }
    else {
        std::cout << 0;
    } 
}