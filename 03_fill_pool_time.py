width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))
volume = (width * length * depth) * 15 / 60
print(f"Time to fill a pool is {volume:.2f} minutes.")