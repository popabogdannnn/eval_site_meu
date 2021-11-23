#include <stdio.h>

int a, b, c;

int main() {

    FILE *fin = fopen("data.in", "r");
    FILE *fout = fopen("data.out", "w");
    
    fscanf(fin, "%d%d", &a, &b);
    
    c = a + b;

    fprintf(fout, "%d\n", c);
    return 0;
}