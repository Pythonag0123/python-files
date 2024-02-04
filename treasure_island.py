print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
dir=input("You are on the cross road where do u want to go?Type left or right").lower().strip()
if dir=="left":
    choice=input("You have come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for the boat or 'swim' to swim across").lower().strip()
    if choice=="wait":
        choice1=input("You have arrived at the island unharmed.There is a house with three doors.One red, one yellow and one blue.Which color do u choose?").lower().strip()
        if choice1=="blue":
            print("you won")
        else:
            print("Game Over")
    else:
        print("Game Over")       
else:
    print("Game Over")    


