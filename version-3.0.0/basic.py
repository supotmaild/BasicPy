'''BasicPy 3.0 ARM Code Club Thailand 2015'''
'''stable version 6 April 2015'''
class basic:
	import os
	print('BasicPy 3.0 by ARM Code Club Thailand 2015')
	print('==========================================')
	print(os.getcwd())
	print('Please change your current workspace')
	print('Enter will go to C:\Program Files\Python 3.5 automatic')
	print('Change  Path:', end='')
	path_change = input()
	if path_change == '':
		os.chdir('C:\Program Files\Python 3.5')
	else:
		os.chdir(path_change) 
	print('Current Path:', end='')
	print(os.getcwd())
	print('===========================================')
	print('Follow this step')
	print('(1) basic  (2) basic.basic  (3) from basic import basic')
	print('(4) x=basic()  start BasicPy by (5) x.program() ')
	print('')
	print('type exit to exit from x.program()')
	print('type x.help() for more information')
	print("Example program x.load('1to1000.py')")
	global line_num, program_text
	line_num = 10
	program_text = []
	program_text.append(0)
	def parseStr(self, x):
		''' parseStr returns integer or float and 
			if a given ASCII string cannot be 
			converted to none of them it returns 
			it untouched. 
			I founded this func in stackoverflow.com
			Q379906 answered Sep 28'11 by krzym  
		'''
		import string
		return x.isalpha() and x or x.isdigit() and \
				int(x) or x.isalnum() and x or \
				len(set(string.punctuation).intersection(x)) == 1 and \
				x.count('.') == 1 and float(x) or x

	def program(self):
		""" Program editor for python
			Version 1 and 2 standard interpreter console
			Version 3 Run on tk
		"""
		import tkinter as tk
		from tkinter import Menu
		from tkinter import messagebox
		import tkinter.scrolledtext as tkst
		import turtle
		global line_num,program_text
		win = tk.Tk()
		win.title('BasicPy 3.0 ARM Code Club Ratchaburi')
		frame1 = tk.Frame(
			master = win,
			bg = '#808000'
		)
		global editArea
		editArea = tkst.ScrolledText(
			master = frame1,
			wrap = tk.WORD,
			width = 50,
			height = 10,
		)
		global displayArea
		displayArea = tkst.ScrolledText(
			master = frame1,
			wrap = tk.WORD,
			width = 50,
			height = 1,
		)
		global tod
		tod = 0
		line_num = 10
		line_text = ''
		for l in program_text:
			if type(l) is str:
				line_text = str(line_num) + ' '
				line_text = line_text + l +'\n'
				line_num = line_num + 10
		if line_text == '':
			line_text = str(line_num)+' '
		else:
			line_text = line_text[0:len(line_text)-1]
			line_num = 10
		for l in range(10):
			program_text.append(l + (line_num - 9))
		frame1.pack(fill='both', expand='yes')
		displayArea.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
		displayArea.insert(tk.INSERT, 'type exit to exit from editor')
		editArea.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
		editArea.insert(tk.INSERT, line_text)
		def key(event):
			global tod
			if event.char!='':
				if ord(event.char)==8:
					tod = 1
				else:
					tod = 0
		editArea.bind('<Key>', key)
		def task():
			global line_num,tod,program_text
			data = editArea.get('1.0', 'end-1c')
			if data.endswith(' ') and tod == 0:
				data = data[0:len(data)-1]
			if data.endswith('\n') and tod == 0:
				atad = ''
				for i in range(len(data)):
					atad = atad + data[(i+1)*(-1)] 
					if atad[-1] == '\n' and i != 0:
						atad == atad[0:len(atad)-1]
						break
				data1 = ''
				data2 = ''
				data3 = ''
				for i in range(len(atad)):
					if data2 == '':
						data1 = data1 + atad[(i+1)*(-1)]
						if data1[-1] == ' ':
							data2 = data1
					else:
						data3 = data3 + atad[(i+1)*(-1)]						
				if data3 == 'exit\n':
					data4 = ''
					data5 = ''
					tod1 = 1
					for i in range(len(data)):
						if data[i]==' ' and tod1 == 1:
							data5 = data4
							data4 = ''
							tod1 = 0
						else:
							if data[i]=='\n':
								tod1 = 1
								if data4 != 'exit':
									n = self.parseStr(data5)
									if type(n) is int:
										line_num = n
									else:
										line_num = 10
									for l in range(10):
										program_text.append(l + (line_num - 9))
									if data4 == '':
										program_text[line_num]=line_num
									else:
										program_text[line_num]=data4
									data4 = ''
							else:
								data4 = data4 + data[i]
					win.destroy()
				if data2!='':
					line_num = int(data2) + 10
				try:
					if type(win.title()) is str:
						editArea.insert(tk.END, str(line_num)+' ')
						line_num = line_num + 10
				except:
					print('end of program editor')
			try:
				if type(win.title()) is str:
					win.after(2000,task)
			except:
				print('You can see your program by type x.list()')

		win.after(2000,task)
		win.mainloop()
	def list(self):
		l = 0
		for i in program_text:
			if type(i) is str:
				print(l, end='')
				print(' ', end='')
				print(i)
			l += 1
	def run(self):
		import time
		t = time.time()
		j = ''
		for i in program_text:
			if type(i) is str:
				j = j + i + '\n'
		if (j != ''):
			exec(j + '\n')
			j = ''
		return 'Run time ' + str(round(time.time()-t,2)) + ' seconds'

	def help(self):
		print('BasicPy version 3.0 Command References')
		print('======================================')
		print('x.cls()		| Clear Screen')
		print('x.new()		| Clear all of Line in Program')
		print('x.help()	| this module')
		print('x.program() 	| Start Line number Programming')
		print('				| type exit to exit from x.program()')
		print('example				| type line number such as 20 ')
		print('10 for i in range(10)		|	   to edit 20 program line')
		print('20 	print(i)		| type line number and enter')
		print("30 print('Ok')			|	   to clear that line")
		print('40 exit')
		print('')
		print('x.list()			| List Program')
		print('x.run()				| Run Program')
		print("x.load('file_name')		| Load Program")
		print("x.save('file_name')		| Save Program")
		print('quit()				| exit Python')
	def cls(self):
		import os
		os.system('cls')
		# print('>>> ', end='')
	def new(self):
		global line_num, program_text
		program_text = []
		program_text.append(0)
		line_num = 10
	def save(self, file_name):
		import os.path
		if os.path.isfile(file_name):
			print('Overwrite (y/n) ? ', end='')
			answer = input()
		else:
			answer = 'y'
		if answer == 'y' or answer == 'Y':
			f =open(file_name, 'w')
			for i in program_text:
				if type(i) is str:
					f.write(i + '\n')
			f.close()
	def load(self, file_name):
		global line_num, program_text
		self.new()
		f = open(file_name, 'r')
		read_text = f.readlines()
		for line in read_text:
			for l in range(10):
				program_text.append(l + (line_num - 9))
			program_text[line_num] = line[0:len(line)-1]			
			line_num = line_num + 10
		f.close()
