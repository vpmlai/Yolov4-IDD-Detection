#!/usr/bin/python3
import os
#DIRNAME="C:\\Users\\hp\Downloa/ds\\Test\\test"
DIRNAME = os.path.normcase(r'C:\Users\hp\Desktop\Master Thesis\Final Thesis\Final Dataset\Final.v1i.darknet\test')
files = os.listdir(DIRNAME)
print(files)
print('HI')
for f in files:
    if 'jpg' in f:
        try:
            print(f)
            newname =f.split('_')[0]
            newname = newname + '.txt'
            print(newname)
            os.rename(f, newname)
        except:
            print ('Error')