print("Welcome to the Interactive data Collector!")
name=input("please enter your name: ")
age=int(input("Please enter your age:"))
height=int(input("Please enter your height in meters: "))
favnum=int(input("Please enter your favourite Number: "))
print("Thank you! Here is the information we collected:")

print("Name:",name,"(Type:",type(name),",Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),",Memory Address:",id(age),")")
print("Height:",height,"(Type:",type(height),",Memory Address:",id(height),")")
print("Favourite Number:",favnum,"(Type:",type(favnum),",Memory Address:",id(favnum),")")
current_year=2026
birth_year=current_year-age
print(f"Your birth year is approximately:{birth_year})(based on your age of {age})")
print("Thank you for using the personal Data Collector.")
print("Goodbye!")
