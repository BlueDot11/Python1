from tkinter import*
screen=None
def buttonPush():
    print ("Button pushed!")
    global screen
    screen.destroy()

def buttonSave():
    #print("Saved successifully")
    tBox=None
    


def main():
    global screen
screen=Tk()
screen.title("Donald Gui")
screen.geometry('450x500')
w=Label(screen,text="Donald Maisiba")
w.pack()
but1=Button(screen,text="Exit",command=buttonPush)
but1.pack()
but2=Button(screen,text="Save",command=buttonSave)
but2.pack()
tBox=Entry(screen)
tBox.pack()

hello=Menu()
menubar=Menu(screen)
filemenu=Menu(menubar)
filemenu.add_command(label="Open" ,command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=screen.destroy)
menubar.add_cascade(label="File",menu=filemenu)
screen.config(menu=menubar)

helloMenu = Menu(menubar)
helloMenu.add_command(label="Say hello", command=hello)
menubar.add_cascade(label="Hello", menu=helloMenu)

subHello = Menu(helloMenu) 
subHello.add_command(label="English", command=hello)
subHello.add_command(label="Spanish", command=hello)
subHello.add_command(label="Chinese", command=hello)
subHello.add_command(label="French", command=hello)







screen.mainloop()
