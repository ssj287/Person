#python ex1.py test.txt ex1_sample.txt 拷贝test.txt内容到ex1_sample.txt中
from sys import argv
from os.path import exists
script,from_file,to_file=argv
print(f"Copying from {from_file} to {to_file}")
in_file=open(from_file)
indata=in_file.read()
print(f"The input file is {len(indata)} bytes long")#len输出获取内容长度
print(f"Does the output file exit?{exists(to_file)}")#exits表示如果一个文件成功被打开输出输出true
print("Ready,hit RETURN to contiiue,CTRL_C to abort.")
input()
out_file=open(to_file,'w')
out_file.write(indata)
print("Alright,all done")
out_file.close()
in_file.close()