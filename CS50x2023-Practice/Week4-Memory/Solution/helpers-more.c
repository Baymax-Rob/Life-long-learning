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

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE image_tmp = image[i][j];
            // So any pixels on the left side of the image should end up on the right, and vice versa.
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = image_tmp;
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    double Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    double Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    RGBTRIPLE copy[height][width];

    //  // The new value of each pixel would be the average of the values of all of the pixels that are within 1 row and column of the original pixel (forming a 3x3 box)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double GxRed = 0;
            double GyRed = 0;
            double GxGreen = 0;
            double GyGreen = 0;
            double GxBlue = 0;
            double GyBlue = 0;

            for (int row = -1; row <= 1; row++)
            {
                for (int col = -1; col <= 1; col++)
                {
                    if ((i + row >= 0 && i + row < height) && (j + col >= 0 && j + col < width))
                    {
                        //  The Sobel filter algorithm combines Gx and Gy into a final value by calculating the square root of Gx^2 + Gy^2,RED BLUE GREEN
                        GxRed += image[i + row][j + col].rgbtRed * Gx[row + 1][col + 1];
                        GyRed += image[i + row][j + col].rgbtRed * Gy[row + 1][col + 1];
                        GxGreen += image[i + row][j + col].rgbtGreen * Gx[row + 1][col + 1];
                        GyGreen += image[i + row][j + col].rgbtGreen * Gy[row + 1][col + 1];
                        GxBlue += image[i + row][j + col].rgbtBlue * Gx[row + 1][col + 1];
                        GyBlue += image[i + row][j + col].rgbtBlue * Gy[row + 1][col + 1];
                    }
                }
            }

            //  the resulting value is rounded to the nearest integer and capped at 255!
            copy[i][j].rgbtRed = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2))) > 255 ? 255 : round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)));
            /*
                Equivalent to:
                red = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)))
                if (red > 255)
                {
                    red = 255;
                }
                else
                {
                    red = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)))
                }
            */
            copy[i][j].rgbtGreen = round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2))) > 255 ? 255 : round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2)));
            copy[i][j].rgbtBlue = round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2))) > 255 ? 255 : round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2)));
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
