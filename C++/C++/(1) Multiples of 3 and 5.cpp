#include <iostream>
using namespace std; 

int main()
{
    int answer = 0; 
    int o = 10; 
    for (int i = 0;  i < 1000; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            answer = answer + i; 
        }
    }
    cout << "Answer is: " << answer << endl;
}
