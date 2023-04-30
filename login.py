from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem   
                            
class Login_Window:
     def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"D:\HTML\login.jpeg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1, relheight=1)
        frame=Frame(self.root, bg="black")
        frame.place(x=610,y=170,width=340, height=450)
        img1=Image.open("D:\HTML\logo.png")
        img1=img1. resize((198, 100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg= "black" ,borderwidth=0)
        lblimg1.place(x=730,y=175,width=100, height=80)
        get_str=Label(frame,text="Get Started",font=("times new roman",20, "bold"),fg="white",bg="black")
        get_str.place(x=95,y=75)
        # label
        username=lbl=Label(frame, text= "Username" ,font=("times new roman",15, "bold") ,fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame, text= "Password" ,font=("times new roman",15, "bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15, "bold"))
        self.txtpass.place(x=40,y=260,width=270)
        
         # ======Icon Images==
        img2=Image.open(r"D:\HTML\login.jpeg")
        img2=img2. resize((100, 196),Image.ANTIALIAS) 
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"D:\HTML\login.jpeg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk. PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black" ,borderwidth=0)
        lblimg1.place(x=650,y=395,width=25, height=25)
         #login btn
        loginbtn=Button(frame,text="Login",font=("times new roman" ,15, "bold"),bd=3,relief=RIDGE, fg="white" ,bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        #register btn
        registerbtn=Button(frame,text= "Register",font=("times new roman" ,15, "bold"),borderwidth=0 ,bd=3,fg="white" ,bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=195,y=350,width=120,height=40)
        
        #forget password
        forgotbtn=Button(frame,text="Forgot Password",font=("times new roman" ,15, "bold"),borderwidth=0 ,bd=3,fg="white" ,bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=350,width=170,height=40) 
        
        
if __name__ == "__main__" : 
   root=Tk()
   app=Login_Window(root)
   root.mainloop()