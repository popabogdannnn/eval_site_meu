#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("adunare.in");
ofstream fout("adunare.out");
int a, b;

int main() 
{   
    fin >> a >> b;
    fout << a + b << "\n";
    
    return 0;
}