INITIAL_BALANCE = 500
ALLOWED_REASON = "спешно"


def read_money(message):
    while True:
        try:
            amount = float(input(message))
            if amount <= 0:
                print("Сумата трябва да е положително число.")
            else:
                return amount
        except ValueError:
            print("Моля, въведете валидна сума.")


def main():
    balance = INITIAL_BALANCE

    print(f"Начална сума в банкомата: {balance:.2f} лв.")
    amount = read_money("Колко пари искате да изтеглите? ")

    if amount > balance:
        print("Няма достатъчно пари в банкомата.")
        return

    reason = input("Защо искате да изтеглите пари? ").strip().lower()

    if reason == ALLOWED_REASON:
        balance -= amount
        print(f"Тегленето е успешно. Оставаща сума: {balance:.2f} лв.")
    else:
        print("Тегленето е отказано. Позволена причина: спешно.")


if __name__ == "__main__":
    main()
