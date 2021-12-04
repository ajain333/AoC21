import os

os.chdir('C:\\users\\abjain\\OneDrive - Microsoft\\MSFT\\Advent of Code')

fn = open('p3input.txt', 'r')

lines = fn.readlines()
list1 = lines
length = len(lines)
no_len = len(lines[0])
o2_gen_rating = []
co2_gen_rating = []

for i in range(no_len):
    zero = 0
    one = 0
    list_zero = []
    list_one = []
    for j in range(length):
        if list1[j][i] == '0':
            zero += 1
            list_zero.append(list1[j])
        else:
            one += 1
            list_one.append(list1[j])

    if zero > one:
        length = len(list_zero)
        if length == 1:
            break
        list1 = list_zero
    else:
        if zero < one:
            length = len(list_one)
            if length == 1:
                break
            list1 = list_one
        else:
            length = len(list_one)

if list_zero != []:
    o2_gen_rating = int("".join(list_zero),2)
    
else:
    o2_gen_rating = int("".join(list_one),2)

print("O2 Generator Rating ", o2_gen_rating)

list1 = lines
length = len(lines)

for i in range(no_len):
    zero = 0
    one = 0
    list_zero = []
    list_one = []
    for j in range(length):
        if list1[j][i] == '0':
            zero += 1
            list_zero.append(list1[j])
        else:
            one += 1
            list_one.append(list1[j])

    if one == 0:
        length = len(list_zero)
        if length == 1:
            break
        list1 = list_zero
    elif zero == 0:
        length = len(list_one)
        if length == 1:
            break
        list1 = list_one
    elif zero < one:
        length = len(list_zero)
        if length == 1:
            break
        list1 = list_zero
    elif zero > one:
        length = len(list_one)
        if length == 1:
            break
        list1 = list_one
    elif zero == one:
        length = len(list_zero)
        if length == 1:
            break
        list1 = list_zero

if list_zero != []:
    co2_gen_rating = int("".join(list_zero),2)
    
else:
    co2_gen_rating = int("".join(list_one),2)

print("CO2 Generator Rating ", co2_gen_rating)

print("Life Support Rating ", o2_gen_rating*co2_gen_rating)
