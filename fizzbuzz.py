
number = int(raw_input("vnesi stevilo od 0 do 100: "))

for number in range(1, number+1):
    if number % 5 == 0 and number % 3 == 0:
        print "FizzBuzz"
    elif number % 5 == 0:
        print "Fizz"
    elif number % 3 == 0:
        print "Buzz"
    else:
        print number

