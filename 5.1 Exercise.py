#Module 3
#Chapter 5 5.1 Exercise
#eS 3/22/25
#CIT-95 spring25

num = 0
tot = 0.0
while True:
    stringval= input('Enter a number: ')
    if stringval =='done':
        break
    try:
        floatval = float(stringval)
    except:
        print('Invalid input')
        continue
    num = num +1
    tot = tot + floatval
print(tot, num, tot/num)