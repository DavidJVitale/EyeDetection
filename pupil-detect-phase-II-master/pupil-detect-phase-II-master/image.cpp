/*
* Author: Ben Durette
* Class: BIEN 4290
* Lab 4
* Date: 3/28/17
* This file defines the image object and its
* associated functions
* Adapted for final project 4/18/17 
*/

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include "image.h"
#include "filter.h"
#include "sobelfilter.h"
using namespace std;

//Constructor for image object
Image::Image(int nrows, int ncols)
{
	num_rows = nrows;
	num_cols = ncols;
	data = new float[num_rows*num_cols];
}

//Copy constructor for image object
Image::Image(const Image &origIm)
{
	num_rows = origIm.num_rows;
	num_cols = origIm.num_cols;
	data = new float[num_rows*num_cols];
	
	//Copies the data from the original image object to the new object
	for(int i = 0; i < (num_rows*num_cols); i++)
	{
		int j;
		data[i] = origIm.data[i];
	}
}

//Deconstructor for image object
Image::~Image(void) {
//	delete [] data;
}

//Retrieves value of a specific pixel
float Image::getVal(int row, int col)
{
	if( (row > num_rows) || (col > num_cols) || (row < 0) || (col < 0) )
	{
		cout << "Error getVal: Requested pixel is outside image size\n";
		cout << "row is: " << row << "    col is: " << col << "\n";
		exit (EXIT_FAILURE);
	}
	return data[((row)*num_cols) + col];
}

//Sets the value of a specific pixel
float Image::setVal(int row, int col, float value)
{
	if( (row > num_rows) || (col > num_cols) || (row < 0) || (col < 0) )
        {
                cout << "Error setVal: Requested pixel is outside image size\n";
                exit (EXIT_FAILURE);
        }
	data[((row)*num_cols) + col] = value;
}

//Reads a data file into the data array for an image object
void Image::readImage(char* filename)
{
	//reads in the binary data into the data array
	std::ifstream infile;
	infile.open(filename, std::ios::in|std::ios::binary);
	if(infile.is_open())
	{
		infile.read((char*)data, num_rows*num_cols*8);//multiplied by bit depth
		infile.close();
	}
	else std::cout << "Unable to open " << filename << " for reading \n";
}

//Writes the data from a data array of an image object to an output file
void Image::writeImage(char* filename)
{
	//writes the data from an image to an output file
	std::ofstream outfile;
	outfile.open(filename, std::ios::out|std::ios::binary);
	if(outfile.is_open())
	{
		outfile.write((char*)data, num_rows*num_cols*4);
		outfile.close();
	}
	else std::cout << "Unable to open " << filename << " for writing \n";
}

