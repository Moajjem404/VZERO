import os
import random
import string
from datetime import date, timedelta

# Street name generator
streets = ["Oak Street", "Maple Street", "Elm Street", "Pine Street", "Cedar Street", "Walnut Street", "Willow Street", "Spruce Street", "Birch Street", "Cherry Street"]

# City generator
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

# State generator
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Zip code generator
def generate_zip_code():
    return str(random.randint(10000, 99999))

# Name generator
first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Phone number generator
def generate_phone_number():
    area_code = str(random.randint(100, 999))
    first_three = str(random.randint(100, 999))
    last_four = str(random.randint(1000, 9999))
    return f"({area_code}){first_three}-{last_four}"

# Email generator
def generate_email(name):
    domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com"])
    name = name.lower().replace(" ", ".")
    letters = string.ascii_lowercase
    random_chars = ''.join(random.choice(letters) for i in range(5))
    return f"{name}.{random_chars}@{domain}"

# Date of birth generator
def generate_date_of_birth():
    today = date.today()
    age = random.randint(18, 80)
    dob = today - timedelta(days=age*365)
    return dob.strftime('%m/%d/%Y')

# Generate 100+ addresses and print them
for i in range(10):
    # Number generator
    street_number = random.randint(100, 9999)

    street_name = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = generate_zip_code()
    name = random.choice(first_names) + " " + random.choice(last_names)
    phone_number = generate_phone_number()
    email = generate_email(name)
    date_of_birth = generate_date_of_birth()

    # Print address, name, phone number, email, and date of birth
    print(f"Name : "f"{name}\n""Street Number : "f"{street_number}\n""Street Name : "f" {street_name}\n""City : "f"{city}, {state} {zip_code}\n""Phone Number : "f"{phone_number}\n""Email : "f"{email}\n""Date Of Birth : "f"{date_of_birth}\n")
    
    
zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')
