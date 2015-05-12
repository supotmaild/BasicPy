'''BasicPy 5.5 ARM Code Club Thailand 2015'''
'''stable version 29 April 2015'''
class basic:
	import os
	print('BasicPy 5.5 by ARM Code Club Thailand 2015')
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
	print('(1) from basic55 import basic')
	print('(2) x=basic()  start BasicPy by (3) x.program() ')
	print('')
	print('type exit to exit from x.program()')
	print('type x.help() for more information')
	print("Example program x.load('1to10_5.py')")
	print('x.run(0) to see real code x.run(1) to execute')
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
		win.title('BasicPy 5.5 ARM Code Club Ratchaburi')
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
										''''Version 5 fill line_num into program_text'''
										program_text[line_num]=data5+' '+data4
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
			def r_for():
				if goto_from[k]==basic_program_line[j] and goto[k]<basic_program_line[j]:
					if goto[k]<basic_program_line[i]:goto_upper[k]='for'
					same_loop = False
					for tl in range(len(too_loop)):
						if too_loop[tl]==goto_real[k]:
							same_loop = True
							break
					if not(same_loop):
						python_add_line.append(goto_real[k])
						python_add.append('While True: #'+str(goto[k]))
						python_add_level.append(python_level[goto_real[k]])
						python_add_last.append('')
						too_loop.append(goto_real[k])
					python_add_line.append(goto_from_real[k]+1)
					python_add.append('continue')
					python_add_level.append(python_level[goto_from_real[k]])
					python_add_last.append('')
					for jj in range(j+1,len(python_program)):
						if python_level[jj] <= python_level[i]:
							bbb = ''
							for bb in range(len(break_end)):
								if break_end_line[bb]==jj:bbb=bbb+'not(g'+str(break_end[bb])+') and '
							if bbb == '':
								python_add_line.append(jj)
								python_add.append('if not(g'+str(k)+'):break')
								python_add_level.append(python_level[i]+1)
								python_add_last.append('')
							else:
								for sb in range(len(python_add)):
									if python_add_line[sb]==jj and python_add[sb][-6:len(python_add[sb])]==':break':
										python_add[sb]='if '+ bbb +'not(g'+str(k)+'):break'
										break
							break_end_line.append(jj)
							break_end.append(k)
							break
				elif goto_from[k]==basic_program_line[j] and goto[k]>basic_program_line[j] and goto[k]>basic_program_line[i]:
					if goto[k]>basic_program_line[i]:goto_lower[k]='for'
					if j+1<len(python_level):
						if python_level[j+1]>=python_level[j]:
							python_add_line.append(j)
							python_add.append('break')
							python_add_level.append(python_level[j])
							python_add_last.append('')
			def r_if():
				if goto_from[k]==basic_program_line[j] and goto[k]<basic_program_line[j]:
					if goto[k]<basic_program_line[i]:goto_upper[k]='if'
					same_loop = False
					for tl in range(len(too_loop)):
						if too_loop[tl]==goto_real[k]:
							same_loop = True
							break
					if not(same_loop):
						python_add_line.append(goto_real[k])
						python_add.append('While True: #'+str(goto[k]))
						python_add_level.append(python_level[goto_real[k]])
						python_add_last.append('')
						too_loop.append(goto_real[k])
					if python_end_loop[goto_from_real[k]]=='run':
						python_add_line.append(goto_from_real[k]+1)
						python_add.append('if not(g'+str(k)+'):')
						python_add_level.append(python_level[goto_from_real[k]])
						python_add_last.append('')
				elif goto_from[k]==basic_program_line[j] and goto[k]>basic_program_line[j] and goto[k]>basic_program_line[i]:
					if goto[k]>basic_program_line[i]:goto_lower[k]='if'
					if j+1<len(python_level):
						if python_level[j+1]>=python_level[j]:
							python_add_line.append(j)
							python_add.append('if not(g'+str(k)+'):')
							python_add_level.append(python_level[j])
							python_add_last.append('')
			basic_program_line = []
			python_program = []
			python_level = []
			g = 0
			goto = []
			goto_real = []
			goto_from = []
			goto_from_real = []
			goto_upper = []
			goto_lower = []
			for i in program_text:
				if type(i) != str:
					continue
				for j in range(len(i)):
					if i[j]==' ':break
				basic_program_line.append(int(i[0:j]))
				python_program.append(i[j+1:len(i)])
			for i in range(len(python_program)):
				level = 0
				for j in range(len(python_program[i])):
					if python_program[i][j] != chr(9):break
					level = level+1
				python_program[i] = python_program[i][j:len(python_program[i])]
				if str(python_program[i][0:4]).lower() == 'goto':
					goto.append(int(python_program[i][5:len(python_program[i])]))
					for k in range(len(basic_program_line)):
						if int(python_program[i][5:len(python_program[i])]) == basic_program_line[k]: break
					goto_real.append(k)
					goto_from.append(basic_program_line[i])
					goto_from_real.append(i)
					goto_lower.append('')
					goto_upper.append('')
					python_program[i] = 'g'+str(g)+' = True #goto '+str(python_program[i][5:len(python_program[i])])
					g = g + 1
				python_level.append(level)
			python_add_line = []
			python_add = []
			python_add_level = []
			python_add_last = []
			too_loop = []
			break_end_line = []
			break_end = []
			loop_track = []
			loop_track_start = []
			loop_track_check = 'main'
			loop_track_start_check = 0
			python_end_loop = []
			for i in range(len(python_program)):
				python_end_loop.append('run')
				if i>1:
					if python_level[i]<python_level[i-1]:
						python_end_loop[i] = 'end'
			for i in range(len(python_program)):
				loop_track_start.append(loop_track_start_check)
				loop_track.append(loop_track_check)
				if python_level[i]==0:
					for k in range(len(goto)):
						if python_level[goto_real[k]]==0 and python_level[goto_from_real[k]]==0 and goto[k]==basic_program_line[i] and goto_from[k]>goto[k]:
							same_loop = False
							for tl in range(len(too_loop)):
								if too_loop[tl]==goto_real[i]:
									same_loop = True
									break
							if not(same_loop):
								python_add_line.append(goto_real[k])
								python_add.append('While True: #'+str(goto[k]))
								python_add_level.append(python_level[goto_real[k]])
								python_add_last.append('')
								too_loop.append(goto_real[k])
						if python_level[goto_real[k]]==0 and python_level[goto_from_real[k]]==0 and goto_from[k]==basic_program_line[i] and goto_from[k]>goto[k]:
							python_add_line.append(goto_from_real[k])
							python_add.append('continue')
							python_add_level.append(python_level[goto_from_real[k]])
							python_add_last.append('last')
						if python_level[goto_real[k]]==0 and python_level[goto_from_real[k]]==0 and goto_from[k]==basic_program_line[i] and goto_from[k]<goto[k]:
							python_add_line.append(goto_from_real[k])
							python_add.append('if not(g'+str(k)+'):')
							python_add_level.append(python_level[goto_from_real[k]])
							python_add_last.append('')
							goto_lower[k]='if'
				if str(python_program[i][0:3]).lower() == 'for' or str(python_program[i][0:3]).lower() == 'while':
					loop_track[i] = 'for'
					loop_track_start[i] = i
					loop_track_check = 'for'
					loop_track_start_check = i
					for j in range(i+1,len(python_program)):
						if python_level[j] <= python_level[i]:break
						if python_level[j] > python_level[i]+1:continue
						for k in range(len(goto)):
							r_for()
							if goto_from[k]==basic_program_line[j] and goto_upper[k] == 'for' and i>=1:
								superloop=i
								while True:
									for t in range(superloop+1,len(python_program)):
										if python_level[t] > python_level[superloop]+1:continue
										if python_level[t] <= python_level[superloop]:
											if loop_track[superloop-1]=='for':
												if python_end_loop[goto_from_real[k]]=='run':
													python_add_line.append(t)
													python_add.append('else: break')
													python_add_level.append(python_level[superloop]+1)									
													python_add_last.append('')
												python_add_line.insert(0,t)
												if loop_track_start[superloop-1]<=goto_real[k]:
													python_add.insert(0,'if g'+str(k)+':continue')
												else:
													python_add.insert(0,'if g'+str(k)+':break')
												python_add_level.insert(0,python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
											if loop_track[superloop-1]=='if':
												python_add_line.append(t)
												if loop_track_start[superloop-1]<=goto_real[k]:
													python_add.append('if g'+str(k)+':continue')
												else:
													python_add.append('if not(g'+str(k)+'):')
												python_add_level.append(python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
									superloop=loop_track_start[superloop-1]
									if loop_track_start[superloop]==0 or goto_real[k]>superloop: break
							elif goto_from[k]==basic_program_line[j] and goto_lower[k] == 'for' and i>=1:
								superloop=i
								while True:
									for t in range(superloop+1,len(python_program)):
										if python_level[t] > python_level[superloop]+1:continue
										if python_level[t] <= python_level[superloop]:
											if loop_track[superloop-1]=='for':
												if python_end_loop[goto_from_real[k]]=='run':
													python_add_line.append(t)
													python_add.append('else: break')
													python_add_level.append(python_level[superloop]+1)									
													python_add_last.append('')
												python_add_line.insert(0,t)
												if t<goto_real[k]:
													python_add.insert(0,'if g'+str(k)+':break')
												python_add_level.insert(0,python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
											if loop_track[superloop-1]=='if':
												python_add_line.append(t)
												if t<goto_real[k]:
													python_add.append('if not(g'+str(k)+'):')
												python_add_level.append(python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
									superloop=loop_track_start[superloop-1]
									if loop_track_start[superloop]==0 or goto_real[k]>superloop: break
				if str(python_program[i][0:2]).lower() == 'if':
					loop_track[i] = 'if'
					loop_track_start[i] = i
					loop_track_check = 'if'
					loop_track_start_check = i
					for j in range(i+1,len(python_program)):
						if python_level[j] <= python_level[i]:break
						if python_level[j] > python_level[i]+1:continue
						for k in range(len(goto)):
							r_if()
							if goto_from[k]==basic_program_line[j] and goto_upper[k] == 'if' and i>=1:
								superloop=i
								while True:
									for t in range(superloop+1,len(python_program)):
										if python_level[t] > python_level[superloop]+1:continue
										if python_level[t] <= python_level[superloop]:
											if loop_track[superloop-1]=='for':
												if python_end_loop[goto_from_real[k]]=='run':
													python_add_line.append(t)
													python_add.append('else: break')
													python_add_level.append(python_level[superloop]+1)
													python_add_last.append('')				
												python_add_line.insert(0,t)
												if loop_track_start[superloop-1]<=goto_real[k]:
													python_add.insert(0,'if g'+str(k)+':continue')
												else:
													python_add.insert(0,'if g'+str(k)+':break')
												python_add_level.insert(0,python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
											if loop_track[superloop-1]=='if':
												python_add_line.append(t)
												if loop_track_start[superloop-1]<=goto_real[k]:
													python_add.append('if g'+str(k)+':continue')
												else:
													python_add.append('if not(g'+str(k)+'):')
												python_add_level.append(python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
									superloop=loop_track_start[superloop-1]
									if loop_track_start[superloop]==0 or goto_real[k]>superloop: break
							elif goto_from[k]==basic_program_line[j] and goto_upper[k] == 'if' and i>=1:
								superloop=i
								while True:
									for t in range(superloop+1,len(python_program)):
										if python_level[t] > python_level[superloop]+1:continue
										if python_level[t] <= python_level[superloop]:
											if loop_track[superloop-1]=='for':
												if python_end_loop[goto_from_real[k]]=='run':
													python_add_line.append(t)
													python_add.append('else: break')
													python_add_level.append(python_level[superloop]+1)
													python_add_last.append('')						
												python_add_line.insert(0,t)
												if t<goto_real[k]:
													python_add.insert(0,'if g'+str(k)+':break')
												python_add_level.insert(0,python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
											if loop_track[superloop-1]=='if':
												python_add_line.append(t)
												if t<goto_real[k]:
													python_add.append('if not(g'+str(k)+'):')
												python_add_level.append(python_level[loop_track_start[superloop-1]]+1)
												python_add_last.append('')
												break
									superloop=loop_track_start[superloop-1]
									if loop_track_start[superloop]==0 or goto_real[k]>superloop: break
			# reverse python_add
			pline=[]
			padd=[]
			plevel=[]
			plast=[]
			for i in range(len(python_add)):
				if i>0:
					if python_add[len(python_add)-(i+1)]=='else: break':
						for j in range(len(pline)):
							if padd[j]!='else: break': break
						if padd[j]!='else: break':
							pline.append(pline[j])
							padd.append(padd[j])
							plevel.append(plevel[j])
							plast.append(plast[j])
						pline[0] = python_add_line[len(python_add)-(i+1)]
						padd[0] = python_add[len(python_add)-(i+1)]
						plevel[0] = python_add_level[len(python_add)-(i+1)]
						plast[0] = python_add_last[len(python_add)-(i+1)]
					else:				
						pline.append(python_add_line[len(python_add)-(i+1)])
						padd.append(python_add[len(python_add)-(i+1)])
						plevel.append(python_add_level[len(python_add)-(i+1)])
						plast.append(python_add_last[len(python_add)-(i+1)])
				else:
					pline.append(python_add_line[len(python_add)-(i+1)])
					padd.append(python_add[len(python_add)-(i+1)])
					plevel.append(python_add_level[len(python_add)-(i+1)])
					plast.append(python_add_last[len(python_add)-(i+1)])
			python_add_line=pline
			python_add=padd
			python_add_level=plevel
			python_add_last=plast
			while True:
				no_cut = True
				for i in range(len(python_add)):
					if python_add_line[i]<len(python_program):
						if python_add[i][0:8]=='if not(g' and python_add[i][-5:len(python_add[i])]!='break' and python_level[python_add_line[i]]<python_add_level[i]:
							# pop from stackoverflow.com Q:627435 answer by Jarret Hardie 9 Mar 2009
							python_add_line.pop(i)
							python_add.pop(i)
							python_add_level.pop(i)
							python_add_last.pop(i)
							no_cut = False
							break
				if no_cut: break
			python_program_oldline=[]
			for i in range(len(python_program)):
				python_program_oldline.append(i)
			for i in range(len(python_add)):
				if python_add_last[i]=='last':
					if python_add_line[i]==len(python_program_oldline)-1:
						python_program.insert(len(python_program),python_add[i])
						python_level.insert(len(python_program),python_add_level[i])
					else:
						python_program.insert(python_program_oldline[python_add_line[i]+1]-1,python_add[i])
						python_level.insert(python_program_oldline[python_add_line[i]+1]-1,python_add_level[i])
				else:
					python_program.insert(python_program_oldline[python_add_line[i]],python_add[i])
					python_level.insert(python_program_oldline[python_add_line[i]],python_add_level[i])
				if python_add[i][-8:len(python_add[i])]!='continue' and python_add[i][-5:len(python_add[i])]!='break':
					for j in range(python_program_oldline[python_add_line[i]]+1,len(python_program)):
						if python_level[j]<python_add_level[i] and python_program[j][0:4]!='else' and python_program[j][0:4]!='elif' : break
						if python_add_level[i]==python_level[j] and python_program[j][0:4]=='else':
							pass
						else:
							block_level = False
							for gg in range(len(goto_real)):
								if  goto_from_real[gg]==python_add_line[i] and (goto_lower[gg]=='for' or goto_lower[gg]=='if') and python_program_oldline[goto_real[gg]]<j:
									block_level = True
							if not(block_level): python_level[j] = python_level[j]+1
					for j in range(i+1,len(python_add)):
						lower=False
						if python_add_line[j]>python_add_line[i]:
							if python_program_oldline[python_add_line[j]]+1<len(python_level):
								l_start = python_level[python_program_oldline[python_add_line[i]]+1]
								for k in range(python_program_oldline[python_add_line[i]]+1,python_program_oldline[python_add_line[j]]+1):
									if python_level[k]<l_start:
										lower=True
										break
								if not(lower):
									block_level = False
									for gg in range(len(goto_real)):
										if goto_from_real[gg]==python_add_line[i] and (goto_lower[gg]=='for' or goto_lower[gg]=='if') and goto_real[gg]>=python_add_line[j]:
											block_level = True
									if not(block_level): python_add_level[j] = python_add_level[j]+1
				for j in range(python_add_line[i],len(python_program_oldline)):
					python_program_oldline[j] = python_program_oldline[j] + 1

			python_text = ''
			for i in range(len(python_program)):
				nn=''
				for j in range(python_level[i]): nn=nn+chr(9)
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
			if line[-1]!='\n':
				program_text[line_num] = line							
			else:
				program_text[line_num] = line[0:len(line)-1]			
			line_num = line_num + 10
		f.close()
