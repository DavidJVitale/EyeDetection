import os
import subprocess
import sys

def main():




#get the i/o path from the gui

	error_code=0
	width=256
	length=256
	fname="dummy_file.txt"


	if os.path.isfile (fname):
		print("The file exists!")

	else:
		print("The file does not exist")
		exit()




#call edge detection filter function
	prog_code=subprocess.run(['echo','edgeFilter {0} {1} {2}'.format(fname,width,lenth)],
		shell=True,
		stdout=subprocess.PIPE)
		

	if(prog_code.returncode==0):
		print("No error occured")

		else:
		print("Error occured in edge detection filter")


#save the output file name from the std


#call the hugh transform


#exit the program, close the 
