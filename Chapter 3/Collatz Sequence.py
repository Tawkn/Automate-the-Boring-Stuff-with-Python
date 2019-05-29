print('Welcome to the Collatz Sequence!')
print('If I were a betting a man, I would bet that starting with integer > 1 you choose, the last return value will be 1!')
print('..Eventually :)')
print('Enter your number!')

number = int(input())

while number != 1:
    if number % 2 == 0:
        number = number // 2
        print(number)
    elif number <= 0:
        print("Nope. I've had enough. Crashing right meow. ZzzZzzZzzz")
        break
    else:
        number = 3 * number + 1
        print(number)





    
