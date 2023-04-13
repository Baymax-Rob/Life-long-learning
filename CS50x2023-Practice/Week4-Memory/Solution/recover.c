#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE buffer[512];
    char filename[8];
    int cnt = 0;
    FILE *output = NULL;

    while (fread(&buffer, 512, 1, input))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (cnt > 0)
            {
                fclose(output);
            }

            sprintf(filename, "%03i.jpg", cnt);
            output = fopen(filename, "w");
            cnt++;
        }

        if (cnt > 0)
        {
            fwrite(&buffer, 512, 1, output);
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}