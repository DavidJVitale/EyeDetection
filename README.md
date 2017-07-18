# Eye Detection

This application reads in a .jpg file of an eye, applies filters to the binary data in that image, and attempts to draw a circle over any detected pupils.

![](http://i983.photobucket.com/albums/ae313/DavidJosephVitale/EyeDetection_zpselgakjiw.png)

## Technical Details

The GUI of this project is written in Python and tkinter. The image filtering and circle detection is done in C++. What is unique and cool about this project is that that the Python calls the C++ binary through Windows CMD prompt. Different teams worked on different components of this project, connecting them together at the last minute.

# Project Structure Breakdown

* ExampleImages
    * Some example pictures of eyes, as well as their converted binary components.
* EyeDetectionGUI.py
    * The main Python GUI as seen above. Controls all project components and how they fit together. 
* Hough
    * The Hough transform C++ files. Compiled using Dev-C++ for Windows, this exectuable takes in a binary file and tries to find 'edges' in the image, converting it to a black-and-white image of only edges.
* MiscSfwComp
    * Miscellanous Software Components, various Python scripts that were used in intermediate steps for development. Still could be useful in the future.
* pupile-detect-phase-II-master
    * The pupil detection C++ files. Compiled using Dev-C++ for Windows, this executable takes in the Hough Transformed binary file and attempts to find all circles in it. This information is written to an output file, which is read in by the Python GUI.
* README.me
    * This file        
