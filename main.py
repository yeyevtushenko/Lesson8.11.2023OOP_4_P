class Calculator:
    @staticmethod
    def find_maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def find_minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def calculate_average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * Calculator.calculate_factorial(n - 1)



numbers = (7, 2, 10, 5)

max_value = Calculator.find_maximum(*numbers)
min_value = Calculator.find_minimum(*numbers)
average_value = Calculator.calculate_average(*numbers)
factorial_values = [Calculator.calculate_factorial(num) for num in numbers]

print("Максимальне значення:", max_value)
print("Мінімальне значення:", min_value)
print("Середнє арифметичне:", average_value)
print("Факторіали чисел:", factorial_values)