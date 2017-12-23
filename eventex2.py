#coding:euc-kr

from  tkinter import *

def greet():
    print("파이썬에 오신 것을 환영합니다.")


window = Tk()

label = Label(window, text="간단한 GUI프로그램!")

label.pack()

greet_button = Button(window, text="클릭하세요!.", command=greet)
close_button = Button(window, text="종료.", command=window.quit)

greet_button.pack()
close_button.pack()

window.mainloop()

