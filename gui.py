from tkinter import *

root=Tk()

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
print(screen_height,screen_width)

ls="#e6ff99"
win="#f2ffcc"
root.geometry(f"{screen_width}x{screen_height}")
root.title("GUI")
root.iconbitmap("./components/editor.ico")
upload=PhotoImage(file="./components/Upload.png")
rm_bg=PhotoImage(file="./components/rm_bg.png")

f1=Frame(root,bg=ls,width=500)
f1.pack(side=RIGHT,fill=Y)
f2=Frame(root,bg=win,height=750)
f2.pack(side=TOP,fill=X)
f3=Frame(root,bg="green",height=450)
f3.pack(side=BOTTOM,fill=X)
b1=Button(f2,image=upload)
b1.pack()
b2=Button(f3,image=rm_bg)
b2.grid(row=0,column=0,)
root.mainloop()