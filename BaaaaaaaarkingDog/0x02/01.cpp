// 10871 X보다 작은 수
#include <iostream>
int main(void) {   
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, X;
    std::cin >> N >> X; 
    
    int* array = new int[N];

    for (int i = 0; i < N; i++){
        std::cin >> array[i];
    }
    for (int i = 0; i < N; i++){
        if(array[i] < X) {
            std::cout << array[i] << " ";
        }
    }
}