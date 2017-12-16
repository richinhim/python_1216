#coding: euc-kr
from tkinter import *

root = Tk()

lbl = Label(root, text ="성명")
lbl.pack() #pack- 배치관리자


lbl.grid(row = 0, column=200)

txt = Entry(root)

txt.grid(row = 0, column=1)

btn = Button(root, text="OK")

btn.grid(row = 1, column=1)

root.mainloop()
