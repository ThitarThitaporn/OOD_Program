class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,num):
        self.items.append(int(num))
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return 'Value in Stack = ' + str(self.items)
                           
            
def MangeStack(S):
    for i in range(len(S)):
        try:
            key, num = S[i].split()
        except:
            key = S[i][0]
        if key == 'A':
            st.push(num)
            print(f'Add = {num}')
        elif key == 'P':
            if st.isEmpty():
                print('-1') 
            else:
                print(f"Pop = {st.peek()}")
                st.pop()
        elif key == 'D':
            if st.isEmpty():
                print('-1')
            else:
                temp = []
                for i in range(st.size()-1,-1,-1):
                    if int(st.items[i]) != int(num):
                        temp.insert(0,int(st.items[i]))
                    else:
                        print(f"Delete = {st.items[i]}")
                st.items = temp
        elif key == 'LD':
            if st.isEmpty():
                print('-1')
            else:
                temp = []
                for i in range(st.size()-1,-1,-1):
                    if int(st.items[i]) >= int(num):
                        temp.insert(0,int(st.items[i]))
                    else:
                        print(f"Delete = {st.items[i]} Because {st.items[i]} is less than {num}")
                st.items = temp
        elif key == 'MD':
            if st.isEmpty():
                print('-1')
            else:
                temp = []
                for i in range(st.size()-1,-1,-1):
                    if int(st.items[i]) <= int(num):
                        temp.insert(0,int(st.items[i]))
                    else:
                        print(f"Delete = {st.items[i]} Because {st.items[i]} is more than {num}")
                st.items = temp
    print(st)
    # print('Value in Stack =' ,st.items)

st = Stack()
S = input("Enter Input : ").split(',')
MangeStack(S)