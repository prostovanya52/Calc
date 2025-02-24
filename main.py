from Calc import add, subtract, multiply, divide


def parse_and_calculate(expression):
    try:

        result = eval(expression)
        print(f"{expression} = {result}")

    except ZeroDivisionError:
        print("Нельзя делить на ноль!")

    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    print("Простой калькулятор")

    while True:
        expression = input("\nВведите выражение (например: 2+2 или q для выхода): ")

        if expression.lower() == 'q':
            break

        parse_and_calculate(expression)


if __name__ == "__main__":
    main()
