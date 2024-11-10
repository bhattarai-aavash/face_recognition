from email import message_from_binary_file
from logging import root
from msilib.schema import RadioButton
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2









class Training:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  #setting windows screen size
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="Train Dataset",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


if __name__=="__main__":
    root = Tk()
    obj = Training(root)
    root.mainloop()