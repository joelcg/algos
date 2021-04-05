import time

#Repeated steps with sleep delay
n = 10
while n > 0:
    print(n)
    n = n - 1
    time.sleep(1)
print('Blastoff!')

#Simple definite loop and iteration variable with integers or strings
friends = ['Joey', 'Zoey', 'Chloe']
for x in [3, 2, 1] :
    print(x)
    time.sleep(1)
for friends in friends :
    print('Happy new year, ',friends, '!')

#Infinite loop
while True:
    print ('loop')
print('this print will never happen')

#Breaking out of loop and finishing an iteration with continue
while True:
    line = input('> ')
    if line == 'Stoppu!' :
        break
    else:
        print("Wot, m8?")
        continue
    print(line)
print('I stopped!')

#Loop to find largest value
largest_so_far = 0
print('Before', largest_so_far)
for num in [2, 7, 3, 4, 8, 5] :
    if num > largest_so_far :
        largest_so_far = num
    print(largest_so_far, num) #print so we can see the process
print('after', largest_so_far)
