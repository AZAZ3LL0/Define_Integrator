import math


def y(x):
    f = math.exp(-2*x) + math.sqrt(3*x) + math.cos(-9*x) - 5*x**1.5
    return f


down_limit = int(input("Введите нижнюю границу интеграла:"))
up_limit = int(input("Введите верхнюю границу интеграла:"))
n = int(input("Введите количество интервалов:"))
dx: float = ((up_limit - down_limit) / n)
integral = 0

for i in range(1, n):
    integral = integral + dx * y(i * dx)

print("Значение определённого интеграла = ", integral)
print("Точность " + str((integral/n) /integral) + '%')
