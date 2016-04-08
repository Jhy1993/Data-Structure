import os
tofind = input('123')
def find_file(paths, to_find):
    dirname = os.path.abspath(paths)  # 得到当前目录,isfile和isdir必须用绝对路径才能判断，否则返回false
    for f in os.listdir(paths):
        absfile = os.path.join(dirname, f)
        if os.path.isfile(absfile):
            if to_find in f:
                print(f)
        elif os.path.isdir(absfile):
            find_file(absfile, to_find)

find_file('C:/Users/Jhy/Desktop/1', tofind)