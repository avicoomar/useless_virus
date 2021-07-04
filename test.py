import os
import sys

def virus(ms):
    switcher = {
        1: "directory",
        2: "file",
    }
    return deldirpath(switcher.get(ms))

def deldirpath(va):
    path=input("Enter path of the %s:" %va)
    if(va == "directory"):
        os.rmdir(path)
    else:
        os.remove(path)

def dafuq():
    driv=input("Enter the drive where the file is located?:")
    brr=input("Specify the name of the file you want to delete:")
    todel=find_files(brr,driv)
    os.remove(todel[0])
    sys.exit("Deleted!")
        
def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

# Driver program
if __name__ == "__main__":
    ms=int(input("1.Delete Directory?\n2.Delete File?\n3.Idk the path\n"))
    if(ms==3):
        dafuq()
    print (virus(ms))




    

