import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Xr = []
Yr = []
Xb = []
Yb = []
color =['red']
color1 = ['blue']

def test_function(x):
    return np.sin(x)

def main_function(x):
    return np.exp(-x**2)

def compute_exact_integral_test_function():
    a = 0
    b = np.pi
    return (-np.cos(b)+np.cos(a))

def compute_exact_integral_main_function():
    return quad(main_function, 0, np.pi)[0]

def generate_random_point():
    x = np.random.uniform(0, np.pi)
    y = np.random.uniform(0, 1)
    return x, y

def monte_carlo_integration(n, function):
   counter = 0
   for _ in range(n):
      x, y = generate_random_point()
      if y <= function(x):
         counter += 1
         Xb.append(x)
         Yb.append(y)
      Xr.append(x)
      Yr.append(y)
   return np.pi * counter/n


def print_plot(function, title):
   xx = np.linspace(0, np.pi, 100)
   yy = function(xx)
   N = str(10000)

   plt.scatter(Xr, Yr, s=10, c=color)
   plt.scatter(Xb, Yb, s=10, c=color1)
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title(title)
   plt.plot(xx, yy, '--')
   plt.grid()
   plt.show()


exact_integral_test = compute_exact_integral_test_function()
print("Точне значення інтеграла тестової функції:", exact_integral_test)

exact_integral_main = compute_exact_integral_main_function()
print("Точне значення інтеграла основної функції:", exact_integral_main)

n = 10000
estimated_integral_test = monte_carlo_integration(n, test_function)
print("\nОцінка інтеграла тестової функції методом Монте-Карло:", estimated_integral_test)
print_plot(test_function, 'sin(x)')

Xr = []
Yr = []
Xb = []
Yb = []

estimated_integral_main = monte_carlo_integration(n, main_function)
print("Оцінка інтеграла основної функції методом Монте-Карло:", estimated_integral_main)
print_plot(main_function, 'e^(-x^2)')

absolute_test = abs(exact_integral_test - estimated_integral_test)
relative_test = absolute_test / exact_integral_test
print("\nАбсолютна похибка тестової функції:", absolute_test)
print("Відносна похибка тестової функції:", relative_test)

absolute_main = abs(exact_integral_main - estimated_integral_main)
relative_main = absolute_main / exact_integral_main
print("Абсолютна похибка основної функції:", absolute_main)
print("Відносна похибка основної функції:", relative_main)

