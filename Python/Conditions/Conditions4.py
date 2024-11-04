print("Welcome in Python Pizza!")
print("#######################")
print("")

x = input("Choose pizza size(S/M/L): ")
bill = 0

if x == "S":
    bill+=15
    peperoni = input("Do you want peperoni?(Y or N): ")
    cheese = input("Do you want cheese?(Y or N): ")
    if peperoni == "Y":
        bill+=2
    if cheese == "Y":
        bill+=1
    print(f"Paid {bill}")
elif x == "M":
    bill+=20
    peperoni = input("Do you want peperoni?(Y or N): ")
    cheese = input("Do you want cheese?(Y or N): ")
    if peperoni == "Y":
        bill+=3
    if cheese == "Y":
        bill+=1
    print(f"Paid {bill}")
else:
    bill+=25
    peperoni = input("Do you want peperoni?(Y or N): ")
    cheese = input("Do you want cheese?(Y or N): ")
    if peperoni == "Y":
        bill+=3
    if cheese == "Y":
        bill+=1
    print(f"Paid {bill}")