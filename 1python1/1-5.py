#หยิน-หยาง
num=int(input("Enter Input : "))

for i in range(num+2):
    for j in range(num-i+1):
        print('.',end='')
    for j in range(i+1):
        print('#',end='')
    for j in range(num+2):
        if i==0 or i==num+1:
            print('+',end='')
        elif j!=0 and j!=num+1:
            print('#',end='')
        else:
            print('+',end='')
    print('')

for i in range(num+2):
    for j in range(num+2):
        if i==0 or i==num+1:
            print('#',end='')
        elif j!=0 and j!=num+1:
            print('+',end='')
        else:
            print('#',end='')
    for j in range(num-i+2):
        print('+',end='')
    for j in range(i):
        print('.',end='')
    print('')
    