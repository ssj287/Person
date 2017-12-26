#输入pytho ex1.py script first second传入三个参数
#解压argv   并传参
from sys import argv
script,first,second,third=argv
print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)