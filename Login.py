from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

def submitButton():
    print("submitted automatically")
def exitButton():
    print("System exited successifully")
def clearButton():
    print("Details cleared")

mouse=Tk()
bg=("blue")
mouse.title("Login ")
mouse.geometry('270x300')
#messagebox.askquestion("confirm","Are you sure?")
Name=Label(mouse,text=" Name",padx=10,pady=11,font=('aerial',12,BOLD),fg="blue")
Name.grid(row=1,column=1)
Email=Label(mouse,text=" Email",padx=10,pady=11,font=('aerial',12,BOLD),fg="blue")
Email.grid(row=2,column=1)
Phone=Label(mouse,text="Phone",padx=10,pady=11,font=('aerial',12,BOLD),fg="blue")
Phone.grid(row=3,column=1)

tbox=Entry(mouse,bg="pink",font=('aerial',11))
tbox.grid(row=1,column=2)
tbox1=Entry(mouse,bg="pink",font=('aerial',11))
tbox1.grid(row=2,column=2)
tbox2=Entry(mouse,bg="pink",font=('aerial',11))
tbox2.grid(row=3,column=2)

btn1=Button(mouse,text="Submit",padx=10,pady=11,bg="green",fg="yellow",font=('aerial',12,BOLD),command=submitButton)
btn1.grid(row=4,column=2)

btn2=Button(mouse,text="Exit",padx=10,pady=11,bg="red",fg="yellow",font=('aerial',14,BOLD),command=exitButton)
btn2.grid(row=5,column=2)

btn3=Button(mouse,text="Clear",padx=10,pady=11,bg="red",fg="purple",font=('aerial',14,BOLD),command=clearButton)
btn3.grid(row=6,column=2)












mouse.mainloop() 
