print("Enter File Name...")
file_name=input()

print("Starting Program...\n-----\n")

import subprocess
import sys

print("Calling edge detection program")

edge_out = subprocess.run([sys.executable, 'mock_edge_program.py', file_name],
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