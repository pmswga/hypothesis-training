import math

"""
Задачи из задачника "Банк заданий для зачёта".
"""


def day_by_day_month(n: int, s: int = 0) -> int:
    """Возвращает день неделю по номеру дня в месяце

    Args:
        n (int): номе дня в месяце
        s (int, optional): номер первого дня в недели, т.е. смещение. По умолчанию - 0, что соответствует понедельнику

    Returns:
        int: день недели
    """
    assert 0 < n <= 31, "month number must be in set of [0..31]"
    assert 0 <= s <= 6, "day offset must be in set of [0..6]"

    mod = n % 7

    match mod:
        case 0:
            return mod + (7 - s)
        case _:
            day = n % 7 + s
            return day - 7 if day > 7 else day
