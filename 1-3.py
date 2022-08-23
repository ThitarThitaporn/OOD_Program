#Loop sum of each digit
print(' *** Summation of each digit ***')
PosN = input('Enter a positive number : ')
PosN = int(PosN)
sum = 0
while PosN > 0   :
     n = PosN % 10
     sum += n
     PosN //= 10
     
print("Summation of each digit = ", int(sum))