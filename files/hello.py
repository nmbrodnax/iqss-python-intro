# hello.py
# Introduction to Python
# NaLette Brodnax
# www.nalettebrodnax.com

print("Hello, world.")

movie = 'Rogue One'
print(movie)
i = 1
i += 1
print(i)
print('A' + 'B')
print('me'*3)
print('a' == 'a')
print('a' == 1)
print(5 != 25/5)

mystring = 'happy'
print(mystring[0])
print(mystring[2:4])

mylist = ['Leia', 'Rey', 'Maz']
print(mylist[-1])

mydict = {'name': 'Kylo', 'side': 'dark'}
print(mydict['name'])

name = 'Grace Hopper'

if len(name) < 20:
    print('Yes')
else:
    print('No')

i = 0
for letter in name:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        i = i + 1
print(name + ' has ' + str(i) + ' vowels.')

i = 0
vowel_count = 0
while i < len(name):
    if name[i] in ['a', 'e', 'i', 'o', 'u']:
        vowel_count = vowel_count + 1
    i = i + 1
print(name + ' has ' + str(vowel_count) + ' vowels.')

my_string = 'aBcDe'
print(my_string)

print(my_string.lower())


def say_hello(name_string):
    print('Hello, ' + str(name_string) + '!')
    return None

say_hello('NaLette')
