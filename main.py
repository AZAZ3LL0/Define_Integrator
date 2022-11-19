import math


def f(x):
    f = math.exp(x) + math.sqrt(3*x) + math.cos(-9*x) - 5*x**2
    return f


down_limit = int(input("Введите нижнюю границу интеграла:"))
up_limit = int(input("Введите верхнюю границу интеграла:"))
n = int(input("Введите количество интервалов:"))
dx = ((up_limit - down_limit) / n)
integral = 0

for i in range(1, n):
    integral = integral + dx * f(i * dx)

print("Значение определённого интеграла = ", integral)
print("Точность" + str((integral/n) /integral) + '%')
