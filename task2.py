def solve() :
    print("Given 3 missionaries and 3 cannibals who have to cross the river but have to follow certain conditions : ")
    boat = 0
    can_at_start = 3
    can_at_end = 0
    miss_at_start = 3
    miss_at_end = 0
    print("\nNumber of cannibals at start : ", can_at_start)
    print("Number of missionaries at start : ", miss_at_start)
    print("Number of cannibals at end : ", can_at_end)
    print("Number of missionaries at end : ", miss_at_end)
    
    while can_at_end != 3 or miss_at_end != 3 :
        if boat == 0 :
            boat = 1
            if can_at_start >= 2 and miss_at_start !=2 :
                print("\nBoat will take 2 cannibals to end")
                can_at_end += 2
                can_at_start -= 2
            else :
                print("\nBoat will take 2 missionaries to end")
                miss_at_end += 2
                miss_at_start -= 2
               
        else :
            boat = 0
            if miss_at_end == 2 :
                print("\nBoat will take 1 missionary and 1 cannibal at end ")
                can_at_end -= 1
                miss_at_end -= 1
                can_at_start += 1
                miss_at_start += 1
            else :
                print("\nBoat will take 1 cannibal to start ")
                can_at_end -= 1
                can_at_start += 1
                
                
        print("Number of cannibals at start :", can_at_start)
        print("Number of missionaries at start :", miss_at_start)
        print("Number of cannibals at end :", can_at_end)
        print("Number of missionaries at end :", miss_at_end)      
    

solve()