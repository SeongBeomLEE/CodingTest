// 2480 주사위 세개
#include <iostream>
int main(void) {
    int A, B, C;
    int array[3];
    int max = -1;
    std::cin >> A >> B >> C;
    array[0] = A;
    array[1] = B;
    array[2] = C;
    for (int i = 0; i < 3; i++) {
        if (max < array[i]) {
            max = array[i];
        }
    }

    if ((array[0] == array[1]) && (array[1] == array[2])) {
        std::cout << 10000 + array[0] * 1000;
    }
    else if ((array[0] != array[1]) && (array[0] != array[2]) && (array[1] != array[2])) {
        std::cout << max * 100;
    }
    else {
        if (array[0] == array[1]){
            std::cout << 1000 + array[0] * 100;
        }
        else if (array[0] == array[2]){
            std::cout << 1000 + array[0] * 100;
        }
        else if (array[1] == array[2]){
            std::cout << 1000 + array[1] * 100;
        }
    }
}