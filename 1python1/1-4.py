#draw heart
print('*** Fun with Drawing ***')
num = int(input('Enter input : '))

for i in range(num) : #for(i=0;i<num;i++)
    for j in range(num-i-1) :
         print('.',end = '')

    print('*',end = '')

    for j in range(2*i-1) :
         print('+',end = '')
    if i!=0:
         print('*',end = '')

    for j in range(2*(num-i)-3):
         print('.',end = '')
    if i!=num-1:
         print('*',end = '')

    for j in range(2*i-1):
         print('+',end = '')
    if i!=0:
         print('*',end = '')

    for j in range(num-i-1):
         print('.',end = '')
    print('')

for i in range(2*num-2):
    for j in range(i+1):
         print('.',end = '')

    print('*',end = '')

    for j in range(2*num-3-i):
        print('+',end = '')

    for j in range(2*num-4-i):
        print('+',end = '')

    if i!=2*num-3:
        print('*',end = '')
    for j in range(i+1):
        print('.',end = '')

    print('')

    
