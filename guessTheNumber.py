import random
print("Hi what is your name")
name = input()
print("Nice to meet you "+name+" Lets play a game")
print("Input first number you want")
rand1 = input()
print("Input second number you want")
rand2 = input()
print(
    f"I will think of a number between {rand1} and {rand2} and you have to guess it in less than 6 guess")
print("Take a guess")
num = input()
num = int(num)
ranNum = random.randint(int(rand1), int(rand2))
maxTry = 5
theTry = 0
while num != ranNum and theTry < maxTry:
    print("Wrong, your guess is not the number")
    print("Take a guess")
    num = input()
    num = int(num)
    theTry += 1
if num == ranNum:
    print(f"Yay yo got the correct answer {ranNum}")
else:
    print(f"Sorry the number I was thinking of was {ranNum}")
    print("You should try again")
