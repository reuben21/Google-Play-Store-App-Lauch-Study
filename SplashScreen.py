import tkinter as tk
from tkinter import PhotoImage,Label


def splashscreen():
	root=tk.Tk()
	w=900
	h=500
	ws=root.winfo_screenwidth()
	hs=root.winfo_screenheight()
	x=(ws/2)-(w/2)
	y=(hs/2)-(h/2)
	root.geometry("%dx%d+%d+%d"%(w,h,x,y))
	root.overrideredirect(1)
	photo=PhotoImage(file="C:\\InternshipFinal\\splashscreen.jpeg")
	l1=Label(root,image=photo)
	l1.place(x=0,y=0)
	root.after(4000,root.destroy)
	root.mainloop()
splashscreen()

