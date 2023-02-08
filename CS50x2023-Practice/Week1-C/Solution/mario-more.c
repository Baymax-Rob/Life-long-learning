#include "cs50.h"
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height > 8 || height < 1);   // input a positive integer between 1 and 8

    //Line wise loop
    for (int i = 1; i <= height; i++)
    {
        // Prints starting spaces
        for (int j = 0; j < (height - i); j++)
        {
            printf(" ");
        }

        //Prints # according to Line
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        printf("  ");   // //Prints spaces between Pyramids
        //Prints second Pyramid
        for (int l = 0; l < i; l++)
        {
            printf("#");
        }
        printf("\n");   //Moves to next line
    }
}