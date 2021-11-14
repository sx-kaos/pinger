import os
import time
from os import system

def main():
	try:
		os.system('title pinger')
		valid = ['y', 'n', 'exit']
		print("WARNING: selecting rainbow mode may induce seizures if you have epilepsy")
		rainbow = input("Rainbow mode?(y/n): ")
		if rainbow == 'y':
			if rainbow == 'exit':
				exit()
			target = input("Target to ping: ")
			if target == 'exit':
				exit()
			while True:
				os.system('color a')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				os.system('color b')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				os.system('color c')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				os.system('color d')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				os.system('color e')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				os.system('color f')
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
			main()
		elif rainbow == 'n':
			target = input("Target to ping: ")
			if target == 'exit':
				exit()
			while True:
				os.system(f'PING -n 1 {target} | FIND "TTL="')
				os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
				os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
			main()
		elif rainbow not in valid:
			print("please enter 'y' or 'n'")
			time.sleep(3)
			os.system('cls')
			main()
	except KeyboardInterrupt:
		os.system('cls')
		main()
main()
