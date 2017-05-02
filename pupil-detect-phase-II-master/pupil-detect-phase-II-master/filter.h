/*
* Author: Ben Durette
* Class: BIEN 4290
* Lab 4
* Date: 3/28/17
* Header file for the general filter class
* Adapted for final project 4/18/17
*/

#ifndef FILTER_H
#define FILTER_H

#include "image.h"

class Filter
{
protected:
	//Virtual function to allow specific filter classes to define their 
	//own updatePixel() functions
	virtual float updatePixel(Image & neighImage, int M, int N);

public:
	Filter();
	Image process(Image & inImage, int M, int N, int imageHeight, int imageWidth);
};

#endif
