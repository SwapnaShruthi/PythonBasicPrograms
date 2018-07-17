print("hi")
fp=open("python.txt",'r+')
print("bye")
fp.write("shruthi")
fp.seek(0)
print(fp.read())
fp.close()
#shruthi ===>Single line commnet
'''
r+ --> reads and writes the existing file
w+ --> reads writes and creates the file if does not exist 

 ==>multiline commnet'''