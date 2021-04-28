#!/usr/bin/python

import os , sys 

os.system("cls")
try:
	liste = open(sys.argv[1],"r+")
	clear = open("clear_list.txt","a+")
	protocole = int(sys.argv[2])

	if (protocole == 1):
		protocole = "http://"
	elif (protocole == 2):
		protocole = "https://"
	else:
		print("[i] - Protocole Error ...")
		sys.exit(0)
	print("[+] - Start : \n")
	for site in liste:
		site = protocole + site
		print(site)
		clear.write(site)

	liste.close()
	clear.close()

	print("\n\n[+] - done .")
except:
	print("Using Python 3")
	print("python script.py liste.txt [protocole[1|2]]")
	print("protocole :  1 - http | 2 - https")
