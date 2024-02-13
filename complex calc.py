x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def complex_calculator():
 print("The complex calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

Choice= input("Enter your choice ")

if Choice == "1":
    print(f"{x}+{y}= {x+y}")
elif Choice == "2":
    print(f"{x}-{y}= {x-y}")
elif Choice =="3":
    print(f"{x}*{y}= {x*y}")
elif Choice =="4":
    print(f"{x}/{y}= {x/y}")
elif Choice =="5":
    print("stop")

