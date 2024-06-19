from tkinter import *

screen=Tk()
screen.geometry("400x500")
abc=PhotoImage(file='1.png')
label1=Label(screen,image=abc).place(x=100,y=50)
screen.mainloop()