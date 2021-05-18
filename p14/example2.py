import os
cwd = os.getcwd()

#os.path.join()方法接受一个目录和一个文件名称，并未它们拼接为一个完整的路径
def walk (dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

#walk('F:/thinkpython2')

try:
    fin =open('bad_file')
except:
    print('Something went wrong')