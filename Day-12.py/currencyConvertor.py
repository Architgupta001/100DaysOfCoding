with open('Python/Day-12.py/currencyData.txt') as f:
    lines = f.readlines()


currencyDict = {}

for line in lines:
    parsed = line.split('\t')
    currencyDict[parsed[0]] = parsed[1]

amount = float(input('Enter any amount you want to convert: '))
print("Choose the currency you want to convert from below - \n")

for key in currencyDict.keys():
    print(f"{key}")

currency = input('Enter the currency you want to convert your money: ')

converted_amount = amount * float(currencyDict[currency])
print(f"Final converted amount is {converted_amount}")

    

