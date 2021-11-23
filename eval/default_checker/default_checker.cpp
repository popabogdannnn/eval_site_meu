#include <bits/stdc++.h>

/*
DEFAULT CHECKER
*/

using namespace std;

int main(int argc, char *argv[]) {

    if(argc != 4) {
        cerr << "Numar incorect de argumente";
        return -1;
    }

    string input_file = string(argv[1]);
    string output_ok_file = string(argv[2]);
    string output_contestant_file = string(argv[3]);

    int proc = 0; //checker-ul afiseaza la stdout pe prima linie un numar de la 0 la 100 care reprezinta 
    //cat % din punctajul asociat testului primeste solutia participantului
    // proc < 0 va fi echivalent cu proc = 0
    // proc > 100 va fi echivalent cu proc = 100
    // Pe a doua linie se va afisa verdictul

    int check = system(("diff -qBbEa " + output_ok_file + " " + output_contestant_file).c_str());
    
    if(check == 0) {
        proc = 100;
        cout << proc << "\n";
        cout << "Raspuns corect!\n";
    } 
    else {
        cout << proc << "\n";
        cout << "Raspuns gresit!\n";
    }
    return 0;
}