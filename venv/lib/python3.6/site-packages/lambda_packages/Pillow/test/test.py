import os
import sys
from PIL import Image

#For Lambda testing
def do(event, context):
	im = Image.open("test.jpg")
	return {'format': im.format, 'size':{'width':im.size[0], 'height':im.size[1]}, 'mode':im.mode}

#For local testing
if __name__ == '__main__':
    print(do(event=None, context=None))