#include <fstream>

using namespace std;

ifstream fin("data.in");
ofstream fout("data.out");


int a, b;

int main() 
{   
    fin >> a >> b;
    fout << a + b << "\n";
    return 0;
}