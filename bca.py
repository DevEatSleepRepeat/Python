# Write your code here :-)
import os, time
from random import randint
from colorama import Fore
from pyfiglet import Figlet
fig = Figlet(font = "larry3d")
def charge():
	for i in range(1,101,1):
		chrg_v = (str(i)+"%")
		chrg_l = len(chrg_v)
		while chrg_l < 4:
			chrg_v = chrg_v + "-"
			chrg_l = len(chrg_v)
		chrg = ("["+chrg_v+"]~")
		if i < 11:
			print(Fore.RED + fig.renderText(chrg))
		elif i > 10 and i < 80:
			print(Fore.YELLOW + fig.renderText(chrg))
		elif i > 40 or i == 40:
			print(Fore.GREEN + fig.renderText(chrg))
		wait = (randint(int(1),int(10))/10)
		time.sleep(wait)
		os.system("clear")
	for x in range(1,6,1):
		print(Fore.GREEN + fig.renderText(chrg))
		time.sleep(0.2)
		os.system("clear")
		print(Fore.WHITE + fig.renderText(chrg))
		time.sleep(0.2)
		os.system("clear")
	print(Fore.GREEN + fig.renderText(chrg))
charge()
