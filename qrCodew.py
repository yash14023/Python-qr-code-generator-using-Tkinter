from tkinter import *
import qrcode
from PIL import Image, ImageTk 
from resizeimage import resizeimage #something worng with dis module

#firstoffall i created a class to keep the code clean
class Qr_Generator:
    def __init__(self,root): 
        self.root =root
        self.root.geometry("990x500+200+50") #to set the height
        self.root.title("CA2 QR CODE | 21BIT009") #title
        self.root.resizable(False,False) #to block the screen we cant minimize 

        #--------------------------------------Heading of page---------------------------------------------------------------
        title=Label(self.root,text= "Qr  Code Genrator | 21BIT009", font=("times new roman",40),bg='black',foreground='white' ).place(x=0, y=0,relwidth=1)

        #----------------------------heading-----frame------------------
        stu_Frame = Frame(self.root,bd=2,relief=RIDGE, bg='white') 
        stu_Frame.place(x=50, y=100, width=500,height=395)

        stu_title=Label(stu_Frame,text= "Student details", font=("goudy old style",25),bg='black',foreground='white' ).place(x=0, y=0,relwidth=1)
        #------------------------manage the value----------------------------------------
        self.var_stu_code = StringVar()
        self.var_stu_name = StringVar()
        self.var_stu_uid = StringVar()
        self.var_stu_department = StringVar()
        # -----------------details-------------------
        lbl_stu_code =Label(stu_Frame,text= "Student Id", font=("times new roman",15 ,'bold'),bg='white').place(x=10,y=60)
        lbl_stu_name =Label(stu_Frame,text= "Student Name", font=("times new roman",15 ,'bold'),bg='white').place(x=10,y=120)
        lbl_stu_uid =Label(stu_Frame,text= "UID", font=("times new roman",15 ,'bold'),bg='white').place(x=10,y=240)
        lbl_stu_department =Label(stu_Frame,text= "Department", font=("times new roman",15 ,'bold'),bg='white').place(x=10,y=180)

        #------------------Input using entry-----------------------
        txt_stu_code =Entry(stu_Frame, font=("times new roman",15),text=self.var_stu_code,bg='lightyellow').place(x=200,y=60)
        txt_stu_name =Entry(stu_Frame, font=("times new roman",15),text=self.var_stu_name,bg='lightyellow').place(x=200,y=120)
        txt_stu_uid =Entry(stu_Frame, font=("times new roman",15),bg='lightyellow',text=self.var_stu_uid).place(x=200,y=240)
        txt_stu_department =Entry(stu_Frame, font=("times new roman",15),bg='lightyellow',text=self.var_stu_department).place(x=200,y=180)
        #-------------------button---------------------------
        btn_generate=Button(stu_Frame, text='Genrate',command=self.generate, font=('times new roman',18,'bold'),bg='black', foreground='white').place(x=50,y=300,width=200,height=30)
        btn_clear=Button(stu_Frame, text='Clear', command=self.clear,font=('times new roman',18,'bold'),bg='black', foreground='white').place(x=260,y=300,width=100,height=30)
        
        #----------------------displaymsg----------------------
        self.msg=''
        self.lbl_msg=Label(stu_Frame,text= self.msg, font=("times new roman",15 ,'bold'),bg='white', foreground='blue')
        self.lbl_msg.place(x=0,y=355,relwidth= 1)

        #--------------------qrframe  frame2-----------------------------
        qr_Frame = Frame(self.root,bd=2,relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=290,height=395)  
        qr_title=Label(qr_Frame,text= "Student Qr Code", font=("goudy old style",25),bg='black',foreground='white',bd=1, relief=RIDGE ).place(x=0, y=0,relwidth=1)
        #------------------------default----------------------
        self.qr_code=Label(qr_Frame,text='Qr code \n not Available', font=('times new roman',15), bg='black',foreground='white')
        self.qr_code.place(x=50, y=100,width=180,height=180)

        #-------------------------Functios for validation------------------
    def generate(self):
        #------------------------if conition for validating form-----------------------------
        if self.var_stu_code.get() == '' or  self.var_stu_name.get() == '' or  self.var_stu_uid == '' or self.var_stu_department  =='':
           self.msg='*All feilds are required'
           self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Student id:{self.var_stu_code.get()} \nStudent name:{self.var_stu_name.get()} \nStudent Department:{self.var_stu_department.get()} \nStudent UID{self.var_stu_uid.get()}") 
            qr_code=qrcode.make(qr_data) #callig make funtion to get the data and MAKE QR CODE 
           
           
           
            ################################################
            #--------------Resizing the image--------------#
            qr_code=resizeimage.resize_cover(qr_code,[150,180])
            ################################################
            #-----------------SAVING THE QR----------------#
            qr_code.save("student_qr/stu"+  str(self.var_stu_code.get())+'.png')
          
            #----------------qr img updateeee-------------------
            self.im=ImageTk.PhotoImage(file="student_qr/stu"+  str(self.var_stu_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #------dynamic upadting---------
            self.msg='Qr Generated successfully!!'
            self.lbl_msg.config(text=self.msg,fg='blue')
    #-----------------------------------function for clear-------------------
    def clear(self):
        self.var_stu_code.set('')
        self.var_stu_name.set('')
        self.var_stu_uid.set('')
        self.var_stu_department.set('')


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
