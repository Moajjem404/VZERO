import requests,json,os,sys
from requests import get

ip = get('https://api.ipify.org').text
print('Your ip is : ',ip)

victim=input('\n\033[1;34;40mVICTIM IP ADDRESS \033[1;33;40m>>>\033[1;32;40m ')
url="http://ip-api.com/json/"+victim
ip=requests.get(url).json()


print(" \033[1;31mVICTIM IP : \033[1;36m "+ip['query'])
print(" \033[1;31mIP STATUS : \033[1;36m "+ip['status'])
print(" \033[1;31mCOUNTRY : \033[1;36m "+ip['country'])
print(" \033[1;31mCOUNTRY CODE : \033[1;36m "+ip['countryCode'])
print(" \033[1;31mDIVISION : \033[1;36m "+ip['regionName'])
print(" \033[1;31mCITY : \033[1;36m "+ip['city'])
#print("DISTRICT : "+ip['district'])
print(" \033[1;31mNETWORK SERVICE : \033[1;36m "+ip['isp'])
print(" \033[1;31mTIMEZONE : \033[1;36m "+ip['timezone'])
print("\033[1;31mAS   :\033[1;36m"+ip['as'])


zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')