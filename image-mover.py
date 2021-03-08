import time
import zipfile
import os 
import pathlib
from datetime import datetime
from random import randint

def movefiles():
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    prenewfilename = current_time + "_" + str(randint(0,100))
    filelist = os.listdir("C:\\Users\\Sowap\\Desktop\\rzeczy\\")
    homedirpath = "C:\\Users\\Sowap\\Desktop\\rzeczy\\"
    print(filelist)
    numberoffiles = 0
    for x in filelist:
        numberoffiles = numberoffiles + 1
    print(numberoffiles)
    i = 0
    while i != numberoffiles:
        filename = filelist[i]
        i = i + 1
        print(filename)
        if(".png" in filename or ".PNG" in filename or ".WEBP" in filename or ".webp" in filename or ".mp4" in filename or ".MP4" in filename or ".jpg" in filename  or ".JPG" in filename or ".JPEG" in filename or ".jpeg" in filename):
            #print(pathlib.Path(filename).suffix)
            newfilename = prenewfilename  + str(i)
            extension = pathlib.Path(filename).suffix
            fullfilepath = homedirpath + filename
            newfilepath = homedirpath + newfilename + extension
            newfilenamewextension = newfilename + extension
            os.rename(str(fullfilepath),str(newfilepath))
            with zipfile.ZipFile("E:\\1_THE_GREAT_IMAGE_ZIP.zip", 'a') as file:
                file.write("C:\\Users\\Sowap\\Desktop\\rzeczy\\" + newfilenamewextension)
            os.remove(newfilepath)
            print(filename + " CORRECT") #E:\\image-collection.zip
print('abcdabcdabcd')
movefiles()