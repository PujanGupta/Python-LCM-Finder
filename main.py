def findLCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
        
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm

while True:
    Num1 = int(input("Number 1: "))
    Num2 = int(input("Number 2: "))
    
    print(f"The LCM of {str(Num1)} and {str(Num2)} is {findLCM(Num1, Num2)}")