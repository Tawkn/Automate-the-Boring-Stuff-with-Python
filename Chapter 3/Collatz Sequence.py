# This is a Collatz Sequence
# if a Negative Even Number is entered, it will test the IF function once but then output the ELIF function

print('Enter an integer!!')

number = int(input())

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number < 0:
            print("Nope. I've had enough. Crashing right meow. ZzzZzzZzzz")
            break
        else:
            number = 3 * number + 1
            print(number)

try:
    collatz(number)
except ValueError:
    print('You suck.')




    
