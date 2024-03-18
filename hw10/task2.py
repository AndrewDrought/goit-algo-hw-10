import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import random


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


def monte_carlo_integration(f, a, b, n=10000):
    sum_of_samples = 0
    for _ in range(n):
        x = random.uniform(a, b)
        sum_of_samples += f(x)
    return (b - a) * sum_of_samples / n


# Обчислення інтеграла
integral_value = monte_carlo_integration(f, a, b)
print(f"Значення інтеграла за допомогою методу Монте-Карло: {integral_value}")

# Аналітичне обчислення інтеграла
analytical_integral_value, _ = quad(f, a, b)
print(f"Аналітичне значення інтеграла: {analytical_integral_value}")

# Порівняння результатів
print(f"Різниця між значеннями: {abs(analytical_integral_value - integral_value)}")
