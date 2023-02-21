#include "cs50.h"
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);


int main(void)
{
    // Get the string
    string word = get_string("Message: ");
    int length = strlen(word);

    // Iterate over each character of the string
    for (int i = 0; i < length; i++)
    {
        // Get the ASCII code of each character
        int Ascii = word[i];

        // Convert each decimal ASCII code to binary
        int bit = 7;
        int Binary[BITS_IN_BYTE] = {0}; // reset
        while (Ascii != 0)
        {
            Binary[bit] = Ascii % 2;
            Ascii /= 2;
            bit--;
        }

        // Each “byte” of 8 symbols should be printed on its own line when outputted
        for (int j = 0; j < 8; j++)
        {
            print_bulb(Binary[j]);
        }
        printf("\n"); // there should be a \n after the last “byte” of 8 symbols as well
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
