
from PIL import Image



def main():

	print "Hello mars"

	img = Image.open('eye_image_test1.jpg').convert('L')
#	img.show()
	img.save('eye_test.bin')


main()
