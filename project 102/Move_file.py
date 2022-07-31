import os
import shutil

src = "/Users/shailendrashukla/Downloads/Document1"
dest = "/Users/shailendrashukla/Desktop/python/project 102"
lists = os.listdir(src)
print(lists)

for filename in lists:
    root,ext = os.path.splitext(filename)
    if ext == " ":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1 = src + "/" + filename
        path2 = dest + "/" + "Document_Files"
        path3 = dest + "/" + "Document_Files" + "/" + filename

        if os.path.exists(path2):
            print("moving  "+ filename + "......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving  "+ filename + "......")
            shutil.move(path1,path3)