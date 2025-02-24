def add(x, y):
    """Сложение двух чисел."""
    return x + y

def subtract(x, y):
    """Вычитание двух чисел."""
    return x - y

def multiply(x, y):
    """Умножение двух чисел."""
    return x * y

def divide(x, y):
    """Деление двух чисел."""
    if y == 0:
        raise ValueError("Нельзя делить на ноль!")
    return x / y
