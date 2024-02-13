x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("select command")

print("1.Add numbers")
print("2.Subtract numbers")
print("3.Multiply numbers")
print("4.Divide numbers")
print("5.Exit")
choice = input("1/2/3/4/5")
if choice == "1":
    print(f"The sum of x and y is {x+y}")
elif choice == "2":
    print(f"The difference of x and y is {x-y}")
elif choice =="3":
    print(f"The product of x and y is {x*y}")
elif choice =="4":
    print(f"The quotient of x and y is {x/y}")
elif choice =="5":
    brake = input("Do you want to stop the calculation? (y/n)")

