#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue; //stores blue index value
            int red = image[i][j].rgbtRed; //stores red index value
            int green = image[i][j].rgbtGreen; //stores green index value
            // take the average of the red, green, and blue values to determine what shade of grey to make the new pixel.
            int average = round((blue + green + red) / 3.0); //averages all values and rounds to nearest integer
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
     for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            // sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            // sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            // guarantee that the resulting red, green, and blue values will be whole numbers between 0 and 255, inclusive.
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE tmp = image[i][j];
            // So any pixels on the left side of the image should end up on the right, and vice versa.
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double sumRed = 0;
            double sumGreen = 0;
            double sumBlue = 0;
            double cnt = 0.0;

            // The new value of each pixel would be the average of the values of all of the pixels that are within 1 row and column of the original pixel (forming a 3x3 box)
            for (int row = -1; row <= 1; row++)
            {
                for (int col = -1; col <= 1; col++)
                {
                    // For a pixel along the edge or corner, like pixel 15, we would still look for all pixels within 1 row and column:
                    if ((i + row >= 0 && i + row < height) && (j + col >= 0 && j + col < width))
                    {
                        sumRed += image[i + row][j + col].rgbtRed;
                        sumGreen += image[i + row][j + col].rgbtGreen;
                        sumBlue += image[i + row][j + col].rgbtBlue;
                        cnt++;
                    }
                }
            }

            copy[i][j].rgbtRed = round(sumRed / cnt);
            copy[i][j].rgbtGreen = round(sumGreen / cnt);
            copy[i][j].rgbtBlue = round(sumBlue / cnt);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}
