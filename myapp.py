from tkinter import *
w=Tk()

w.configure(bg="#5c8a8a")
w.geometry("400x220")
w.title("MyApp")
w.resizable(FALSE,FALSE)

photo=PhotoImage(file="icon.png")
w.iconphoto(False,photo)

f1=Frame(w)
f1.configure(bg="#476b6b",highlightbackground="black",highlightcolor="black",highlightthickness=1)
f1.grid(row=0,column=0,padx=10,pady=10,ipadx=190,ipady=50)
f1.grid_propagate(0)

e=Entry(f1,font=(10),borderwidth=2,bg="#5c8a8a")
e.grid(row=0,column=0,padx=35,pady=20,ipadx=40,ipady=3)
e.configure(highlightcolor="black",highlightthickness=2)
joinbtn=Button(f1,text="Join",bg="#009900",fg="white",padx=15,pady=3)
joinbtn.place(x=160,y=65)

f2=Frame(w)
f2.configure(bg="#5c8a8a")
f2.grid(row=1,column=0,ipadx=150,ipady=40)
f2.grid_propagate(0)

cambtn=Button(f2,text="Camera",fg="white",bg="#cc7a00",padx=20,pady=3)
cambtn.place(x=10,y=10)
audbtn=Button(f2,text="Audio",fg="white",bg="#cc7a00",padx=23,pady=3)
audbtn.place(x=200,y=10)
sharebtn=Button(f2,text="Share",fg="white",bg="#cc7a00",padx=25,pady=3)
sharebtn.place(x=10,y=50)
leavebtn=Button(f2,text="Leave",fg="white",bg="#cc7a00",padx=23,pady=3)
leavebtn.place(x=200,y=50)

w.mainloop()