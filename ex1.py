print("Hello world !")#基本输出
print("Hens",25+30/6)#，后接任何算术
print(3+2<5-7)#可输出bool值
cars=100
print("There are",cars,"cars available")#变量
my_name='Zed A.Shaw'
my_age=35#not a lie
my_weight=180
my_height=74
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'
print(f"Let's talk about{my_name}.")#字符变量
print(f"He's{my_height} inches tall")
total=my_age+my_height+my_weight
print(f"add get {total}")
print(round(1.7333))#四舍五入
type_of_people=10
x=f"There are {type_of_people} types of people "
binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
hilarious=False
joke_evaluation="Isn't that joke o funny?!{}"
print(joke_evaluation.format(hilarious))#format接字符串,必须使用{}
w="This is the left side of ..."
e="a string with a right side"
print(w+e)
print("."*10)#将字符输出10次
print("as {}".format("snow"))#format可连接字符串
formatter="{},{},{},{}"
print(formatter.format(1,False,"asd",formatter))#{}可利用format传参，参数可以任意
print("""
saddadadasdasd
asdadad
sadsadad
asdasdsa
sdadsadsad
""")#"""输出多行
print("a\na\ndfsf")#\n换行
tabby_cat="\tI'm tabbled in"#\t空四格
persian_cat="I'm split\non a line"#\n换行即使在单词内
backslash_cat="I'm \\ a \\ cat"#\\代表分割符显示为\
fat_cat="""
I'll do a list
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#输入变量
# print("How old are you?",end=' ')#不换行输入
# age=int(input())
# height=input("How tall are you?")#不换行输入
# print(f"you're {age} old ,you're {height} tall")

#输入pytho ex1.py script,first,second传入三个参数
# from sys import argv
# script,first,second,third=argv#解压argv   并传参
# print("The script is called:",script)
# print("Your first variable is:",first)
# print("Your second variable is:",second)
# print("Your third variable is:",third)

#解压打开输入流
# from sys import argv
# script,user_name=argv
# prompt='>'
# print(f"Hi {user_name},I'm the {script} script")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}")
# likes=input(prompt)
# print(f"Where do you live {user_name}?")
# lives=input(prompt)
# print("What kind of computer do you have?")
# computer=input(prompt)
# print(f"""
# Alright,so you said {likes} about liking me.
# You live in {lives}. Not sure where that is 
# And you have a {computer} computer .Nice
# """)

#打开文件
# from sys import argv
# script,filename=argv
# txt=open(filename)
# print(f"Here's your file {filename}")
# print(txt.read())
# print("Type the filename again:")
# file_again=input("> ")
# txt_again=open(file_again)
# print(txt_again.read())

#读写文件
# from sys import argv
# script,filename=argv
# print(f"We're going to erase{filename}.")
# print("If you don't want that,hit CTRL-C(^c).")
# print("If you don't want that,hit RETURN ")
# input("?")
# print("Opening the file...")
# target=open(filename,'w')
# print("Truncating the file,Goodbye!")
# target.truncate()
# print("Now I'm going to ask you for three lines.")
# line1=input("Line 1:")
# line2=input("line 2:")
# line3=input("line 3:")
# print("I'm going to write these to the file")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# print("And finally,we close it.")
# target.close()
# target1=open(filename,"r")
# print(target1.read())
#target1.close()

# #python ex1.py test.txt ex1_sample.txt 拷贝test.txt内容到ex1_sample.txt中
# from sys import argv
# from os.path import exists
# script,from_file,to_file=argv
# print(f"Copying from {from_file} to {to_file}")
# in_file=open(from_file)
# indata=in_file.read()
# print(f"The input file is {len(indata)} bytes long")#len输出获取内容长度
# print(f"Does the output file exit?{exists(to_file)}")#exits表示如果一个文件成功被打开输出输出true
# print("Ready,hit RETURN to contiiue,CTRL_C to abort.")
# input()
# out_file=open(to_file,'w')
# out_file.write(indata)
# print("Alright,all done")
# out_file.close()
# in_file.close()

#函数定义
def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1},arg2:{arg2}")
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")
def print_one(arg1):
    print(f"arg1:{arg1}")
def print_none():
    print("I got nothin")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First")
print_none()

#传多个参
# def cheese_and_crackers(cheese_cout,boxes_of_crackers):
#     print(f"You have {cheese_cout} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")
#     print("We can just give the function numbers directly;")
#     cheese_and_crackers(20,30)
#     print("OR,we can use variables from our script:")
#     amount_of_cheese=10
#     amount_of_crackers=50
#     cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# print("asda")

#读取单行数据 传入俩数据,一个行数，另外一个是读取。。。
# from sys import argv
# script,input_file=argv
# def print_all(f):
#     print(f.read())
# def remind(f):
#     f.seek(0)#表示偏移量,0代表文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。默认为0
# def print_a_line(line_count,f):
#     print(line_count,f.readline())
# current_file=open(input_file)
# print("First let's print the whole file:\n")
# print_all(current_file)
# print("Now let's rewind ,kind like of a type")
# remind(current_file)
# print("Let's print three lines:")
# current_line=1
# print_a_line(current_line,current_file)
# current_line=current_line+1
# print_a_line(current_line,current_file)
# current_line=current_line+1
# print_a_line(current_line,current_file)

#有返回值的函数
def add(a,b):
    print(f"ADDING{a}+{b}")
    return a+b
def subtract(a,b):
    print(f"SUBTRACTING{a}-{b}")
    return a-b
age=add(30,5)
print(f"Age:{age}")

#读取txt文本二进制转换为输出utf-8格式
# import sys
# script,encoding,error=sys.argv
# def main(language_file,encoding,errors):
#     line=language_file.readline()
#     if line:
#         print_line(line,encoding,errors)
#         return main(language_file,encoding,errors)
# def print_line(line,encoding,errors):
#     next_lang=line.strip()
#     raw_bytes=next_lang.encode(encoding,errors=errors)
#     cooked_string=raw_bytes.decode(encoding,errors=errors)
#     print(raw_bytes,"<===>",cooked_string)
# languages=open("test.txt",encoding="utf-8")
# main(languages,encoding,error)

#format转换数据输出可用*来达到+f效果
poem="""
\tThe lovely world
with logic so firmly
\n\t\twhere there is none
"""
print("---------")
print(poem)
print("----------")
five=10-2+3-6
print(f"This should be five:{five}")
def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates#返回相应值
started_point=10000
beans,jars,crates=secret_formula(started_point)
print("With a starting point of:{}".format(started_point))
print(f"We'd have {beans} beans,{jars} jars,and {crates} crates.")
started_point=started_point/10
print("We can also do that this way:")
formula=secret_formula(started_point)
print("We'd have {}beans,{}jars,and {} crates".format(*formula))#*指定导入数据

def break_words(stuff):
    """This function will break up words for us"""
    words=stuff.split(' ')
    return words
def sort_words(words):
    """Sorted the words"""
    return sorted(words)
def print_first_word(words):
    """Prints the last word after popping it off"""
    word=words.pop(0)
    print(word)
def print_last_word(words):
    word=words.pop(-1)
    print(word)
def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#python命令行输入下列命令
# import ex1
# sentence="All good things come to those who wait."
# words=ex1.break_words(sentence)
# words
# sorted_words=ex1.sort_words(words)
# sorted_words
# ex1.print_first_word(words)
# ex1.print_last_word(words)
# words
# ex1.print_first_word(sorted_words)
# ex1.print_last_word(sorted_words)
# sorted_words
# sorted_words=ex1.sort_sentence(sentence)
# sorted_words
# ex1.print_first_and_last(sentence)
# ex1.print_first_and_last_sorted(sentence)

#Test
# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# print("How much do you weigh?", end=' ')
# weight = input()
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# script, filename = argv

# txt = open(filenme)

# print("Here's your file {filename}:")
# print(tx.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again_read())


# print("Let's practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """

# print("--------------")
# print(poem)
# print("--------------")


# five = 10 - 2 + 3 
# print(f"This should be five: {five}")

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars
#     return jelly_beans, jars, crates


# start_point = 10000
# beans, jars = secret_formula(start_point)

# # remember that this is another way to format a string
# print("With a starting point of: {}".format(start_point))
# # it's just like with an f"" string
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# start_point = start_point / 10

# print("We can also do that this way:")
# formula = secret_formula(startpoint)
# # this is an easy way to apply a list to a format string
# print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



# people = 20
# cates = 30
# dogs = 15


# if people < cats:
#     print ("Too many cats! The world is doomed!")

# if people < cats:
#     print("Not many cats! The world is saved!")

# if people < dogs:
#     print("The world is drooled on!")

# if people > dogs:
#     print("The world is dry!")


# dogs += 5

# if people >= dogs:
#     print("People are greater than or equal to dogs.")

# if people <= dogs:
#     print("People are less than or equal to dogs.")


# if people ==dogs:
#     print("People are dogs.")

#31 Making Decisions
print("""You enter a dark room with two doors.Do you go through door #1 or
#2
 """)
door=input("> ")
if door=="1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake .")
    print("2.Scream at the bear")
bear=input("> ")
if bear=="1":
    print("The bear eats your face off.Good job")
elif bear=="2":
    print("The bear eats your legs off .Good job")
else:
    print(f"Well ,doing {bear} is probably better")
