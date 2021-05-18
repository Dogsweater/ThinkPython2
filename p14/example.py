
#open()返回的是一个文件对象
fout = open('output.txt','w') 
line1 ='This here`s the wattle,\n'
#返回值是文档对象会记录写到了哪里；
fout.write(line1)

line2='the emblem of our land.\n'
fout.write(line2)

#fout.close()

x=53
fout.write(str(x))

