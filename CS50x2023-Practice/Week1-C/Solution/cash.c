#include "cs50.h"
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    return cents;
}

int calculate_quarters(int cents)
{
    // TODO:quarters = 25$
    if (cents == 25)
    {
        return 1;
    }
    else if (cents >= 26 && cents <= 49)
    {
        return 1;
    }
    else if (cents >= 50 && cents <= 74)
    {
        return 2;
    } // And so forth
    else if (cents >= 75 && cents <= 99)
    {
        return 3;
    }
    else if (cents >= 100 && cents <= 124)
    {
        return 4;
    }
    else if (cents >= 125 && cents <= 149)
    {
        return 5;
    }
    else if (cents >= 150 && cents <= 174)
    {
        return 6;
    }

    return 0;
}


int calculate_dimes(int cents)
{
    // TODO dimes = 10$
    if (cents == 10)
    {
        return 1;
    }
    else if (cents >= 11 && cents <= 19)
    {
        return 1;
    }
    else if (cents >= 20 && cents <= 24)
    {
        return 2;
    }
    return 0;
}

int calculate_nickels(int cents)
{
    // TODO:nickels = 5$
    if (cents == 5)
    {
        return 1;
    }
    else if (cents >= 6 && cents <= 9)
    {
        return 1;
    }
    return 0;
}

int calculate_pennies(int cents)
{
    // TODO:pennies = 1$
    if (cents == 1)
    {
        return 1;
    }
    else if (cents >= 2 && cents < 5)
    {
        return cents;
    }
    return 0;
}
