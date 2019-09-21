#!/usr/bin/python
#coding=utf-8
# --------------- 请在python2环境运行  ---------------
import time
from time import strptime
num = 1 ; olive=5
def topic(num,answer, correct='答题正确,请继续.', mistake='错误，请复习后再战！'):
    if answer == taking:
        print('\033[34;1m%s\033[0m' % correct)
    else:
        global live
        live-=1
        if live==0:
            print('\033[35;1m游戏结束，正确答案:%s ; %s条命的超人变成了一个普通人。\033[0m'%(answer,olive))
            exit()
        print('\033[31;1m%s还剩%s条命！正确答案:%s\033[0m' % (mistake,live,answer))
    print("")
    num += 1
    time.sleep(0.2)
    return num

try:
    olive=int(input("\n来吧超人，初始%s条命，如果您认为不能闯到最后一关的话，可以运用神力改命，您需要吗？\n"
                    "希望超人拥有几条命："%olive))
    if not 0 < olive < 21:
        olive = 20
        raise NameError("传说中的狸猫也才9条命,贵为超人最多只能拥有20条命。")
except (NameError,SyntaxError) as e_value:
    print("\033[33;1m改命不成功！初始%s条命.%s\033[0m"%(olive,e_value))
    if olive != 2 and olive != 5: exit(1)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(2)
live=olive
try:
    print("")
    taking = raw_input('''%s.如果想在 print('Hello', 'World'）代码中增加各项间的分隔符应该使用：
      A.＋
      B.end=
      C.seq=
      D.sep=
    请选择正确答案:''' % num)
    num=topic(num,'D', '答题正确,预热才刚开始呢,请继续.')

    taking = raw_input('''%s.在python3的 n = input('number: ') 代码中用户输入一个数字,n 的类型一定为：
      A.字符
      B.数字
      C.元组
      D.数组
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.以下在python的变量命名中，错误的命名是:
      A.Value
      B.one
      C._1_user
      D.py-str
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input("""%s.python变量赋值 n=2+5%%2 ,n值等于:
      A.4
      B.3
      C.2
      D.5
    请选择正确答案:"""% num)
    num=topic(num,'B')

    taking = raw_input('''%s.Python之禅主要体现哪三个意思？
      A.美胜丑
      B.明胜暗
      C.少胜多
      D.简胜繁
    请选多个正确答案:''' % num)
    num=topic(num,'ABD')

    taking = raw_input('''%s.Python代码 a,b=divmod(7,3) 中,a和b的值分别是？
      A.1,2
      B.2,1
      C.2,3
      D.3,4
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.python运算中， 7//3 的结果是？
      A.1
      B.2
      C.3
      D.4
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''.python算术运算符中，和模运算相关的符号是？
      A./
      B.//
      C.%
      D.**
    请选择正确答案:''')
    num=topic(num,'C', 'A是相除，B得商，C求余也称求模，D幂运算')

    taking = raw_input('''%s.python3运算函数 round() 的结果为四舍六入五成偶，round(5/2)等于？
      A.2
      B.2.5
      C.3
      D.无法运算
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.逻辑运算 1>2 or 4>3 and 5>2 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.逻辑运算 1!=1 and 0/2 or not 3==4 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.逻辑运算 not 0 or False 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.python中数字默认以10进制输出，整数不同的前缀表示不同的进制，0o开头表示？进制数，0b开头表示？进制数，0x开头表示？进制数：
      A.2，8，16
      B.8，2，16
      C.16，8，2
      D.16，2，8
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.python将10进制数转成16进制数的函数是？
      A.oct()
      B.bin()
      C.hex()
      D.int()
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.python将10进制数转成8进制数的函数是？
      A.oct()
      B.bin()
      C.hex()
      D.int()
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.python将10进制数转成2进制数的函数是？
      A.oct()
      B.bin()
      C.hex()
      D.int()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.Python Console中直接输入print("%%s+%%s=2"%%(1,s))得到的输出是？
      A.%%s+%%s=2
      B.1+s=2
      C.1+1=2
      D.NameError
    请选择正确答案:'''% num)
    num=topic(num,'D')

    taking = raw_input('''%s.mystr='01234567';print(len('mystr'))得到的输出是？
      A.6
      B.5
      C.8
      D.7
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.mystr='01234567';print(mystr[])得到的输出是？
      A.01234567
      B.'01234567'
      C.mystr[]
      D.都不对
    请选择正确答案:''' % num)
    num=topic(num,'D', 'mystr[:]才是输出整个字符串。')

    taking = raw_input('''%s.mystr='01234567';print(mystr[3:5:3])得到的输出是？
      A.25
      B.36
      C.2
      D.3
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.mystr='01234567';print(mystr[5:2:-1])得到的输出是？
      A.432
      B.543
      C.54
      D.65
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.已知 mystr='01234567' ,下面错误的字符串切片是？
      A.mystr[8:]
      B.mystr[0]
      C.mystr[8]
      D.mystr[::-9]
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.逻辑运算 mystr='01234567';'67' not in {'mystr'} 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.已知 alist=[{(1),'2'},(3,[4])] ,函数 len(alist) 输出是？
      A.1
      B.2
      C.3
      D.4
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.关于字典的理解,下面说法错误的是？
      A.字典是无序的
      B.采用key: val的形式
      C.字典通过下标读取val
      D.字典的key是唯一的
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.数据类型按存储模型可分为 标量类型(只有一种对象的数值、字符串)；容器类型(可以保存各种对象的列表、元组、字典)？
      A.正确
      B.错误
    请选择答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.数据类型按更新模型可分为 可变类型(列表、字典)；不可变类型(数字、字符串、元组)？
      A.正确
      B.错误
    请选择答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.数据类型按访问方式可分为 直接访问(数字、元组)；顺序访问(字符串、列表)；映射访问(字典)？
      A.正确
      B.错误
    请选择答案:''' % num)
    num=topic(num,'B', '元组是顺序访问')

    taking = raw_input('''%s.关于循环语句，下面说法错误的是？
      A.如果循环次数未知，用while
      B.如果循环次数已知，用for
      C.while循环只能被 break 结束
      D.如果循环次数已知，可以用while循环
    请选择答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.在for循环语句中，continue是否可以结束循环？
      A.while循环中可以，for循环中不可以
      B.while循环中不可以，for循环中可以
      C.无论while循环还是for循环都可以
      D.无论while循环还是for循环都不可以
    请选择答案:''' % num)
    num=topic(num,'D', 'continue是跳过本次循环的剩余代码，继续下一轮循环')

    taking = raw_input('''%s.print(range(1, 5, 2))得到的输出是？
      A.[1, 3]
      B.[1, 3, 5]
      C.[1, 4]
      D.range(1, 5, 2)
    请选择正确答案:''' % num)
    num=topic(num,'A',mistake='BC项为错误list,range()是定义范围。')

    taking = raw_input('''%s.Python Console中直接输入list(range(0, 6, 3))得到的输出是？
      A.[0, 3]
      B.[1, 4]
      C.[0, 3, 6]
      D.空值
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.Console中直接输入[1 + i for i in range(1, 5) if i %% 2 == 1]得到的输出是？
      A.[2, 4, 6]
      B.[2, 4]
      C.[1, 3, 6]
      D.空值
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.已知 n=5 if 3 not in range(3,5,3) else 6 ;n等于？
      A.3
      B.5
      C.6
      D.空值
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.逻辑运算 5 not in range(1,5,2) 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.>>> list(range(9,0,-3))得到的输出是？
      A.[]
      B.[9, 8, 7, 6, 5, 4]
      C.[9, 6, 3]
      D.[8, 4, 2]
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.给出 mystr='12345'，如何使用字符串切片取出字符'5'？
      A.mystr[4]
      B.mystr[5]
      C.mystr[5:]
      D.mystr[:5]
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.已知 mystr='01234567';逻辑运算 '67' not in {mystr} 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.已知 mystr='01234567';逻辑运算 '67' not in [mystr] 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.已知 mystr='01234567';逻辑运算 '67' not in (mystr) 的结果是？
      A.True
      B.False
    请选择正确答案:''' % num)
    num=topic(num,'B','恭喜你，已经能理解列表、元组、字典的区别。')

    taking = raw_input('''%s.下面哪个IP地址不在列表 ['192.168.1.%%s' %%i for i in range(1, 255)] 中？
      A.192.168.1.0
      B.192.168.1.254
      C.192.168.1.255
      D.以上都是
    请多选择正确答案:''' % num)
    num=topic(num,'AC')

    taking = raw_input('''%s.已知 mylist=[1,2,3];想让 mylist=[1,2,3,4,5] 可以？
      A.mylist=[1,2,3,4,5]
      B.mylist[3]=4;mylist[4]=5
      C.mylist.append(4);mylist.append(5)
      D.以上都可以
    请多选择正确答案:''' % num)
    num=topic(num,'AC')

    taking = raw_input('''%s.已知 adict={'one':1,'two':2} ; bstr='345' ; clist=[6,7] ; dtuple=(8,9) ;下面为True正确成立的是？
      A.adict[1] + adict[2] = 3
      B.bstr[1] + bstr[2] = 7
      C.clist[0] + clist[1] = 13
      D.dtuple[0] + dtuple[1] == 17
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.已知 adict={'one':1,'two':2} ; bstr='345' ; clist=[6,7] ; dtuple=(8,9) ;下面为True正确成立的是？
      A.adict[0] + adict[1] == 3
      B.bstr[0] + bstr[1] == 9
      C.clist[0] + clist[1] == 13
      D.dtuple[1] + dtuple[2] == 17
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.已知 adict={'one':1,'two':2} ; bstr='345' ; clist=[6,7] ; dtuple=(8,9) ;下面为True正确成立的是？
      A.adict[one] + adict[two] == 3
      B.int(bstr[0] + bstr[1]) == 7
      C.clist[1] + clist[2] == 13
      D.clist[1] + dtuple[1] == 16
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.已知 adict={'one':1,'two':2} ; bstr='345' ; clist=[6,7] ; dtuple=(8,9) ;下面为True正确成立的是？
      A.adict['one'] * adict['two'] == 3
      B.int(bstr[0]) + int(bstr[1]) == 7
      C.clist[0] * clist[1] == 13
      D.clist[1] + dtuple[-1] == 16
    请多选择正确答案:''' % num)
    num=topic(num,'BD')

    taking = raw_input('''%s.已知 adict={'one':1,'two':2} ; bstr='345' ; clist=[6,7] ; dtuple=(8,9) ;下面为True正确成立的是？
      A.adict['one'] ** adict['two'] == 1
      B.int(bstr[-0]) + int(bstr[-2]) == 7
      C.dtuple[-2] - clist[1] == 1
      D.clist[1] // dtuple[-1] == 0
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.Python 导入模块的方法中，下面正确的是？
      A.import time
      B.from random import choice,randint
      C.import sys, os, abc
      D.import getpass as gp
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.Python 从一个序列对象中随机选择一项的函数是？
      A.getpass.getpass()
      B.random.choice()
      C.random.randint()
      D.sys.argv[]
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.Python 打开一个文件时需不需要加载哪个模块？
      A.import sys
      B.import os
      C.直接使用内建函数
      D.import open
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.Python 关于文件对象访问文件模式下面说法错误的是？
      A.'r' 以只读方式打开，文件不存在则报错
      B.'w' 以写方式打开，文件不存在则创建，存在则读取
      C.'a' 以追加模式打开，文件在必要时创建
      D.'b' 以二进制模式打开
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.Python 关于文件对象访问文件模式下面说法正确的是？
      A.'r+' 以读写方式打开，文件不存在则报错
      B.'w+' 以擦写模式打开，文件不存在则创建，存在则清空
      C.'a+' 以追加读写模式打开，文件在必要时创建
      D. 以上都正确
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.文件对象read()方法可以直接读取所有字节到字符串中的是？
      A. fobj=open('/etc/passwd');data = fobj.read(0)
      B. fobj=open('/etc/passwd');data = fobj.read(99)
      C. fobj=open('/etc/passwd');data = fobj.read(-99)
      D. file_obj=open('/etc/passwd');data = fobj.read()
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.文件对象readline()方法可以一行一行地读取整行字节到字符串中，下面可以只取出‘student’字符的是？
      A. fobj=open('/etc/passwd');data = fobj.read(4)
      B. fobj=open('/etc/passwd');data = fobj.read(-1)
      C. fobj=open('/etc/passwd');data = fobj.read(-7)
      D. fobj=open('/etc/passwd');data = fobj.read(7)
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.循环迭代处理一个文本文件，一般常用的方法是？
      A. fobj=open('/etc/passwd');with eachline as fobj: ...
      B. fobj=open('/etc/passwd');for eachline in fobj: ...
      C. fobj=open('/etc/passwd');with eachline in fobj: ...
      D. fobj=open('/etc/passwd');for eachline as fobj: ...
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.在下面写入文件方法中，test文件结果为2行的是？
      A. fobj=open('/tmp/test', 'w');fobj.write('hello world!\ni hao!')
      B. fobj=open('/tmp/test', 'w');fobj.flush()
      C. fobj=open('/tmp/test', 'w');fobj.writelines(['hello', 'world'])
      D. fobj=open('/tmp/test', 'w');fobj.writelines(['hello\n', r'world\n'])
    请多选择正确答案:''' % num)
    num=topic(num,'AD')

    taking = raw_input('''%s.在下面处理文件方法中，打开、读取内容后会自动关闭文件的是？
      A. for line in open('/etc/passwd'): print(line, end='')
      B. fobj=open('/tmp/passwd', 'r');fobj.flush()
      C. with open('/tmp/passwd') as fobj: fobj.readlines()
      D. fobj=open('/tmp/passwd', 'r');fobj.readlines()
    请多选择正确答案:''' % num)
    num=topic(num,'AC','A选项是直接在for循环打开，文件随循环存在而打开。lsof可查看文件是否打开。')

    taking = raw_input('''%s./tmp/f文件内容为7个字母: abcdefg，f=open('/tmp/f','rb');f.seek(-3,2);str=f.read(0)；str的值为？
      A. b''
      B. b'e'
      C. b'f'
      D. b'g'
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s./tmp/f文件内容为7个字母: abcdefg，f=open('/tmp/f','rb');f.seek(-3,2);str=f.read(1)；str的值为？
      A. b''
      B. b'e'
      C. b'f'
      D. b'g'
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s./tmp/f文件内容为7个字母: abcdefg，f=open('/tmp/f','rb');f.seek(-3,2);str=f.read(-1)；str的值为？
      A. b'd'
      B. b'e'
      C. b'f'
      D. b'fg\n'
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s./tmp/f文件内容为7个字母: abcdefg，f=open('/tmp/f','rb');f.seek(2,0);str=f.read(3)；str的值为？
      A. b'ab'
      B. b'bc'
      C. b'bcd'
      D. b'cde'
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.python 函数定义时，里面的代码不会执行； 通过()调用时执行或者import导入模块时执行一次的函数应该怎么定义？
      A. print 函数名(参数...):
      B. input 函数名(参数...):
      C. def 函数名(参数...):
      D. sys 函数名(参数...):
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input('''%s.python 函数被执行后，关于函数返回值下面说法正确的是？
      A. 函数的返回值就是函数运行后的结果，值为None；
      B. 函数内的变量值只能通过return返回，如果没有return则返回None；
      C. 函数内的变量值如果是一个全局变量则无需return返回；
      D. return返回值只能是函数运行后的结果或者返回None。
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.python 每个模块都有一个特殊的变量叫__name__，下面说法正确的是？
      A. __name__值在不同的情况下不同；
      B. 如果模块文件直接运行，值为__main__；
      C. 如果模块因为import间接运行，值为None；
      D. 如果模块因为import间接运行，值为模块名。
    请选多个正确答案:''' % num)
    num=topic(num,'ABD')

    taking = raw_input('''%s.处理一个非文本文件，下面常用的打开文件方式是？
      A. for line in open(非文本文件,'rb'):
             data=fobj.read(4096) ...
      B. fobj=open(非文本文件, 'rb');
         data=fobj.read(4096) ...
      C. with open(非文本文件,'rb') as fobj:
             while True:
                 data=fobj.read(4096) ...
      D. fobj=open(非文本文件, 'rb');
         for line in fobj:
             data=fobj.read(4096) ...
    请选择正确答案:''' % num)
    num=topic(num,'C','处理非文本文件:while循环')

    taking = raw_input('''%s.python 有个shutil模块用于实现文件管理操作，和shell命令cp -r /etc/security/ /tmp/anquan相同效果的是？
      A. shutil.copy('/etc/security', '/tmp/anquan')
      B. shutil.copytree('/etc/security', '/tmp/anquan')
      C. shutil.move('/etc/security', '/tmp/anquan')
      D. shutil.rmtree('/etc/security')
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.python 有个subprocess模块用于执行系统命令，和shell命令 ls ~ 相同效果的是？
      A. subprocess.stdout('ls ~')
      B. subprocess.run('ls ~')
      C. subprocess.run('ls ~', shell=True)
      D. subprocess.stdout('ls ~', shell=True)
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.执行result = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)后，下面哪种方法可以知道john用户存不存在？
      A. result.returncode
      B. result.stdout
      C. result.stderr
      D. result.stdout.decode()
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.python 多元赋值:  A,B='12';A,B=B,A;请问A值是？
      A. 1
      B. ‘1’
      C. 2
      D. ‘2’
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input('''%s.python 的函数命名不可以和关键字还有内建重名，请问如何查看关键字列表？
      A. help("keywords")
      B. import keyword;
         keyword.kwlist
      C. import keyword;print(keyword.kwlist)
      D. print(keyword.kwlist)
    请选多个正确答案:''' % num)
    num=topic(num,'ABC')

    taking = raw_input('''%s.python 的函数命名不可以和关键字还有内建重名，请问下面哪些是内建名（内置函数）？
      A. int
      B. range
      C. if
      D. len
    请选多个正确答案:''' % num)
    num=topic(num,'ABD')

    taking = raw_input('''%s.python 在字符串的转换中，下面可以转换成字符的是？
      A. str(12345)
      B. str((12345))
      C. str([12345])
      D. str({12345})
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.python 在列表的转换中，下面可以转换成列表的是？
      A. list(12345)
      B. list('12345')
      C. list((12345))
      D. list({12345})
    请多选择正确答案:''' % num)
    num=topic(num,'BD')

    taking = raw_input('''%s.python 在元组的转换中，下面可以转换成元组的是？
      A. tuple(12345)
      B. tuple('12345')
      C. tuple([12345])
      D. tuple({12345})
    请选多个正确答案:''' % num)
    num=topic(num,'BCD')

    taking = raw_input('''%s.python 在字典的转换中，下面可以转换成字典的是？
      A. dict([(1,'a'), (2, 'b')])
      B. dict(((1,'a'), (2, 'b')))
      C. dict([(1,'a'), (2, 'b')])
      D. dict([[1,'a'], (2, 'b')])
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input('''%s.已知nums = [i+i for i in range(100) if i<5] ； 那么 list(reversed(nums)) 输出的是？
      A. [0, 2, 4, 6, 8]
      B. [8, 6, 4, 2, 0]
      C. [0, 2, 4, 6, 8,......,200]
      D. [198, 196, 194, 192, 190]
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input('''%s.已知nums = [i+i for i in range(100) if i<5] ； 那么 sorted(nums) 输出的是？
      A. [0, 2, 4, 6, 8]
      B. [8, 6, 4, 2, 0]
      C. [0, 2, 4, 6, 8,......,200]
      D. [198, 196, 194, 192, 190]
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input('''%s.关于字符编码，下面说法错误的是？
      A. 万国码unicode包含了gbk、iso-8859-1、ASCII字符集的所有字符。
      B. UTF8是unicode的一种编码方案，一个英文字符用1个字节表示，一个汉字用3个字节表示。
      C. ASCII、iso-8859-1、latin-1、gbk、gb18030、gb2312字符集组合起来就是unicode字符集。
      D. string类型是字符类型，btyes类型是字节类型，所以两者的长度计算方式不一样。
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.已知 '中国'.encode() 输出的是 b'\xe4\xb8\xad\xe5\x9b\xbd' ，那么 '中国'.encode().decode() 的输出是？
      A. '中国'
      B. b'\xe4\xb8\xad\xe5\x9b\xbd'
      C. '\xe4\xb8\xad\xe5\x9b\xbd'
      D. Error
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.字符串格式化 '%%d is %%s years old' %% ('tom', 20) 下面正确输出的是？
      A. '20 is tom years old'
      B. 'tom is 20 years old'
      C. 20 is 'tom' years old
      D. TypeError
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.字符串格式化 '%%-8s%%-8s' %% ('name', 'age') 下面正确输出的是？
      A. '    name     age'
      B. 'name    age     '
      C. '     name    age     '
      D. '    name     age     '
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.下面字符串格式化小数位输出3位小数的是？
      A. '%%3f' %% (5 / 3)
      B. '%%.3f' %% (5 / 3)
      C. '%%6.3f' %% (5 / 3)
      D. '%%e' %% (3)
    请多选择正确答案:''' % num)
    num=topic(num,'BC')

    taking = raw_input(r'''%s.下面字符串格式化以16进制格式输出的是？
      A. '%%#x' %% 10
      B. '%%#o' %% 16
      C. '%%#e' %% 8
      D. '%%#d' %% 8
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.下面字符串格式化以以10进制格式输出的是？
      A. '%%#x' %% 10
      B. '%%#o' %% 16
      C. '%%#e' %% 8
      D. '%%#d' %% 8
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.下面字符串格式化以以8进制格式输出的是？
      A. '%%#x' %% 10
      B. '%%#o' %% 16
      C. '%%#e' %% 8
      D. '%%#d' %% 8
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.字符串格式化 '{1} is {0} years old'.format(20, 'two') 下面正确输出的是？
      A. '20 is two years old'
      B. 'two is 20 years old'
      C. 20 is 'two' years old
      D. TypeError
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.字符串的处理方法中 '  \t hello   \n'.lstrip() 得到下面正确输出的是？
      A. 'hello'
      B. 'hello   \n'
      C. '  \t hello'
      D. '\t hello   \n'
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.字符串的处理方法中 'hello'.ljust(10, '+') 得到下面正确输出的是？
      A. '+++++hello'
      B. '++++++++++hello'
      C. 'hello+++++'
      D. 'hello++++++++++'
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.字符串的处理方法中，下面能将字母转换成小写的是？
      A. 'hello'.upper()
      B. 'hao123'.lower()
      C. 'Hao123'.islower()
      D. 'hello'.isdigit()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.字符串的处理方法中，下面能输出 'he.o' 的是？
      A. '.o'.startswith('he')
      B. 'he'.endswith('.o')
      C. 'hello'.replace('ll', '.')
      D. 'h.e.o'.split('.')
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.列表属于容器、可变、序列类型,下面列表的常用方法中，错误的用法是？
      A. alist.insert(2, 100)
      B. alist.sort(reverse=True)
      C. clist = alist.copy()
      D. alist.del(2)
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.下面列表的常用方法中，可以删除指定下标元素的用法是？
      A. alist.append(20)
      B. alist.pop()
      C. alist.pop(4)
      D. alist.remove(15)
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.元组属于容器、不可变、序列类型，下面常用方法中，错误的用法是？
      A. atup.count(20)
      B. atup.index(20)
      C. btup = atup.copy()
      D. atup.pop(2)
    请多选择正确答案:''' % num)
    num=topic(num,'CD')

    taking = raw_input(r'''%s.字典属于容器、可变、映射类型，下面创建赋值方法中，错误的是？
      A. dict(['ab', ['name', 'bob'], ('age', 20)])
      B. adict[(10, 20)] = 'beijing'
      C. {}.fromkeys(['tom', 'jerry', 'bob'], 18)
      D. adict[[10, 20]] = 'beijing'
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.下面字典的常用方法中，用法错误的是？
      A. adict.update({'qq': '123456', 'phone': '110'})
      B. adict.get('qq')
      C. list(adict.keys())
      D. adict.remove('phone')
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.集合是一个数学上的概念，由不同元素构成，下面理解正确的是？
      A. 集合元素必须是不可变的
      B. 集合元素不同能重复
      C. 集合有可变集合set和不可变集合frozenset
      D. 集合可以看作是一个无值的字典
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.下面列表的常用方法中，可以删除指定元素的用法是？
      A. alist.del(20)
      B. alist.pop()
      C. alist.pop(4)
      D. alist.remove(15)
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.时间的9元组时间表示方法除了 年/月/日/时/分/秒 还包括哪三项？
      A. 一年中的第几天
      B. 一周中的第几天
      C. 一月中的第几天
      D. 是否使用夏时制
    请选多个正确答案:''' % num)
    num=topic(num,'ABD')

    taking = raw_input(r'''%s.time模块的时间戳是指1970-1-1 0:0:0 到某一时间点之间的秒数，获得当前时间戳的方法是？
      A. import time
      B. time.time()
      C. time.ctime()
      D. time.localtime()
    请多选择正确答案:''' % num)
    num=topic(num,'AB')

    taking = raw_input(r'''%s.加载time模块后，能灵活指定显示当前时间字符串格式的方法是？
      A. time.strftime()
      B. time.strptime()
      C. time.ctime()
      D. time.localtime()
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.加载time模块后，能将字符串时间格式转换为truct_time对象的方法是？
      A. time.strftime()
      B. time.strptime()
      C. time.ctime()
      D. time.localtime()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.除了time模块能处理时间对象，datetime模块也能处理对象，datetime.now()返回的是？
      A. 9元组时间
      B. 年、月、日、时、分、秒、当天的总秒数
      C. 年、月、日、时、分、秒、毫秒
      D. 年、月、日、时、分、秒、时间戳
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.如果想要计算两个时间对象的时间差，例如计算100天3小时之前的时间是什么时候应该用哪个方法？
      A. datetime.now()
      B. timedelta()
      C. datetime()
      D. time.localtime()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.python的异常处理解决方案中，将可能发生异常的语句放在哪个语句后面？
      A. try:
      B. except:
      C. else:
      D. finally:
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.python的异常处理解决方案中，将异常不发生才执行的代码放在哪个语句后面？
      A. try:
      B. except:
      C. else:
      D. finally:
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.python的异常处理解决方案中，将解决方案代码放在哪个语句后面？
      A. try:
      B. except:
      C. else:
      D. finally:
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.python的异常处理解决方案中，将异常发不发生都要执行的代码放在哪个语句后面？
      A. try:
      B. except:
      C. else:
      D. finally:
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.python中如需要主动触发异常，可以通过哪些方式？
      A. ValueError
      B. raise
      C. assert
      D. AssertionError
    请多选择正确答案:''' % num)
    num=topic(num,'BC')

    taking = raw_input(r'''%s.os模块是python访问操作系统功能的主要接口， 对文件系统的访问大多通过此os模块实现，下面常用方法错误的是？
      A. os.getcwd()
      B. os.listdir()
      C. os.copy()
      D. os.makedirs()
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.os模块是python访问操作系统功能的主要接口， 对文件系统的访问大多通过此os模块实现，下面常用方法错误的是？
      A. os.symlink()
      B. os.move()
      C. os.mknod()
      D. os.chown()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.os模块可以实现对文件系统的访问，能对目录文件进行查看创建删除和修改属主权限，下面修改文件权限方法正确的是？
      A. os.chmod('mytest.txt', 0o644)
      B. os.chmod('mytest.txt', 2770)
      C. os.chown('mytest.txt', 0o711)
      D. os.chown('mytest.txt', 2770)
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.os模块中的path函数有各种判断方法和文件路径处理方法，下面常用方法正确的是？
      A. os.path.abspath()
      B. os.path.dirname()
      C. os.path.basename()
      D. os.path.split()
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.os模块中的path函数有各种判断方法和文件路径处理方法，下面常用方法正确的是？
      A. os.path.isfile()
      B. os.path.exists()
      C. os.path.islink()
      D. os.path.join()
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.如果想把任意的数据类型写入文件，还要无损地取出，那么写入的方法是？
      A. os.write()
      B. pickle.dump()
      C. pickle.load()
      D. os.writelines()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.如果把任意的数据类型写入文件，需要无损地取出，那么取出的方法是？
      A. os.write()
      B. pickle.dump()
      C. pickle.load()
      D. os.writelines()
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.函数用def语句创建,标题行由def关键字,函数的名字,以及参数的集合(如果有的话)组成,下面说法正确的是？
      A. 定义函数的时候，参数它的值不确定，只是起个名称，形式上占个位置，所以叫形式参数，简称形参；
      B. 调用函数的时候，将具体的数据传递进去，这个时候相当于是变量赋值，因为使用的数据值已经确定，是实际使用的参数，叫作实际参数，简称实参；
      C. 多个函数创建的顺序不重要，重要的是调用顺序；
      D. 函数的参数，如果是key=val的形式，称作关健字参数；如果是只有参数arg1,arg2...称作位置参数。
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.函数可以通过关健字参数传参或通过位置参数传参,关于传参方法下面说法错误的是？
      A. 函数传递参数时，实参的个数须和形参个数一致，不然会出现TypeError；
      B. 当同时传递关健字参数和位置参数时，关健字参数需放在位置参数后面；
      C. 定义函数时，在形参前加一个*表示使用元组接收参数，加两个*表示用字典接收参数；
      D. 调用函数时，在实参前加一个*表示把序列对象拆开，加两个*号表示把字典拆开。
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.通过lambda关键字定义的、“没有名字”的函数又称为匿名函数,关于匿名函数下面说法错误的是？
      A. 匿名函数可以传递多个参数；
      B. 匿名函数有多行代码组成；
      C. 匿名函数主体只有一行代码；
      D. 匿名函数必须lambda关键字才能定义。
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.只接受两个参数，第一个参数是函数且返回值是True或False；第二个参数是序列对象，它的每个数据都成为第一个函数的参数，如果结果为真则保留为假则丢弃的是？
      A. partial函数
      B. map函数
      C. filter函数
      D. lambda函数
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.只接受两个参数，第一个参数是函数且接收一个参数进行加工处理；第二个参数是序列对象，它的每个数据都成为第一个函数的参数进行加工后返回，该函数是？
      A. partial函数
      B. map函数
      C. filter函数
      D. lambda函数
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.按变量作用域可分全局变量（在函数外面定义的变量。从定义开始到函数结束，一直是可见可用的。）和局部变量（在函数内定义，只在函数内部使用，外界看不到这个函数。），下面说法正确的是？
      A. 全局和局部有同名变量，函数内的变量将遮盖住全局变量；
      B. 如果希望在局部改变全局变量，可以使用global关键字；
      C. 如果希望在局部使用全局变量，可以定义一个同名全局变量的局部变量；
      D. 函数在查找名称时，先在局部查找，再查全局，最后查内建。
    请选多个正确答案:''' % num)
    num=topic(num,'ABD')

    taking = raw_input(r'''%s.当一个函数有多个参数传参，但使用时仅需修改数个或一个参数，可以把函数的某些参数固定下来，生成新的偏函数，用到的相关模块和方法是？
      A. import getpass as gp
      B. gp.getpass()
      C. from functools import partial
      D. partial()
    请多选择正确答案:''' % num)
    num=topic(num,'CD')

    taking = raw_input(r'''%s.列表所有数据都在内存中，有海量数据的话将会非常耗内存，如果列表元素能按照某种算法推算出来，不用完整列表只需在循环的过程中不断推算出后续的元素从而节省大量的空间，这些由生成器(generator)完成，下面正确的是？
      A. 生成器可以用表达式生成元素
      B. 生成器可以用函数方式生成元素
      C. 函数方式生成器通过yield关键字可以生成很多中间结果
      D. 生成器只能通过yield关键字生成元素
    请选多个正确答案:''' % num)
    num=topic(num,'ABC')

    taking = raw_input(r'''%s.导入模块时，如果希望自己写的模块文件像系统模块一样，在任何位置都可以导入，以下哪些方法可以实现？
      A. 将文件拷贝到site-packages目录
      B. 定义环境变量PYTHONPATH
      C. 在sys.path中添加文件路径
      D. 定义环境变量PATH
    请选多个正确答案:''' % num)
    num=topic(num,'ABC')

    taking = raw_input(r'''%s.以下哪个模块用于计算数据的哈希值？
      A. hexdigest
      B. md5
      C. hashlib
      D. tarfile
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.现有一个mytest.tar.gz压缩文件，python解压缩到/tmp目录的过程是？
      A. tar.extractall(path='/tmp/')
      B. tar = tarfile.open('/nsd1904/mytest.tar.gz')
      C. import tarfile
      D. tar.close()
    请选多个正确答案:''' % num)
    num=topic(num,'CBAD')

    taking = raw_input(r'''%s.如何获取一个空的md5加密算法对象？
      A. mobj = hashlib.md5()
      B. import hashlib
      C. m.update(data)
      D. m.hexdigest()
    请多选择正确答案:''' % num)
    num=topic(num,'BA')

    taking = raw_input(r'''%s.python代码行中 os.path.basename('/tmp/demo/filename') 输出的是？
      A. '/tmp/demo/filename'
      B. '/tmp/demo/'
      C. 'filename'
      D. filename
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.python代码行中 time.strftime('%%d%%m%%Y') 输出的格式似？
      A. %s
      B. %s
      C. %s
      D. %s
    请选择正确答案:''' % (num,time.strftime('%Y%d%m'),time.strftime('%Y-%d-%m'),time.strftime('%d%m%Y'),time.strftime('%d-%m-%Y')))
    num=topic(num,'C')

    taking = raw_input(r'''%s.python代码行中 os.path.join('dst/test', 'fname') 输出的是？
      A. '/dst/test/fname'
      B. 'dst/test/fname'
      C. '/dst/test/fname/'
      D. '/dst/testfname'
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.要实现完全备份，把/fname目录以gzip格式打包到/backup目录，下面正确顺序是？
      A. tar.add('/fname')
      B. import tarfile
      C. tar = tarfile.open('/backup/fname.bk', 'w:gz')
      D. tar.close()
    请选多个正确答案:''' % num)
    num=topic(num,'BCAD')

    taking = raw_input(r'''%s.python代码行中 m=list(os.walk('/home')) 输出内容下面正确的是？
      A. m[0] 对应的是 '/home' 的文件路径
      B. m[1] 对应的是 '/home' 的文件夹
      C. m[2] 对应的是 '/home' 的文件
      D. m[0][0] 对应的是 '/home' 文件路径
    请选择正确答案:''' % num)
    num=topic(num,'D')

    taking = raw_input(r'''%s.类(Class)是用来描述具有相同的属性和方法的对象的集合,实例化类实例时默认会调用的方法是？
      A. __init__方法
      B. __str__方法
      C. __call__方法
      D. __name__方法
    请选择正确答案:''' % num)
    num=topic(num,'A')

    taking = raw_input(r'''%s.类(Class)是蓝图,实例是根据蓝图创建出来的具体对象,用于创建可调用的实例的方法是？
      A. __init__方法
      B. __str__方法
      C. __call__方法
      D. __name__方法
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.类(Class)中定义的方法需要绑定在具体的实例,由实例调用,用于返回字符串,打印/显示实例时调用的方法是？
      A. __init__方法
      B. __str__方法
      C. __call__方法
      D. __name__方法
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.python允许多重继承,即一个类可以是多个父类的子类,子类可以拥有所有父类的属性，其继承顺序是？
      A. 组合应用中从上到下
      B. 组合应用中从下到上
      C. 同一基类中从左到右
      D. 同一基类中从右到左
    请多选择正确答案:''' % num)
    num=topic(num,'BC')

    taking = raw_input(r'''%s.os.walk返回值由多个元组构成，每个元组由三项构成：(字符串， 列表， 列表)，下面理解正确的是？
      A. 元组中的第一项字符串，是路径
      B. 元组中的第二项列表，是路径下的所有目录
      C. 元组中的第三项列表，是路径下的所有文件
      D. 只要将路径和路径下的文件进行拼接，即可得到文件的路径
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.关于OOP面向对象的编程，将现实世界的实体抽象成类（将数据属性和函数属性整合在一起的class,用来描述具有相同的属性和方法的对象的集合），下面理解正确的是？
      A. 实例，对象：通过类定义的数据结构实例。
      B. 方法：定义在类中的函数。
      C. 组合：两个类明显不同，其中一个类是另一个类的组件，使用组合。
      D. 继承：当两个类有很多一样的地方，但是又有一些不同，使用继承。
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.python中使用正则表达式，需要加载哪个模块？
      A. os
      B. re
      C. hashlib
      D. tarfile
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.re模块的方法中，能在字符串中匹配所有匹配字符的方法是？
      A. re.match()
      B. re.findall()
      C. re.search()
      D. re.finditer()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.python中使用正则表达式，如果有大量内容需要匹配，把模式先进行编译将会得到更好的效率的方法是？
      A. re.match()
      B. re.group()
      C. re.compile()
      D. re.finditer()
    请选择正确答案:''' % num)
    num=topic(num,'C')

    taking = raw_input(r'''%s.由于字典本身没有顺序,可以通过将字典转成列表再排序，将 adict={'c':3,'d':1,'i':2,'t':4} 升序排序的方法是？
      A. alist.sort(key=lambda s:s[-1],reverse=1)
      B. alist.sort(key=lambda s:s[-1])
      C. alist=list(adict.items())
      D. adict=dict(alist)
    请选多个正确答案:''' % num)
    num=topic(num,'CBD')

    taking = raw_input(r'''%s.python模块安装有在线安装和本地安装，使用国内镜像站点在线安装需配置哪个文件？
      A. /.pip/pip.conf
      B. ~/.pip/pip.conf
      C. /etc/pip.conf
      D. /etc/.pip/pip.conf
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.关于数据库范式下面说法正确的是？
      A. 第一范式指数据库表的每一列都是不可分割的原子数据项；
      B. 第二范式指满足第一范式且每行记录都要有主键；
      C. 第三范式指所有非主属性，不能依赖其他非主属性；
      D. 第五范式指的是非关系型数据库达到的最理想状态。
    请选多个正确答案:''' % num)
    num=topic(num,'ABC')

    taking = raw_input(r'''%s.python连接关系型数据库有下面哪些模块？
      A. sqlalchemy.orm
      B. PyMySQL
      C. sqlalchemy
      D. sqlalchemy.ext.declarative
    请多选择正确答案:''' % num)
    num=topic(num,'BC')

    taking = raw_input(r'''%s.sqlalchemy使用ORM只需要熟数据库工作原理不用编写SQL语句就可以连接各种关系型数据库，下面说法正确的是？
      A. 将数据中的表和一个python的class关联
      B. 表中的字段和class的类变量关联
      C. 数据类型和sqlalchemy的类关联
      D. 表中的一行记录与类的一个实例关联
    请选多个正确答案:''' % num)
    num=topic(num,'ABCD')

    taking = raw_input(r'''%s.python中使用正则表达式匹配字符串，如果匹配到内容，能返回匹配内容的是？
      A. re.match()
      B. re.group()
      C. re.compile()
      D. re.finditer()
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.sqlalchemy通过哪种方法创建会话类？
      A. Base = declarative_base()
      B. Session = sessionmaker(bind=engin)
      C. Base.metadata.create_all(engin)
      D. engin = create_engine( )
    请选择正确答案:''' % num)
    num=topic(num,'B')

    taking = raw_input(r'''%s.pymysql通过哪种方法创建到数据的连接？
      A. conn = pymysql.connect()
      B. cur = conn.cursor()
      C. cur.execute()
      D. conn.commit()
    请选择正确答案:''' % num)
    num=topic(num,'A')

except (KeyboardInterrupt, EOFError):
    print('\n\033[35;1mBye-bye,不服欢迎回来再战。\033[0m')
    exit(2)