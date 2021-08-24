from tkinter import *
from tkinter.font import BOLD
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=" "
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=" "

Calculator=Tk()
Calculator.minsize(width=340,height=500)
Calculator.maxsize(width=320,height=500)
Calculator.title("calculator")
operator=" "
text_Input=StringVar()

txtDisplay=Entry(Calculator,font=('arial',18,BOLD),textvariable=text_Input,bd=30,insertwidth=4,bg="blue",justify="right").grid(columnspan=4)

btn7=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)

#-----------------------------------------------------------------------------------------
btn4=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)
    
btn5=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)

subtraction=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)

#------------------------------------------------------------------------------------------------------
btn1=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)
    
btn2=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)

Multply=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)

#---------------------------------------------------------------------------------------
btn0=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)
    
btnClear=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="C",bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="=",bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(Calculator,padx=16,pady=16,bd=8,fg="black",font=('arial',20,BOLD),
    text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)


Calculator.mainloop()