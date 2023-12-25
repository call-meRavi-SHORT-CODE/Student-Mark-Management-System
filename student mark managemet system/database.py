import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('data.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists comp(Admission no integer primary key , Name varchar(255), DOB varchar(255), Gender varchar(255) ,Contact no varchar(255),Email Id varchar(255),Address varchar(255))')
		self._db.commit()
	def Add(self, name, gender, comment):
		self._db.execute('insert into Comp (Admission no,Name,DOB,Gender,Contact no,Email Id ,Address ) values (?,?,?,?,?,?,?)',(Admission_no,Name,DOB,Gender,Contact_no,Email_Id ,Address))
		self._db.commit()
		return 'Your complaint has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
