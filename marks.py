marks = int(input("Enter marks: "))

if marks>85 and marks<=100:
    print("You get an A")
elif marks>60 and marks<=85:
    print("You get a B+")
elif marks>40 and marks<=60:
    print("You get a B")
elif marks>30 and marks<=40:
    print("You get a C")
else:
    print("You fail")
