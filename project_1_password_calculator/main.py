PASSWORD = "1234"
MAX_ATTEMPTS = 3


def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Моля, въведете цяло число.")


def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            return None
        return first_number / second_number
    return None


def main():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        password = input("Въведете парола: ")

        if password == PASSWORD:
            print("Достъпът е разрешен.")

            first_number = read_int("Въведете първо число: ")
            second_number = read_int("Въведете второ число: ")
            operation = input("Изберете операция (+, -, *, /): ")

            result = calculate(first_number, second_number, operation)

            if result is None:
                print("Невалидна операция или деление на нула.")
            else:
                print(f"Резултат: {result}")
            return

        attempts_left = MAX_ATTEMPTS - attempt
        if attempts_left > 0:
            print(f"Грешна парола. Остават {attempts_left} опита.")

    print("Достъпът е забранен.")


if __name__ == "__main__":
    main()
