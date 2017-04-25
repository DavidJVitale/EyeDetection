from PIL import Image
import struct

def main():
        f = open('new_img.bin','wb')
        img = Image.open('eye_test_image1.jpg')

        img.show()

        height = img.height
        width = img.width
        for i in range(height):
                for j in range(width):
                        pixel=img.getpixel((j,i))
                        pixel_byte = struct.pack("f",float(pixel))
                        f.write(pixel_byte)
        f.close()
main()
