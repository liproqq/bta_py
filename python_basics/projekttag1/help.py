number = int(input("Enter a number: "))
primelist = [2, 3, 5, 7]
if number > 1:
    if number in primelist:
        print(number in primelist == True)
        print("It is a prime number.")
    else:
        for x in range(2, number+1):
            if number % x == 0:
                print("It is not a prime number.")
                break
            else:
                print("It is a prime number.")
                break
else:
    print("Please enter a positive number.")
