 
name= input("what is your name?: ")
age = int(input("how old are you?:"))
age = age + 10


print(f"hello ma {name}!")
print("happy birthday ")
print(f" you are {age} years old")

# Exercise 1 area

length = float(input("Enter the length"))
width = float(input("Enter the width"))
area = length * width 

print(f"the area is: {area}cm²")

# Exercise 2 shopping cart

item = input("what item would you like to buy today?")
price = float(input("what is the price?"))
quantity = int(input("how many would you like?:")) 
total = price * quantity 

print (f"thank you for your purchase of: {quantity} x {item}'s")
print (f"your total is: ${total}")

