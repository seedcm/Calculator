#!/usr/bin/python

#_*_ codeing : utf-8 _*_

'''

created on 2017-10-26

@author : seedcm

'''
from tkinter import *
from tkinter import messagebox
import time
temp = []
num = ''
fnum = ''
def update():
	tm = time.strftime("%Y-%m-%d %H:%M:%S")
	tml.configure(text=tm)
	tml.after(1000,update)
def show():
	num = ''.join(temp)
	lb['text'] = num
def count():
	num = ''.join(temp)
	try:
		fnum = eval(num)
	except ZeroDivisionError as e:
		fnum = 0
		lb['text'] = fnum
	except SyntaxError as e:
		fnum = 0
		lb['text'] = '公式错误！'
	while True:
		if len(temp) == 0:
			break
		else:
			temp.pop()
	temp.append(str(fnum))
	lb['text'] = fnum
def AC():
	while True:
		if len(temp) == 0:
			break
		else:
			temp.pop()
			lb['text'] = '已重置'
def C():
	if len(temp) == 0:
		lb['text'] = 0
	else:
		temp.pop()
		lb['font'] = ('yahei',32,'bold')
		lb['text'] = temp
def add0():
	temp.append('0')
	show()
def add00():
	temp.append('00')
	show()
def add1():
	temp.append('1')
	show()
def add2():
	temp.append('2')
	show()
def add3():
	temp.append('3')
	show()
def add4():
	temp.append('4')
	show()
def add5():
	temp.append('5')
	show()
def add6():
	temp.append('6')
	show()
def add7():
	temp.append('7')
	show()
def add8():
	temp.append('8')
	show()
def add9():
	temp.append('9')
	show()
def dot():
	temp.append('.')
	show()
def l_kuohao():
	temp.append('(')
	show()
def r_kuohao():
	temp.append(')')
	show()
def jia():
	temp.append('+')
	show()
def jian():
	temp.append('-')
	show()
def cheng():
	temp.append('*')
	show()
def chu():
	temp.append('/')
	show()
def baifenhao():
	temp.append('%')
	show()

main = Tk()
main.title('计算器')
main.geometry('320x210')
main.resizable(False,False)
lb = Label(main,text="0",font=('yahei',32,'bold'),bg='white',width=20)
lb.pack(padx=5,pady=2)
cent = Frame(main).pack()
tp2 = Frame(main)
tp2.pack(side=TOP)
tp = Frame(main)
tp.pack(side=TOP)
lf = Frame(cent)
lf.pack(side=LEFT,padx=3)
rf = Frame(cent)
rf.pack(side=RIGHT,padx=3)
tml = Label(tp2,text='',font=('yahei'))
tml.grid(row=0,column=0)
b = Button(lf,text='7',font=('yahei',16,'bold'),width=3,command=add7).grid(row=0,column=0)
b = Button(lf,text='8',font=('yahei',16,'bold'),width=3,command=add8).grid(row=0,column=1)
b = Button(lf,text='9',font=('yahei',16,'bold'),width=3,command=add9).grid(row=0,column=2)
b = Button(lf,text='4',font=('yahei',16,'bold'),width=3,command=add4).grid(row=1,column=0)
b = Button(lf,text='5',font=('yahei',16,'bold'),width=3,command=add5).grid(row=1,column=1)
b = Button(lf,text='6',font=('yahei',16,'bold'),width=3,command=add6).grid(row=1,column=2)
b = Button(lf,text='1',font=('yahei',16,'bold'),width=3,command=add1).grid(row=2,column=0)
b = Button(lf,text='2',font=('yahei',16,'bold'),width=3,command=add2).grid(row=2,column=1)
b = Button(lf,text='3',font=('yahei',16,'bold'),width=3,command=add3).grid(row=2,column=2)
b = Button(lf,text='0',font=('yahei',16,'bold'),width=3,command=add0).grid(row=3,column=0)
b = Button(lf,text='.',font=('yahei',16,'bold'),width=3,command=dot).grid(row=3,column=1)
b = Button(lf,text='%',font=('yahei',16,'bold'),width=3,command=baifenhao).grid(row=3,column=2)
b = Button(rf,text='/',font=('yahei',16,'bold'),width=3,command=chu).grid(row=0,column=0)
b = Button(rf,text='x',font=('yahei',16,'bold'),width=3,command=cheng).grid(row=1,column=0)
b = Button(rf,text='-',font=('yahei',16,'bold'),width=3,command=jian).grid(row=2,column=0)
b = Button(rf,text='+',font=('yahei',16,'bold'),width=3,command=jia).grid(row=3,column=0)
b = Button(rf,text='C',font=('yahei',16,'bold'),width=3,command=C).grid(row=0,column=1)
b = Button(rf,text='(',font=('yahei',16,'bold'),width=3,command=l_kuohao).grid(row=1,column=1)
b = Button(rf,text=')',font=('yahei',16,'bold'),width=3,command=r_kuohao).grid(row=2,column=1)
b = Button(rf,text='=',font=('yahei',16,'bold'),width=3,command=count).grid(row=3,column=1)
update()
main.mainloop()

