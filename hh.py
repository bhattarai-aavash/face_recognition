from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
# from typing_extensions import Self
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
from Srudent import Student
from main import Face_Recognition_System
# from studentdetailpage import Student

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        username=lbl=Label(frame,text="Email Address",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        

        password=lbl=Label(frame,text="Date Of Birth",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #login button
        loginbtn=Button(frame,command=self.student_loginn,text="Login",font=("times now roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

class hello(student):
        def student_loginn(self):
            print(std.txtuser.get())
            pass

def student_login():
        return student(Tk())
    
std = student_login()
# print(std.txtuser.get())





if __name__ == "__main__":
    root=Tk()
    app=student(root)
    root.mainloop()  
        

        