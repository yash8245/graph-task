def solve(Jug1_capacity, Jug2_capacity, target) :
    large_jug = 0
    small_jug = 0
    larger_capacity = max(Jug1_capacity, Jug2_capacity)
    smaller_capacity = min(Jug1_capacity, Jug2_capacity)
    
    print("\nInitial values : ")
    print("Large jug : ", large_jug, "\nSmall jug : ",small_jug)
    
    while small_jug != target :
        
        if small_jug == 0 :
            print("\nFilling small jug ");
            small_jug += smaller_capacity
        elif small_jug == smaller_capacity : 
            print("\nPouring small jug water into larger jug until possible : ")
            while small_jug != 0 and large_jug != larger_capacity :
                large_jug += 1
                small_jug -= 1
            
        print("Large jug : ", large_jug, "\nSmall jug : ", small_jug)
     
    large_jug = small_jug
    small_jug = 0
    print("\nFinal result : ")
    print("Large jug : ", large_jug, "\nSmall jug : ", small_jug)
    return True



Jug1_capacity = int(input("Enter first jug capacity : "))
Jug2_capacity = int(input("Enter second jug cpacity : "))
target =  int(input("Enter targted value means the amount water to be filled in large jug : "))

if solve(Jug1_capacity, Jug2_capacity, target) :
    print("\nSolution exists")
else :
    print("\nSolution does not exists")
    