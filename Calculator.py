#coding:euc-kr

from  tkinter import *

def update_add():
    print("더하기")

def update_substract():
    print("빼기")

def update_init():
    print("초기화")


window = Tk()

label = Label(window, text="현재 합계:")

label.pack()

add_button = Button(window, text="더하기(+)", command=update_add)

subs_button = Button(window, text="빼기(+)", command=update_substract)

init_button = Button(window, text="초기화(+)", command=update_init)

add_button.pack()
subs_button.pack()
init_button.pack()

window.mainloop()