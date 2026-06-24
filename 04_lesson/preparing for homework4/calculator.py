class Calculator:

    @staticmethod
    def sum(a, b):
        result = a + b
        return result

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if (b == 0):
            raise ZeroDivisionError("На ноль делить нельзя")
        return a / b

    @staticmethod
    def pow(a, b=2):
        return a ** b

    @staticmethod
    def avg(nums):
        if (len(nums) == 0):
            return 0

        s = 0
        for num in nums:
            s = s + num

        l = len(nums)
        return s / l
