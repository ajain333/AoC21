import os
os.chdir('C:\\users\\abjain\\OneDrive - Microsoft\\MSFT\\Advent of Code')

fn = open('p2input.txt', 'r')

lines = fn.readlines()

hor = 0
ver = 0
aim = 0
for i in range(len(lines)):
    x = lines[i]
    y = len(x)
    z = int(x[-2])
    if y < 6:
        aim = aim - z
    else:
        if y == 7:
            aim = aim + z
        else:
            hor = hor + z
            ver = ver + (aim*z)

#    print (hor,ver,aim)
print(hor*ver)

