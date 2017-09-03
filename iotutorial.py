import io
import os

print(io.DEFAULT_BUFFER_SIZE)

fo = open("myfile3.txt","r+")
print("Name of file:", fo.name)

str = fo.read(19);
print ("Read String is : ", str)

position = fo.tell()
print("Current position of cursor",position)

fo.seek(16,0);
newstr = fo.read(10);
print ("Again Reading String is : ", newstr)

fo.close()

allfiles = dir()
print(allfiles)

# os.mkdir("Tesdir")
dirstr = os.getcwd()
print(dirstr)
