
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
# from typing_extensions import Self
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
from Srudent import Student
from main import Face_Recognition_System
# from studentdetailpage import Student



import mysql.connector


class student_login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\bipin\Desktop\Python-Face\Images\back.jfif")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=115,y=110)

        # lable
        username=lbl=Label(frame,text="Email Address",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        

        password=lbl=Label(frame,text="Date Of Birth",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # #========Icon Image==========
        # img2=Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\user-gfec30f9d9_1920.png")
        # img2=img2.resize((25,25),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        # lblimg1.place(x=650,y=323,width=25,height=25)


        # img3=Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\castle-gab5402b80_1920.jpg")
        # img3=img3.resize((25,25),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lblimg1.place(x=650,y=395,width=25,height=25)

        #login button
        loginbtn=Button(frame,command=self.student_login,text="Login",font=("times now roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
         
    #     #registerbutton
    #     regiterbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
    #     loginbtn.place(x=15,y=350,width=160)
        
    #     #forgetpasswordbtn

        # forgotbtn=Button(frame,text="forget password",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        # forgotbtn.place(x=100,y=370,width=160)
        
        
    def student_login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field Required")
        else:
            try:
                
                conn = mysql.connector.connect(host="localhost",username="root",password="Bipinlm@10",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where Email=%s and DOB=%s",(self.txtuser.get(),self.txtpass.get()))
                row = my_cursor.fetchone()
                # print(self.txtuser.get())
                
                if row==None:
                    messagebox.showerror("Error","Invalid Email and Date of birth",parent=self.root)
                else:
                    from StudLoggedPage import Student
                    self.new_window = Toplevel(self.root)
                    self.app = Student(self.new_window,self.txtuser,self.txtpass)
                    

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        
    

if __name__ == "__main__":
    root=Tk()
    app=student_login_window(root)
    root.mainloop()       