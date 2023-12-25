

import tkinter
import customtkinter as ct
from tkinter import messagebox
import mysql.connector
ct.set_appearance_mode("dark")





mydb= mysql.connector.connect( host='127.0.0.1',user='root', password='00725ravi',port=3306,database='sys')

con=mydb.cursor()

con.execute('create table if not exists ADMIN1(ID varchar(100),NAME VARCHAR(100))')

query1='insert into ADMIN1(ID,NAME) values (%s,%s)'
student=[("JC 241","NAVNIT"),
         ("JC 254","PRAKASH S"),
         ('JC 243','ASWINI J'),
         ('JC 249','DEEPA PRABHA P'),
         ('JC 236','DEEPIKA S'),
         ('JC 269','HEMA V'),
         ('JC 270','KALKI G K'),('JC 239','KALPANA M P'),('JC 260','KIRUTHIKA D M'),('JC 252',"LAVANYA S R"),
         ('JC 272','MADHUMITHA K'),('JC 245',"NARMADHA J S"),('JC 264','RAGHAVI V P'),('JC 214','RAKSHITHA M M '),('JC 213','SHAMITHA K J'),
         ('JC 257','SEMMATHI G S'),('JC 237',"SERENA NATHAN"),('JC 225',"SHANMUGA PRIYA J"),('JC 212',"THARINI A S"),
         ('JC 259',"VIGNASHRI M N"),('JC 261',"ARUL KUMARAN P"),('JC 266','BALAJI R'),
         ('JC 268',"JAIVANTH SRINIVASAN"),
   ('JC 274',"LOKESH KUMAR"),('JC 216','PRANAV KESAV RAJ'),('JC 222',"PRASANTH S"),('JC 263',"PRASHIK P"),('JC 223','RAVIKRISHNA'),('JC 256',"RAVINETHIRAN"),
   ('JC 267',"SEKKAPPAN "),('JC 238','VISHAL SAI B J'),
   ('JC 229',"ANANYA"),('JC 255','HARINI S'),
   ('JC 275','HARNITHA S'),('JC 262','KEERTHANA R'),
   ('JC 277','SHAILAJAA M'),('JC 280','TRISHUL AKASH')]

con.executemany(query1,student)
    



mydb.commit()



























def add():
    print("h")




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

button= ct.CTkButton(master=frame1, text="ADD",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button= ct.CTkButton(master=frame1, text="UPDATE",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

button= ct.CTkButton(master=frame1, text="DELETE",text_font=("Microsoft Sans Serif","15"),command=add,fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

















app1.mainloop()
