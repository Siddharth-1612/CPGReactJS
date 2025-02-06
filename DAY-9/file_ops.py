file=open("file_ops.txt","w")
file.write("hello this is a write file")
file.close()
# with open ("file_ops.txt","r") as file:
#      content=file.read()
#      print(content)
with open("file_ops.txt","r") as file:
    for line in file:
        print(line.strip())
