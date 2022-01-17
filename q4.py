import os
#
print(os.stat("q4.py").st_size == 0)


#/////////////////////////////////////////////


filesize = os.path.getsize("sample.txt")

if filesize == 0:
    print("The file is  empty")
else:
    print("The file is  not empty")