name = input("What is your name ")
number1 = int(input("Enter Your Favorite 1st Number "))
number2 = int(input("Enter Your Favorite 2nd Number "))
number3 = int(input("Enter Your Favorite 3rd Number "))
print(f"We Warmly Welcome {name} Here !")
print(f"Lets Explore Your Favorite Number {name}")
list1 = []
list1.append(number1)
list1.append(number2)
list1.append(number3)
for numbers in list1:
    if numbers % 2 == 0:
        print(f"Your Given Number {numbers} Is Even")
    else :
        print(f"Your Given Number {numbers} Is Odd")  

for squares in list1:
    square = squares**2
    print(f"The Square of Number {squares} is {square}")
    tuples = (squares,square)
    print(tuples)

sum = number1 + number2 + number3
print(f"The Sum Of All Your Favorite Numbers Is {sum}")

is_prime_number = True
if sum > 1:
    for num in range(2, int(sum**0.5) + 1):
        if sum % num == 0:
            is_prime_number = True
            print(f"WoW ! Your Given Number {sum} is Not Prime")
            break
    else:
        is_prime_number = False
        print(f"Wow ! Your Given Number {sum} Is Prime Number")


