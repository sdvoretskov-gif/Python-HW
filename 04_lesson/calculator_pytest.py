from calculator import Calculator

calculator = Calculator()

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-6, -10)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(3.7, 6.2)
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10

res = calculator.div(10, 2)
assert res == 5

#res = Calculator.div(10,0)
#assert res == None

numbers = []
res = calculator.avg(numbers)
print(res)
assert res == 0

numbers = [1, 4, 4]
res = calculator.avg(numbers)
print(res)
assert res == 3
