
from PIL import Image
import argparse

ascii_char = list ("!@#$%^&*()ASDFGqwertyuiopHJKLZXCVBNMQWERTYUIOP{}<>?")
def get_char(r,g,b,alpha=256):
	if alpha==0:
		return ' '
	length=len(ascii_char)
	gray=int(0.2126*r+0.7152*g+0.0722*b)#
	unit=(256.0+1)/length
	return ascii_char[int(gray/unit)]

parser=argparse.ArgumentParser()#create a parser object
parser.add_argument('file')#from parser add a file
parser.add_argument('-o','--output')#create a outputfile of this object
parser.add_argument('--width',type=int,default=80)#create a parameter of object 
parser.add_argument('--height',type=int,default=80)#the same with
args=parser.parse_args()#parser the image

IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

if __name__=='__main__':

	im=Image.open(IMG)
	im=im.resize((WIDTH,HEIGHT),Image.NEAREST)
	txt=""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt+=get_char(*im.getpixel((j,i)))
		txt+='\n'
	print txt

	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open("output.txt",'w') as f:
			f.write(txt)



