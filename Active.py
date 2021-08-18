from tkinter import *
wd=Tk()
wd.title("Donald GUI")
text_Input=StringVar()
wd.geometry("400x300")
Username=Label(wd,text="Username").place(x=30,y=50)
Username=StringVar()
password=Label(wd,text="password").place(x=30,y=90)
Email=Label(wd,text="Email").place(x=30,y=130)
b=Button(wd,text="Login").place(x=30,y=170)
r=Button(wd,text="Reset").place(x=100,y=170)





txtDisplay=Entry(wd,textvariable=text_Input,insertwidth=5,justify="left",bg="purple",).pack()

    



wd.mainloop()
