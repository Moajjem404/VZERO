#!/system/bin/python
#coding=utf-8
import os 
import sys 
import time


def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9. / 500)

import pyshorteners
long_url = input("Enter the URL to shorten : ")
 
#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

slowprint('\n\t\033[32m██████████████]99%\n')
 
print("\033[1;34;40mThe Shortened URL is \033[1;33;40m: \033[1;32;40m" + short_url)


zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')




