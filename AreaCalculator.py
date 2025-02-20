print("==================")
print("Area Calculator 📐")
print("==================\n")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")

shape = input("Which shape? ")

if shape == "1":
    base = float(input("\nBase: "))
    height = float(input("Height: "))
    area = (height * base) / 2
    
    print("\nThe area is ", area)

elif shape == "2":
    length = float(input("\nLength: "))
    width = float(input("Width: "))
    area = length * width
    
    print("\nThe area is ", area)

elif shape == "3":
    side = float(input("\nSide: "))
    area = side * side
    
    print("\nThe area is ", area)

elif shape == "4":
    radius = float(input("\nRadius: "))
    area = 3.14 * radius * radius

    print("\nThe area is ", area)

elif shape == "5":
    print("\nExiting...")
    exit(0)

else:
    print("\nInvalid choice!")