from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('List of Complaints')
		tv = Treeview(self._root)
		tv.pack()
	
		tv.configure(column=('#Admission no', '#Name', '#DOB','#Gender','#Contact no',"#Email Id",'#Address'))
		tv.heading('#Admission no', text='Admission no')
		tv.heading('#Name', text='Name')
		tv.heading('#DOB', text='DOB')
		tv.heading('#Gender', text='Gender')
		tv.heading('#Contact no', text='Contact no')
		tv.heading('#Email Id', text='Email Id')
		tv.heading('#Address', text='Address')
		cursor = self._dbconnect.ListRequest()
		for row in cursor:
			
			tv.set('#{}'.format(row['ID']),'#Admission no',row['Admission no'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#DOB',row['DOB'])
			tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
			tv.set('#{}'.format(row['ID']),'#Contact no',row['Contact no'])
			tv.set('#{}'.format(row['ID']),'#Email Id',row['Email Id'])
			tv.set('#{}'.format(row['ID']),'#Address',row['Address'])
			
