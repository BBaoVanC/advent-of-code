#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char rawNums[16384];
    // for (int i = 0; i < sizeof(rawNums); i++) {
    //     rawNums[i] = (char) malloc(5);
    // }

    int c = getc(stdin);
    for (int i = 0; c != EOF; i++) {
        rawNums[i] = c;
        c = getc(stdin);
    }
    getchar();
    
    prinf("rawNums is %s", rawNums);

    return 0;
}
