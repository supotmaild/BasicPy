'''BasicPy 2.0 ARM Code Club Thailand 2015'''
'''stable version 3 April 2015'''
class basic:
	import os	
	print('BasicPy 2.0 by ARM Code Club Thailand 2015')
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
		"""
		global line_num
		line_text = ''
		while line_text != 'exit':
			print(line_num, end='')
			for l in range(10):
				program_text.append(l + (line_num - 9))
			print(' ', end='')
			line_text=input()
			n = self.parseStr(line_text)
			if type(n) is int:
				line_num = n 
			elif line_text != 'exit':
				if line_text == '':
					program_text[line_num]=line_num
				else:
					program_text[line_num]=line_text
				line_num = line_num + 10
	def list(self):
		l = 0
		for i in program_text:
			if type(i) is str:
				print(l, end='')
				print(' ', end='')
				print(i)
			l += 1
	def run(self):
		j = ''
		for i in program_text:
			if type(i) is str:
				if i[-1] == ':':
					j = j + i
				elif (i[0] == ' ') or (ord(i[0]) == 9):
					j = j + i + ';'
				else:
					exec(j)
					j = ''
					exec(i)
	'''Version 2.0'''
	def help(self):
		print('BasicPy version 2.0 Command References')
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
