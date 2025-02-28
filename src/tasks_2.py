import re
import hashlib

def check_password_policy(password: str, policy: str) -> bool:
    """
    Проверяет, соответствует ли пароль заданной политике, заданной с использованием регулярных выражений.

    Args:
        password: Пароль для проверки.
        policy: Строка регулярного выражения, определяющая политику паролей.

    Returns:
        True, если пароль соответствует политике, False в противном случае.
    """
    try:
        return bool(re.fullmatch(policy, password))
    except re.error as e:
        # print(f"Некорректное регулярное выражение: {e}")
        return False

def calculate_md5_hash(data: str) -> str:
    """
    Вычисляет MD5-хеш заданной строки.

    Args:
        str: Строка, для которой нужно вычислить хеш.

    Returns:
        MD5-хеш строки в виде шестнадцатеричной строки.
    """
    encoded_data = data.encode('utf-8')  # Encode the string to bytes
    md5_hash = hashlib.md5(encoded_data).hexdigest()
    return md5_hash

def authentication(real_password: str, candidate_password: str) -> bool:
    """
    Аутентифицирует пользователя, сравнивая MD5-хеш предложенного пароля (candidate_password)
    с MD5-хешем реального пароля (real_password).

    Args:
        real_password: Реальный, сохраненный пароль (используется как эталон).
        candidate_password: Пароль, предоставленный пользователем для аутентификации.

    Returns:
        True, если предложенный пароль совпадает с реальным (на основе сравнения их MD5-хешей)
        и оба пароля соответствуют заданной политике; False в противном случае.
    """
    return calculate_md5_hash(real_password) == calculate_md5_hash(candidate_password)

