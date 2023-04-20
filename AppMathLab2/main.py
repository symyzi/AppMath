import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


def right_derivative_at_point(f, x, h):
  return (f(x + h) - f (x))/h

def right_derivative(f, x, h, n):
  result = []
  for i in range(n + 1):
      result.append(right_derivative_at_point(f, x[i], h))
  return np.array(result)

def left_derivative_at_point(f, x, h):
  return (f(x) - f(x - h))/h

def left_derivative(f, x, h, n):
  result = []
  for i in range(n + 1):
    result.append(left_derivative_at_point(f, x[i], h))
  return np.array(result)

def central_derivative_at_point(f, x, h):
  return (f(x + h) - f(x - h))/(2*h)

def central_derivative(f, x, h, n):
  result = []
  for i in range(n + 1):
      result.append(central_derivative_at_point(f, x[i], h))
  return np.array(result)


f = lambda x : x**4
f_derivative = lambda x : 4*x**3
a, b = -5, 5
h = 1
n = int((b - a)/h)
x = []
for i in range(n + 1):
  x.append(a + h*i)

fig, (ax) =  plt.subplots(nrows = 1, ncols = 3) #, sharex = True, sharey = True)
fig.set_figwidth(20)
fig.set_figheight(15)
ax[0].stem(np.array(x), right_derivative(f, x, h, n), 'g')
ax[0].plot(np.array(x), f_derivative(np.array(x)), label = "Аналитическая производная")
ax[1].stem(np.array(x), left_derivative(f, x, h, n), 'g')
ax[1].plot(np.array(x), f_derivative(np.array(x)), label = "Аналитическая производная")
ax[2].stem(np.array(x), central_derivative(f, x, h, n), 'g')
ax[2].plot(np.array(x), f_derivative(np.array(x)), label = "Аналитическая производная")
ax[0].set_title("Правая разностная производная")
ax[1].set_title("Левая разностная производная")
ax[2].set_title("Центральная разностная производная")
plt.legend()
plt.savefig("f_derivative")


f = lambda x : np.cos(x)
# аналитическая (истинная) производная
f_derivative = lambda x : -np.sin(x)
# интервал, на котором мы определяем функцию
a, b = -5, 15
# шаг разбиения
h = 1
n = int((b - a)/h)
x = []
for i in range(n + 1):
  x.append(a + h*i)

fig, (ax) =  plt.subplots(nrows = 1, ncols = 3) #, sharex = True, sharey = True)
fig.set_figwidth(20)
fig.set_figheight(15)
ax[0].stem(np.array(x), right_derivative(f, x, h, n), 'g')
ax[0].plot(np.linspace(-5, 15), f_derivative(np.linspace(-5, 15)), label = "Аналитическая производная")
ax[1].stem(np.array(x), left_derivative(f, x, h, n), 'g')
ax[1].plot(np.linspace(-5, 15), f_derivative(np.linspace(-5, 15)), label = "Аналитическая производная")
ax[2].stem(np.array(x), central_derivative(f, x, h, n), 'g')
ax[2].plot(np.linspace(-5, 15), f_derivative(np.linspace(-5, 15)), label = "Аналитическая производная")
ax[0].set_title("Правая разностная производная")
ax[1].set_title("Левая разностная производная")
ax[2].set_title("Центральная разностная производная")
plt.legend()
plt.savefig("f_derivative_2")


def standard_deviation(numerical, true):
  summ = 0
  for i in range(len(true)):
    summ += (numerical[i] - true[i])**2
  return np.sqrt(summ/len(true))


f = lambda x: x ** 4
f_derivative = lambda x: 4 * x ** 3
h = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
a, b, = -5, 5


def array_x(a, b, h):
  n = int((b - a) / h)
  x = []
  for i in range(n + 1):
    x.append(a + h * i)
  return x, n


right_derivative_error = []
left_derivative_error = []
central_derivative_error = []
print("Среднеквадратическое отклонение")
for i in range(len(h)):
  x, n = array_x(a, b, h[i])
  array_f_derivative = list(map(lambda x: f_derivative(x), x))
  right_derivative_error.append(standard_deviation(right_derivative(f, x, h[i], n), array_f_derivative))
  left_derivative_error.append(standard_deviation(left_derivative(f, x, h[i], n), array_f_derivative))
  central_derivative_error.append(standard_deviation(central_derivative(f, x, h[i], n), array_f_derivative))

fig, (ax) = plt.subplots(nrows=1, ncols=3)
fig.set_figwidth(20)
fig.set_figheight(15)
ax[0].stem(h, right_derivative_error, 'g')
ax[0].plot(h, right_derivative_error, "k--")
ax[1].stem(h, left_derivative_error, 'g')
ax[1].plot(h, left_derivative_error, "k--")
ax[2].stem(h, central_derivative_error, 'g')
ax[2].plot(h, central_derivative_error, "k--")
ax[0].set_title("Правая разностная производная")
ax[1].set_title("Левая разностная производная")
ax[2].set_title("Центральная разностная производная")
plt.savefig("f_error_1")
plt.show()

f = lambda x: np.cos(x)
f_derivative = lambda x: -np.sin(x)
h = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
a, b, = -5, 15


def array_x(a, b, h):
  n = int((b - a) / h)
  x = []
  for i in range(n + 1):
    x.append(a + h * i)
  return x, n


right_derivative_error = []
left_derivative_error = []
central_derivative_error = []
print("Среднеквадратическое отклонение")
for i in range(len(h)):
  x, n = array_x(a, b, h[i])
  array_f_derivative = list(map(lambda x: f_derivative(x), x))
  right_derivative_error.append(standard_deviation(right_derivative(f, x, h[i], n), array_f_derivative))
  left_derivative_error.append(standard_deviation(left_derivative(f, x, h[i], n), array_f_derivative))
  central_derivative_error.append(standard_deviation(central_derivative(f, x, h[i], n), array_f_derivative))

fig, (ax) = plt.subplots(nrows=1, ncols=3)
fig.set_figwidth(15)
fig.set_figheight(10)
ax[0].stem(h, right_derivative_error, 'g')
ax[0].plot(h, right_derivative_error, "k--")
ax[1].stem(h, left_derivative_error, 'g')
ax[1].plot(h, left_derivative_error, "k--")
ax[2].stem(h, central_derivative_error, 'g')
ax[2].plot(h, central_derivative_error, "k--")
ax[0].set_title("Правая разностная производная")
ax[1].set_title("Левая разностная производная")
ax[2].set_title("Центральная разностная производная")
plt.savefig("f_error_2")
plt.show()

def elementary_rectangle(f, x, h):
  return f(x) * h

def left_rectangles(f, a, h, n):
  result = 0
  for i in range(1, n + 1):
      result += elementary_rectangle(f, a + h * (i - 1), h)
  return result

def right_rectangles(f, a, h, n):
  result = 0
  for i in range(1, n + 1):
    result += elementary_rectangle(f, a + h * i, h)
  return result

def medium_rectangles(f, a, h, n):
  result = 0
  for i in range(1, n + 1):
    result += elementary_rectangle(f, a + h * (i - 1/2), h)
  return result


def trapeze(f, a, h, n):
  result = 0
  for i in range(1, n + 1):
    result += h/2 * (f(a + h * i) + f(a + h * (i - 1)))
  return result


def simpson(f, a, h, n):
  result = 0
  for i in range(1, n + 1):
    result += h/6 * (f(a + h * (i - 1)) + f(a + h * (i + 1)) + 4 * f(a + h * (i - 1/2)))
  return result


f = lambda x : x**4
integral = 20000
a, b = 0, 10
h = 1
n = int((b - a)/h)

print("По формуле левых прямоугольников: ", left_rectangles(f, a, h, n))
print("По формуле правых прямоугольников: ", right_rectangles(f, a, h, n))
print("По формуле средних прямоугольников: ", medium_rectangles(f, a, h, n))


print("По формуле трапеций: ", trapeze(f, a, h, n))


print("По формуле Симпсона: ", simpson(f, a, h, n))

f = lambda x: x ** 4
integral = 20000
h = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
a, b, = 0, 10

right_rectangle_error = []
left_rectangle_error = []
medium_rectangle_error = []
trapeze_error = []
simpson_error = []
print("Среднеквадратическое отклонение")
for i in range(len(h)):
  n = int((b - a) / h[i])
  right_rectangle_error.append(standard_deviation([right_rectangles(f, a, h[i], n)], [integral]))
  left_rectangle_error.append(standard_deviation([left_rectangles(f, a, h[i], n)], [integral]))
  medium_rectangle_error.append(standard_deviation([medium_rectangles(f, a, h[i], n)], [integral]))
  trapeze_error.append(standard_deviation([trapeze(f, a, h[i], n)], [integral]))
  simpson_error.append(standard_deviation([simpson(f, a, h[i], n)], [integral]))

fig, (ax) = plt.subplots(nrows=1, ncols=5)
fig.set_figwidth(25)
fig.set_figheight(10)
ax[0].stem(h, right_rectangle_error, 'g')
ax[0].plot(h, right_rectangle_error, "k--")
ax[1].stem(h, left_rectangle_error, 'g')
ax[1].plot(h, left_rectangle_error, "k--")
ax[2].stem(h, medium_rectangle_error, 'g')
ax[2].plot(h, medium_rectangle_error, "k--")
ax[3].stem(h, trapeze_error, 'g')
ax[3].plot(h, trapeze_error, "k--")
ax[4].stem(h, simpson_error, 'g')
ax[4].plot(h, simpson_error, "k--")
ax[0].set_title("Метод правых прямоугольников")
ax[1].set_title("Метод левых прямоугольников")
ax[2].set_title("Метод средних прямоугольников")
ax[3].set_title("Метод трапеций")
ax[4].set_title("Метод Симпсона")

plt.savefig("f_error_integra")
plt.show()

f = lambda x : np.cos(x)
integral = -1.9178
a, b = -5, 5
h = 1
n = int((b - a)/h)

print("По формуле левых прямоугольников: ", left_rectangles(f, a, h, n))
print("По формуле правых прямоугольников: ", right_rectangles(f, a, h, n))
print("По формуле средних прямоугольников: ", medium_rectangles(f, a, h, n))


print("По формуле трапеций: ", trapeze(f, a, h, n))


print("По формуле Симпсона: ", simpson(f, a, h, n))

f = lambda x: np.cos(x)
integral = -1.9178
h = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
a, b, = -5, 5

right_rectangle_error = []
left_rectangle_error = []
medium_rectangle_error = []
trapeze_error = []
simpson_error = []
print("Среднеквадратическое отклонение")
for i in range(len(h)):
  n = int((b - a) / h[i])
  right_rectangle_error.append(standard_deviation([right_rectangles(f, a, h[i], n)], [integral]))
  left_rectangle_error.append(standard_deviation([left_rectangles(f, a, h[i], n)], [integral]))
  medium_rectangle_error.append(standard_deviation([medium_rectangles(f, a, h[i], n)], [integral]))
  trapeze_error.append(standard_deviation([trapeze(f, a, h[i], n)], [integral]))
  simpson_error.append(standard_deviation([simpson(f, a, h[i], n)], [integral]))

fig, (ax) = plt.subplots(nrows=1, ncols=5)
fig.set_figwidth(20)
fig.set_figheight(10)
ax[0].stem(h, right_rectangle_error, 'g')
ax[0].plot(h, right_rectangle_error, "k--")
ax[1].stem(h, left_rectangle_error, 'g')
ax[1].plot(h, left_rectangle_error, "k--")
ax[2].stem(h, medium_rectangle_error, 'g')
ax[2].plot(h, medium_rectangle_error, "k--")
ax[3].stem(h, trapeze_error, 'g')
ax[3].plot(h, trapeze_error, "k--")
ax[4].stem(h, simpson_error, 'g')
ax[4].plot(h, simpson_error, "k--")
ax[0].set_title("Метод правых прямоугольников")
ax[1].set_title("Метод левых прямоугольников")
ax[2].set_title("Метод средних прямоугольников")
ax[3].set_title("Метод трапеций")
ax[4].set_title("Метод Симпсона")
plt.savefig("f_error_integra_2")
plt.show()



