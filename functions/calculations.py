from typing import TypeVar

T = TypeVar("T", int, float)
PI = 3.14

PA = 101325
GAMMA = 1.31
U = 0.8
A = 0.134614104
RoV = 1

""" Ap = PI * ((d - 2 * 0.006) ** 2) / 4 """ 
""" g = ((PH * Ap * K ** 0.5) / (R * Z * TH) ** 0.5) * (2 / (K - 1)) ** ((k + 1) / (2* (k - 1))) """

PH = 7500000
R = 519
TH = 9
L = 196.6
Z = 1
K = 1.31

def calc_method_one(k: T, d: T) -> tuple[T, T]:
    """
    Как называется этот метод?
    - Струйное горение (факел)

    :rtype: tuple[float, float]
    """
    Ap = PI * ((d - 2 * 0.006) ** 2) / 4
    g = ((PH * Ap * K ** 0.5) / (R * Z * TH) ** 0.5) * (2 / (K - 1)) ** ((k + 1) / (2* (k - 1)))

    torch_length = k * g**0.4
    torch_width = 0.15 * torch_length
    return torch_length, torch_width


def calc_method_two(k: T, pv: T) -> tuple[T, T]:
    """
    Как называется этот метод?
    - Истечение сжатого газа

    :rtype: tuple[float, float]
    """
    if (PA / pv) >= ((2 / (GAMMA + 1)) ** (GAMMA / (GAMMA - 1))):
        g = A * U * (pv * RoV * (2 * GAMMA / (GAMMA - 1)) * (PA / pv) ** (2 / GAMMA) * (1 - (PA / pv) ** ((GAMMA - 1) / GAMMA)) ** 0.5)
    else:
        g = A * U * (pv * RoV * GAMMA * (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (GAMMA - 1))) ** 0.5
    return calc_method_one(k, g)


def calculate_all(k: T, g: T, pv: T) -> tuple[tuple[float, float], tuple[float, float]]:
    """
    Метод для расчётов сразу двух методов

    :rtype: tuple[tuple[float, float], tuple[float, float]]
    """
    return calc_method_one(k, g), calc_method_two(k, pv)


if __name__ == "__main__":
    K = (12.5, 13.5, 15)
    D = (0.025, 0.05, 0.1, 0.426)
    pv_input = int(input())

    for i in range(3):
        Lf, Df = calc_method_one(K[i], D[i])
        print(f"1-ый метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")
        Lf, Df = calc_method_two(K[i], pv_input)
        print(f"2-ой метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")
