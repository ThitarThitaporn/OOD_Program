#หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล
def hbd(age):
    
    sum = age % 2
    if sum == 0 :
        
        print("saimai is just 20, in base", age//2 ,end="!")

    else :
        print("saimai is just 21, in base", age//2 ,end="!")

year = int(input("Enter year : "))
(hbd(int(year)))
