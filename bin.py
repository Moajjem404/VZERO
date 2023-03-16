import random
import os

def generate_bin(country_code):
    iin_range = None
    if country_code == "US":
        iin_range = range(400000, 500000)
        length = 16
    elif country_code == "CA":
        iin_range = [450644, 451015, 451407]
        length = 16
    elif country_code == "AU":
        iin_range = [400837, 400849, 400850, 400860, 400883, 400884, 400885]
        length = 16
    else:
        raise ValueError("Invalid country code")

    # Generate random IIN within the specified range
    iin = str(random.choice(iin_range))
    #Viper Moajjem
    bin_num = iin
    for i in range(length - len(iin) - 1):
        bin_num += str(random.randint(0, 9))
    
    # Calculate and append the check digit using Luhn algorithm
    digits = [int(d) for d in bin_num]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    check_digit = (10 - sum(digits) % 10) % 10
    bin_num += str(check_digit)
    
    return bin_num

def generate_pin():
    # Generate a random 4-digit PIN
    return str(random.randint(0, 9999)).zfill(4)

def generate_expected_date():
    # Generate a random month and year within a certain range
    month = str(random.randint(1,12)).zfill(2)
    year = str(random.randint(2023, 2030))
    return month + "/" + str(year)[-2:]

countries = ["US", "CA", "AU"]
for country in countries:
    print("Country:", country)
    for i in range(5):
        bin_16 = generate_bin(country)
        exp_date = generate_expected_date()
        pin = generate_pin()
        print("Generated BIN:", bin_16)
        print("Expected date:", exp_date)
        print("Generated PIN:", pin)
        print("")
        
        
zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')
