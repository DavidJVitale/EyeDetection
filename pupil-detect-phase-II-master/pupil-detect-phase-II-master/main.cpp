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
	int imageHeight = atoi(argv[2]);
	int imageWidth = atoi(argv[3]);
	Image image1(imageHeight,imageWidth);
        Image newImage(imageHeight,imageWidth);


//        char readFile[] = "./images/lab5_spatial_image.bin";
	char* readFile = argv[1]; //"eye_test_image1.jpg.bin"; //argv[1];
        char writeFile[] = "out.bin"; //".\\images\\outfile.bin";

        image1.readImage(readFile);

        SobelFilter sobelfilter;
        newImage = sobelfilter.process(image1,kernelDimension,kernelDimension,imageHeight,imageWidth);

        newImage.writeImage(writeFile);

}
