# -*- coding: utf-8 -*-
import os.path, os
import cv2

cnt = 1

def processDirectory ( args, dirname, filenames ):
    global  cnt
    print 'Directory',dirname
    for filename in filenames:
        if (os.path.isdir(path + dirname + "\\" + filename)):
            continue
        temp=cv2.imread(path + dirname + "\\" + filename)
		#os.remove(path+"\\imgs\\"+img)
        cv2.imwrite(path+"\\JPEGImages\\"+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg",temp)
        print "renamed "+filename+" to "+prename[0:len(prename)-len(str(cnt))]+str(cnt)+".jpg"
        cnt+=1
 
# os.path.walk(r'.\imgs', processDirectory, None )

if __name__=="__main__":
    path = os.getcwd()
    if os.path.exists('JPEGImages') == False:
        os.mkdir('JPEGImages')
    if os.path.exists('Annotations') == False:
        os.mkdir('Annotations')
    if os.path.exists('ImageSets') == False:
        os.mkdir('ImageSets')
        os.mkdir('ImageSets/Main')

    prename = "000000"
    os.path.walk(r'.\imgs', processDirectory, None )
    print 'done!'
