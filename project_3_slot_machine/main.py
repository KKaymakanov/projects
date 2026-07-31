import random


START_MONEY = 50
BET = 10
WIN_PRIZE = 100


def spin():
    return [random.randint(1, 9) for _ in range(3)]


def is_winning_spin(numbers):
    return numbers[0] == numbers[1] == numbers[2]


def main():
    answer = input("Искате ли да заредите 50 лв. за игра? (да/не): ").strip().lower()

    if answer != "да":
        print("Играта приключи.")
        return

    money = START_MONEY

    while money >= BET:
        money -= BET
        numbers = spin()
        print(f"Числа: {numbers[0]} {numbers[1]} {numbers[2]}")

        if is_winning_spin(numbers):
            money += WIN_PRIZE
            print(f"Печелите {WIN_PRIZE} лв. Общо пари: {money} лв.")
        else:
            print(f"Няма печалба. Остават ви {money} лв.")

        if money < BET:
            break

        again = input("Искате ли да опитате отново? (да/не): ").strip().lower()
        if again != "да":
            break

    print(f"Край на играта. Крайна сума: {money} лв.")


if __name__ == "__main__":
    main()
