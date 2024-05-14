def calculate(k, g):
    torch_length = k * g ** 0.4
    torch_width = 0.15 * torch_length
    return(torch_length, torch_width)

k_values = (12.5, 13.5, 15)

g_product_flow = float(input('Введите расход продукта (кг/с): '))
k_quotient = k_values[int(input('Выберите эмпирический коэффициент из списка (1, 2, 3)\n1. k = 12.5\n2. k = 13.5\n3. k = 15\n'))]

results = calculate(k_quotient, g_product_flow)
print(f'Lf = {results[0]:.5}, Df = {results[1]:.5}')