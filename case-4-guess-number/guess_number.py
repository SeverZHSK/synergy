"""
Кейс-задача №4. Игра "Угадай число".

Функциональность:
1. Программа случайным образом выбирает число в диапазоне (по умолчанию 1..100).
2. Запрашивает у пользователя предположение.
3. Проверяет, совпадает ли предположение с загаданным числом.
4. Даёт подсказки: "слишком маленькое" / "слишком большое".
5. Ограничивает количество попыток (по умолчанию 7 — этого достаточно, чтобы
   гарантированно угадать число от 1 до 100 при оптимальной стратегии
   бинарного поиска: ceil(log2(100)) = 7).
6. После окончания раунда предлагает сыграть ещё раз и ведёт статистику
   по всем сыгранным раундам за сессию.

Автор: практикант, направление "Информационные системы и технологии",
профиль "Тестирование и DevOps".
"""

import random


def get_guess(low: int, high: int, attempts_left: int) -> int:
    """
    Запрашивает у пользователя число в диапазоне [low, high].

    Некорректный ввод (не число, число вне диапазона) не считается
    израсходованной попыткой — пользователь просто получает сообщение
    об ошибке и вводит число заново. Это осознанное решение по UX:
    попытка списывается только за содержательную, "засчитанную" догадку.
    """
    while True:
        raw_value = input(
            f"Попыток осталось: {attempts_left}. "
            f"Введите число от {low} до {high}: "
        ).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print(f'Ошибка: "{raw_value}" не является целым числом. Попробуйте снова.')
            continue

        if not (low <= value <= high):
            print(f"Ошибка: число должно быть в диапазоне от {low} до {high}.")
            continue

        return value


def play_round(low: int = 1, high: int = 100, max_attempts: int = 7) -> int:
    """
    Проводит один раунд игры.

    Возвращает количество затраченных попыток, если пользователь угадал
    число, и None, если попытки закончились. (Технически для простоты
    возвращаем -1 при поражении, чтобы не усложнять типизацию.)
    """
    secret_number = random.randint(low, high)
    print(f"\nЯ загадал число от {low} до {high}. У вас есть {max_attempts} попыток.")

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(low, high, max_attempts - attempt + 1)

        if guess == secret_number:
            print(f"Поздравляю, вы угадали число {secret_number} за {attempt} попыток(ки)!")
            return attempt

        if guess < secret_number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")

    print(f"\nПопытки закончились. Загаданное число было: {secret_number}.")
    return -1


def print_instructions() -> None:
    print("=" * 50)
    print("ИГРА «УГАДАЙ ЧИСЛО»")
    print("=" * 50)
    print(
        "Правила: компьютер загадывает число от 1 до 100.\n"
        "Ваша задача — угадать его за ограниченное число попыток.\n"
        "После каждой попытки вы получите подсказку:\n"
        "  «Слишком маленькое» — загаданное число больше;\n"
        "  «Слишком большое»   — загаданное число меньше.\n"
    )


def main() -> None:
    print_instructions()

    games_played = 0
    wins = 0
    attempts_in_wins = []

    while True:
        result = play_round(low=1, high=100, max_attempts=7)
        games_played += 1
        if result != -1:
            wins += 1
            attempts_in_wins.append(result)

        again = input("\nСыграть ещё раз? (y/n): ").strip().lower()
        if again not in ("y", "yes", "д", "да"):
            break

    print("\n--- Статистика за сессию ---")
    print(f"Сыграно раундов: {games_played}")
    print(f"Побед: {wins} из {games_played}")
    if attempts_in_wins:
        avg_attempts = sum(attempts_in_wins) / len(attempts_in_wins)
        print(f"Среднее число попыток при победе: {avg_attempts:.1f}")
    print("Спасибо за игру!")


if __name__ == "__main__":
    main()
