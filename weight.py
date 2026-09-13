weight = int(input("weight: "))
unit = input("(L)bs or (K)kg:")
if unit.upper() == "L":
     coverted = weight * 0.45
     print("converted")
     print(f"you are {coverted} KILOS")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
         