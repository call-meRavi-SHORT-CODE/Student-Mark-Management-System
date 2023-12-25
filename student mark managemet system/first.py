import customtkinter as ct
import tkinter
from tkinter import messagebox
from time import sleep
from tkinter import messagebox
from tkinter import ttk
def firstrun():
    
    ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"

    def admin():
        a={"1234":'ADMIN'}
        def task():
            sleep(2) # Replace this with the code you want to run
            app.destroy()
        def submit():
             
            b= mac.get()
            f= mac2.get()
            
            if f in a and a[f]==b:
                app.after(200,task)
            else:
                messagebox.showerror("$$","incorrect user name or password")
        app1.destroy()
        ct.set_appearance_mode("dark") 

        
        app = ct.CTk()
        app.geometry("%dx%d+0+0"%(2005,2005))
        app.title("CustomTkinter simple_example.py")

        f=ct.CTkFrame(app,width=500,height=850,border_width=3,fg_color='black',border_color='black',corner_radius=10)
        f.pack(pady=100,ipady=10)


        label1 = ct.CTkLabel(master=app, text="ADMIN LOGIN",width=50,
                                   height=25,
                                   
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)



        label1 = ct.CTkLabel(master=f, text="USER NAME",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        label2 = ct.CTkLabel(master=f, text="PASSWORD",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
        label2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        mac=ct.StringVar()
        mac2=ct.StringVar()
        entry = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac,fg_color=("#DCDCDC"),placeholder_text="username",width=300,text_color=("black"))
        entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        entry1 = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac2,text_color=("black"),fg_color=("#DCDCDC"),placeholder_text="password",width=300)
        entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button= ct.CTkButton(master=f,command=submit, text="Submit",text_font=("Microsoft Sans Serif","15"),fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
        button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
      
        app.mainloop()
                                  

    def student():
        ct.set_appearance_mode("dark")
        app = ct.CTk()
        app.geometry("%dx%d+0+0"%(2005,2005))
        app.title("CustomTkinter simple_example.py")



        f=ct.CTkFrame(app,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
        f.pack(pady=0,ipady=10)


        

        frame = ct.CTkFrame(master=app,width=600,fg_color=('blue','grey75'), height=545,corner_radius=10)
        frame.pack(pady=3, ipady=10)

        n="JC 223"
        m="RAVIKRISHNA"

        label1 = ct.CTkLabel(master=frame, text=n,width=50,
                                   height=25,
                                   fg_color=("grey75"),
                                   text_color=("black"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.1, rely=0.04, anchor=tkinter.CENTER)

        label1 = ct.CTkLabel(master=frame, text=m,width=50,
                                   height=25,
                                   fg_color=("grey75"),
                                   text_color=("black"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.7, rely=0.04, anchor=tkinter.CENTER)




        Student_table=ttk.Treeview(frame,column=("ENGLISH","MATH/LANGUAGE","PHYSICS","CHEMISTRY","BIO/CS"))








        Student_table.heading("ENGLISH",text="ENGLISH")
        Student_table.heading("MATH/LANGUAGE",text="MATH/LANGUAGE")
        Student_table.heading("PHYSICS",text="PHYSICS")
        Student_table.heading("CHEMISTRY",text="CHEMISTRY")
        Student_table.heading("BIO/CS",text="BIO/CS")


        Student_table['show']= 'headings'
        Student_table.column("ENGLISH",width=15)
        Student_table.column("MATH/LANGUAGE",width=15)
        Student_table.column("PHYSICS",width=18)
        Student_table.column("CHEMISTRY",width=15)
        Student_table.column("BIO/CS",width=15)


        Student_table.place(x=0,y=100,width=900,height=500)









        label1 = ct.CTkLabel(master=app, text="UNIT 1",width=50,
                                       height=25,
                                       
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","10"))
        label1.place(relx=0.21,rely=0.3, anchor=tkinter.CENTER)

        label2 = ct.CTkLabel(master=app, text="UNIT 2",width=50,
                                       height=25,
                                       
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","10"))
        label2.place(relx=0.21, rely=0.38, anchor=tkinter.CENTER)

        label3 = ct.CTkLabel(master=app, text="UNIT 3",width=50,
                                       height=25,
                                       
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","10"))
        label3.place(relx=0.21, rely=0.48, anchor=tkinter.CENTER)


        label4 = ct.CTkLabel(master=app, text="QUATERLY",width=50,
                                       height=25,
                                      
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","10"))
        label4.place(relx=0.21, rely=0.58, anchor=tkinter.CENTER)

        label5 = ct.CTkLabel(master=app, text="HALFYEARLY",width=10,
                                       height=25,
                                       
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","10"))
        label5.place(relx=0.21, rely=0.68, anchor=tkinter.CENTER)


        button= ct.CTkButton(master=frame, text="performance",text_font=("Microsoft Sans Serif","15"),fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
        button.place(relx=0.5, rely=0.89, anchor=tkinter.CENTER)
        app.mainloop()



    def TEACHER():
        a={"123":'ADMIN'}
        def task():
            sleep(2) # Replace this with the code you want to run
            app.destroy()
        def submit():
             
            b= mac.get()
            f= mac2.get()
            
            if f in a and a[f]==b:
                app.after(200,task)
            else:
                messagebox.showerror("$$","incorrect user name or password")
        app1.destroy()
        ct.set_appearance_mode("dark") 

        
        app = ct.CTk()
        app.geometry("%dx%d+0+0"%(2005,2005))
        app.title("CustomTkinter simple_example.py")

        f=ct.CTkFrame(app,width=500,height=850,border_width=3,fg_color='black',border_color='black',corner_radius=10)
        f.pack(pady=100,ipady=10)


        label1 = ct.CTkLabel(master=app, text="TEACHER LOGIN",width=50,
                                   height=25,
                                   
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)



        label1 = ct.CTkLabel(master=f, text="USER NAME",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
        label1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        label2 = ct.CTkLabel(master=f, text="PASSWORD",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
        label2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        mac=ct.StringVar()
        mac2=ct.StringVar()
        entry = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac,fg_color=("#DCDCDC"),placeholder_text="username",width=300,text_color=("black"))
        entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        entry1 = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac2,text_color=("black"),fg_color=("#DCDCDC"),placeholder_text="password",width=300)
        entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button= ct.CTkButton(master=f,command=submit, text="Submit",text_font=("Microsoft Sans Serif","15"),fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
        button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
      
        app.mainloop()
                                  
        
        
    def STUDENT():
         a={"JC 241":"NAVNIT","JC 254":"PRAKASH S",'JC 243':'ASWINI J','JC 249':'DEEPA PRABHA P','JC 236':'DEEPIKA S','JC 269':'HEMA V','JC 270':'KALKI G K','JC 239':'KALPANA M P','JC 260':'KIRUTHIKA D M','JC 252':"LAVANYA S R",'JC 272':'MADHUMITHA K','JC 245':"NARMADHA J S",'JC 264':'RAGHAVI V P',
       'JC 214':'RAKSHITHA M M ','JC 213':'SHAMITHA K J','JC 257':'SEMMATHI G S','JC 237':"SERENA NATHAN",'JC 225':"SHANMUGA PRIYA J",'JC 212':"THARINI A S",'JC 259':"VIGNASHRI M N",'JC 261':"ARUL KUMARAN P",'JC 266':'BALAJI R','JC 268':"JAIVANTH SRINIVASAN",
       'JC 274':"LOKESH KUMAR",'JC 216':'PRANAV KESAV RAJ','JC 222':"PRASANTH S",'JC 263':"PRASHIK P",'JC 223':'RAVIKRISHNA','JC 256':"RAVINETHIRAN",
       'JC 267':"SEKKAPPAN ",'JC 238':'VISHAL SAI B J',
       'JC 229':"ANANYA",'JC 255':'HARINI S',
       'JC 275':'HARNITHA S','JC 262':'KEERTHANA R',
       'JC 277':'SHAILAJAA M','JC 280':'TRISHUL AKASH SUCHITRA'}
         def task():
            sleep(2) # Replace this with the code you want to run
            app.destroy()
            
            
         def submit():
             
            b= mac.get()
            f= mac2.get()
            
            if f in a and a[f]==b:
                app.after(200,task)
                student()
                
            else:
                messagebox.showerror("$$","incorrect user name or password") 
                     


         app1.destroy()
         ct.set_appearance_mode("dark") 

        
         app = ct.CTk()
         app.geometry("%dx%d+0+0"%(2005,2005))
         app.title("CustomTkinter simple_example.py")

         f=ct.CTkFrame(app,width=500,height=850,border_width=3,fg_color='black',border_color='black',corner_radius=10)
         f.pack(pady=100,ipady=10)


         label1 = ct.CTkLabel(master=app, text="STUDENT LOGIN",width=50,
                                   height=25,
                                   
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","20"))
         label1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)



         label1 = ct.CTkLabel(master=f, text="USER NAME",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
         label1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

         label2 = ct.CTkLabel(master=f, text="PASSWORD",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey75"),
                                   text_font=("Microsoft Sans Serif","20"))
         label2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
         mac=ct.StringVar()
         mac2=ct.StringVar()
         entry = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac,fg_color=("#DCDCDC"),placeholder_text="username",width=300,text_color=("black"))
         entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

         entry1 = ct.CTkEntry(master=f,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac2,text_color=("black"),fg_color=("#DCDCDC"),placeholder_text="password",width=300)
         entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

         button= ct.CTkButton(master=f,command=submit, text="Submit",text_font=("Microsoft Sans Serif","15"),fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
         button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
      
         app.mainloop()
        
        




    def task():
        # The window will stay open until this function call ends.
        sleep(2) # Replace this with the code you want to run
        app.destroy()
        

    def submit():
         b= mac.get()
         f= mac2.get()
         if b in a and a[b]==f:
            

             app.after(200,task)
         else:
             messagebox.showerror("Error","incorrect user name or password")

    app1 = ct.CTk()
    app1.geometry("%dx%d+0+0"%(2005,2005))
    app1.title("Login")
    f=ct.CTkFrame(app1,width=500,height=850,border_width=3,fg_color='black',border_color='black',corner_radius=10)
    f.pack(pady=100,ipady=10)


    label1 = ct.CTkLabel(master=f, text="MAHARISHI VIDYA MANDIR",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","20"))
    label1.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)



    label1 = ct.CTkLabel(master=f, text="MARK SHEET",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","20"))
    label1.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    label1 = ct.CTkLabel(master=f, text="LOGIN AS",width=50,
                                   height=25,
                                   fg_color=("black"),
                                   text_color=("grey100"),
                                   text_font=("Microsoft Sans Serif","17"))
    label1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    button= ct.CTkButton(master=f,command=STUDENT, text="STUDENT",text_font=("Microsoft Sans Serif","15"),fg_color=("GREY100"),hover_color=("#87CEFA"),text_color=("BLACK"))
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    button= ct.CTkButton(master=f,command=TEACHER, text="TEACHER",text_font=("Microsoft Sans Serif","15"),fg_color=("GREY100"),hover_color=("#87CEFA"),text_color=("BLACK"))
    button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button= ct.CTkButton(master=f,command=admin, text="ADMIN",text_font=("Microsoft Sans Serif","15"),fg_color=("GREY100"),hover_color=("#87CEFA"),text_color=("BLACK"))
    button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)



             






    app1.mainloop()
firstrun()
    
