#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("date.in");

int a, b;
int A[1000005];

int main() 
{
    fin >> a >> b;
    for(int i = 1; i <= 1000000; i++) {
        for(int j = 0; (1 << j) < i; j++) {
            A[i] ^= (1 << j);
        }
    }
    cout << a + b;
    return 0;
}