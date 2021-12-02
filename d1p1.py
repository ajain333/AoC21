import os
os.chdir('C:\\users\\abjain\\OneDrive - Microsoft\\MSFT\\Advent of Code')

fn = open('p1input.txt', 'r')

lines = fn.readlines()
count = 0
for i in range(1,len(lines)):

    if (int(lines[i-1]) < int(lines[i])):
        count = count + 1
    else:
        continue

print(count)

