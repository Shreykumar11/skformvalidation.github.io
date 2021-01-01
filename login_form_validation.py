from tkinter import *
from tkinter import messagebox

class form:
    def __init__(self):
        self.main()
        
    def fun1(self):
        self.lbl.destroy()
        self.f2=Frame(self.root, width=250, height=400, bg="red", relief=SUNKEN)
        self.f2.pack(padx=10, pady=25)

        self.l1=Label(self.f2, text="LOGIN", fg="white", bg="red", font="Cambria 28 bold underline")
        self.l1.place(x=70, y=30)
    
        self.l2=Label(self.f2, text="EMAIL", fg="white", bg="red", font="Cambria 14 bold")
        self.l2.place(x=30, y=110)
        self.e1=Entry(self.f2, textvariable=self.s1, bg="cyan", width=30)
        self.e1.place(x=30, y=160)
    
        self.l3=Label(self.f2, text="PASSWORD", fg="white", bg="red", font="Cambria 14 bold")
        self.l3.place(x=30, y=210)
        self.e2=Entry(self.f2, textvariable=self.s2, bg="cyan", width=30)
        self.e2.place(x=30, y=260)

        self.b1=Button(self.f2, text="SUBMIT", fg="white", bg="green", command=self.submit)
        self.b1.place(x=100, y=320)

    def fun3(self):
        self.lbl.destroy()
        self.f2.destroy()
        self.f4=Frame(self.root, width=400, height=400, relief=SUNKEN)
        self.f4.pack(padx=10, pady=25)

        self.K="*\nIT IS A FORM VALIDATION \nUSING PYTHON GUI INTERFACE. \n\nIT INCLUDES FRAMES, LABELS, \nENTRIES, BUTTONS, "
        self.M="MENU \nBUTTON, AND MESSAGE BOX.\n*"

        self.l1=Label(self.f4, text=self.K+self.M, fg="purple", font="Cambria 20 bold")
        self.l1.place(x=5, y=30)
    
    def fun4(self):
        self.lbl.destroy()
        self.f2.destroy()
        self.f4.destroy()
        self.f5=Frame(self.root, width=400, height=400, relief=SUNKEN)
        self.f5.pack(padx=10, pady=25)

        self.l1=Label(self.f5, text="CONTACT", fg="blue", font="Cambria 28 bold underline")
        self.l1.place(x=100, y=30)
    
        self.l2=Label(self.f5, text="SHREY kUMAR SAXENA \n\n skshrey11@gmail.com", fg="blue", font="Cambria 24 bold")
        self.l2.place(x=30, y=110)

    def fun5(self):
        self.f1.destroy()
        self.root.destroy()

    def submit(self):
        dict1={'skshrey11@gmail.com': '123', 'suman123@gmail.com': 'suman'}
        d1={}
        a=self.s1.get()
        b=self.s2.get()
        d1[a]=b
        for i in d1:
            if i in dict1:
                self.f2.destroy()
                self.f6=Frame(self.root, width=400, height=400, relief=SUNKEN)
                self.f6.pack(padx=10, pady=25)

                self.l1=Label(self.f6, text="WELCOME \nTO \nSHREY'S WINDOW...", fg="blue", font="Cambria 28 bold")
                self.l1.place(x=70, y=30)

                self.b1=Button(self.f6, text="LOGOUT", fg="white", bg="red", command=self.logout)
                self.b1.place(x=200, y=320)

            else:
                messagebox.showinfo("WARNING", "WRONG PASSWORD !!")

        self.s1.set("")
        self.s2.set("")

    def logout(self):
        self.f6.destroy()
        self.fun1()

    def main(self):
        self.root=Tk()
        self.root.title("WINDOW")
        self.root.geometry("500x500")

        self.f1=Frame(self.root, relief=RAISED, borderwidth=3, bg="yellow")
        self.f1.pack(fill="x")

        self.s1=StringVar()
        self.s1.set("")
        self.s2=StringVar()
        self.s2.set("")

        self.lbl=Label(self.root, text="HAPPY MORNING, \n INDIA !!", fg="gold", bg="brown", font="Cambria 28 bold")
        self.lbl.place(x=100, y=200)

        self.mb1=Menubutton(self.f1, text="Home", relief=RAISED)
        self.mb2=Menubutton(self.f1, text="About Us", relief=RAISED)
        self.mb3=Menubutton(self.f1, text="Exit", relief=RAISED, bg="red", fg="white")
        self.mb1.menu=Menu(self.mb1, tearoff=0)
        self.mb2.menu=Menu(self.mb2, tearoff=0)
        self.mb3.menu=Menu(self.mb3, tearoff=0)

        self.mb1["menu"]=self.mb1.menu
        self.mb2["menu"]=self.mb2.menu
        self.mb3["menu"]=self.mb3.menu

        self.mb1.menu.add_command(label="LOGIN", command=self.fun1)
        self.mb2.menu.add_command(label="INTRO", command=self.fun3)
        self.mb2.menu.add_command(label="CONTACT US", command=self.fun4)
        self.mb3.menu.add_command(label="EXIT", command=self.fun5)

        self.mb1.pack(side="left")
        self.mb2.pack(side="left")
        self.mb3.pack(side="right")

        self.root.mainloop()

A=form()




