from threading import Thread
import sys, os
from hashlib import md5
from time import sleep

os.system('clear')
print("              ___ ________")
sleep(0.08)
print("  _____    __| _/|   ____/")
sleep(0.08)
print(" /     \  / __ | |____  \ ")
sleep(0.08)
print("|  Y Y  \/ /_/ | /       \ ")
sleep(0.08)
print("|__|_|  /\____ |/______  /")
sleep(0.08)
print("      \/      \/       \/\n")

try:
	md5_code = sys.argv[1]
	file_name = sys.argv[2]
except:
	print('\033[1;31m[-]\033[1;m Enter your hash and dectionary .')
	exit(0)

def message(msg):
        for char in msg:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
def cracking(md5_code, passw):
	passwe = passw.encode('utf-8')
	if md5_code == md5(passwe).hexdigest():
		print('\033[1;32m[+]\033[1;m password has been cracked \033[1;32m: \033[1;m')
		print(md5_code + '\033[1;32m : \033[1;m' + passw)
		exit(0)
try:
	message('\033[1;33m[*]\033[1;m reading file .\n')
	file_open = open(file_name, 'r', encoding='utf-8')
	file_read = file_open.readlines()
	message('\033[1;33m[*]\033[1;m start cracking ....\n')
	message('\033[1;33m[?]\033[1;m wait few seconds ...\n')
	for line in file_read:
		passw = line.strip('\n')
		t = Thread(target=cracking, args=(md5_code, passw))
		t.start()
except KeyboardInterrupt:
	print('\033[1;31m[-]\033[1;m Canceled by the user')
	exit(0)
except IOError:
	error = "there was an error reading to ", file_name, "\n"
	message(error)
	sys.exit(0)
