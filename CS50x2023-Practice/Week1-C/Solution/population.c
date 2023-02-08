#include "cs50.h"
#include <stdio.h>

int main(void)
{
    int ss; // ss = start size
    int es; // es = end size
    // TODO: Prompt for start size
    do
    {
        ss = get_int("Starting Population Size: ");
    }
    while (ss < 9);

    // TODO: Prompt for end size
    do
    {
        es = get_int("Ending Population Size : ");
    }
    while (es < ss);

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    while (ss < es)
    {
        ss = ss + (ss / 3) - (ss / 4);
        year++;
    }
    // TODO: Print number of years
    printf("Years: %i", year);
}