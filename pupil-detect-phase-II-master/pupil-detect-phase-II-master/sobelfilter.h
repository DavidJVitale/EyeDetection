/*
* Author: Ben Durette
* Class: BIEN 4290
* Lab 4
* Date: 3/28/17
* Header file for the non-linear noise reduction filter file
*/

#ifndef NLNOISEREDUCTIONFILTER_H
#define NLNOISEREDUCTIONFILTER_H

#include "image.h"

//Inherets from base Filter class
class SobelFilter: virtual public Filter
{

protected:
	//Defines it's own virtual function
	float updatePixel(Image & neighImage, int M, int N);

public:
	SobelFilter();

};

#endif
