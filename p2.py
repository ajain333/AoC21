import os
os.chdir('C:\\users\\abjain\\OneDrive - Microsoft\\MSFT\\Advent of Code')

fn = open('p1input.txt', 'r')

lines = fn.readlines()
count = 0

for i in range(3,len(lines)):
    x = int(lines[i])+int(lines[i-1])+int(lines[i-2])
    y = int(lines[i-1])+int(lines[i-2])+int(lines[i-3])
    if x > y:
       count = count + 1
    else:
       continue

print(count)

