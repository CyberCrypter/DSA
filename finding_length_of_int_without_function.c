#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main () {
    int num = 1500;
    int count=0;
    while (num!=0){
        if(num<10){
            count += 1;
            num = 0;
            
        }
        else if(num %10 != -1){
            count +=1;
            num /= 10;
        }
    }
    printf("digits : %d ", count);

}