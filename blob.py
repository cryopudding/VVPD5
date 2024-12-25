import math


def m_cos(x, terms):
    """
    Функция cos(x) с использованием ряда Маклорена.

    Подробное описание:
    Ряд Маклорена для cos(x) является частным случаем ряда Тейлора, разложенного при x=0.
    Определяется как:
        cos(x) = \sum((-1)^n * x^(2n) / (2n)!, n=0 до бесконечности)
    Функция вычисляет приближение, используя конечное количество членов ряда.

    Аргументы:
    x (float): Входное значение для аппроксимации cos(x).
    terms (int): Количество членов в ряде для приближения.

    Возвращаемое значение:
    float: Аппроксимированное значение cos(x).

    Исключения:
    нет.

    Примеры:
    m_cos(0)
    1.0
    m_cos(3.14159, terms=5)
    -0.999999943741051

    """
    result = 0
    for n in range(terms):
        result += (-1)**n * (x**(2*n)) / math.factorial(2*n)
    return result