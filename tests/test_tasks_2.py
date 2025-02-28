from hypothesis import given, settings
from hypothesis import strategies as st
from hypothesis.strategies import composite

from src.tasks_2 import *

# policies = [
#     r"^[a-zA-Z0-9]{8,}$",  # Alphanumeric, min 8 chars
#     r"^[a-z]+$",  # All lowercase
#     r"^\d{6}$",  # Exactly 6 digits
#     r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$" # 8+ chars, lowercase, uppercase, digit
# ]

@composite
def generate_password(draw):
    """
    Генерирует пароль, соответствующий политике (буквенно-цифровые символы, минимум 8 символов).

    Args:
        draw: Функция, используемая Hypothesis для рисования значений из стратегии.

    Returns:
        Сгенерированный пароль.
    """
    return draw(st.text(st.characters(min_codepoint=48, max_codepoint=122), min_size=8)) # Alphanumeric range


@given(data=generate_password())
@settings(max_examples=10000)
def test_authentication(data):
    """
    Тестирует аутентификацию с использованием сгенерированных паролей.

    Args:
        Сгенерированный пароль от Hypothesis.
    """
    password_policy =  r"^[a-zA-Z0-9]{8,}$"
    real_password = "SecurePassword123"

    #  Убеждаемся, что реальный пароль соответствует политике
    assert check_password_policy(real_password, password_policy), f"real_password не соответствует заданной политике {password_policy}"

    candidate_password = data

    # Убеждаемся, что кандидатский пароль соответствует политике
    assert check_password_policy(candidate_password, password_policy), f"candidate_password не соответствует заданной политике {password_policy}"

    #  Проверяем аутентификацию и выявляем коллизии
    if authentication(real_password, candidate_password):
        # Пароли не должны совпадать, если аутентификация прошла успешно
        assert real_password != candidate_password, f"Обнаружена коллизия!  real_password: {real_password}, candidate_password: {candidate_password}"
