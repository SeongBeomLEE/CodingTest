// 2309 일곱 난쟁이
#include <iostream>
#include <algorithm>

int main(void) {
    int sum = 0;
    int array[9];
    for (int i = 0; i < 9; i++) {
        std::cin >> array[i];
        sum += array[i];
    }
    std::sort(array, array+9);
    for (int i = 0; i < 9; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (sum - (array[i] + array[j]) == 100){
                for (int z = 0; z < 9; z++) {
                    if ((z != i) && (z != j)){
                        std::cout << array[z] << "\n";
                    }
                }
                return 0;
            }
        }
    }
}