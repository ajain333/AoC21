import os
os.chdir('C:\\users\\abjain\\OneDrive - Microsoft\\MSFT\\Advent of Code')

fn = open('p3input.txt', 'r')

lines = fn.readlines()
no_len = len(lines[0])
gamma = []
epsilon = []

for i in range(no_len-1):
    zero = 0
    one = 0

    for j in range(len(lines)): 
        if lines[j][i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')
gamma = "".join(gamma)
epsilon = "".join(epsilon)

dec_gamma = int(gamma,2)
dec_epsilon = int(epsilon,2)

print(dec_gamma)
print(dec_epsilon)
print(dec_gamma*dec_epsilon)

