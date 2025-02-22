from hypothesis import given, assume, settings
from hypothesis import strategies as st
from hypothesis.strategies import composite

from src.tasks_1 import *


@composite
def months(draw):
    """Возвращает случайные номера месяцев

    Args:
        draw SearchStrategy: генератор данных

    Returns:
        List: Список месяцев, каждый из которых содержит список номеров дней
    """

    return [
        draw(
            st.lists(st.integers(min_value=1, max_value=30), min_size=1)
        ),  # 4,6,9,11 months
        draw(
            st.lists(st.integers(min_value=1, max_value=31), min_size=1)
        ),  # 1,3,5,7,8,12 months
        draw(st.lists(st.integers(min_value=1, max_value=28), min_size=1)),  # Feb
        draw(st.lists(st.integers(min_value=1, max_value=29), min_size=1)),  # Feb leap
    ]


@given(months=months(), offset=st.integers(min_value=0, max_value=6))
@settings(max_examples=10000)
def test_day_by_day_month(months, offset):
    """Проверим, что наша функция работает корректно для каждого месяца и для каждого смещения

    Args:
        n int: номер месяца
        s int: номер дня начала недели

    Detected & fixed falsifying examples:
        1) n=7 s=0
        2) n=2 s=6
        3) n=1 s=0
    """

    for month in months:
        for day in month:
            week_day = day_by_day_month(day, offset)

    assert week_day in set([1, 2, 3, 4, 5, 6, 7])
