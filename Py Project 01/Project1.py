''' Pizza order and bill generation'''


small_pizza= 15
medium_pizza=20
large_pizza= 25

add_pepper_small_pizza=2
add_papper_large_or_medium_pizza= 3

add_cheese_any_size_pizza= 1



size=input("What size of pizza do you want?[S/M/L]: ")
add_pepper= input("Do you want pepper?[Y/N]:")
add_extra_cheese= input("Do you want extra cheese?[Y/N]:")


#size

Bill=0

if size == "S":
    Bill+=small_pizza

elif size=="M":
    Bill+=medium_pizza

elif size == "L":
    Bill+=large_pizza

else:
    print("Invalid input")   



#Add pepper

if add_pepper == "Y":
    if size == "S":
        Bill += add_pepper_small_pizza
    else:
        Bill+= add_papper_large_or_medium_pizza    


#Add cheese  

if add_extra_cheese == "Y":
    Bill+= add_cheese_any_size_pizza

print()


print(f"Your final bill is ${Bill}")   
print()


print("Thank you! Come agin")











