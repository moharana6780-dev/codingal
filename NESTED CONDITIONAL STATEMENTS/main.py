print("=========================")
print("WELCOME TO RIDE BUILDER:-") 
print("=========================")
print()
print("STEP 1 :- PICK YOUR VEHICLE")
print("1. Bike \n2. Car ")
print()
choice = int(input("enter 1 or 2:-")) 
if choice ==  1 :
    print("STEP 2 :- Pick your bike type ") 
    print("1. KAWASAKI \n 2. KTM ") 
    BikeType = int(input("EITHER CHOOSE 1 OR 2"))
    if BikeType == 1 :
        print("You picked a kawasaki , and your top speed is 500 miles per hour ") 
    else : 
        print("You picked KTM , and your top speed is 250 miles per hour ")
elif choice == 2 :
    print("Step 2:- Pick you car type ")
    print("1. Toyota supra \n 2. Bugatti Bodel ")
    cartype = int(input("Either choose 1 or 2"))
    if cartype == 1 : 
       print("You picked Toyota supra , and your top speed is 950 miles per second ")
    else :
        print("you picked a bugatti bodel , and your top speed is 1200 miles per second ") 
    
    
