import win32com.client as wincl
from tkinter import *

def speaking():
    text= str(entry.get())
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)
def enter(event):
    speaking()
    
root = Tk()
root.geometry("200x100")
frame = Frame(root, width=200, height=100, bg = "grey13")
root.configure(background="grey13")
root.title("reader")
label = Label(frame, text = "reader", bg = "grey13", fg = "white")
label.grid(row = 0, column = 2)
entry = Entry(frame, bg = "grey20", fg = "white")
entry.grid(row = 1, column = 1, columnspan = 3)
button1 = Button(frame, text = "speak", width = 7, command = speaking, bg = "grey20", fg = "white")
button1.grid(row = 3, column = 2)
frame.pack()
frame.focus_set()
root.mainloop()
