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
from tkinter import filedialog
import os
import csv







mydata = []


class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  #setting windows screen size
        self.root.title("Face Recognition System")

        ##########33 VAriables #########3
        self.var_atten_id = StringVar()
        self.roll_id = StringVar()
        self.name_id = StringVar()
        self.dep_id = StringVar()
        self.time_id = StringVar()
        self.data_id = StringVar()
        self.attendance_id = StringVar()


        title_lbl = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img1 = Image.open(r"C:\Users\bipin\Desktop\Python-Face\Images\background.jpg")
        img1 = img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image = self.photoimg1)
        bg_img.place(x=0,y=45,width=1530,height=710)

        #Making Frame
        main_fame = Frame(bg_img,bd=2,bg="white")
        main_fame.place(x=10,y=10,width=1530,height=710)

        
        #left side label frame
        Left_frame = LabelFrame(main_fame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=680) 

        left_inside_fame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_fame.place(x=5,y=10,width=745,height=630)

        #Labels and Entry
        #student ID
        attendance_id_label = Label(left_inside_fame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        name_id_label = Label(left_inside_fame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_id_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        nameID_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.name_id,font=("times new roman",13,"bold"))
        nameID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        Rollnumber_id_label = Label(left_inside_fame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        Rollnumber_id_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        RollnumberID_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.roll_id,font=("times new roman",13,"bold"))
        RollnumberID_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        department_label = Label(left_inside_fame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.dep_id,font=("times new roman",13,"bold"))
        department_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        time_id_label = Label(left_inside_fame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_id_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        timeID_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.time_id,font=("times new roman",13,"bold"))
        timeID_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        date_id_label = Label(left_inside_fame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_id_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        dateID_entry=ttk.Entry(left_inside_fame,width=20,textvariable=self.data_id,font=("times new roman",13,"bold"))
        dateID_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        attendancestatusLabel = Label(left_inside_fame,text = "Attendance Status",font=("times new roman",12,"bold"),bg = "white")
        attendancestatusLabel.grid(row=6,column=0)

        self.atten_status = ttk.Combobox(left_inside_fame,width=20,textvariable=self.attendance_id,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row = 6,column=1,pady = 8)
        self.atten_status.current(0)


        btn_frame = Frame(left_inside_fame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=735,height=200)

        #Save Button
        save_btn = Button(btn_frame,text="Import CSV",command=self.importCsv,width=70,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        #Update Button
        update_btn = Button(btn_frame,text="Export CSV",command=self.exportCsv,width=70,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0,padx=5,pady=5)

        #Delete Button
        delete_btn = Button(btn_frame,text="Update",width=70,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=2,column=0,padx=5,pady=5)

        #Delete Button
        reset_btn = Button(btn_frame,text="Reset",width=70,command = self.reset_data,font=("times new roman",13,"bold"),bg="red",fg="white")
        reset_btn.grid(row=3,column=0,padx=5,pady=5)


        

        


         #right side label frame
        right_frame = LabelFrame(main_fame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=710,height=680) 

        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=500)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column= ("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill=Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command= self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getCursor)


        #### fetch data ###
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    ##CSV file lai import gareko 
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    ##Export garna ko lagi

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","NO Data found to export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title = "Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)

            with open(fln,mode = "w", newline="") as myFile:
                exp_write = csv.writer(myFile,delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your data has been successfully exported to"+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    def getCursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.roll_id.set(rows[1])
        self.name_id.set(rows[2])
        self.dep_id.set(rows[3])
        self.time_id.set(rows[4])
        self.data_id.set(rows[5])
        self.attendance_id.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.roll_id.set("")
        self.name_id.set("")
        self.dep_id.set("")
        self.time_id.set("")
        self.data_id.set("")
        self.attendance_id.set("")




if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()