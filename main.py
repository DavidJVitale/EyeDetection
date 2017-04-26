print("Enter File Name...")
file_name=input()

print("Starting Program...\n-----\n")

from PIL import Image

import struct
import subprocess
import sys

f = open("out.bin",'wb')
img = Image.open(file_name)
height = img.height
width = img.width
for i in range(height):
    for j in range(width):
        pixel=img.getpixel((j,i))
        pixel_byte = struct.pack("f",float(pixel))
        f.write(pixel_byte)

f.close()
print("height => {} width => {}".format(height, width))


print("Calling edge detection program")

edge_out = subprocess.run([sys.executable, 'mock_edge_program.py', "out.bin"],
			   shell=True,
			   stdout=subprocess.PIPE)

print("stdout of edge => {}".format(edge_out.stdout))
print("reutnr code of edge => {}".format(edge_out.returncode))
after_edge_file_name = str(edge_out.stdout)

print("\n-----\nCalling circle program...")

circ_out = subprocess.run([sys.executable, 'mock_circle_program.py', after_edge_file_name],
			   shell=True,
			   stdout=subprocess.PIPE)

print("stdout of circle => {}".format(circ_out.stdout))
print("reutnr code of circle => {}".format(circ_out.returncode))
