#coding:euc-kr

from  tkinter import *

def greet():
    print("���̽㿡 ���� ���� ȯ���մϴ�.")


window = Tk()

label = Label(window, text="������ GUI���α׷�!")

label.pack()

greet_button = Button(window, text="Ŭ���ϼ���!.", command=greet)
close_button = Button(window, text="����.", command=window.quit)

greet_button.pack()
close_button.pack()

window.mainloop()

