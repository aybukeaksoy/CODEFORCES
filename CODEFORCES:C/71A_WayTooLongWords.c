#include <stdio.h>
#include <string.h>

int main(int argc,char **argv){
    char word[101];
    int n_lines;
    int i;
    scanf("%d",&n_lines);
    for (i=0;i<n_lines;i++){
        scanf("%s",word);
        if (strlen(word)>10){
            printf("%c",word[0]);
            printf("%d",strlen(word)-2);
            printf("%c\n",word[strlen(word)-1]);

        }else{
            printf("%s\n",word);
        }

    }
    return 0;
    
}
