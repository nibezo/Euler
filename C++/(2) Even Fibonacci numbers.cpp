#include <iostream>
int x = 0;
int n = 1;
int sum_fib = 0;

int fibonacci(int n) {
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main()
{
    while (x < 4000000) {
        x = fibonacci(n);
        if (x%2 == 0) {
            sum_fib = sum_fib + x;
        }
        n++;
    }
    std::cout << "Answer is: " << sum_fib << std::endl;
}
