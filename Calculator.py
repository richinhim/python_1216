#coding:euc-kr

from  tkinter import *

def update_add():
    print("���ϱ�")

def update_substract():
    print("����")

def update_init():
    print("�ʱ�ȭ")


window = Tk()

label = Label(window, text="���� �հ�:")

label.pack()

add_button = Button(window, text="���ϱ�(+)", command=update_add)

subs_button = Button(window, text="����(+)", command=update_substract)

init_button = Button(window, text="�ʱ�ȭ(+)", command=update_init)

add_button.pack()
subs_button.pack()
init_button.pack()

window.mainloop()