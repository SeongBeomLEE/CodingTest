// 2587 대표값2
#include <iostream>
#include <algorithm>
int main(void) {
    int array[5];
    int mean = 0;
    for (int i = 0; i < 5; i++){
        std::cin >> array[i];
        mean += array[i];
    }
    std::sort(array, array + 5);
    std::cout << mean / 5 << "\n" << array[2];
}