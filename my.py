n = int(input("Enter a no."))
m = n
rev = 0
while n>0:
    r = n%10
    rev = 10*rev+r
    n = n//10
    if n == rev:
     print("pallindrom")
else:
    print("Not pallindrom") 