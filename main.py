class GeometryCalculator:
    calculation_count = 0

    @staticmethod
    def calculate_triangle_area(base, height):
        GeometryCalculator.calculation_count += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_rectangle_area(length, width):
        GeometryCalculator.calculation_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        GeometryCalculator.calculation_count += 1
        return side ** 2

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        GeometryCalculator.calculation_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return GeometryCalculator.calculation_count



triangle_area = GeometryCalculator.calculate_triangle_area(5, 8)
rectangle_area = GeometryCalculator.calculate_rectangle_area(4, 6)
square_area = GeometryCalculator.calculate_square_area(3)
rhombus_area = GeometryCalculator.calculate_rhombus_area(7, 9)

print("Площа трикутника:", triangle_area)
print("Площа прямокутника:", rectangle_area)
print("Площа квадрата:", square_area)
print("Площа ромба:", rhombus_area)
print("Кількість підрахунків площі:", GeometryCalculator.get_calculation_count())
