#FT
# -*- coding: utf-8 -*-
import os
import sys
import time
import random
#import ctypes
#import inspect
import platform
import datetime

from subprocess import call as system_call

sys.dont_write_bytecode = True

version = '0.0.4'

term_style = 'f4' #f3 OR f4 OR f4_arc OR f4_inst

debug = 1
password = 'root'

os_type = platform.system()
os_release = platform.release() 

rows, columns = os.popen('stty size', 'r').read().split()

yes = {'yes', 'y'}
no = {'no', 'n'}

server = random.randint(1, 20)
space_f3 = (int(columns) / 2) -22

mode_def = """
n - no variants
100 - 100 attempts
p - verbose password
0 - none
1 - beginner
2 - intermediate
3 - advanced
4 - master
"""

error_codes = {
'0xE---': 'Error code lost due to data loss',
'0xE000': 'Error',
'0xE001': 'System error',
'0xE002': 'Startup error',
'0xE003': 'Load error',
'0xE004': 'Load mode error',
'0xE005': '',
'0xE006': '',
'0xE007': '',
'0xE008': '',
'0xE009': '',
'0xE010': 'Unknown instruction',
'0xE011': 'Permission error'
}

f3_preload_1 = """ 
>SET TERMINAL/INQUIRE

RIT-V300

>SET FILE/PROTECTION-OWNER:RWED ACCOUNTS.F
>SET HALT RESTART/MAINT
"""

f3_preload_2 = """
Initializing Robco Industries(TM) MF Boot Agent v2.3.0
RETROS BIOS
RBIOS-4.02.08.00 52EE5.E7.E8
Copyright 2201-2203 Robco Ind.
Uppermem: 64 KB
Root (5A8)

Maintebece mode
"""

f3_preload_3 = """
>RUN DEBUG/ACCOUNTS.F
"""

f3_wellcome = """
{}ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM
{}	COPYRIGHT 2075-2077 ROBCO INDUSTRIES
{}				-Server {}-
"""

char_1_arr = ['A', 'B', 'C', 'D', 'F', '0', '1', '2', '3', '4', '5', '6', 'A', 'B', 'C', 'D', 'F', '0', '1', '2', '3', '4', '5', '6', 'A', 'B', 'C', 'D', 'F', '0', '1', '2', '3', '4', '5', '6']
chars = ['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
'`',
'{',
"""'""",
'@',
'+',
'/',
'=',
'^',
'(',
'%',
'"',
'?',
'.',
'[',
']',
'>',
'<',
';',
'_',
'-',
',',
'#',
'$',
'*'
]

words4 = [
'pack',
'pawn',
'pump',
'peak',
'wait',
'half',
'hour',
'wave',
'tent',
'slot',
'cast',
'fuel',
'last',
'even',
'gain',
'east',
'stab',
'test',
'seem',
'mile',
'lost',
'ruin',
'fade',
'camp',
'city',
'joke',
'bang',
'nail',
'hero',
'halt',
'sofa',
'crew',
'coin',
'bait',
'huge',
'trip',
'baby',
'game',
'film',
'west',
'wire',
'hill',
'help',
'coup',
'fish',
'load',
'tire',
'form',
'area',
'swim',
]

def clear():
	if os_type == 'Windows':
		system_call("cls", shell=True)
	else:
		system_call("clear", shell=True)	

def ProgressBar(bar_width, bar_upd_time):
	sys.stdout.write("[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1))

	for i in xrange(bar_width):
		time.sleep(bar_upd_time) 
    	# update the bar
		sys.stdout.write("#")
		sys.stdout.flush()

	sys.stdout.write("\n")		


chars_radom = []

char_1_c = random.randint(1, 12)
char_2_c = random.randint(1, 16)
char_3_c = random.randint(1, 16)
char_4_c = random.randint(1, 16)

string_codes = []
def string_codes_list_gen():
	global string_codes
	global char_2_c
	global char_3_c
	global char_4_c
	a = '0x' + char_1_arr[char_1_c] + chars[char_2_c] + chars[char_3_c] + chars[char_4_c] 
	for x in range(32):
		a = ''
		cnt = 1
		a = '0x' + char_1_arr[char_1_c] + chars[char_2_c + 1] + chars[char_3_c + 1] + chars[char_4_c + 1]
		char_2_c = char_2_c + 1
		char_3_c = char_3_c + 1
		char_4_c = char_4_c + 1
		string_codes.append(a)

string_codes_list_gen()


def load():
	clear()
	print(mode_def)
	print('')
	print('mode:')
	mode_ = raw_input('>')
	clear()

	if term_style == 'f3':
		print('WELLCOME TO ROBCO IDUSTRIES (TM) TERMLINK')
		for l in f3_preload_1:
			sys.stdout.write(l)
		 	sys.stdout.flush()
			time.sleep(0.068)

		for l in f3_preload_2:
			sys.stdout.write(l)
		 	sys.stdout.flush()
			time.sleep(0.02)

		for l in f3_preload_3:
			sys.stdout.write(l)
		 	sys.stdout.flush()
			time.sleep(0.068)

		raw_input()
	clear()
	crack(mode_)


mode = 'n'
attempt_cnt = 1


def crack(c_mode):
	global mode
	global attempt_cnt
	if c_mode == 'n':
		mode = 'n'
		attempt_cnt = 4
		init_attempt_cnt = 4
		crack_interpreter_loop()
	elif c_mode == 'p':
		mode = 'p'
		attempt_cnt = 1
		crack_interpreter_loop()
	elif c_mode == '100':
		mode = 100
		attempt_cnt = 100
		init_attempt_cnt = 100
		crack_interpreter_loop()
	elif c_mode == '0':
		mode = 0
		attempt_cnt = 1
		init_attempt_cnt = 1
		crack_interpreter_loop()
	elif c_mode == '1':
		mode = 1
		attempt_cnt = 6
		init_attempt_cnt = 6
		crack_interpreter_loop()
	elif c_mode == '2':
		mode = 2
		attempt_cnt = 5
		init_attempt_cnt = 5
		crack_interpreter_loop()
	elif c_mode == '3':
		mode = 3
		attempt_cnt = 4
		init_attempt_cnt = 4
		crack_interpreter_loop()
	elif c_mode == '4':
		mode = 4
		attempt_cnt = 4
		init_attempt_cnt = 4
		crack_interpreter_loop()
	else:
		print('[ERROR 0xE003]')
		sys.exit()


def random_symbol_gen(symbols_range):
	a = ''
	for i in range(symbols_range):
		global a 
		a += str(symbols[random.randint(0, 23)]) 
	return a


answer = words4[random.randint(0, 49)]
answer_pos_v = random.randint(1, 16)    #vertical
answer_pos_h = random.randint(1, 4)     #horizontal

def string_interpreter():
	column_1_cnt = 0
	column_2_cnt = 15

	if mode == 'n':
		for x in range(16):
			print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 		
			column_1_cnt += 1
			column_2_cnt += 1
	
	elif mode == 'p':
		print('Password: ')

	elif mode == 0:
		for x in range(16):
			if x == answer_pos_v:
				if answer_pos_h == 1:
					print(string_codes[column_1_cnt] + ' ' + answer.upper() + str(random_symbol_gen(8)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
				elif answer_pos_h == 2:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + answer.upper() + str(random_symbol_gen(8)) + ' ') 
				elif answer_pos_h == 3:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(4)) + answer.upper() + str(random_symbol_gen(4)) + ' ') 
				elif answer_pos_h == 4:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(4)) + answer.upper() + str(random_symbol_gen(4)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
			else:	
				print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 

			column_1_cnt += 1
			column_2_cnt += 1

	elif mode == 1:
		for x in range(16):
			random_words = random.randint(1, 5)
			if x == answer_pos_v:
				if answer_pos_h == 1:
					print(string_codes[column_1_cnt] + ' ' + answer.upper() + str(random_symbol_gen(8)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
				elif answer_pos_h == 2:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + answer.upper() + str(random_symbol_gen(8)) + ' ') 
				elif answer_pos_h == 3:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(4)) + answer.upper() + str(random_symbol_gen(4)) + ' ') 
				elif answer_pos_h == 4:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(4)) + answer.upper() + str(random_symbol_gen(4)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
			else:
				if random_words == 1:
					print(string_codes[column_1_cnt] + ' ' + words4[random.randint(0, 49)].upper() + str(random_symbol_gen(8)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
				elif random_words == 2:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + words4[random.randint(0, 49)].upper() + str(random_symbol_gen(8)) + ' ') 
				elif random_words == 3:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(8)) + words4[random.randint(0, 49)].upper() + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 
				elif random_words == 4:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(8)) + words4[random.randint(0, 49)].upper() + ' ') 
				elif random_words == 5:
					print(string_codes[column_1_cnt] + ' ' + str(random_symbol_gen(12)) + ' ' + string_codes[column_2_cnt] + ' ' + str(random_symbol_gen(12)) + ' ') 

			column_1_cnt += 1
			column_2_cnt += 1
	

def attempts_interpreter():
	if term_style == 'f3':
		if attempt_cnt >= ((int(columns) - 17 ) / 3):
			return attempt_cnt
		else:
			attempts_sym_cnt = ('██ ' * attempt_cnt)
			return attempts_sym_cnt
	elif term_style == 'f4' or term_style == 'f4_arc':
		if attempt_cnt >= ((int(columns) - 20 ) / 3):
			return attempt_cnt
		else:
			attempts_sym_cnt = ('██ ' * attempt_cnt)
			return attempts_sym_cnt

history = []

def crack_interpreter():
	global history
	global attempt_cnt

	ci_1 = raw_input('>')

	if ci_1 == 'exit':
		sys.exit()
	elif mode == 'p' and ci_1 == password:
		crack_pass()
	elif ci_1.lower() == answer:
		if mode == 0 or mode == 1 or mode == 2 or mode == 3 or mode == 4:
			crack_pass() 
		else:
			pass

	elif ci_1 == 'SET DEBUG:ATTEMPT ADD':
		history = history + ' {}'.format(ci_1)
		clear()
		attempt_cnt = attempt_cnt + 1
		crack_interpreter_loop()
	elif ci_1 == 'SET DEBUG:ATTEMPT RESET':
		history = history + ' {}'.format(ci_1)
		clear()
		attempt_cnt = attempts
		crack_interpreter_loop()
	else:
		if mode == 1 and len(ci_1) == 4:
			likeness = 0
			if ci_1[0] == answer[0]:
				likeness += 1
			if ci_1[1] == answer[1]:
				likeness += 1
			if ci_1[2] == answer[2]:
				likeness += 1
			if ci_1[3] == answer[3]:
				likeness += 1

			history.append('>{} '.format(ci_1))
			history.append('>Entry Denied')
			history.append('>Likeness: {}'.format(likeness))
		clear()
		attempt_cnt = attempt_cnt - 1
		crack_interpreter_loop()


def crack_interpreter_loop():
	#visuals begin
	if term_style == 'f3':
		print('ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL')
		print('ENTER PASWORD NOW \n')
		print('ATTEMPT(S) LEFT: {}'.format(attempts_interpreter())) #17
	elif term_style == 'f4' or term_style == 'f4_arc' or term_style == 'f4_inst':
		if term_style == 'f4':
			print('Wellcome to ROBCO Industries (TM) Termlink')
		elif term_style == 'f4_arc':
			print('ArcJet Systems | ArcNet')
		elif term_style == 'f4_inst':
			print('==== Institute Central Network ====')
		print('Password Required')
		print('Attempts Remaining: {}'.format(attempts_interpreter())) #20

	string_interpreter()

	#test
	if debug == 1:
		print('c:' + str(columns) + ' m:' + str(mode) + ' a:' + str(attempt_cnt) + ' ' + answer + ' ' + str(answer_pos_v) + ' ' + str(answer_pos_h))
	#visuals end


	if (int(rows) - 21) <= len(history):
		for x in history[:(int(rows)-22)]:
			sys.stdout.write(x)
			sys.stdout.write('\n')
	
	else:
		for x in history:
			sys.stdout.write(x)
			sys.stdout.write('\n')

	#print(history)

	if attempt_cnt == 0:
		print('Ininiating lockdown...')
		time.sleep(0.65)
		print('[Poccess Completed]')
		sys.exit()
	
	crack_interpreter()






def crack_pass():
	clear()
	if term_style == 'f3':
		print(f3_wellcome.format(space_f3, space_f3, space_f3, server))
	elif term_style == 'f4':
		print('Wellcome to ROBCO Industries (TM) Termlink')
	elif term_style == 'f4_arc':
		print('ArcJet Systems | ArcNet')
	elif term_style == 'f4_inst':
		print('==== Institute Central Network ====')

	print('\nInitializing....')

	print('\n' * (int(rows) - 5))
	command_ = raw_input('> Password Accepted ')
	cmd_loop('')


def cmd():
	print('\n' * (int(rows) - 5))
	command_ = raw_input('>')
	cmd_loop(command_)

def cmd_loop(command):
	if command == 'exit':
		clear()
		print('[Proccess Competed]')
		sys.exit()
	else:
		clear()
		if term_style == 'f3':
			print(f3_wellcome.format(space_f3, space_f3, space_f3, server))
		elif term_style == 'f4':
			print('Wellcome to ROBCO Industries (TM) Termlink')
		elif term_style == 'f4_arc':
			print('ArcJet Systems | ArcNet')
		elif term_style == 'f4_inst':
			print('==== Institute Central Network ====')

		print('\nInitializing....')

		cmd()

load()
