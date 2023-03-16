#Viper
import os
import pyfiglet


mkk = input('\t\033[1;32;40mEnter Text\033[1;31;40m :\033[1;33;40m ')

result = pyfiglet.figlet_format(mkk, font = "bulbhead" )
print('\033[1;36;40m',result)

  
result = pyfiglet.figlet_format(mkk, font = "digital" )
print(result)

result = pyfiglet.figlet_format(mkk, font = "bubble" )
print(result)


#result = pyfiglet.figlet_format(mkk, font = "dotmatrix" )
#print(result)



result = pyfiglet.figlet_format(mkk, font = "alligator" )
#print(result)

result = pyfiglet.figlet_format(mkk, font = "letters" )
print(result)


result = pyfiglet.figlet_format(mkk, font = "isometric1" )
print(result)



result = pyfiglet.figlet_format(mkk, font = "doh" )
print(result)



result = pyfiglet.figlet_format(mkk, font = "banner3-D" )
print(result)



result = pyfiglet.figlet_format(mkk, font = "alphabet" )
print(result)


result = pyfiglet.figlet_format(mkk, font = "5lineoblique" )
print(result)


result = pyfiglet.figlet_format(mkk, font = "3x5" )
print('\033[1;32;40m',result)






result = pyfiglet.figlet_format(mkk, font = "3-d" )
print(result)


result = pyfiglet.figlet_format(mkk, font = "slant"  )
print(result)



result = pyfiglet.figlet_format(mkk)
print('\033[1;32;40m',result)


#result = pyfiglet.figlet_format(mkk, font = "Precious"  )
#print(result)

zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')
