print("Welcome to the tip Calculator.")
bill = input("What was the total bill $")
tip = input("what percentage tip would you like to give? 10, 12 or 15 ")

tip = int(tip)
bill = float(bill)
bill = bill + ((tip * bill)/100)

people = input("how many people to split the bill? ")
people = int(people)
final = round(bill/people,2)
print(f"Each person should pay ${final}")