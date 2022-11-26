from math import *
from numpy import *
from scipy.misc import derivative

def search (x): #Допоміжна функція пошуку f(0)
    return (3*pow(x, 4)) - (4*pow(x, 3)) + (2*pow(x, 2)) - (4*x) - 1

def xn(a, b): #Допоміжна функція пошуку Хn
    return (a+b)/2

def module(a, b): #Допоміжна функція пошуку модуля |a - b|
    return abs(a-b)

def search_from_e (a, b, eps):  #Функція знаходження кореня
    n = 0                        #Лічільник ітерацій
    while (module(a, b) > eps):   #Якщо модуль більше чим умовна одиниця точності
        x_n = xn(a, b)  #Шукаємо середній корінь
        if search(x_n) > 0:
            b = x_n    #За теоремою якщо f(середнього корня)
        else:
            a = x_n                  #більша за 0, то b = с.корню
        n+=1                           #менша за 0, то а = с.корню
    print("Оскільки |a", n,  " – b", n, "| меньше за ", eps, "то ітераційний процес зупиняємо.")
    print("За наближене значення кореня візьмемо", round((a+b)/2, 4))
    print("Відповідь: х2 =", round((a+b)/2, 4), ", х1 = -", round((a+b)/2, 4), ".")

search_from_e(sqrt(3)/3, 1, 0.01)   #Викликаємо функцію з аргументами с розрахунків


def hord(a, b, eps):
    if (module(a, b) < eps):
        print("Кореня немає!")
        return
    if (search(a)*derivative(search, a, n=2) > 0):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * search(xi) / (search(xi) - search(x0))
    while (abs(search(xi_1) - search(xi)) > eps):
        xi = xi_1
        xi_1 = xi - (xi - x0) * search(xi) / (search(xi) - search(x0))
    else:
        print(f'Корінь знаходиться в точці x =', round(xi_1, 4))
hord(sqrt(3)/3, 1, 0.01)