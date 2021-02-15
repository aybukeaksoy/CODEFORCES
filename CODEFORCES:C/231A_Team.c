#include <stdio.h>

int main(int argc, char **argv){
    int n_lines;
    int answer_count=0;
    int first,second,third;
    int i;
    scanf("%d",&n_lines);
    for (i=0;i<n_lines;i++){
        scanf("%d %d %d",&first,&second,&third);
        

        if ((first==1 && (second==1 || third==1))||(second == 1 && third==1)){
            answer_count+=1;
        }
        
    }
    printf("%d",answer_count);
    return 0;
}

    
    