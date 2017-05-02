/*
* Author: Ben Durette
* Class: BIEN 4290
* Lab 4
* Date: 3/28/17
* This file defines the non-linear noise reduction filter object and its
* associated functions
*/

#include <iostream>
#include <cmath>
#include "filter.h"
#include "sobelfilter.h"
#include "image.h"
using namespace std;

SobelFilter::SobelFilter() {}

//Virtual function redifined for this specific filter
float SobelFilter::updatePixel(Image & neighImage, int M, int N)
{
	float threshold = 100;
	float floatOne = 1.000;
	float floatZero = 0.000;
	float GxSum = 0;
        float GySum = 0;
        float mag;
	int GxKernel[3][3] = {
				{-1,0,1},
				{-2,0,2},
				{-1,0,1}
			     };
	int GyKernel[3][3] = {
				{1,2,1},
				{0,0,0},
				{-1,-2,-1}
			     };

	//Determine the sum of the neighbors
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			GxSum += GxKernel[i][j]*neighImage.getVal(i,j);
			GySum += GyKernel[i][j]*neighImage.getVal(i,j);
		}
	}
	mag = abs(sqrt(pow(GxSum,2) + pow(GySum,2)));
	//cout << "mag = " << mag << "\n";


	if (mag > threshold)
	{
		//cout << "1\n";
		return floatOne;
	}
	else
	{
		//cout << "0\n";
		return floatZero;
	}
}

