# 2+2 is an expression
#expressions consist of values and operators and reduce down to a single value
# this means expressions can be used wherever values are used
import random
a = 9/2
b = 9//2 #3
c = 9%2 #1
integer = 2
float = 2.0
string = 'anything within single inverted commas'

#ask for name and print it
'''
print('What\'s your name ?')
myName = input()
print("It's goood to meet you: " + myName)
print('\n Length of your name is : ' + str(len(myName)))
print('WHat is your age ? ')
myAge = input()
print('You will be 69 years old in ' + str(69-int(myAge)) + ' years')
'''
for i in range(0,10,2):
    print(random.randint(1,10))