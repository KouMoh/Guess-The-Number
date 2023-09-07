import random

range= int(input("Enter the range of the guess starting from 0: "))

number= random.randint(0,range)

a=None
count =0


while (a!=number):

    a=int(input("Enter your guessed number: "))

    if(a>range):
        print("Out of range number!")
        continue

    if(a<number):
        print("Think of a higher number")
        count+=1
    else :
        print("Think of a lower number")
        count+=1

print(f"Yes the number {a} is the correct choice!")
print(f"You have guessed the correct number after {count} times! ")
