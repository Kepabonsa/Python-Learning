# If = Do some code only IF some condition is True
# Else do something else
name = input("What is your name?: ")
if name  == "":
    print("So you dont talk to much...")
else:
    print(f"Wassup {name}")    

age = int(input("How old are you?:"))

if age >=100:
    print("100? You are old!")    
elif age >= 18:
    print("You are in")
elif age < 0:
    print("0 years old? you are trolling or sum?")    
else:
    print("No Kid, only 18+")   
    

response = input("Would you like food homie? (Y/N): ")

if response == "Y":
    print("Take it bro!")
else:
    print("Ok, you will be hungry later")


#Boolean

for_sale = True 

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = True

if online:
    print("You are online")
else:
    print("You are offline ")
