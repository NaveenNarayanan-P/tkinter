from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

class application:
    def __init__(self,parent):
        self.parent = parent
        self.ui_frame()         #Parent Window
        self.ui_topframe()      #Top menu Frames
        

#-------------------------------------------------------------------------------------------------------------------------------------------------->
    def save_process(self):             #>>>>>>>Save Process<<<<<<<<<<#
        self.id=self.en_id.get()
        self.name=self.en_name.get()
        self.cname=self.en_cn_name.get()
        self.dnost=self.en_drno_st.get()
        self.area=self.en_area.get()
        self.dis=self.en_dis.get()
        self.pin=self.en_pin.get()
        self.lm=self.en_lm.get()
        self.phno1=self.en_phno1.get()
        self.phno2=self.en_phno2.get()
        self.email=self.en_email.get()
        self.gstno=self.en_gst_no.get()
        self.actv=self.var.get()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>validations
        if(self.name==""):
            self.en_name.configure(highlightbackground="red")
            self.v_name=Label(self.new_frame,image=self.alert_img,text="Enter Name",fg="red",compound="left").place(x=70,y=80)
            
        else:
            self.en_name.configure(highlightbackground="black")
            self.v_name=Label(self.new_frame,text="                                   ",fg="red").place(x=70,y=82)
        if(self.cname==""):
            self.en_cn_name.configure(highlightbackground="red")
            self.v_cname=Label(self.new_frame,image=self.alert_img,text="Enter Contact name ",fg="red",compound="left").place(x=360,y=80)
            
        else:
            self.en_cn_name.configure(highlightbackground="black")
            self.v_cname=Label(self.new_frame,text="                                                        ",fg="red").place(x=360,y=82)    
        if((self.dnost=="")or(self.area=="")or(self.dis=="")or(self.lm=="")or(self.pin=="")):
            self.v_address=Label(self.new_frame,image=self.alert_img,text="Fill all the Address Fields",fg="red",compound="left").place(x=105,y=140)
            self.en_drno_st.configure(highlightbackground="red")
            self.en_area.configure(highlightbackground="red")
            self.en_dis.configure(highlightbackground="red")
            self.en_lm.configure(highlightbackground="red")
            self.en_pin.configure(highlightbackground="red")
        else:
            self.v_address=Label(self.new_frame,text="                                                    ").place(x=105,y=142)
            self.en_drno_st.configure(highlightbackground="black")
            self.en_area.configure(highlightbackground="black")
            self.en_dis.configure(highlightbackground="black")
            self.en_lm.configure(highlightbackground="black")
            self.en_pin.configure(highlightbackground="black")
        
        if((self.phno1=="")or(self.phno2=="")or(self.email=="")):
            self.v_contact=Label(self.new_frame,image=self.alert_img,text="Fill all the Contact Fields",fg="red",compound="left").place(x=180,y=372)
            self.en_phno1.configure(highlightbackground="red")
            self.en_phno2.configure(highlightbackground="red")
            self.en_email.configure(highlightbackground="red")

        else:
            self.v_contact=Label(self.new_frame,text="                                                   ").place(x=180,y=374)
            self.en_phno1.configure(highlightbackground="black")
            self.en_phno2.configure(highlightbackground="black")
            self.en_email.configure(highlightbackground="black")
        if(self.gstno==""):
            self.en_gst_no.configure(highlightbackground="red")
            self.v_gst=Label(self.new_frame,image=self.alert_img,text="Enter Gst Number",fg="red",compound="left").place(x=115,y=508)
            
        else:
            self.en_gst_no.configure(highlightbackground="black")
            self.v_gst=Label(self.new_frame,text="                                   ").place(x=70,y=82)
        


        
        if((self.id=="")or(self.name=="")or(self.cname=="")or(self.dnost=="") or (self.area=="") or (self.dis=="") or (self.pin=="") or (self.lm=="") or (self.phno1=="") or (self.phno2=="") or (self.email=="") or (self.gstno=="") or (self.actv=="")):
            self.msg_em=Label(self.new_frame, text="                                             ",font=('50'),fg="red").place(x=234,y=0)
            self.msg_em=Label(self.new_frame,text="Please fill all the fields!!!",font=('50'),fg="Blue").place(x=204,y=0)
        else:
            try:
                conn = sqlite3.connect('appdb.db')
                cursor=conn.cursor()
                sql="INSERT INTO customer(cust_id,cust_name,cust_cname,cust_drno_st,cust_area,cust_tlk_dst,cust_pincode,cust_landmark,cust_phone1,cust_phone2,cust_emailid,cust_gstin_no,cust_inactive) Values ("+'"'+str(self.id)+'",'+'"'+self.name+'",'+'"'+self.cname+'",'+'"'+self.dnost+'",'+'"'+self.area+'",'+'"'+self.dis+'",'+'"'+str(self.pin)+'",'+'"'+self.lm+'",'+'"'+str(self.phno1)+'",'+'"'+str(self.phno2)+'",'+'"'+self.email+'",'+'"'+str(self.gstno)+'",'+'"'+str(self.actv)+'"'+")"
                print(sql)
                cursor.execute(sql)
                conn.commit()
                msg_em=Label(self.new_frame, text="                                                     ",font=('50'),fg="red").place(x=234,y=0)
                msg_em=Label(self.new_frame, text="New Customer Added...",font=('50'),fg="red").place(x=234,y=0)
            except sqlite3.Error as err:
                print(":( {}".format("Customer Allready Exist"))
                self.msg_em=Label(self.new_frame, text="Customer Already Exists....",font=('50'),fg="red").place(x=234,y=0)
                conn.rollback()
            cursor.close()
            conn.close()       
        
#------------------------------------------------------------------------------------------------------------------------------------------------->
    def ui_frame(self):                 #>>>>>>>Parent Window<<<<<<<<<<#
        self.parent.title("Customer")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        self.parent.geometry("%dx%d" % (w, h))
        self.rt_frame = Frame(self.parent,height=802,width=790,highlightbackground="black",highlightthickness=1)#Right Frame
        self.rt_frame.place(x=800,y=0)
        self.f3 = Frame(self.parent,height=100,width=700,highlightbackground="#cfcfc6",highlightthickness=1)#Menu Frame top
        self.f3.place(x=100,y=0)
        # self.right_frame()
        # self.root_img = ImageTk.PhotoImage(Image.open("side1.png"))              #Root Photo
        # # # self.l1 = Label(self.parent,image=self.root_img)
        # # # self.l1.place(x=-150,y=600)                                                 
        # self.l2 = Label(self.parent,image=self.root_img)                            
        # self.l2.place(x=-5,y=135)
        
#----------------------------------------------------------------------------------------------------------------------------->
    def ui_home(self):                  #>>>>>>>>>>>>Home Menu Function<<<<<<<<<<#
        self.arrow.place(x=34,y=0)
        self.menu_frame.destroy()           #Clears the old Frame
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1) #Fuctions Frame
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="Customer Home",width=150,height=2,bg='green',fg="white",font=("Helvetica",12,"bold"),justify="center")
        self.add_label.place(x=-680,y=0)
        self.frame_img = Label(self.menu_frame,image=self.home_cus_img)
        self.frame_img.place(x=50,y=100)

#----------------------------------------------------------------------------------------------------------------------------->
    def ui_logout(self):                #>>>>>>>>>>>>Delete button<<<<<<<<<<<<<<<#
        MsgBox=messagebox.askquestion("Confirm Logout","Are You Sure you want to exit?",icon="warning")
        if MsgBox=='yes':
            self.parent.destroy()
    
#----------------------------------------------------------------------------------------------------------------------------->
    def ui_new(self):                   #>>>>>>>>>>>>New Menu Function<<<<<<<<<<#

        def enter(self):        #Hover Functions
            b1_save['fg'] = 'green'
        def leave(self):
            b1_save['fg'] = 'black'
        def enter1(self):
            b2_cancel['fg'] = 'red'
        def leave1(self):
            b2_cancel['fg'] = 'black'
        self.arrow.place(x=168,y=0)
        self.menu_frame.destroy()           #Clears the old Frame
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1) #Fuctions Frame
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="New Customer",width=100,height=2,bg='green',fg="white",font=("Helvetica",12,"bold"))
        self.add_label.place(x=-286,y=0)
        self.new_frame = Frame(self.menu_frame,height=580,width=680) #New Frame  
        self.new_frame.place(x=10,y=68)  
        self.id=Label(self.new_frame,text="Id",font=("Helvetica",12,"bold"))          #Id
        self.id.place(x=20,y=15)
        self.en_id = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1,state="disabled")
        self.en_id.place(x=20,y=40)
        self.name=Label(self.new_frame,text="Name  ",font=("Helvetica",12,"bold"))          #Name
        self.name.place(x=20,y=80)
        self.en_name = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_name.place(x=21,y=107)
        self.cn_name=Label(self.new_frame,text="Contact Name ",font=("Helvetica",12,"bold"))          #Contact Name
        self.cn_name.place(x=250,y=80)
        self.en_cn_name = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_cn_name.place(x=251,y=107)
        self.address=Label(self.new_frame,text="Address ",font=("Helvetica",12,"bold")).place(x=20,y=140)          #Address
        self.en_drno_st= Entry(self.new_frame,font=("Helvetica",10,"bold"),width=55,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_drno_st.place(x=20,y=170)
        self.lb_drno_st=Label(self.new_frame,text="(door number, street) ",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_drno_st.place(x=20,y=192)
        self.en_area = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=55,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_area.place(x=20,y=225)
        self.lb_area=Label(self.new_frame,text="(area) ",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_area.place(x=20,y=247)
        self.en_dis = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_dis.place(x=20,y=275)
        self.lb_dis=Label(self.new_frame,text="(district) ",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_dis.place(x=20,y=297)
        self.en_pin = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_pin.place(x=250,y=275)
        self.lb_pin=Label(self.new_frame,text="(pincode) ",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_pin.place(x=250,y=297)
        self.en_lm = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_lm.place(x=20,y=325)
        self.lb_lm=Label(self.new_frame,text="(landmark) ",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_lm.place(x=20,y=347)
        self.cn_info=Label(self.new_frame,text="Contact Information ",font=("Helvetica",12,"bold"))          #Contact Name
        self.cn_info.place(x=20,y=370)
        self.en_phno1 = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_phno1.place(x=20,y=405)
        self.lb_phno1=Label(self.new_frame,text="(phone number 1)",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_phno1.place(x=20,y=427)
        self.en_phno2 = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_phno2.place(x=250,y=405)
        self.lb_phno2=Label(self.new_frame,text="(phone number 2)",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_phno2.place(x=250,y=427)
        self.en_email = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=55,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_email.place(x=20,y=450)
        self.lb_email=Label(self.new_frame,text="(e-mail)",font=("Helvetica",8,"bold"),fg="gray")    
        self.lb_email.place(x=20,y=475)
        self.gst_no=Label(self.new_frame,text="Gst Number ",font=("Helvetica",12,"bold"))          #Contact Name
        self.gst_no.place(x=20,y=505)
        self.en_gst_no = Entry(self.new_frame,font=("Helvetica",10,"bold"),width=25,justify="center",fg="#3f423e",highlightbackground="black",highlightthickness=1)
        self.en_gst_no.place(x=20,y=535)
        self.var = IntVar()
        self.frame1=LabelFrame(self.new_frame,height=80,width=170,text="Customer Active",font=("Helvetica",10,"bold")).place(x=250,y=495)
        self.r1_yes = Radiobutton(self.new_frame, text="Yes", variable=self.var, value=1,font=("Helvetica",13),cursor="hand2")
        self.r1_yes.place(x=260,y=525)
        self.r2_no = Radiobutton(self.new_frame, text="No", variable=self.var, value=0,font=("Helvetica",13),cursor="hand2",state="disabled")
        self.r2_no.place(x=340,y=525)
        self.r1_yes.select()
        #button
        b1_save=Button(self.new_frame,text="Save ",image=self.save_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.save_process)
        b1_save.place(x=510,y=5)
        b2_cancel=Button(self.new_frame,text="Cancel",image=self.cancel_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_home)
        b2_cancel.place(x=570,y=8)
        b1_save.bind("<Enter>",enter)
        b1_save.bind("<Leave>",leave)
        b2_cancel.bind("<Enter>",enter1)
        b2_cancel.bind("<Leave>",leave1)

        


        
       

        
    

#-------------------------------------------------------------------------------------------------------------------------------------------------->
    def ui_search(self):                #>>>>>>>>>>>>Search Menu Function<<<<<<<<<<#
        self.arrow.place(x=300,y=0)
        self.menu_frame.destroy()           #Clears the old Frame
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1) #Fuctions Frame
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="Search Customer",width=85,height=2,bg='green',fg="white",font=("Helvetica",12,"bold"),justify="center")
        self.add_label.place(x=-80,y=0)
        # self.srch_img = ImageTk.PhotoImage(Image.open("search_a.png"))
        # self.lb_serch = Label(self.menu_frame,image=self.srch_img)                            
        # self.lb_serch.place(x=0,y=15)

        


#-------------------------------------------------------------------------------------------------------------------------------------------------->
    def ui_edit(self):                #>>>>>>>>>>>>Edit Menu Function<<<<<<<<<<#
        self.arrow.place(x=440,y=0)
        self.menu_frame.destroy()           #Clears the old Frame
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1) #Fuctions Frame
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="Edit Customer",width=97,height=2,bg='green',fg="white",font=("Helvetica",12,"bold"),justify="center")
        self.add_label.place(x=-1,y=0)
#-------------------------------------------------------------------------------------------------------------------------------------------------->
    def ui_delete(self):                #>>>>>>>>>>>>Delete Menu Function<<<<<<<<<<#
        self.arrow.place(x=570,y=0)
        self.menu_frame.destroy()           #Clears the old Frame
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1) #Fuctions Frame
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="Delete Customer",width=23,height=1,bg='green',fg="white")
        self.add_label.place(x=530,y=0)

#-------------------------------------------------------------------------------------------------------------------------------------------------->
    def ui_topframe(self):              #>>>>>>>>Left view Parent Window<<<<<<<<<#
        def enter(self):        #Hover Functions
            b1['fg'] = 'blue'
        def leave(self):
            b1['fg'] = 'black'
        def enter1(self):
            b2['fg'] = 'blue'
        def leave1(self):
            b2['fg'] = 'black'
        def enter2(self):
            b3['fg'] = 'blue'
        def leave2(self):
            b3['fg'] = 'black'
        def enter3(self):
            b4['fg'] = 'blue'
        def leave3(self):
            b4['fg'] = 'black'
        def enter4(self):
            b5['fg'] = 'blue'
        def leave4(self):
            b5['fg'] = 'black'
        def enter5(self):
            b6['fg'] = "red"
            
        def leave5(self):
            b6['fg'] = 'black'
            
        
        #Images
        
        self.logout_img = ImageTk.PhotoImage(Image.open("logo3.png"))
        self.cancel_img = ImageTk.PhotoImage(Image.open("cancel7.png"))
        self.alert_img = ImageTk.PhotoImage(Image.open("alert1.png"))
        self.save_img = ImageTk.PhotoImage(Image.open("tick1.png")) 
        self.insert_img = ImageTk.PhotoImage(Image.open("ins1.png"))
        self.search_img = ImageTk.PhotoImage(Image.open("vw1.png"))
        self.home_img = ImageTk.PhotoImage(Image.open("home2.png"))
        self.edit_img = ImageTk.PhotoImage(Image.open("up1.png"))
        self.del_img = ImageTk.PhotoImage(Image.open("del1.png"))
        self.arrow_img = ImageTk.PhotoImage(Image.open("arr1.png"))
        self.home_cus_img = ImageTk.PhotoImage(Image.open("img_f.png"))
        #Buttons
        b1=Button(self.f3,text="Home",image=self.home_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_home)
        b1.place(x=50,y=13)
        b2=Button(self.f3,text="New",image=self.insert_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_new)
        b2.place(x=170,y=6)
        b3=Button(self.f3,text="Search",image=self.search_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_search)
        b3.place(x=300,y=2)
        b4=Button(self.f3,text="Edit",image=self.edit_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_edit)
        b4.place(x=440,y=2)
        b5=Button(self.f3,text="Delete",image=self.del_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_delete)
        b5.place(x=570,y=5)
        b6=Button(self.parent,text="Logout",image=self.logout_img,bd=0,cursor="hand2",compound="top",relief=SUNKEN,command=self.ui_logout)
        b6.place(x=15,y=23)
        #Button Functions
        b1.bind("<Enter>",enter)
        b1.bind("<Leave>",leave)
        b2.bind("<Enter>",enter1)
        b2.bind("<Leave>",leave1)
        b3.bind("<Enter>",enter2)
        b3.bind("<Leave>",leave2)
        b4.bind("<Enter>",enter3)
        b4.bind("<Leave>",leave3)
        b5.bind("<Enter>",enter4)
        b5.bind("<Leave>",leave4)
        b6.bind("<Enter>",enter5)
        b6.bind("<Leave>",leave5)
        self.f4 = Frame(self.parent,height=40,width=700)       #Defauut (Inits)
        self.f4.place(x=100,y=100)
        self.arrow=Label(self.f4,image=self.arrow_img)
        self.arrow.place(x=34,y=0)
        self.menu_frame = Frame(self.parent,height=680,width=700,highlightbackground="#cfcfc6",highlightthickness=1)
        self.menu_frame.place(x=100,y=136)
        self.add_label=Label(self.menu_frame,text="Customer Home",width=150,height=2,bg='green',fg="white",font=("Helvetica",12,"bold"),justify="center")
        self.add_label.place(x=-680,y=0)
        self.frame_img = Label(self.menu_frame,image=self.home_cus_img)
        self.frame_img.place(x=50,y=100)
#-------------------------------------------------------------------------------------------------------------------------------------------------->
    # def right_frame(self):
    #     self.tb_frame = Frame(self.parent,height=800,width=733,highlightbackground="black",highlightthickness=1).place(x=800,y=50)
    #     # lst=[("id","name","Contact person","Address 1","Area","District","Pincode","landmark","PhoneNumber1","PhoneNumber2","E-mail","Gst Number"),("cu454451001","Instagram","Kevin Systrom","Detroid","lords","Michigan","48001","Hendry Ford Museum","12315789","454645645","kevinsystrom@gmail.com","5789789"),("cu454451001","Instagram","Kevin Systrom","Detroid","lords","Michigan","48001","Hendry Ford Museum","12315789","454645645","kevinsystrom@gmail.com","5789789"),("cu454451001","Instagram","Kevin Systrom","Detroid","lords","Michigan","48001","Hendry Ford Museum","12315789","454645645","kevinsystrom@gmail.com","5789789")]
    #     # #find the no of rows and cols in the list 
    #     # total_rows = len(lst)
    #     # total_cols=len(lst[0])
    #     # for i in range(total_rows):
    #     #     for j in range(total_cols):
    #     #         if i==0:
    #     #             e = Entry(self.tb_frame, width=5, fg='white',bg="steelblue",justify="center",font=('Arial',16,'bold'))
    #     #             e.grid(row=i, column=j)
    #     #             e.insert(END, lst[i][j])
    #     #         else:
    #     #             e = Entry(self.tb_frame, width=5, fg='blue',font=('Arial',16,'bold'))
    #     #             e.grid(row=i, column=j)
    #     #             e.insert(END, lst[i][j])
#-------------------------------------------------------------------------------------------------------------------------------------------------->

root = Tk()
app = application(root)
mainloop()