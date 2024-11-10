# from cProfile import label
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk
from Srudent import Student
import os
import numpy as np
import cv2
from face_recognition import FaceRecognizer
from attendance import Attendance





class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  #setting windows screen size
        self.root.title("Face Recognition System")

        #Adding Background Image
        img1 = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\background.jpg")
        img1 = img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image = self.photoimg1)
        bg_img.place(x=0,y=45,width=1530,height=710)

        #Title of the system
        title_lbl = Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student button
        stu_img = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\1.jpg")
        stu_img = stu_img.resize((200,220),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(stu_img)

        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=90,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=90,y=300,width=220,height=40)

        #Button for Detection face
        det_img = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\Recognition.jpg")
        det_img = det_img.resize((200,220),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(det_img)

        b1 = Button(bg_img,image=self.photoimg3,command=self.face_data,cursor="hand2")
        b1.place(x=350,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=350,y=300,width=220,height=40)

        #Button for attendance face
        att_img = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\attendance.jpg")
        att_img = att_img.resize((200,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(att_img)

        b1 = Button(bg_img,image=self.photoimg4,command = self.attendance,cursor="hand2")
        b1.place(x=610,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Attendance",cursor="hand2",command = self.attendance,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=610,y=300,width=220,height=40)

        #Button for Training faces
        Train_img = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\training.jpg")
        Train_img = Train_img.resize((200,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(Train_img)

        b1 = Button(bg_img,image=self.photoimg5,command=self.train_image,cursor="hand2")
        b1.place(x=90,y=400,width=220,height=220)

        b1_l = Button(bg_img,text="Training",cursor="hand2",command=self.train_image,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=90,y=620,width=220,height=40)

        #Button for Photos 
        Photo_image = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\Photos.jpg")
        Photo_image = Photo_image.resize((200,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(Photo_image)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=400,width=220,height=220)

        b1_l = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=350,y=620,width=220,height=40)

        Photo_image = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\exit.png")
        Photo_image = Photo_image.resize((200,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(Photo_image)

        b1 = Button(bg_img,image=self.photoimg7,command=root.quit,cursor="hand2")
        b1.place(x=610,y=400,width=220,height=220)

        b1_l = Button(bg_img,text="Exit",cursor="hand2",command=root.quit,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_l.place(x=610,y=620,width=220,height=40)


    def open_img(self):
        os.startfile("data")

        #########3 Function Buttons #############

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    ########## Training images LBPH algorithm ################
    def train_image(self):
        data_dir = "data"
        path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        
        for image in path:
            img= Image.open(image).convert('L')         ## Converting to grayscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        
        ########### Training classifier ##########3
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognizer(self.new_window)
    

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

 
    def quiting(self):
        self.new_window = Toplevel(self.root)
        self.app = starting_window(self.new_window)








if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
