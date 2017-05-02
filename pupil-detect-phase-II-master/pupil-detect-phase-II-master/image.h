/*
* Author: Ben Durette
* Class: BIEN 4290
* Lab 4
* Date: 3/28/17
* The header file for the image class
* Adapted for final project 4/18/17
*/

#ifndef IMAGE_H
#define IMAGE_H

class Image
{
private:
	int num_rows;
	int num_cols;
	float *data;

public: 
	//Constructor, copy constructor, and deconstructor
	Image(int nrows, int ncols);
	Image(const Image &origIm);
	~Image(void);
	
	int getNumRows() { return num_rows; }
	int getNumCols() { return num_cols; }
	float getVal(int row, int col);
	float setVal(int row, int col, float value);
	void readImage(char* filename);
	void writeImage(char* filename);

};

#endif
