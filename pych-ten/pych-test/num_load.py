import json

def primes(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True
numbers = [i for i in range(2,15) if primes(i)]
filename = 'pych-test\\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
