from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
from login import login_window
from studentlogin import student_login_window

class starting_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\bipin\Desktop\Python-Face\Images\background-gc98bc0bf0_1920.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        title_lbl = Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img1=Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Button(self.root,image=self.photoimage1,command=self.admin_log_page,bg="white",borderwidth=0,cursor="hand2")
        lblimg1.place(x=850,y=300,width=200,height=100)

        Adminloginbtn=Button(self.root,text="Admin Login",command=self.admin_log_page,font=("times now roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",cursor="hand2")
        Adminloginbtn.place(x=850,y=410,width=200,height=50)

        
        img2=Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\[Downloader.la]-622b4d11b2f3e.jpg")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Button(self.root,image=self.photoimage2,command = self.student_login,bg="white",borderwidth=0,cursor="hand2")
        lblimg2.place(x=400,y=300,width=200,height=100)



        Studentloginbtn=Button(self.root,text="Student Login",command=self.student_login,font=("times now roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",cursor="hand2")
        Studentloginbtn.place(x=400,y=410,width=200,height=50)


    def admin_log_page(self):
        self.new_window = Toplevel(self.root)
        self.app = login_window(self.new_window)

    def student_login(self):
        self.new_window = Toplevel(self.root)
        self.app = student_login_window(self.new_window)

        

if __name__ == "__main__":
    root=Tk()
    app=starting_window(root)
    root.mainloop()       