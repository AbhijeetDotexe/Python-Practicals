# Currency converter
with open('currency.txt') as f:
    a = f.readlines()
currencyD={}
for lines in a:
    parsed = lines.split('\t')
    currencyD[parsed[0]] = parsed[1]

amount=int(input('Enter amount : '))
print('Enter he name of the currency you want to convert this amount to ? : ')
print('Available conversions : ')
for i in currencyD.keys():
    print(i)
curr= input('Please enter any one of these values : \n ')
print(f'{amount} INR is equal to {amount *float(currencyD[curr])} {curr}')