#include <stdio.h>
#include <stdlib.h>
int main(int argc,char **argv){
    char char_weight[4];
    int int_weight;
    gets(char_weight);
    int_weight=atoi(char_weight);
    if (int_weight == 2){
        printf("NO");
    }
    else if (int_weight%2 ==1 ){
        printf("NO");
    }
    else{
        printf("YES");
    }
    return 0;
}