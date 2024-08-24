import math
import os,sys
import cv2
import numpy as np
import streamlit as st
def Yituosi(img):
    height,width=img.shape[:2]
    print(height,width)
    img_out=np.zeros((1001,1001,3), np.uint8)
    r=width/6.2831
    for i in range(-500,500):
        for j in range(-500,500):
            t=math.sqrt((4*i*i+4*j*j)/(r*r))
            z=(1-t)*r/(1+t)
            if abs(z)>r:
                continue
            k=z/r
            x=(r+z)*2*i/r
            y=(r+z)*2*j/r
            v=math.acos(k)
            u=math.atan2(j,i)
            if u<0:
                u+=2*3.1415926
            xx=int(u*width/(2*3.1415926))
            yy=int(v*height/(3.1415926))
            if xx<0 or yy<0:
                print(xx,yy)
            img_out[-i+500][j+500]=img[yy][xx]
    return img_out

os.chdir(sys.path[0])
im=st.text_input("图片名称：\n")
img = cv2.imread(im)
img_out=Yituosi(img)
cv2.imwrite("Yituosi-{}.png".format(im[:-4]),img_out)
st.image(img_out)
print("成功")
cv2.waitKey(0)
