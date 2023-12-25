import customtkinter as ct
import tkinter
from tkinter import messagebox
from time import sleep
from tkinter import messagebox
from tkinter import ttk






ct.set_appearance_mode("dark")
app = ct.CTk()
app.geometry("%dx%d+0+0"%(2005,2005))
app.title("CustomTkinter simple_example.py")



f=ct.CTkFrame(app,width=1500,height=100,border_width=3,fg_color='black',border_color='black',corner_radius=10)
f.pack(pady=0,ipady=10)


text_var = tkinter.StringVar(value="REPORT CARD")

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




"""button= ct.CTkButton(master=frame, text="Add",text_font=("Microsoft Sans Serif","15"),fg_color=("#413839"),hover_color=("#87CEFA"),text_color=("white"))
button.place(relx=0.5, rely=0.89, anchor=tkinter.CENTER)

entry = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),fg_color=("#DCDCDC"),placeholder_text="Enter the addmission no",width=300,text_color=("black"))
entry.place(relx=0.65, rely=0.15, anchor=tkinter.CENTER)

entry1 = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),placeholder_text="Enter the name",width=300)
entry1.place(relx=0.65, rely=0.25, anchor=tkinter.CENTER)

entry2 = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"),placeholder_text="Enter the dob",width=300)
entry2.place(relx=0.65, rely=0.35, anchor=tkinter.CENTER)

entry3= ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), placeholder_text="Enter the gender",width=300)
entry3.place(relx=0.65, rely=0.45, anchor=tkinter.CENTER)

entry4 = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), placeholder_text="Enter the contact no",width=300)
entry4.place(relx=0.65, rely=0.55, anchor=tkinter.CENTER)

entry5 = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), placeholder_text="Enter the email id",width=300)
entry5.place(relx=0.65, rely=0.65, anchor=tkinter.CENTER)

entry6 = ct.CTkEntry(master=frame,height=40,text_font=("Microsoft Sans Serif","15"),text_color=("black"),fg_color=("#DCDCDC"), placeholder_text="Enter the address",width=300)
entry6.place(relx=0.65, rely=0.75, anchor=tkinter.CENTER)"""






















app.mainloop()





































"""def Submit():
    a={"JC 241":"NAVNIT","JC 254":"PRAKASH S",'JC 243':'ASWINI J','JC 249':'DEEPA PRABHA P','JC 236':'DEEPIKA S','JC 269':'HEMA V','JC 270':'KALKI G K','JC 239':'KALPANA M P','JC 260':'KIRUTHIKA D M','JC 252':"LAVANYA S R",'JC 272':'MADHUMITHA K','JC 245':"NARMADHA J S",'JC 264':'RAGHAVI V P',
   'JC 214':'RAKSHITHA M M ','JC 213':'SHAMITHA K J','JC 257':'SEMMATHI G S','JC 237':"SERENA NATHAN",'JC 225':"SHANMUGA PRIYA J",'JC 212':"THARINI A S",'JC 259':"VIGNASHRI M N",'JC 261':"ARUL KUMARAN P",'JC 266':'BALAJI R','JC 268':"JAIVANTH SRINIVASAN",
   'JC 274':"LOKESH KUMAR",'JC 216':'PRANAV KESAV RAJ','JC 222':"PRASANTH S",'JC 263':"PRASHIK P",'JC 223':'RAVIKRISHNA','JC 256':"RAVINETHIRAN",
   'JC 267':"SEKKAPPAN ",'JC 238':'VISHAL SAI B J',
   'JC 229':"ANANYA",'JC 255':'HARINI S',
   'JC 275':'HARNITHA S','JC 262':'KEERTHANA R',
   'JC 277':'SHAILAJAA M','JC 280':'TRISHUL AKASH SUCHITRA'}
    if """


