from typing import TypeVar

T = TypeVar("T", int, float)


def calc_method_one(k: T, g: T) -> tuple[T, T]:
    """
    Как называется этот метод?

    :rtype: tuple[float, float]
    """
    torch_length = k * g**0.4
    torch_width = 0.15 * torch_length
    return torch_length, torch_width


def calc_method_two(k: T, g: T) -> tuple[T, T]:
    """
    Как называется этот метод?

    :rtype: tuple[float, float]
    """
    pass


if __name__ == "__main__":
    K = (12.5, 13.5, 15)
    g_input = int(input())
    
    for i in range(3):
        Lf, Df = calc_method_one(K[i], g_input)
        print(f"1-ый метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")
        Lf, Df = calc_method_two(K[i], g_input)
        print(f"2-ой метод:\nLf = {Lf:.5}, Df = {Df:.5}\n")


"""def calculate(k, g):
    torch_length = k * g ** 0.4
    torch_width = 0.15 * torch_length
    return(torch_length, torch_width)

k_values = (12.5, 13.5, 15)

g_product_flow = float(input('Введите расход продукта (кг/с): '))
k_quotient = k_values[int(input('Выберите эмпирический коэффициент из списка (1, 2, 3)\n1. k = 12.5\n2. k = 13.5\n3. k = 15\n'))]

results = calculate(k_quotient, g_product_flow)
print(f'Lf = {results[0]:.5}, Df = {results[1]:.5}')"""
