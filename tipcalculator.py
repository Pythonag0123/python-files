#day2-project2
print("Welcome to the tip calculator")
bill=(input("What was the total bill?").replace("$",""))
bill=int(bill)
tip=int(input("what percentage tip would u like to pay?"))
People=int(input("How many people are splitting bill?"))
per_person_tip=(((tip/100)*bill)+bill)/People
print("Each person should pay: $" + str(per_person_tip))
