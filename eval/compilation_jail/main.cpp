#include <iostream>
#include <fstream>

#define N_MAX 1000000

using namespace std;

ifstream fin("data.in");
ofstream fout("data.out");

int a, b;
int A[N_MAX + 5];

int main() 
{   
    fin >> a >> b;
    
    for(int i = 1; i <= N_MAX; i++) {
        A[i] = i - 1;
    }

    for(int i = 2; i <= N_MAX; i++) {
        for(int j = i + i; j <= N_MAX; j += i) {
            A[j] -= A[i];
        }
    }
    
    fout << a + b << "\n";
    
    return 0;
}