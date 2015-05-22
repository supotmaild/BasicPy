'''BasicPy 5.6 ARM Code Club Thailand 2015'''
'''stable version 29 April 2015'''
class basic:
	import os
	print('BasicPy 5.6 by ARM Code Club Thailand 2015')
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
	print('(1) from basic56 import basic')
	print('(2) x=basic()  start BasicPy by (3) x.program() ')
	print('')
	print('type exit to exit from x.program()')
	print('type x.help() for more information')
	print("Example program x.load('1to10_5.py')")
	print('x.run(0) to see real code x.run(1) to execute')
	print('')
	print('Please do not begin variable with letter "g"')
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
		win.title('BasicPy 5.6 ARM Code Club Ratchaburi')
		frame1 = tk.Frame(
			master = win,
			bg = 'DarkOrange1'
		)
		global editArea
		editArea = tkst.ScrolledText(
			master = frame1,
			wrap = tk.WORD,
			width = 100,
			height = 20,
		)
		global displayArea
		displayArea = tkst.ScrolledText(
			master = frame1,
			wrap = tk.WORD,
			width = 100,
			height = 1,
		)
		global tod,steve_job
		tod = 0
		line_num = 10
		line_text = ''
		for l in program_text:
			if type(l) is str:
				#line_text = line_text + str(line_num) + ' '
				line_text = line_text + l +'\n'
				#line_num = line_num + 10
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
			global line_num,tod,program_text,steve_job
			data = editArea.get('1.0', 'end-1c')
			line = 1
			for i in range(len(data)):
				if data[i]=='\n': line = line + 1
				try:
					if data[i]=='\n' and data[i+1]=='\n':
						for j in range(i+2,len(data)):
							if data[j]==' ':break
						n = self.parseStr(str(data[i+2:j]))
						data = data[0:i+1]+str(n+10)+' '+data[i+1:len(data)]
						line0 = 0
						for j in range(i):
							if data[j]=='\n' or line0==0:
								line0 = line0 + 1
								for k in range(j+1,i):
									if data[k]==' ':break
								if data[k+1:k+5]=='goto':
									for l in range(k+6,i):
										if data[l]=='\n':break
									nn = self.parseStr(str(data[k+6:l]))
									if nn>n:
										editArea.delete(str(line0)+'.0+'+str((k+7)-(j+1))+'c',str(line0)+'.0+'+str(l-j)+'c')
										editArea.insert(str(line0)+'.0+'+str((k+7)-(j+1))+'c',str(nn+10))
						line2 = line
						for j in range(i+1,len(data)):
							if data[j]=='\n': 
								line2 =line2+1
								for k in range(j+1,len(data)):
									if data[k]==' ':break
								nn = self.parseStr(str(data[j+1:k]))
								editArea.delete(str(line2)+'.0',str(line2)+'.0+'+str(k-(j+1))+'c')
								editArea.insert(str(line2)+'.0',str(nn+10))
						editArea.insert(str(line)+'.0',str(n)+' ')
						break
				except:
					pass
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
					data = editArea.get('1.0', 'end-1c')
					program_text = []
					for i in range(len(data)):
						if (data[i]==' ' or data[i]==chr(9)) and tod1 == 1:
							data5 = data4
							if data[i]==chr(9):
								data4 = chr(9)
							else:
								data4 = ''
							tod1 = 0
						else:
							if data[i]=='\n':
								n = self.parseStr(data5)
								if type(n) is int:
									line_num = n
								if i>0: 
									mx = data[i-1]
								else:
									mx = '\n' 
								if data4 != 'exit' and type(n) is int and tod1==0 and mx!='\n':
									if line_num+1>len(program_text):
										ll=len(program_text)
										for l in range(ll,line_num+1):
											program_text.append(l + ll)
									if data4 == '':
										program_text[line_num]=line_num
									else:
										''''Version 5 fill line_num into program_text'''
										program_text[line_num]=data5+' '+data4
									data4 = ''
								tod1 = 1
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
					steve_job = win.after(2000,task)
			except:
				print('You can see your program by type x.list()')
		def on_closing():
			global steve_job
			win.after_cancel(steve_job)
			win.destroy()

		steve_job = win.after(2000,task)
		# root.protocol from stackoverflow Q:111155 answer by Matt Gregory 21 Sep 2008
		win.protocol("WM_DELETE_WINDOW", on_closing)
		win.mainloop()
	def list(self):
		for i in program_text:
			if type(i) is str:
				print(i)
	def run(self, i):
		def real():
			basic_program_line = []
			python_program_line = []
			python_program_add = []
			python_program = []
			python_level = []
			goto = []
			goto_real = []
			goto_from = []
			goto_from_real = []
			goto_reach = []
			goto_loop = []
			line = 0
			for i in range(len(program_text)):
				if type(program_text[i])==str:
					for j in range(len(program_text[i])):
						if program_text[i][j]==' ': break
					for k in range(j+1,len(program_text[i])):
						if program_text[i][k]!=chr(9): break
					try: 
						if k!=len(program_text[i])-1:
							basic_program_line.append(int(program_text[i][0:j]))
							python_program_line.append(line)
							python_program_add.append(0)
							python_program.append(program_text[i][k:len(program_text[i])])
							python_level.append(k-(j+1))
					except:
						pass
					line = line + 1
			for i in range(len(python_program)):
				if python_program[i][0:4]=='goto':
					gt = int(python_program[i][5:len(python_program[i])])
					for j in range(len(python_program)):
						if basic_program_line[j]==gt: break
					goto.append(gt)
					goto_real.append(j)
					goto_from.append(basic_program_line[i])
					goto_from_real.append(python_program_line[i])
					goto_reach.append(False)
					goto_loop.append(False)
			g=1
			for i in range(len(goto)):
				for j in range(len(python_program)):
					if goto_from_real[i]==python_program_line[j] and python_program_add[j]==0:
						# 10 goto 20
						if goto_real[i]>goto_from_real[i]:
							ol=python_level[j]
							ll=python_level[j]
							python_program[j]='g'+str(g)+'=True #'+str(goto[i])
							basic_program_line.insert(j+1,0)
							python_program_line.insert(j+1,python_program_line[j]+1)
							python_program_add.insert(j+1,g)
							python_program.insert(j+1,'if not(g'+str(g)+'):')
							python_level.insert(j+1,ll)
							ll=ll+1
							for k in range(j+2,len(python_program)):
								if (ol<=python_level[k] or (ol==python_level[k] and python_program[k][0:5]=='else:'))and python_program_line[k]<goto_real[i]:
									python_level[k]=python_level[k]+1
								else: break
							g=g+1
							break
					if goto_real[i]==python_program_line[j] and python_program_add[j]==0:
						# 20 goto 10
						if goto_from_real[i]>goto_real[i]:
							same_loop = False
							for ss in range(len(python_program)):
								# \ from stackoverflow Q:53162 answer by Harley Holcombe 9 Sep 2008
								if python_program_line[ss]==python_program_line[j] \
								and python_program_add[ss]!=0 and python_program[ss][0:11]=='while True:':
									same_loop = True
									break
							if not(same_loop):
								basic_program_line.insert(j,0)
								python_program_line.insert(j,python_program_line[j])
								python_program_add.insert(j,g)
								python_program.insert(j,'while True: #goto'+str(goto[i]))
								jj=python_level[j]
								python_level.insert(j,python_level[j])
								for l in range(j+1,len(python_program)):
									if jj<=python_level[l]:
										python_level[l]=python_level[l]+1
									else: break
							for k in range(j+2,len(python_program)):
								if goto_from_real[i]==python_program_line[k] and python_program_add[k]==0: break
							ol=python_level[k]
							ll=python_level[k]
							python_program[k]='g'+str(g)+'=True #'+str(goto[i])
							if python_level[k]!=0:
								basic_program_line.insert(k+1,0)
								python_program_line.insert(k+1,python_program_line[k]+1)
								python_program_add.insert(k+1,g)
								python_program.insert(k+1,'if not(g'+str(g)+'):')
								python_level.insert(k+1,ll)
								ll=ll+1
								g=g+1
								for l in range(k+2,len(python_program)):
									if ol<=python_level[l]:
										python_level[l]=python_level[l]+1
									else: break
							break
			basic_program_line.insert(0,0)
			python_program_line.insert(0,0)
			python_program.insert(0,'while True: #Super Loop')
			python_level.insert(0,0)
			for j in range(1,len(python_program)):
				python_level[j]=python_level[j]+1
			python_loop = []
			python_loop_level = []
			python_loop_start = []
			python_loop_end = []
			for j in range(len(python_program)):
				if python_program[j][0:3]=='for' or python_program[j][0:5]=='While':
					python_loop.append('for')
					python_loop_level.append(python_level[j])
					python_loop_start.append(python_program_line[j])
					for k in range(j+1,len(python_program)):
						if python_level[k]<=python_level[j] and python_program[k][0:5]!='else:': break
					python_loop_end.append(python_program_line[k])
				elif python_program[j][0:2]=='if':
					python_loop.append('if')
					python_loop_level.append(python_level[j])
					python_loop_start.append(python_program_line[j])
					for k in range(j+1,len(python_program)):
						if python_level[k]<=python_level[j] and python_program[k][0:5]!='else:': break
					python_loop_end.append(python_program_line[k])
#			for j in range(len(python_loop)):
#				print(python_loop_level[j],end='')
#				print(' ',end='')
#				print(python_loop[j],end='')
#				print(' ',end='')
#				print(python_loop_start[j],end='')
#				print(' ',end='')
#				print(python_loop_end[j])
			jo=0
			while True:
				ByPass = True
				for j in range(jo,len(python_program)):
					gg=''
					if python_program[j][0:3]=='for' or python_program[j][0:5]=='while':
						jo=j+1
						ol=python_level[j]
						for kk in range(j+1,len(python_program)):
							if python_level[kk]<=ol: break
						for jj in range(len(goto)):
							if goto_from_real[jj]>python_program_line[j] and goto_real[jj]>=python_program_line[kk]:
								if gg=='':
									gg = 'g'+str(jj+1)
								else:
									gg = gg+' or g'+str(jj+1)
						if gg!='' and ol+1>1:
							basic_program_line.insert(kk,0)
							python_program_line.insert(kk,python_program_line[kk])
							python_program.insert(kk,'if '+gg+': break')
							python_level.insert(kk,ol+1)
							ByPass = False
				if ByPass: break
			if len(python_level)>0:
				ol=python_level[0]
			else:
				ol=0
			loop_now=''
			level_now=0
			python_add_line=[]
			python_add=[]
			python_add_level=[]
			for j in range(len(python_program)):
				if python_level[j]<ol and loop_now=='if':
					plus=0
					for k in range(len(python_add)):
						if python_add_line[k]>=j: 
							python_add_line[k]=python_add_line[k]+1
						else:
							plus=plus+1
					python_add_line.append(j+plus)
					python_add.append('pass')
					python_add_level.append(level_now+1)
				ol=python_level[j]	
				if python_program[j][0:2]=='if' and python_program[j][-5:]!='break': 
					loop_now='if'
					level_now=python_level[j]
				else:
					loop_now=''			
			for j in range(len(python_add)):
				basic_program_line.insert(python_add_line[j],0)
				python_program_line.insert(python_add_line[j],python_program_line[python_add_line[j]])
				python_program.insert(python_add_line[j],python_add[j])
				python_level.insert(python_add_line[j],python_add_level[j])

			python_add_line=[]
			python_add=[]
			python_add_level=[]
			sb = ''
			for j in range(len(goto)):
				super_break=False
				for k in range(len(python_program)):
					if python_program_line[k]>=goto_from_real[j]: break
				for kk in range(k,len(python_program)):
					jj=1
					if j>10: jj=2
					if j>100: jj=3
					if python_program[kk][0:5]!='while' and python_program[kk][0:3]!='for' and \
					python_program[kk][0:2]!='if' and python_program[kk][0:4]!='pass' and \
					python_program[kk][0:4]!='else' and python_program[kk][0:4]!='elif':
						ol=python_level[kk]
						for kkk in range(kk,len(python_program)):
							if python_level[kkk]<ol or python_level[kkk]==1: break
						if (python_program_line[kkk]<goto_real[j] and goto_real[j]>goto_from_real[j]) or \
						(python_program_line[kkk]>goto_real[j] and goto_real[j]<goto_from_real[j]):
							aa=(-1)
							find=0
							for aa in range(len(python_add)):
								if python_add_line[aa]==kk:
									find=1 
									break
							if find==1:
								python_add[aa]=python_add[aa][0:len(python_add[aa])-5]+' and not(g'+str(j+1)+'): #if'
							else:
								python_add_line.append(kk)
								python_add.append('if not(g'+str(j+1)+'): #if')
								python_add_level.append(python_level[kk])
					if python_program[kk][0:4+jj]=='if g'+str(j+1):
						ol=python_level[kk]
						for kkk in range(kk,len(python_program)):
							if python_level[kkk]<ol: break
						if python_program_line[kkk]>=goto_real[j] and goto_real[j]>goto_from_real[j]:
							super_break=True
							#break						
					if python_program[kk][0:8+jj]=='if not(g'+str(j+1):
						ol=python_level[kk]
						for kkk in range(kk,len(python_program)):
							if python_level[kkk]<ol: break
						if python_program_line[kkk]>=goto_real[j] and goto_real[j]>goto_from_real[j]:
							super_break=True
							#break
					if python_program[kk][0:5]=='while' or python_program[kk][0:3]=='for' or \
					(python_program[kk][0:2]=='if' and python_program[kk][0:8+jj]!='if not(g'+str(j+1)):
						ol=python_level[kk]
						for kkk in range(kk,len(python_program)):
							if python_level[kkk]<ol: break
						if python_program_line[kkk]<goto_real[j]:
							for ss in range(len(python_program[kk])):
								if python_program[kk][ss]==':': break
							if python_program[kk][0:2]=='if':
								if python_program[kk][0:8]=='if not(g':
									python_program[kk]=\
									python_program[kk][0:ss]+' and not(g'+str(j+1)+'): #if'
								elif python_program[kk][0:4]=='if g':
									pass
								#	python_program[kk]=\
								#	python_program[kk][0:ss]+' or g'+str(j+1)+': break'									
								else:
									if python_program[kk][3]=='(':
										python_program[kk]=\
										python_program[kk][0:ss]+' and not(g'+str(j+1)+'):'
									else:
										python_program[kk]=python_program[kk][0:3]+'('+\
										python_program[kk][3:ss]+') and not(g'+str(j+1)+'):'
							elif python_program[kk][0:5]=='while' and python_program[kk][12:23]!='#Super Loop':
								python_program[kk]=\
								python_program[kk][0:ss]+' and not(g'+str(j+1)+'): #while'
							elif python_program[kk][0:3]=='for':
								python_program[kk]=\
								python_program[kk][0:ss]+' and not(g'+str(j+1)+'): #for'
					if python_program_line[kk]>=goto_real[j] and goto_real[j]>goto_from_real[j]:
						super_break=True
						#break

				if not(super_break):
					if sb=='':
						sb = 'g'+str(j+1)
					else:
						sb = sb+' or g'+str(j+1)
					for kkk in range(len(python_program)): # Knock Out Loop
						if python_program[kkk][0:5]!='while' and python_program[kkk][0:3]!='for' and \
						python_program[kkk][0:2]!='if' and python_program[kkk][0:4]!='pass' and \
						python_program[kkk][0:4]!='else' and python_program[kkk][0:4]!='elif':
							if python_program_line[kkk]<goto_real[j]:
								aa=(-1)
								find=0
								for aa in range(len(python_add)):
									if python_add_line[aa]==kkk:
										find=1 
										break
								if find==1:
									python_add[aa]=python_add[aa][0:len(python_add[aa])-5]+' and not(g'+str(j+1)+'): #if'
								else:
									python_add_line.append(kkk)
									python_add.append('if not(g'+str(j+1)+'): #if')
									python_add_level.append(python_level[kkk])
						if python_program[kkk][0:5]=='while' or python_program[kkk][0:3]=='for' or \
						(python_program[kkk][0:2]=='if' and python_program[kkk][0:8+jj]!='if not(g'+str(j+1)):
							ol=python_level[kkk]
							for kkkk in range(kkk,len(python_program)):
								if python_level[kkkk]<ol: break
							if python_program_line[kkkk]<goto_real[j]:
								for ss in range(len(python_program[kkk])):
									if python_program[kkk][ss]==':': break
								for sss in range(len(python_program[kkk])):
									if python_program[kkk][sss]=='#': break
								if python_program[kkk][0:2]=='if':
									if python_program[kkk][0:8]=='if not(g':
										python_program[kkk]=\
										python_program[kkk][0:ss]+' and not(g'+str(j+1)+'): #if'
									elif python_program[kkk][0:4]=='if g':
										pass
									#	python_program[kkk]=\
									#	python_program[kkk][0:ss]+' or g'+str(j+1)+': break'									
									else:
										if python_program[kkk][3]=='(':
	 										python_program[kkk]=\
											python_program[kkk][0:ss]+' and not(g'+str(j+1)+'):'
										else:
											python_program[kkk]=python_program[kkk][0:3]+'('+\
											python_program[kkk][3:ss]+') and not(g'+str(j+1)+'):'
								elif python_program[kkk][0:5]=='while' and python_program[kkk][12:23]!='#Super Loop':
									python_program[kkk]=\
									python_program[kkk][0:ss]+' and not(g'+str(j+1)+'): #while'
								elif python_program[kkk][0:3]=='for':
									python_program[kkk]=\
									python_program[kkk][0:ss]+' and not(g'+str(j+1)+'): #for'

			poppop=[]
			for j in range(len(python_add)):
				popup=1
				for jj in range(j+1,len(python_add)):
					if python_add_level[jj]==python_add_level[j] and \
					python_add[jj]==python_add[j]:
						pp=0
						if python_add_line[jj]>python_add_line[j]:
							stj=python_add_line[j]
							enj=python_add_line[jj]
						else:
							stj=python_add_line[jj]
							enj=python_add_line[j]
						if stj==enj:
							pp=1
						else:
							ol=python_level[stj]
							for cc in range(stj,enj):
								if python_level[cc]!=ol:
									pp=1
									break
						for p in range(len(poppop)):
							if poppop[p]==jj:
								pp=1
								break
						if pp==0:
							poppop.append(jj)
						popup=popup+1
			for j in range(len(poppop)):
				python_add_line.pop(poppop[j])
				python_add.pop(poppop[j])
				python_add_level.pop(poppop[j])
				for p in range(j+1,len(poppop)):
					if poppop[p]>j:
						poppop[p]=poppop[p]-1
			for j in range(len(python_add)):
				for jj in range(j+1,len(python_add)):
					if python_add_line[jj]>python_add_line[j]:
						python_add_line[jj]=python_add_line[jj]+1
			for j in range(len(python_add)):
				basic_program_line.insert(python_add_line[j],0)
				python_program_line.insert(python_add_line[j],python_program_line[python_add_line[j]])
				python_program.insert(python_add_line[j],python_add[j])
				python_level.insert(python_add_line[j],python_add_level[j])
			python_add_line=[]
			python_add=[]
			python_add_level=[]
			for j in range(len(python_program)):
				if python_program[j][-4:]=='#for':
					for kk in range(len(python_program[j])):
						if python_program[j][kk:kk+9]=='and not(g': break
					if python_program[j+1]=='if '+python_program[j][kk+4:-5]+' #if':
						pass
					else:
						python_add_line.append(j+1)
						python_add.append('if '+python_program[j][kk+4:-5]+' #if')				
						python_add_level.append(python_level[j]+1)
					python_program[j]=python_program[j][0:kk-1]+':'
				if python_program[j][-6:]=='#while':
					for kk in range(len(python_program[j])):
						if python_program[j][kk:kk+9]=='and not(g': break
					if python_program[j+1]=='if '+python_program[j][kk+4:-7]+' #if':
						pass
					else:
						python_add_line.append(j+1)
						python_add.append('if '+python_program[j][kk+4:-7]+' #if')				
						python_add_level.append(python_level[j]+1)
					python_program[j]=python_program[j][0:kk-1]+':'
			for j in range(len(python_add)):
				for jj in range(j+1,len(python_add)):
					if python_add_line[jj]>python_add_line[j]:
						python_add_line[jj]=python_add_line[jj]+1
			for j in range(len(python_add)):
				basic_program_line.insert(python_add_line[j],0)
				python_program_line.insert(python_add_line[j],python_program_line[python_add_line[j]])
				python_program.insert(python_add_line[j],python_add[j])
				python_level.insert(python_add_line[j],python_add_level[j])
			for j in range(len(python_program)):
				if python_program[j][-3:]=='#if':
					python_program[j]=python_program[j][0:-4]
					ol=python_level[j]
					for jj in range(j+1,len(python_program)):
						if python_level[jj]<ol:
							break
						elif python_program[jj][0:2]=='if' and python_level[jj]==ol:
							break
						elif python_program[jj][0:3]=='for' and python_level[jj]==ol:
							break
						elif python_program[jj][0:5]=='while' and python_level[jj]==ol:
							break
						else:
							python_level[jj]=python_level[jj]+1

			for j in range(len(goto)):
				gx=goto_real[j]
				for k in range(len(python_program)):
					if python_program_line[k]==goto_real[j]:
						for kk in range(k+1,len(python_program)):
							if python_program_line[kk]!=gx or \
							python_program[kk][0:8]=='if not(g': break
						if not(goto_reach[j]):
							if kk+1>=len(python_program):
								python_program_line.append(python_program_line[kk])
								python_program.append('g'+str(j+1)+'=False')
								python_level.append(1)
							else:
								python_program_line.insert(kk+1,python_program_line[kk+1])
								python_program.insert(kk+1,'g'+str(j+1)+'=False')
								python_level.insert(kk+1,python_level[kk+1])
							goto_reach[j]=True

			for j in range(len(goto)):
				basic_program_line.insert(0,0)
				python_program_line.insert(0,python_program_line[0])
				python_program.insert(0,'g'+str(len(goto)-j)+'=False')
				python_level.insert(0,0)				

			basic_program_line.append(0)
			python_program_line.append(python_program_line[len(python_program_line)-1])
			python_program.append('if '+sb+': continue')
			python_level.append(1)
			basic_program_line.append(0)
			python_program_line.append(python_program_line[len(python_program_line)-1])
			python_program.append('break')
			python_level.append(1)
			python_text = ''
			for j in range(len(python_program)):
				if python_program[j][-1:]==':' and \
				(python_program[j+1][0:2]=='if' or python_program[j+1][0:3]=='for' or \
				python_program[j+1][0:5]=='while'):
					basic_program_line.insert(j+1,0)
					python_program_line.insert(j+1,python_program_line[j])
					python_program.insert(j+1,'pass')
					python_level.insert(j+1,python_level[j]+1)

			for j in range(len(python_program)-1):
				indent=0
				if python_program[j][0:2]!='if' and python_program[j][0:3]!='for' and \
				python_program[j][0:5]!='while' and python_program[j][0:4]!='else' and \
				python_program[j][0:4]!='elif':
					indent=(python_level[j+1]-python_level[j])
				if indent>0 and python_level[j]<python_level[j+1]:
					for k in range(j+1,len(python_program)):
						if python_level[k]<=python_level[j]: break
						python_level[k]=python_level[k]-indent

			for j in range(len(python_program)-1):
				indent=1
				if (python_program[j][0:2]=='if' or python_program[j][0:3]=='for' or \
				python_program[j][0:5]=='while' or python_program[j][0:4]=='else' or \
				python_program[j][0:4]=='elif') and python_program[j][-1]==':':
					indent=(python_level[j+1]-python_level[j])
				if indent==0 and python_level[j]==python_level[j+1]:
					for k in range(j+1,len(python_program)):
						if python_level[k]!=python_level[j] or \
						python_program[k][0:2]=='if' or python_program[k][0:3]=='for' or \
						python_program[k][0:5]=='while' or python_program[k][0:4]=='else' or \
						python_program[k][0:4]=='elif':
							break
						python_level[k]=python_level[k]+1

			for i in range(len(python_program)):
				nn=''
				for j in range(python_level[i]): nn=nn+'  '
				python_text=python_text+nn+str(python_program[i])+'\n'
			return python_text
		#def Run
		import time
		t = time.time()
		'''Version 5 Execute by call real function'''
		if i == 0:
			print(real())
		else:
			exec(real())
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
		print('x.list()		| List Program')
		print('x.run(0)		| See Python Compile Code from Basic Program')
		print('x.run(1)             | Run Program')
		print("x.load('file_name')		| Load Program")
		print("x.save('file_name')		| Save Program")
		print('quit()				| exit Python')
		print('')
		print('Do not use g letter variable in program')
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
			if line[-1]!='\n':
				program_text[line_num] = line							
			else:
				program_text[line_num] = line[0:len(line)-1]			
			line_num = line_num + 10
		f.close()
