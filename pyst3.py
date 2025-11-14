    #  prime number 
number = int(input("Enter a number: "))
if number <= 1:
    print(number," is not prime.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(number," is not prime.")
            break 
    else:
        print(number," is prime.")


        # Reverse a Number

n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse number is:", rev)


    #    HCF of two Number 

num1 = int(input("Enter smaller number:"))
num2 = int(input("Enter largest number:"))
if num1 < num2:
    smaller = num1
else:
    smaller = num2
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"The HCF of {num1} and {num2} is {hcf}")



        # Automorphic Number


num = int(input("Enter a number:"))
square = num * num 
str_num = str(num)
str_square = str(square)
if str_square.endswith(str_num):
    print(f"{num} is an Authomorphic number")
else:
    print(f"{num} is not an Authomorphic number")

    #  Harshad Number

num = int(input("Enter a number:"))
sum_of_digit = sum(int(digit) for digit in str(num))
if num % sum_of_digit == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")


    # Perfect Number
num = int(input("Enter a number:"))
sum_of_divisors = 0
for i in range(1, num):
     if num % i == 0:
         sum_of_divisors = sum_of_divisors + i
if sum_of_divisors == num:
        print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

    #   Strong number

import math
num = int(input("Enter a number:"))
original_num = num
sum_of_factorials = 0
while num > 0:
    digit = num % 10
    sum_of_factorials += math.factorial(digit)
    num = num // 10
if sum_of_factorials == original_num:
    print(f"{original_num} is a strong number")
else:
    print(f"{original_num} is not a strong number")