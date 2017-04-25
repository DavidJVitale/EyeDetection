from PIL import Image
import struct

def main():
        print("Enter file name!")
        filename = input()
        f = open("out.bin",'wb')
        img = Image.open(filename)

        img.show()

        height = img.height
        width = img.width
        for i in range(height):
                for j in range(width):
                        pixel=img.getpixel((j,i))
                        pixel_byte = struct.pack("f",float(pixel))
                        f.write(pixel_byte)
        f.close()
        print("height => {} width => {}".format(height, width))
main()
