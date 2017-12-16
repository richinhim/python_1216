#coding: euc-kr
from tkinter import *

root = Tk()

lbl = Label(root, text ="성명")
lbl.pack() #pack- 배치관리자

txt = Entry(root)

txt.pack()

btn = Button(root, text="OK")


btn.pack()

root.mainloop()
