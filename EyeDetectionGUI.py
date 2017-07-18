#The main Eye Detection GUI that combines all parts into a functional GUI
#Completed by David Vitale and members of the BIEN4290 class

import tkinter
from tkinter import *

import PIL
import os
from PIL import ImageTk, Image, ImageDraw

from tkinter import filedialog, messagebox

import csv

import subprocess
import struct

global input_path
global inputImagePanel
global outputImagePanel
global ResultLabel

from PIL import Image
global CircleProp

#global width and height
width=-1
height=-1

# Global exit flag
exit_flag = False

# To label text box for input/output
inputimageLabel = None
outputimageLabel = None

# image path
input_path = None
output_path = None
MinRadius = None
MaxRadius = None
# Threshold = None

# Labels for Properties of Circle
ResultLabel = None
CircleProp = []


# Global databuffer for saving to CSV
csv_buffer = [[0 for x in range(2)] for y in range(50)]
csv_counter = 0

def read_CSV():
    global csv_buffer
    csvResult = ""
    
    with open("out.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        CircleProp[:] = []
        counter = 0
        
        for line in reader :
            for value in line:
                print(value)
                csvResult += value + "\t"
                CircleProp.append(value)
        
    ResultLabel.config(text = "<Circle Properties>\n\nX\tY\tR\n" + csvResult)

def folderButtonCB():
    global input_path, width, height
    
    inputImageFullPath=filedialog.askopenfilename()
    print(inputImageFullPath)
    input_path = inputImageFullPath
    
    if(input_path.endswith(".jpg")):
        img = Image.open(input_path)
        width = img.width
        height = img.height
        print("width => {} height => {}".format(width, height))
        newImg = ImageTk.PhotoImage(img)
        inputImagePanel.configure(image = newImg)
        inputImagePanel.image = newImg
        
        # Dynamically create binary file ===========
        binary_path = input_path + ".bin"
        name_without_path = os.path.basename(binary_path)
        f = open(name_without_path,'wb')
        
        for i in range(height):
                for j in range(width):
                        pixel=img.getpixel((j,i))
                        pixel_byte = struct.pack("f",float(pixel))
                        f.write(pixel_byte)
        f.close()
        # ==========================================

        Tk.update(root)
            
    else:
        messagebox.showinfo("Error", "Please select an input file with .jpg extension")
    
def startFilterCB():
    global input_path
    
    binary_path = input_path + ".bin"
    
    name_without_path = os.path.basename(binary_path)
    
    print("filename = {}".format(name_without_path))
    
    edge_command = "pupil-detect-phase-II-master\\Project11.exe {} {} {}".format(name_without_path, height, width)
    print("edge command => {}".format(edge_command))
    edge_out = subprocess.run(edge_command,
                shell=True,
                stdout=subprocess.PIPE)

    print("stdout of edge => {}".format(edge_out.stdout))
    print("reutnr code of edge => {}".format(edge_out.returncode))
    after_edge_file_name = str(edge_out.stdout)

    print("\n-----\nCalling circle program...")

    MinRadius=MinRadiusEntry.get()   # Save MinRadius
    MaxRadius=MaxRadiusEntry.get()   # Save MaxRadius
    print("minRad => {} MaxRad => {}".format(MinRadius, MaxRadius))
    hough_command = "Hough\\Hough.exe {} {} {} {} {}".format("out.bin", height, width, MinRadius, MaxRadius)
    print("hough_command = {}".format(hough_command))
    circ_out = subprocess.run(hough_command,shell=True,stdout=subprocess.PIPE)

    print("stdout of circle => {}".format(circ_out.stdout))
    print("reutnr code of circle => {}".format(circ_out.returncode))

    if(input_path.endswith(".jpg")):
        outputImageFullPath=outputFileEntry.get()   # in this path, create image with circles
        # Threshold=ThresholdEntry.get()   # Save ThresholdRadius
        print(outputImageFullPath)
        print(MinRadius)
        print(MaxRadius)
        # print(Threshold)
        
        if(outputImageFullPath.endswith(".jpg")):
            
            read_CSV()
            drawCircle()
            
            output_path = outputImageFullPath

            newImg = ImageTk.PhotoImage(Image.open(output_path))
            outputImagePanel.configure(image = newImg)
            outputImagePanel.image = newImg
            
            Tk.update(root)    
        else:
            messagebox.showinfo("Error", "Please enter an output name with .jpg extension")
    else:
        messagebox.showinfo("Error", "Please select an input image to start filtering")
        
def drawCircle():
    print("Drawing circle...")
    print("input = " + input_path)
    
    circleImg = Image.open(input_path)
    draw = ImageDraw.Draw(circleImg)
    
    xCoord = int(CircleProp[0])
    yCoord = int(CircleProp[1])
    radius = int(CircleProp[2])
    
    x0 = xCoord - radius
    y0 = yCoord - radius
    x1 = xCoord + radius
    y1 = yCoord + radius
    
    draw.ellipse((x0,y0,x1,y1), outline ='orange')
    
    outputImageFullPath=outputFileEntry.get()
    circleImg.save(outputImageFullPath)
    
if __name__ == '__main__':
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    
    # Left Frame
    FrameL = tkinter.Frame(root, width=200, height=300, background="bisque")
    FrameL.pack(side=LEFT)
   
    title_L = Label(FrameL, text = "EYE DETECTION - AUTOGONI INC.", font=("Helvetica", 12))
    title_L.pack(pady=20, padx=20)
    
    folderButton = Button(FrameL, justify = LEFT, command = folderButtonCB)
    photo = PhotoImage(file="Folder.png")
    folderButton.config(image=photo,width="100",height="30")
    folderButton.pack(side=TOP, pady=10, padx=10) 

    OpenFolderLabel = Label(FrameL, text = "Open Image", font = ("Helvetica", 12))
    OpenFolderLabel.pack(side=TOP, pady=10, padx=10)
    
    outputFileEntry = Entry(FrameL, width=40)
    outputFileEntry.insert(END, 'OutputFileName.jpg')
    outputFileEntry.pack(side=TOP)
    
    MinRadiusEntry = Entry(FrameL, width=40)
    MinRadiusEntry.insert(END, '<Enter Minimum Radius>')
    MinRadiusEntry.pack(side=TOP)
    
    MaxRadiusEntry = Entry(FrameL, width=40)
    MaxRadiusEntry.insert(END, '<Enter Maximum Radius>')
    MaxRadiusEntry.pack(side=TOP)
    
    # ThresholdEntry = Entry(FrameL, width=40)
    # ThresholdEntry.insert(END, '<Enter Threshold>')
    # ThresholdEntry.pack(side=TOP)

    startButton = Button(FrameL, text = "Start Filter", justify = LEFT, command = startFilterCB)
    startButton.pack(side=TOP, pady=20, padx=20)
    
    # Right Frame  ----------------------
    FrameR = tkinter.Frame(root, width=400, height=300, background="teal")
    FrameR.pack(side=RIGHT)

    # Input Image
    input_path = "DefaultImage.png"
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    in_img = ImageTk.PhotoImage(Image.open(input_path))
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    inputImagePanel = tkinter.Label(FrameR, image = in_img)
    inputImagePanel.pack(fill="both", expand="yes", padx=20, pady=20)
    
    inputimageLabel = Label(FrameR, text = "Input Image", font=("Comic Sans", 12))
    inputimageLabel.pack(padx=20, pady=20)

    # Output Image
    output_path = "DefaultImage.png"
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    out_img = ImageTk.PhotoImage(Image.open(output_path))
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    outputImagePanel = tkinter.Label(FrameR, image = out_img)
    outputImagePanel.pack(fill="both", expand="yes", padx=20, pady=20)
    
    outputimageLabel = Label(FrameR, text = "Output Image", font=("Comic Sans", 12))
    outputimageLabel.pack(padx=20, pady=20)
    
    ResultLabel = Label(FrameR, text = "<Circle Properties>\n\nX\tY\tR\n", font = ("Helvetica", 12))
    ResultLabel.pack(anchor=S, padx=20, pady=20)

    # --------------------------------------------------

    root.mainloop()

    exit_flag = True # Set the exit flag
    t.join()



