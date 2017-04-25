from PIL import Image
import struct

print("Enter file name:")
filename = input()

f = open(filename, 'rb')
output = []
try:
    fourbytes = bytes(f.read(4))
    while fourbytes:
        val = float(struct.unpack("f", fourbytes)[0])
        #print("val => {}".format(val))
        output.append(val)
        fourbytes = f.read(4)
finally:
    f.close()

print("enter height")
height = int(input())
print("enter width")
width = int(input())

length=height

im = Image.new("L",(length,width))

counter = 0
for i in range(length):
    for j in range(width):
        val = int(output[counter])
        #print("output => {}".format(output[counter]))
        im.putpixel((i,j),val)
        counter += 1

im.show()
