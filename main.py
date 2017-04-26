import struct
import subprocess
import sys

print("Enter filename")
filename=input()

print("Enter width")
width=input()

print("Enter height")
height=input()

print("height => {} width => {}".format(height, width))


print("Calling edge detection program")

edge_out = subprocess.run([sys.executable, 'mock_edge_program.py', filename],
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
