import os
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
num = input("\t\033[1;34;40mEnter Number \033[1;33;40m>>>\033[1;32;40m ")
pN = phonenumbers.parse(num)
print(pN)
tZ = timezone.time_zones_for_number(pN)
print(tZ)
C = carrier.name_for_number(pN, 'en')
R = geocoder.description_for_number(pN, 'en')
print(C)
print(R)

#viper
# Program to check whether a phone number is 
# valid or not 

import phonenumbers 


phone_number = phonenumbers.parse("+91987654321") 

  
# Validating a phone number 

valid = phonenumbers.is_valid_number(phone_number) 

  
# Checking possibility of a number 

possible = phonenumbers.is_possible_number(phone_number) 

  
# Printing the output 

print(valid) 

print(possible) 



zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')