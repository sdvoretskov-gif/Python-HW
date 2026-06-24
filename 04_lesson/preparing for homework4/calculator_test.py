import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize('num1, num2, result', [(4,5,9), (6,-2,4), (7,0,7), (-5,5,0), (7.5, 3.3, 10.8)])
def test_sum_positive_nums(num1, num2, result):
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.xfail
def test_sum_negative_nums():
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    res = calculator.sum(3.7, 6.2)
    assert res == 9.9

@pytest.mark.skip
def test_sum_zero_nums():
    res = calculator.sum(12, 0)
    assert res == 12

def test_div_positive_nums():
    res = calculator.div(8, 4)
    assert res == 2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        res = calculator.div(10, 0)
        assert res == 0
@pytest.mark.parametrize('nums, result', [([], 0), ([4,4,1], 3)])
def test_avg_double_list(nums, result):
    res = calculator.avg(nums)
    assert res == result

def test_avg_positive_list():
    numbers = [2,4,6,8]
    res = calculator.avg(numbers)
    assert res == 5


#def test_sum_positive_num():
#res = calculator.sum(4, 5)
#assert res == 9

#res = calculator.sum(-6, -10)
#assert res == -16

#res = calculator.sum(-6, 6)
#assert res == 0

#res = calculator.sum(3.7, 6.2)
#assert res == 9.9

#res = calculator.sum(10, 0)
#assert res == 10

#res = calculator.div(10, 2)
#assert res == 5

#res = Calculator.div(10,0)
#assert res == None

#numbers = []
#res = calculator.avg(numbers)
#print(res)
#assert res == 0

#numbers = [1, 4, 4]
#res = calculator.avg(numbers)
#print(res)
#assert res == 3
