str1, str2 = input('Enter Input :').split(',')
class Stack :
    def __init__(self, list = None) :
        if list == None :
            self.items = []
        else:
            self.item = list
