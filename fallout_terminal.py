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

version = '0.0.1'

term_style = 'f4' #f3 OR f4 OR f4_arc OR f4_inst

os_type = platform.system()
os_release = platform.release() 

rows, columns = os.popen('stty size', 'r').read().split()

yes = {'yes', 'y'}
no = {'no', 'n'}

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

string_codes_f3 = {
'1': '0xF4F0',
'2': '0xF4FC',
'3': '0xF514',
'4': '0xF520',
'5': '0xF52C',
'6': '0xF538',
'7': '0xF544',
'8': '0xF550',
'9': '0xF55C',
'10': '0xF568',
'11': '0xF574',
'12': '0xF580',
'13': '0xF58C',
'14': '0xF598',
'15': '0xF5A4',
'16': '0xF5B0',
'17': '0xF5BC',
'18': '0xF5CB',
'19': '0xF5D4',
'20': '0xF5E0',
'21': '0xF5EC',
'22': '0xF5F8',
'23': '0xF604',
'24': '0xF610',
'25': '0xF61C',
'26': '0xF628',
'27': '0xF634',
'28': '0xF640',
'29': '0xF64C',
'30': '0xF658',
'31': '0xF664',
'32': '0xF670'
}

string_codes_f4 = {
'1': '0xC330',
'2': '0xC33C',
'3': '0xC348',
'4': '0xC354',
'5': '0xC360',
'6': '0xC36C',
'7': '0xC378',
'8': '0xC384',
'9': '0xC390',
'10': '0xC39C',
'11': '0xC3AB',
'12': '0xC3B4',
'13': '0xC3C0',
'14': '0xC3CC',
'15': '0xC3D8',
'16': '0xC3E4',
'17': '0xC3F0',
'18': '0xC3FC',
'19': '0xC408',
'20': '0xC414',
'21': '0xC420',
'22': '0xC42C',
'23': '0xC438',
'24': '0xC444',
'25': '0xC450',
'26': '0xC45C',
'27': '0xC468',
'28': '0xC474',
'29': '0xC480',
'30': '0xC48C',
'31': '0xC498',
'32': '0xC4A4'
}

string_codes_f4_arc = {
'1': '0x0000',
'2': '0x000C',
'3': '0x0010',
'4': '0x0018',
'5': '0x0024',
'6': '0x0030',
'7': '0x003C',
'8': '0x0048',
'9': '0x0054',
'10': '0x0060',
'11': '0x006C',
'12': '0x0078',
'13': '0x0084',
'14': '0x0090',
'15': '0x009C',
'16': '0x00A8',
'17': '0x00B4',
'18': '0x00C0',
'19': '0x00CC',
'20': '0x00D8',
'21': '0x00E4',
'22': '0x00F0',
'23': '0x00FC',
'24': '0x0108',
'25': '0x0114',
'26': '0x0120',
'27': '0x012C',
'28': '0x0138',
'29': '0x0144',
'30': '0x0150',
'31': '0x015C',
'32': '0x0168'
}

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
		attempt_cnt = 1
		crack_interpreter_loop()
	elif c_mode == 'p':
		mode = 'p'
		attempt_cnt = 1
		crack_interpreter_loop()
	elif c_mode == '100':
		mode = '100'
		attempt_cnt = 100
		crack_interpreter_loop()
	elif c_mode == '0':
		mode = 0
		attempt_cnt = 1
		crack_interpreter_loop()
	elif c_mode == '1':
		mode = 1
		attempt_cnt = 6
		crack_interpreter_loop()
	elif c_mode == '2':
		mode = 2
		attempt_cnt = 5
		crack_interpreter_loop()
	elif c_mode == '3':
		mode = 3
		attempt_cnt = 4
		crack_interpreter_loop()
	elif c_mode == '4':
		mode = 4
		attempt_cnt = 4
		crack_interpreter_loop()
	else:
		print('[ERROR 0xE003]')
		sys.exit()

def random_sybol_gen():
	a = ''
	for i in range(12):
		global a 
		a += str(symbols[random.randint(0, 23)]) 
	return a

def string_interpreter():
	column_1_cnt = 1
	column_2_cnt = 17
	for x in range(16):
		if term_style == 'f3':
			print(string_codes_f3['{}'.format(column_1_cnt)] + ' ' + str(random_sybol_gen()) + ' ' + string_codes_f3['{}'.format(column_2_cnt)] + ' ' + str(random_sybol_gen()) + ' ') 
		elif term_style == 'f4':
			print(string_codes_f4['{}'.format(column_1_cnt)] + ' ' + str(random_sybol_gen()) + ' ' + string_codes_f4['{}'.format(column_2_cnt)] + ' ' + str(random_sybol_gen()) + ' ') 
		elif term_style == 'f4_arc':
			print(string_codes_f4_arc['{}'.format(column_1_cnt)] + ' ' + str(random_sybol_gen()) + ' ' + string_codes_f4_arc['{}'.format(column_2_cnt)] + ' ' + str(random_sybol_gen()) + ' ') 

		else:
			print('[ERROR 0xE0]')
			sys.exit()

		column_1_cnt += 1
		column_2_cnt += 1
		"""+ ' ' * 13 + string_code_2['{}'.format(x * 2)])"""

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

def crack_interpreter():
	#print('')
	ci_1 = raw_input('>')
	global attempt_cnt
	attempt_cnt = attempt_cnt - 1
	if ci_1 == 'exit':
		sys.exit()
	else:
		print('[ERROR 0xE010]')
		time.sleep(0.2)

	clear()
	crack_interpreter_loop()


def crack_interpreter_loop():
	#visuals begin
	if term_style == 'f3':
		print('ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL')
		print('ENTER PASWORD NOW \n')
		print('ATTEMPT(S) LEFT: {}'.format(attempts_interpreter())) #17
	elif term_style == 'f4' or term_style == 'f4_arc':
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
	#print(''.join(symbols))
	print('c:' + str(columns) + ' m:' + str(mode) + ' a:' + str(attempt_cnt))
	#visuals end

	if attempt_cnt == 0:
		print('Ininiating lockdown...')
		time.sleep(0.65)
		print('[Poccess Complete]')
		sys.exit()

	crack_interpreter()





load()
