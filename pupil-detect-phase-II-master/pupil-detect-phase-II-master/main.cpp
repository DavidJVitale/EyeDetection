#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "image.h"
#include "filter.h"
#include "sobelfilter.h"
using namespace std;

int main(int argc, char* argv[])
{
	int kernelDimension = 3;
	int imageHeight = 100; //atoi(argv[2]);
	int imageWidth = 90; //atoi(argv[3]);
	Image image1(imageHeight,imageWidth);
        Image newImage(imageHeight,imageWidth);


//        char readFile[] = "./images/lab5_spatial_image.bin";
	char readFile[] = "eye_test_image1.jpg.bin"; //argv[1];
        char writeFile[] = "outfile.bin"; //".\\images\\outfile.bin";

        image1.readImage(readFile);

        SobelFilter sobelfilter;
        newImage = sobelfilter.process(image1,kernelDimension,kernelDimension,imageHeight,imageWidth);

        newImage.writeImage(writeFile);

}
