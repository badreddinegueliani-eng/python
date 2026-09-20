prices = [5, 2, 5, 2, 2]
total = 0 
for price in prices:
    total += price
print(f"total: {total}")

for x in range(0, 3):
    for y in range(2):
        print(f"({x}, {y})")
    
    for y in range(2):
        print(y)