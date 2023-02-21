#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// argc refers to the number of incoming parameters
// argv[] is an array of pointers to each argument passed to the program
int main(int argc, string argv[])
{

    // If your program is executed without any command-line arguments or with more than one command-line argument
    if (argc != 2)
    {
        // your program should print an error message of your choice (with printf) and return from main a value of 1 (which tends to signify an error) immediately.
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // If the key is invalid (as by not containing 26 characters
    if (strlen(argv[1]) != 26)  //  argv[1] is a pointer to the first command-line argument
    {
        printf("Key must containing 26 characters!\n ");
        return 1;
    }

    for (int i = 0; i < 26; i++)
    {
        char a = argv[1][i];
        // The key itself should be case-insensitive
        char c = toupper(a);

        // containing any character that is not an alphabetic character
        if (c < 'A' || c > 'Z')
        {
            printf("Key must containing alphabetic characters!\n");
            return 1;
        }

        // not containing each letter exactly once
        for (int j = i + 1; j < 26; j++)
        {
            char b = toupper(argv[1][j]);
            if (a == b)
            {
                printf("Key should containing each character exactly once\n");
                return 1;
            }
        }
    }
    // Your program must output plaintext: (without a newline) and then prompt the user for a string of plaintext (using get_string).
    string Pt = get_string("plaintext: ");
    int lengthPt = strlen(Pt);

    printf("ciphertext: ");
    for (int i = 0; i < lengthPt; i++)
    {
        char c = Pt[i];

        if (isupper(c))
        {
            char cipher = toupper(argv[1][c - 65]);
            printf("%c", cipher);
        }
        else if (islower(c))
        {
            char cipher = tolower(argv[1][c - 97]);
            printf("%c", cipher);
        }
        else // non-alphabetical characters should be outputted unchanged.
        {
            printf("%c", c);
        }
    }
    // After outputting ciphertext, you should print a newline
    printf("\n");
}