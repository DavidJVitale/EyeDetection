# pupil-detect-phase-II

To run program
- to run this program, all you have to do is run the makefile script to compile (execute the command: ./makefile), and then run the output file
- all the make file contains is: "g++ image.cpp filter.cpp sobelfilter.cpp main.cpp"
- the only stipulation is where the image files are located, they are in a subfolder called "images"
- so for organization, but all .cpp and .h files in the same directory that you are running the program out of and create a subdirectory called "images" that contains the images to be processed
- the output file will be written to the "images" subdirectory
- this current setup will run the filter with a 3x3 size filter, if you would like to use a larger filter, change the dimensions passed into the process() funtion in the main.cpp file


Contents

filter.cpp
- this file contains the base Filter virtual class
- it is a virtual class, so no matter how many specific filters inheret
  from the Filter class, there will only be one instance of it
- it contains two functions: updatePixel() and process()
	- updatePixel() is a virtual function that derived filters are able
	  make their own definitions for
	- process does the bulk of the work	
		- it creates a copy image object for out
		- creates a temporary image object for image processing
		- loads the temporary image object with the current pixel and its neighbors
		- calls the updatePixel() function to process the filter algorithm
		- writes the updated pixel value to the output image

filter.h
- filter.h is the header file for filter.cpp

sobelfilter.cpp
- this file implements the updatePixel method for processing images with the edge-detecting Sobel filter
- updatePixel()
	- convolves the neighborhood of the image with 2 3x3 kernels emphasizing the edges vertically and horizontally
	- adds the squared sums of these convolutions
	- takes the magnitude of the square root of the total
	- compares this value to the threshold value and sets to either 0 or 1
	- returns the binary pixel value

sobelfilter.h
- this is the header file for sobelfilter.cpp

image.cpp
- this file contains the Image class
- the image class contains two int variable for the dimensions of the image, and a data array
  containing all the data
- the class contains multiple functions: a constructor, copy constructor, destructor,
  getVal, setVal, readImage, and writeImage
- the copy constructor copies an image object that is sent to it
- the destructor releases the memory used by the data array
- getVal and setVal retrieve or set the value of a specific pixel in the image
- readImage and writeImage read a data file and write to a data file

image.h
- this is the header file for image.cpp

main.cpp
- the main file runs the whole program
- it create both the original image object, and the image object to be the output file
- it calls the readImage function to set the data to the original image object
- it then passes the image object to the filter to be processed
- it takes the returned image object and writes it to a data file

A makefile was used to compile all of the files together, it output a.out

