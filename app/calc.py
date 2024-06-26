from math import log10, sqrt


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        #if not app.util.validate_permissions(f"{x} * {y}", "user1"):
        #    raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return pow(x, y)
    
    def square(self, x, y):
        self.check_types(x, y)
        return sqrt(x)
    
    def log10(self, x, y):
        self.check_types(x, y)
        if x <= 0:
            raise TypeError("To use log10 please enter a number greater than 0")
        return log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    #result = calc.add(2, 2)
    result = calc.log10(10, 0)
    print(result)
