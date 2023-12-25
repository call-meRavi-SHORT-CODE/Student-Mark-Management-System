

import tkinter
import customtkinter as ct
from tkinter import messagebox
import mysql.connector



        




def tadd():
        

        def back():
                ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


                app = ct.CTk()
                app.geometry("%dx%d+0+0"%(2005,2005))
                app.title("CustomTkinter simple_example.py")



                f=ct.CTkFrame(app,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
                f.pack(pady=0,ipady=10)


                text_var = tkinter.StringVar(value="MARK REGISTER")

                label = ct.CTkLabel(master=f,
                                               textvariable=text_var,
                                               width=500,
                                               height=25,
                                               fg_color=("white", "black"),
                                               text_font=("Microsoft Sans Serif","50"),
                                               corner_radius=8)
                label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                frame = ct.CTkFrame(master=app,width=600,fg_color=('blue','grey75'), height=545,corner_radius=10)
                frame.pack(pady=3, ipady=10)


                frame1= ct.CTkFrame(master=frame,width=400,fg_color=('blue','black'), height=400,corner_radius=10)
                frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                label1 = ct.CTkLabel(master=frame, text="ENTER THE STUDENT NUMBER",width=50,
                                               height=25,
                                               fg_color=("black"),
                                               text_color=("grey100"),
                                               text_font=("Microsoft Sans Serif","18"))
                label1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

                mac2=ct.StringVar()

                entry = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac2,fg_color=("#DCDCDC"),width=100,text_color=("black"))
                entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

                button= ct.CTkButton(master=frame1, text="SUBMIT",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
                button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
                        


        def add():
                a={"JC 241":"NAVNIT","JC 254":"PRAKASH S",'JC 243':'ASWINI J','JC 249':'DEEPA PRABHA P','JC 236':'DEEPIKA S','JC 269':'HEMA V','JC 270':'KALKI G K','JC 239':'KALPANA M P','JC 260':'KIRUTHIKA D M','JC 252':"LAVANYA S R",'JC 272':'MADHUMITHA K','JC 245':"NARMADHA J S",'JC 264':'RAGHAVI V P',
           'JC 214':'RAKSHITHA M M ','JC 213':'SHAMITHA K J','JC 257':'SEMMATHI G S','JC 237':"SERENA NATHAN",'JC 225':"SHANMUGA PRIYA J",'JC 212':"THARINI A S",'JC 259':"VIGNASHRI M N",'JC 261':"ARUL KUMARAN P",'JC 266':'BALAJI R','JC 268':"JAIVANTH SRINIVASAN",
           'JC 274':"LOKESH KUMAR",'JC 216':'PRANAV KESAV RAJ','JC 222':"PRASANTH S",'JC 263':"PRASHIK P",'JC 223':'RAVIKRISHNA','JC 256':"RAVINETHIRAN",
           'JC 267':"SEKKAPPAN ",'JC 238':'VISHAL SAI B J',
           'JC 229':"ANANYA",'JC 255':'HARINI S',
           'JC 275':'HARNITHA S','JC 262':'KEERTHANA R',
           'JC 277':'SHAILAJAA M','JC 280':'TRISHUL AKASH SUCHITRA'}
                a1={"JC 241":"NAVNIT","JC 254":"PRAKASH S",'JC 243':'ASWINI J','JC 249':'DEEPA PRABHA P','JC 236':'DEEPIKA S','JC 269':'HEMA V','JC 270':'KALKI G K','JC 239':'KALPANA M P','JC 260':'KIRUTHIKA D M','JC 252':"LAVANYA S R",'JC 272':'MADHUMITHA K','JC 245':"NARMADHA J S",'JC 264':'RAGHAVI V P',
           'JC 214':'RAKSHITHA M M ','JC 213':'SHAMITHA K J','JC 257':'SEMMATHI G S','JC 237':"SERENA NATHAN",'JC 225':"SHANMUGA PRIYA J",'JC 212':"THARINI A S",'JC 259':"VIGNASHRI M N"}
                
                 
                
                f1= mac2.get()
                
                if f1 in a:
                        if f1 in a1:
                                def submit():
                                        
                                        c=mac2.get()
                                        a=mac1.get()
                                        b=mac.get()
                                        g=mac6.get()
                                        d=mac3.get()
                                        e=mac4.get()
                                        i=mac5.get()
                                        f=combobox.get()
                                        
                                        
                                        

                                        mydb= mysql.connector.connect( host='127.0.0.1',user='root', password='00725ravi',port=3306,database='sys')

                                        con=mydb.cursor()

                                        def class_12a1():
                                            con.execute('create table if not exists BIO(ID varchar(8),EXAM VARCHAR(15),ENGLISH INT(3) ,MATHSLANGUAGE INT(3),PHYSICS INT(3),CHEMISTRY INT(3),BIOLOGY INT(3))')
                                            query1="insert into BIO(ID,EXAM,ENGLISH ,MATHSLANGUAGE,PHYSICS,CHEMISTRY,BIOLOGY)values('{}','{}',{},{},{},{},{})".format(c,f,a,b,d,e,i)
                                            con.execute(query1)

                                            
                                            mydb.commit()


                                        class_12a1()

                                        












                                        
                                app.destroy()
                                ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


                                app1= ct.CTk()
                                app1.geometry("%dx%d+0+0"%(2005,2005))
                                app1.title("CustomTkinter simple_example.py")



                                f=ct.CTkFrame(app1,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
                                f.pack(pady=0,ipady=10)


                                text_var = tkinter.StringVar(value="MARK REGISTER")

                                label = ct.CTkLabel(master=f,
                                                               textvariable=text_var,
                                                               width=500,
                                                               height=25,
                                                               fg_color=("white", "black"),
                                                               text_font=("Microsoft Sans Serif","50"),
                                                               corner_radius=8)
                                label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                                frame = ct.CTkFrame(master=app1,width=600,fg_color=('blue','grey75'), height=545,corner_radius=10)
                                frame.pack(pady=3, ipady=10)


                                frame1= ct.CTkFrame(master=frame,width=400,fg_color=('blue','black'), height=400,corner_radius=10)
                                frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                                label1 = ct.CTkLabel(master=frame, text=f1,width=50,
                                                               height=25,
                                                               fg_color=("grey75"),
                                                               text_color=("black"),
                                                               text_font=("Microsoft Sans Serif","20"))
                                label1.place(relx=0.25, rely=0.10, anchor=tkinter.CENTER)

                                label2 = ct.CTkLabel(master=frame1, text="ENGLISH",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label2.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

                                label3 = ct.CTkLabel(master=frame1, text="MATHS/LANGUAGE",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label3.place(relx=0.3, rely=0.35, anchor=tkinter.CENTER)


                                label4 = ct.CTkLabel(master=frame1, text="PHYSICS",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label4.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

                                label5 = ct.CTkLabel(master=frame1, text="CHEMISTRY",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label5.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)

                                label6 = ct.CTkLabel(master=frame1, text="BIOLOGY",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label6.place(relx=0.33, rely=0.80, anchor=tkinter.CENTER)






                                button= ct.CTkButton(master=frame, text="Add",text_font=("Microsoft Sans Serif","15"),command=submit,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
                                button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
                                
                                mac1=ct.StringVar()
                                mac=ct.StringVar()
                                mac3=ct.StringVar()
                                mac4=ct.StringVar()
                                mac5=ct.StringVar()
                                mac6=ct.StringVar()
                                
                

                                entry = ct.CTkEntry(master=frame1,textvariable=mac1,height=40,text_font=("Microsoft Sans Serif","15"),fg_color=("#DCDCDC"),width=50,text_color=("black"))
                                entry.place(relx=0.78, rely=0.2, anchor=tkinter.CENTER)

                                entry1 = ct.CTkEntry(master=frame1,textvariable=mac,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),width=50)
                                entry1.place(relx=0.78, rely=0.35, anchor=tkinter.CENTER)

                                entry2 = ct.CTkEntry(master=frame1,textvariable=mac3,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),width=50)
                                entry2.place(relx=0.78, rely=0.5, anchor=tkinter.CENTER)

                                entry3= ct.CTkEntry(master=frame1,textvariable=mac4,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), width=50)
                                entry3.place(relx=0.78, rely=0.65, anchor=tkinter.CENTER)

                                entry4 = ct.CTkEntry(master=frame1,textvariable=mac5,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), width=50)
                                entry4.place(relx=0.78,rely=0.80, anchor=tkinter.CENTER)
                                

                               

                                combobox = ct.CTkComboBox(master=frame,
                                                                     values=["Unit 1", "Unit 2","Quarterly Exam","Unit 3","Half Yearly"],
                                                                     width=270,
                                                                     height=33
                                                          
                                                                     )
                                combobox.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)                        
                                app1.mainloop()

                        else:
                                def submit():
                                        
                                        c=mac2.get()
                                        a=mac1.get()
                                        b=mac.get()
                                        g=mac6.get()
                                        d=mac3.get()
                                        e=mac4.get()
                                        i=mac5.get()
                                        f=combobox.get()
                                        mydb= mysql.connector.connect( host='127.0.0.1',user='root', password='00725ravi',port=3306,database='sys')

                                        con=mydb.cursor()

                                        def class_12a2():
                                            con.execute('create table if not exists CS(ID varchar(8),EXAM VARCHAR(15),ENGLISH INT(3) ,MATHSLANGUAGE INT(3),PHYSICS INT(3),CHEMISTRY INT(3),CS INT(3))')
                                            query1="insert into CS(ID,EXAM,ENGLISH ,MATHSLANGUAGE,PHYSICS,CHEMISTRY,CS)values('{}','{}',{},{},{},{},{})".format(c,f,a,b,d,e,i)
                                            con.execute(query1)

                                            
                                            mydb.commit()


                                        class_12a2()

                                        
                                        
                                        

                                       

                                app.destroy()
                                ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


                                app1= ct.CTk()
                                app1.geometry("%dx%d+0+0"%(2005,2005))
                                app1.title("CustomTkinter simple_example.py")



                                f=ct.CTkFrame(app1,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
                                f.pack(pady=0,ipady=10)


                                text_var = tkinter.StringVar(value="MARK REGISTER")

                                label = ct.CTkLabel(master=f,
                                                               textvariable=text_var,
                                                               width=500,
                                                               height=25,
                                                               fg_color=("white", "black"),
                                                               text_font=("Microsoft Sans Serif","50"),
                                                               corner_radius=8)
                                label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                                frame = ct.CTkFrame(master=app1,width=600,fg_color=('blue','grey75'), height=545,corner_radius=10)
                                frame.pack(pady=3, ipady=10)


                                frame1= ct.CTkFrame(master=frame,width=400,fg_color=('blue','black'), height=400,corner_radius=10)
                                frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                                label1 = ct.CTkLabel(master=frame, text=f1,width=50,
                                                               height=25,
                                                               fg_color=("grey75"),
                                                               text_color=("black"),
                                                               text_font=("Microsoft Sans Serif","20"))
                                label1.place(relx=0.25, rely=0.10, anchor=tkinter.CENTER)

                                label2 = ct.CTkLabel(master=frame1, text="ENGLISH",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label2.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

                                label3 = ct.CTkLabel(master=frame1, text="MATHS/LANGUAGE",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label3.place(relx=0.3, rely=0.35, anchor=tkinter.CENTER)


                                label4 = ct.CTkLabel(master=frame1, text="PHYSICS",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label4.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

                                label5 = ct.CTkLabel(master=frame1, text="CHEMISTRY",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label5.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)

                                label6 = ct.CTkLabel(master=frame1, text="COMPUTER SCIENCE",width=50,
                                                               height=25,
                                                               fg_color=("black"),
                                                               text_color=("grey100"),
                                                               text_font=("Microsoft Sans Serif","18"))
                                label6.place(relx=0.33, rely=0.80, anchor=tkinter.CENTER)






                                button= ct.CTkButton(master=frame, text="Add",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
                                button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

                                entry = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),fg_color=("#DCDCDC"),width=50,text_color=("black"))
                                entry.place(relx=0.78, rely=0.2, anchor=tkinter.CENTER)

                                entry1 = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),width=50)
                                entry1.place(relx=0.78, rely=0.35, anchor=tkinter.CENTER)

                                entry2 = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),width=50)
                                entry2.place(relx=0.78, rely=0.5, anchor=tkinter.CENTER)

                                entry3= ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), width=50)
                                entry3.place(relx=0.78, rely=0.65, anchor=tkinter.CENTER)

                                entry4 = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), width=50)
                                entry4.place(relx=0.78,rely=0.80, anchor=tkinter.CENTER)
                                

                               

                                combobox = ct.CTkComboBox(master=frame,
                                                                     values=["Unit 1", "Unit 2","Quarterly Exam","Unit 3","Half Yearly"],
                                                                     width=270,
                                                                     height=33
                                                          
                                                                     )
                                combobox.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)



                                
                                app1.mainloop()

                                
                        
                   
                    
                else:
                    messagebox.showerror("$$","incorrect student number") 
             






                
                





         






                





        ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


        app = ct.CTk()
        app.geometry("%dx%d+0+0"%(2005,2005))
        app.title("CustomTkinter simple_example.py")



        f=ct.CTkFrame(app,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
        f.pack(pady=0,ipady=10)


        text_var = tkinter.StringVar(value="MARK REGISTER")

        label = ct.CTkLabel(master=f,
                                       textvariable=text_var,
                                       width=500,
                                       height=25,
                                       fg_color=("white", "black"),
                                       text_font=("Microsoft Sans Serif","50"),
                                       corner_radius=8)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        frame = ct.CTkFrame(master=app,width=600,fg_color=('blue','grey75'), height=545,corner_radius=10)
        frame.pack(pady=3, ipady=10)


        frame1= ct.CTkFrame(master=frame,width=400,fg_color=('blue','black'), height=400,corner_radius=10)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label1 = ct.CTkLabel(master=frame, text="ENTER THE STUDENT NUMBER",width=50,
                                       height=25,
                                       fg_color=("black"),
                                       text_color=("grey100"),
                                       text_font=("Microsoft Sans Serif","18"))
        label1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        mac2=ct.StringVar()

        entry = ct.CTkEntry(master=frame1,height=40,text_font=("Microsoft Sans Serif","15"),textvariable=mac2,fg_color=("#DCDCDC"),width=100,text_color=("black"))
        entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        button= ct.CTkButton(master=frame1, text="SUBMIT",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
        button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        app.mainloop()


t1add()


























































































