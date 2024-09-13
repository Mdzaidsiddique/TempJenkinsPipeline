# wap to prime number up to 20
import math
def is_prime(num):
    for i in range(2, num):
        return False if num%i==0 else True
    

for i in range(0, 21):
    if is_prime(i):
        print(i)
            
# wap to check string is palindrome or not

def is_palindrome(string):
    return string == string[::-1]

print("palindrome") if is_palindrome('racecar') else print("Not a palindrome")

# string = input("Please enter a sting that has to be check: ")

def is_palindrome(string):
    return string == string[::-1]

# print(f"{string} is Palindrome" if is_palindrome(string) else print(f"{string} is not a palindrome"))


# wap to take user input as Md Zaid Siddique and print M.Z. Siddique

# user_input = input("Please enter the full name : ")

def format_string(string):
    str = string.split(" ")
    print(str[0][0]+"."+str[1][0]+"."+str[2])

# format_string(user_input)

# wap to remove nth occurance of a word from a list

# list = ['zaid', 'alif', 'sidd', 'ad', 'zaid', 'zaid', 'alif', 'zaid'] # remove 3rd occurance of 'zaid'

def remove_occ(list, occurance, word):
    if occurance > list.count(word):
        return -1
    count = 0
    for i in range(len(list)-1):
        if list[i] == word:
            count+=1
            if count==occurance:
                list.pop(i)

# remove_occ(list, 3, 'zaid')

# print(list)

# decorators

def decorator1(func):
    def wrapper(*args, **kwargs):

        print(*args)
        func(*args)
        print('After function execution')

    return wrapper


@decorator1
def norml(a,b,c):
    print(a,b,c)

norml(2,3,4)

lsit_p = ['zaid', 'umair', 'salman']

email_list = [x+"@gmail.com" for x in lsit_p]
print(email_list)

l1 = [1,2,3]
l2 = [10,11,12]
d1 = {l1[i]:l2[i] for i in range(len(l1))}
print(d1)

# Faker
# pip install faker
# form faker import Faker
# f = Faker()
# f.name()

s = "zaidndfdkjsb"
a = s[0:3]


# modify elements of a tuple
t = (1,2,3,4,5,4)
print(t)

l = list(t)
l[0] = 100
t = tuple(l)

# print(t)

# map function
a = [1,2,3,4]
def sq(num):
    return num**2

sn = map(sq, a)

# filter out even numbers
def filter_ev(num):
    return num%2==0

fev = filter(filter_ev, a)

# reduce
import functools

p = functools.reduce(lambda a,b: a*b, a)
print(p)
a = tuple([1,2,3])
d = {a:1, "b": 2, "c":3}
print(d)
