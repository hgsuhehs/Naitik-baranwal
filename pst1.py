# Input from the user
number = int(input("Enter a number: "))
# Check if the number is prime
if number <= 1:
    print(number," is not prime.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(number," is not prime.")
            break 
        else:
            print(number," is prime.")
        