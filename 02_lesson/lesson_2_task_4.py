def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


fizz_buzz(6)
