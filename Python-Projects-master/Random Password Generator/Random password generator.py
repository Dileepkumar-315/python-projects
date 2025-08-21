import string
import random
print("welcome to the password generator!")
n_letters=int(input("how many letters would you have like in your password?\n"))
n_symbols=int(input("how many symbols would you like?\n"))
n_numbers=int(input("how many numbers would you like?\n"))
all_letters=list(string.ascii_letters)
all_symbols=list(string.punctuation)
all_numbers=list(range(10))
password=""
for i in range(n_letters):
    l=random.choice(all_letters)
    password+=str(l)
    #print(l,end='')
for i in range(n_symbols):
    s=random.choice(all_symbols)
    password+=str(s)
    #print(s,end='')
for i in range(n_numbers):
    n=random.choice(all_numbers)
    #print(n,end='')
    password +=str(n)
print(password)
li=list(password)
random.shuffle(li)
pas=''.join(li)
print(pas)
