// 2752 세수정렬
#include <iostream>
#include <algorithm>
int main(void) {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int array[3];
    for (int n = 0; n < 3; n++){
        std::cin >> array[n];
    }

    std::sort(array, array + 3);
    
    for (int n = 0; n < 3; n++){
        std::cout << array[n] << " ";
    }
}