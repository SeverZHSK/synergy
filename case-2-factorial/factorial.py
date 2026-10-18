import math
import time


def get_positive_integer(prompt: str = "Введите положительное целое число: ") -> int:
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print(
                f'Ошибка: "{raw_value}" не является целым числом. '
                "Повторите ввод (например: 5)."
            )
            continue

        if value < 0:
            print("Ошибка: число не может быть отрицательным. Повторите ввод.")
            continue

        return value


def factorial_manual(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_optimized(n: int) -> int:
    return math.factorial(n)


def compare_performance(n: int) -> None:
    start = time.perf_counter()
    manual_result = factorial_manual(n)
    manual_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized_result = factorial_optimized(n)
    optimized_time = time.perf_counter() - start

    assert manual_result == optimized_result, "Результаты реализаций не совпадают!"

    print("\n--- Сравнение производительности ---")
    print(f"Собственная реализация:      {manual_time:.6f} сек.")
    print(f"math.factorial (оптимизир.): {optimized_time:.6f} сек.")


def main() -> None:
    print("Программа вычисления факториала числа")
    print("=" * 45)

    n = get_positive_integer()

    result = factorial_optimized(n)

    digits = len(str(result))
    if digits <= 50:
        print(f"\n{n}! = {result}")
    else:
        print(f"\n{n}! содержит {digits} цифр.")
        print(f"Первые 30 цифр: {str(result)[:30]}...")
        print(f"Последние 30 цифр: ...{str(result)[-30:]}")

    if n >= 200:
        compare_performance(n)


if __name__ == "__main__":
    main()
