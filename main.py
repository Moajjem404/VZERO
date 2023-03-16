#!/system/bin/python
#coding=utf-8
import os 
import sys 
import time
os.system('clear')


def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(15. / 500)


logo = '''
  \033[1;32;40m██╗░░░██╗\033[1;33;40m██╗\033[1;32;40m██████╗░\033[1;33;40m███████╗\033[1;32;40m██████╗░
  \033[1;32;40m██║░░░██║\033[1;33;40m██║\033[1;32;40m██╔══██╗\033[1;33;40m██╔════╝\033[1;32;40m██╔══██╗
  \033[1;32;40m╚██╗░██╔╝\033[1;33;40m██║\033[1;32;40m██████╔╝\033[1;33;40m█████╗░░\033[1;32;40m██████╔╝
  \033[1;32;40m░╚████╔╝░\033[1;33;40m██║\033[1;32;40m██╔═══╝░\033[1;33;40m██╔══╝░░\033[1;32;40m██╔══██╗
  \033[1;32;40m░░╚██╔╝░░\033[1;33;40m██║\033[1;32;40m██║░░░░░\033[1;33;40m███████╗\033[1;32;40m██║░░██║
  \033[1;32;40m░░░╚═╝░░░\033[1;33;40m╚═╝\033[1;32;40m╚═╝░░░░░\033[1;33;40m╚══════╝\033[1;32;40m╚═╝░░╚═╝
  '''

#Viper


print(logo)

moa = '''\033[1;33;40m╔══════════════════════════════════╗
\033[1;33;40m║ \033[1;34;40mTols Name \033[0;37;40m: \033[1;32;40mVZERO    
\033[1;33;40m║ \033[1;34;40mAuthor \033[0;37;40m   : \033[1;32;40mMoajjem | Viper        
\033[1;33;40m║ \033[1;34;40mFacebook \033[0;37;40m : \033[1;32;40mMd.Moajjem.Hossen.4O4
\033[1;33;40m║ \033[1;34;40mGithub \033[0;37;40m   : \033[1;32;40mMoajjem404
\033[1;33;40m╚══════════════════════════════════╝
  '''
  
print (moa)
time.sleep(1)

slowprint('This Is A Demo Version')

mun = '''
\033[1;31;40m [\033[1;33;40m01\033[1;31;40m]\033[1;36;40m Ip To Information
\033[1;31;40m [\033[1;33;40m02\033[1;31;40m]\033[1;36;40m Number To Information
\033[1;31;40m [\033[1;33;40m03\033[1;31;40m]\033[1;36;40m Style TexT
\033[1;31;40m [\033[1;33;40m04\033[1;31;40m]\033[1;36;40m Internet Speed Cheak
\033[1;31;40m [\033[1;33;40m05\033[1;31;40m]\033[1;36;40m Short URL
\033[1;31;40m [\033[1;33;40m06\033[1;31;40m]\033[1;36;40m Bin Genarator
\033[1;31;40m [\033[1;33;40m07\033[1;31;40m]\033[1;36;40m Fake Address
\033[1;31;40m [\033[1;33;40m08\033[1;31;40m]\033[1;36;40m Download Youtube Video
\033[1;31;40m [\033[1;33;40m00\033[1;31;40m]\033[1;36;40m EXIT

'''

print(mun)

mu = input('\t\033[1;32;40mEnter\033[1;31;40m >>>\033[1;33;40m ')

if mu == '1':
	
	os.system('python ip.py')
	
elif mu == '2':
	
	os.system('python phn.py')
	
elif mu == '3':
	os.system('python stext.py')
	
elif mu == '4':
	os.system('python spedtest.py')
	
elif mu == '5':
	os.system('python surl.py')

elif mu == '6':
	slowprint('\n\t\033[32m██████████████]99%\n')
	os.system('python bin.py')
	
	
elif mu == '7':
	print("\nRanDom 1 Or Us Enter 2\n")
	mm = input("Enter >>> ")
	if mm == '1':
		slowprint('\n\t\033[32m██████████████]99%\n')
		os.system('python fadrs.py')
	elif mm == '2':
		slowprint('\n\t\033[32m██████████████]99%\n')
		os.system('python usadrs.py')
elif mu == '8':
	os.system('python ytdw.py')

elif mu == '0':
	os.system('exit')
	
	
else:
	print('\n\t\033[1;33;40m>>>>\033[1;32;40mPlease Select Correct \033[1;31;40mOption\033[1;33;40m<<<<')
	time.sleep(1.5)
	os.system('python main.py')
