from typing import TypeVar

T = TypeVar("T", int, float)

PA = 101325
G = 1.31
U = 0.8
A = 0.134614104
RoV = 1


def calc_method_one(k: T, g: T) -> tuple[T, T]:
    """
    Как называется этот метод?
    - Струйное горение (факел)

    :rtype: tuple[float, float]
    """
    torch_length = k * g**0.4
    torch_width = 0.15 * torch_length
    return torch_length, torch_width


def calc_method_two(k: T, pv: T) -> tuple[T, T]:
    """
    Как называется этот метод?
    - Истечение сжатого газа

    :rtype: tuple[float, float]
    """
    if (PA / pv) >= ((2 / (G + 1)) ** (G / (G - 1))):
        g = A * U * (pv * RoV * (2 * G / (G - 1)) * (PA / pv) ** (2 / G) * (1 - (PA / pv) ** ((G - 1) / G)) ** 0.5)
    else:
        g = A * U * (pv * RoV * G * (2 / (G + 1)) ** ((G + 1) / (G - 1))) ** 0.5
    return calc_method_one(k, g)


def calculate_all(k: T, g: T, pv: T) -> tuple[tuple[float, float], tuple[float, float]]:
    """
    Метод для расчётов сразу двух методов

    :rtype: tuple[tuple[float, float], tuple[float, float]]
    """
    return calc_method_one(k, g), calc_method_two(k, pv)


if __name__ == "__main__":
    K = (12.5, 13.5, 15)
    g_input = int(input())
    pv_input = int(input())

    for i in range(3):
        Lf, Df = calc_method_one(K[i], g_input)
        print(f"1-ый метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")
        Lf, Df = calc_method_two(K[i], pv_input)
        print(f"2-ой метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")
