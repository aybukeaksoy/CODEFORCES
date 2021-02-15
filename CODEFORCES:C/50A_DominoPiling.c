#include <stdio.h>

int main(int argc,char **argv){
    #define MAX(x, y) (((x) > (y)) ? (x) : (y))
    #define MIN(x, y) (((x) < (y)) ? (x) : (y))
    int n;
    int m;
    scanf("%d %d",&n,&m);
    if (m%2==0 || n%2==0){
        printf("%d",m*n/2);
    }
    else{
        printf("%d",MAX(m,n)/2*MIN(m,n)+MIN(m,n)/2);
    }
    return 0;
}
