import os

path = input("please enter python file path: ")
files=os.listdir(path)
print(files) 

for i in files:
    oldname = path + "/"+ i
    a = i.split(".")
    if len(a) != 2:
        continue
    if a[1] == "py":
        new = a[0] + ".pyx"
        newname = path + "/" + new
        print(newname)
        os.rename(oldname, newname)








