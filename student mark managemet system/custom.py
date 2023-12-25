import tkinter
import customtkinter as ct
from tkinter import messagebox

ct.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"


app = ct.CTk()
app.geometry("%dx%d+0+0"%(2005,2005))
app.iconbitmap('download.png')
app.title("Home.py")


f=ct.CTkFrame(app,width=1500,height=100,border_width=3,fg_color='#EE4B2B',border_color='#EE4B2B',corner_radius=10)
f.pack(pady=0,ipady=10)

app.mainloop()

