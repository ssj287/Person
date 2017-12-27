#读取单行数据 传入俩数据,一个行数，另外一个是读取。。。
from sys import argv
script,input_file=argv
def print_all(f):
    print(f.read())
def remind(f):
    f.seek(0)#表示偏移量,0代表文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。默认为0
def print_a_line(line_count,f):
    print(line_count,f.readline())
current_file=open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind ,kind like of a type")
remind(current_file)
print("Let's print three lines:")
current_line=1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)