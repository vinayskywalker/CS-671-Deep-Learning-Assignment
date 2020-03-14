import sys
import os
import cv2
import matplotlib
import numpy as np
import math
import random



Angle=[8,23,38,53,68,83,98,113,128,143,158,173]
Width=[1,3]
Color=[(255,0,0),(0,0,255)]
Length=[7,15]

path="/home/vinay/Documents/DL Assignment/Assignment 1/data/"











def main():
    classes=1
    for i in range(len(Angle)):
        for j in range(len(Width)):
            for k in range(len(Color)):
                for l in range(len(Length)):
                    # 
                    ss=path+"class"+str(classes)+"/"
                    os.mkdir(ss)
                    for m in range(1000):
                        x1=random.randint(0,28)
                        y1=random.randint(0,28)
                        x2=x1+(int(Length[l]*math.cos(Angle[i]*((math.pi)/180))))
                        y2=y1+(int(Length[l]*math.cos(Angle[i]*((math.pi)/180))))
                        image=(np.zeros((28,28,3),np.uint8))
                        cv2.line(image,(x1,y1),(x2,y2),Color[k],Width[j])
                        cv2.imwrite(os.path.join(ss,str(m)+".jpg"),image)
                    
                    classes=classes+1

    








if __name__ == "__main__":
    main()