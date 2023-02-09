#include <stdio.h>
#include "cs50.h"

char check_card(long n);    // check card numbers' company

char check_validity(int s); // check card numbers' validity

int main(void)
{
    int i = 0;
    char card; // Store Card Company
    long number; // Store Card Number
    char validity;
    int index = 1;
    int s1 = 0; // Sum of odd digits
    int s2 = 0; // Sum of even digits*2
    int sum = 0; // Total Sum

    number = get_long("Number: "); // write a program that prompts the user for a credit card number

    while (number != 0)
    {
        i = number % 10;    //  Get the first digit on the right

        if (index % 2 == 1)
        {
            s1 = s1 + i;
        }
        else
        {
            int even = i * 2;
            if (even > 9)
            {
                s2 = s2 + (even / 10) + (even % 10);    // If the even is greater than 9, you need to get each bit separately as a separate number
            }
            else
            {
                s2 = s2 + even;
            }
        }

        if (number >= 10 && number <= 99)  // Start with the first two digits of the card number
        {
            card = check_card(number);
        }
        number = number / 10;
        index++;
    }

    sum = s1 + s2;
    validity = check_validity(sum);
    index = index - 1;
    //  Reports (via printf) whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each’s format herein
    if (validity == 'V' && card == 'A' && index == 15)  // American Express uses 15-digit numbers
    {
        printf("AMEX\n");
    }
    else if (validity == 'V' && card == 'M' && index == 16) // MasterCard uses 16-digit numbers
    {
        printf("MASTERCARD\n");
    }
    else if (validity == 'V' && card == 'V' && (index == 13 || index == 16)) // Visa uses 13- and 16-digit numbers
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

char check_card(long n)
{
    if (n == 34 || n == 37) //  All American Express numbers start with 34 or 37
    {
        return ('A');   // American
    }
    else if (n >= 51 && n <= 55)    // Most MasterCard numbers start with 51, 52, 53, 54, or 55
    {
        return ('M');   // MasterCard
    }
    else if ((n / 10) == 4) // All Visa numbers start with 4
    {
        return ('V');
    }
    else
    {
        return ('I');   // Invalid
    }
}

char check_validity(int s)
{
    if (s % 10 == 0)    //  if the total modulo 10 is congruent to 0
    {
        return ('V');   // Valid
    }
    else
    {
        return ('I');   // Invalid
    }
}