#include "cs50.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

// argc refers to the number of incoming parameters
// argv[] is an array of pointers to each argument passed to the program
int main(int argc, string argv[])
{

    // If program is executed without any command-line arguments or with more than one command-line argument,
    // your program should print an error message of your choice (with printf) and return from main a value of 1 (which tends to signify an error) immediately.
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // argv[0] stores the name of the program, argv[1] is a pointer to the first command-line argument
    int length = strlen(argv[1]);

    // If any of the characters of the command-line argument is not a decimal digit,
    // your program should print the message Usage: ./caesar key and return from main a value of 1
    for (int i = 0; i < length; i++)
    {
        if (argv[1][i] < '0' || argv[1][i] > '9')
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);  // Convert string to int
    // Your program must output plaintext: (with two spaces but without a newline) and then prompt the user for a string of plaintext (using get_string).
    string Pt = get_string("plaintext: ");   // pt = plain text
    int lengthPt = strlen(Pt);
    printf("ciphertext: ");

    for (int j = 0; j < lengthPt; j++)
    {
        char p = Pt[j]; // Get each character of a string
        char c;

        if (isupper(p)) // Checks upper case
        {
            // capitalized letters, though rotated, must remain capitalized letters
            c = (((p - 65) + k) % 26) + 65;
            printf("%c", c);
        }
        else if (islower(p))  // Checks lower case
        {
            // lowercase letters, though rotated, must remain lowercase letters.
            c = (((p - 97) + k) % 26) + 97;
            printf("%c", c);
        }
        else // non-alphabetical characters should be outputted unchanged.
        {
            printf("%c", p);
        }
    }
    printf("\n");
}