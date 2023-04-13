#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1: the number of command-line arguments can be found in the argc variables passed to the main function when the program is executed
    if (argc != 3)
    {
        printf("Error: usage ./reverse.c <input_file> <output_file>");
        return 1;
    }

    // Open input file for reading
    // TODO #2:open the input file in “read-only” mode
    FILE *inputf = fopen(argv[1], "r");
    if (inputf == NULL)
    {
        //  print an appropriate error message and return 1, exiting the program.
        printf("Error: can't open file");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER bh;
    fread(&bh, sizeof(WAVHEADER), 1, inputf);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(bh) == 0)
    {
        printf("Error: file type not supported");
        return 1;
    }

    // Open output file for writing
    // TODO #5:the output file using argv[2].
    FILE *outputf = fopen(argv[2], "w");
    if (outputf == NULL)
    {
        return 1;
    }

    // Write header to file
    // TODO #6:copy the header we read in from the input file in the third TODO to the output file.
    fwrite(&bh, sizeof(WAVHEADER), 1, outputf);

    // Use get_block_size to calculate size of block
    // TODO #7:
    int block_size = get_block_size(bh);

    // Write reversed audio to file
    // TODO #8:where the actual reversing of the audio takes place
    fseek(inputf, block_size * -1, SEEK_END);
    while (ftell(inputf) >= 44)
    {
        BYTE sound_piece[block_size];
        //  read in each block of auditory data starting from the very end of the input file and moving backwards
        fread(sound_piece, block_size, 1, inputf);
        //  writing each block to the output file so they are written in reverse order
        fwrite(sound_piece, block_size, 1, outputf);
        fseek(inputf, block_size * 2 * -1, SEEK_CUR);
    }

    fclose(inputf);
    fclose(outputf);

    return 0;
}

int check_format(WAVHEADER header)
{
    // TODO #4:If header indicates the file is indeed a WAV file, the check_format function should return true.
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    //  If not, check_format should return false
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7:Notice that one of the members of WAVHEADER is bitsPerSample. But to calculate block size, you’ll need bytes per sample!
    int bytesPerSample = header.bitsPerSample / 8;
    // number of channels multiplied by bytes per sample
    return header.numChannels * bytesPerSample;
}