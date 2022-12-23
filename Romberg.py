import numpy as np
from scipy import integrate 

def f(x):
    return x**2
    
interg = lambda x: f(x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

a = 0
b = 1
n = 4
result_trapezoidal = trapezoidal(a, b, n)

romberg = integrate.romberg(interg, a, b, show = True) 
result_romberg = romberg

print("Hasil perhitungan metode Trapezoidal:", result_trapezoidal)
print("Hasil perhitungan metode Integrasi Romberg:", result_romberg)

true_result = 0.3333333333333333  
Trelative_error = abs(true_result - result_trapezoidal) / abs(true_result)
Rrelative_error = abs(true_result - result_romberg) / abs(true_result)

print("Trapezoidal Err :", Trelative_error)
print("Romberg Err :", Rrelative_error)  