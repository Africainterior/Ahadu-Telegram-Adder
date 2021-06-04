#!bin/env python3
#! Coded by Ahadu, Ethiopia

import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    os.system('clear')
    print(gr+"______  _____   _____               _____           ")
    print(gr+"|       |         |     |      |   |     |          ")
    print(gr+"|       |         |     |      |   |     |          ")
    print(gr+"|_____  |____     |     |      |   |_____|         ")
    print(re+"      | |         |     |      |   |               ")
    print(re+"      | |         |     |      |   |               ")
    print(re+"______| |____     |     |______|   |               ")

    print(gr+"            Version: 2.1                           ")
    print(gr+"           --------------                          ")
    print(gr+"      Made By Ahadu Eyasu, Ethiopia                ")
    print(re+"    ---------------------------------              ")

    print(gr+" For more information and hacking tools plase join my channel https://t.me/ethio_all_in")
    print(re+"            If you need some help please read README.html file.                        ")

banner()
print(gr+"[+] Installing useful datas...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Enter api Id: "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Enter hash ID: "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Enter phone number: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"You are loged sucessfully.")
print(gr+"Now you can activate the hack.")
print(re+"For more information join https://t.me/ethio_all_in")
    