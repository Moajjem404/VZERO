import os
x = range(6)

for n in x:
  print(n)
  from faker import Faker
  fake=Faker()
  print('Name:',fake.name())
  print('Date of Birth:',fake.date_of_birth())
  print('Address:',fake.address())
  print('Country:',fake.country())
  print('Email:',fake.email())
  print('\n\n')


zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')


