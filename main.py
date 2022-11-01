#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build a robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!¡!!!!!!!!!!!!")

name = input("What is your name?\n")

print("Hello " + name + " , thank you so much for coming in today.")  
  

Menu = "Black Coffee, Expreeso, Latte, Cappucino"

print("Hello, " + name + ", what would you like from our menu today? Here is what we serve.\n"+ Menu)

order = input()

price = 3

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))



print("Sounds good " + name + ", we'll have your " + quantity + " " +order + " ready for you in a moment.")

