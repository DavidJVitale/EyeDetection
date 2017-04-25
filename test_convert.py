from PIL import Image


def main():

	print "Hello mars"

	f = open('new_img.bin','w')
	img = Image.open('eye_image_test1.jpg')
	
	#img.getPixel((0,0))

	height = img.height
	width = img.width


	for i in height:
		for j in width:
			pixel=img.getPixel((i,j))
			f.write(pixel + '\n')
	f.close
main()
