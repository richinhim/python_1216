#coding: euc-kr
from tkinter import *

root = Tk()

lbl = Label(root, text ="����")
lbl.pack() #pack- ��ġ������

txt = Entry(root)

txt.pack()

btn = Button(root, text="OK")


btn.pack()

root.mainloop()
