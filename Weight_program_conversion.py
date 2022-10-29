Weights = input("Weight: ")
unit = input("(L)bs or (K)g: ")
answer = 0

if unit.upper() == 'L':
    answer = float(Weights) * 0.453592
    print(f"You are {answer} pounds")
elif unit.upper() == 'K':
    answer = float(Weights) * 2.220462
    print(f"You are {answer} kilos")
