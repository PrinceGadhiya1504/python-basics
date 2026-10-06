num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /, %): ").strip()

match operator:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        print("Result:", num1 / num2)

    case "%":
        print("Result:", num1 % num2)

    case _:
        print("Invalid operator.")