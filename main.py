# WORKS ON ANY SYSTEMS, JUST KEEP THE "lucon.ttf" FILE!
# TO INSTALL THE MODULES THAT ARE IN, USE THE COMMAND IN THE TERMINAL:
"pip install -r requirements.txt"
# THEN CHANGE THE LINE WHICH CONTAINS THE VIDEO PATH TO YOUR VIDEO.
# BEFORE USING DOWNLOAD THE REPL TO YOUR PC BECAUSE THE OPENCV MODULE IN REPLIT.COM IS KIND OF BROKEN FOR SOME REASON. OTHERWISE, IT WILL GIVE THIS ERROR:
"""
ImportError: OpenCV loader: missing configuration file: ['config.py']. Check OpenCV installation.
"""
from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math

videopath = "example.mp4"

characters = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
characterlist = list(characters)
characterlen = len(characterlist)
interval = characterlen/256
scale_factor = 0.09
characterwidth = 10
characterheight = 10

def get_char(i) -> None:
    return characterlist[math.floor(i*interval)]

capture = cv2.VideoCapture(videopath)

Font=ImageFont.truetype('lucon.ttf',15)

while True:
    _,image = capture.read()
    image = Image.fromarray(image)
    width,height = image.size
    image = image.resize((int(scale_factor*width),int(scale_factor*height*(characterwidth/characterheight))),Image.NEAREST)
    width,height = image.size
    pixel=image.load()
    outputImage=Image.new("RGB",(characterwidth*width,characterheight*height),color=(0,0,0))
    destination = ImageDraw.Draw(outputImage)
    for i in range(height):
        for j in range(width):
            r,g,b = pixel[j,i]
            h = int(0.299*r+0.587*g+0.114*b)
            pixel[j,i] = (h,h,h)
            destination.text((j*characterwidth,i*characterheight),get_char(h),font=Font,fill=(r,g,b))

    open_cv_image = np.array(outputImage)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
    cv2.imshow(videopath,open_cv_image)
  
capture.release()
cv2.destroyAllWindows()