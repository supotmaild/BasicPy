'''BasicPy 1.0 ARM Code Club Thailand 2015'''
class basic:
	global line_num, program_text
	line_num = 10
	program_text = []
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
			for l in range(line_num + 1):
				program_text.append(l)
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
				j = j + i + '\n'
		if (j != ''):
			exec(j + '\n')
			j = ''
	
