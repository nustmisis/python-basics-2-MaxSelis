"""
Реализуйте класс Complex, экземпляры которого представляют собой комплексные
числа.

Обратите внимание! Python предоставляет встроенный интерфейс для работы с
комплексными числами: тип complex (со строчной буквы). В рамках этого задания
считайте, что этого типа не существует.

Конструктор Complex должен принимать два параметра: 

- real типа int или float, отражающий вещественную часть числа;
- imag типа int или float, отражающий множитель числа i. 

Оба параметра должны поддерживать позиционные и ключевые аргументы и иметь
значение по умолчанию 0.

Примеры использования конструктора Complex:

>>> Complex()
0+0i

>>> Complex(1)
1+0i

>>> Complex(-2, 0.5)
-2+0.5i

>>> Complex(imag=-1)
0-1i

>>> Complex(real=4, imag=2)
4+2i

Экземпляры Complex должны иметь поля real и imag, содержащие соответствующие им
значения вещественной части числа и коэффициента числа i

>>> Complex(10, 20).real
10

>>> Complex(imag=-1.0).imag
-1.0

Строковое представление экземпляров Complex должно иметь вид a+bi, при
отрицательных b знак "+" опускается. Примеры:

>>> Complex()
0+0i

>>> Complex(1)
1+0i

>>> Complex(1, 2)
1+2i

>>> Complex(-1, -2)
-1-2i

Экземпляры Complex должны поддерживать следующие операции:

- сложение (+);
- вычитание (-);
- умножение (*);
- деление (/);
- проверка равенства (==, !=).

Результатом всех операций (кроме == и !=) должны быть новые экземпляры Complex,
старые экземпляры при этом не должны изменяться.

Эти операции должны поддерживаться между любыми экземплярами Complex или
встроенных типов int и float вне зависимости от порядка аргументов. Примеры
допустимых операций:

>>> 1 + Complex(1, 2)
2+2i

>>> Complex(3, 4) - 0.5
2.5+4i

>>> 3 / Complex(-2, 1)
-1.2-0.6i

>>> Complex(5, 1) * Complex(0.4, 0.3)
1.7+1.9i

>>> 7.7 == Complex(real=7.7)
True

>>> -1 == Complex(real=-1, imag=4)
False
"""

from __future__ import annotations  # игнорируйте эту строку


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        return other.__sub__(self)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)
        
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        return other.__truediv__(self)
    
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other)
        return self.real == other.real and self.imag == other.imag
    
    def __noteq__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        real_str = f"{self.real:.10g}" if isinstance(self.real, float) else str(self.real)
        imag_str = f"{self.imag:.10g}" if isinstance(self.imag, float) else str(self.imag)
        
        if self.real == 0 and self.imag == 0:
            return "0+0i"
        elif self.real == 0:
            return f"{imag_str}i"
        elif self.imag == 0:
            return f"{real_str}+0i"
        elif self.imag > 0:
            return f"{real_str}+{imag_str}i"
        else:
            return f"{real_str}{imag_str}i"


if __name__ == "__main__":
    c1 = Complex(1)
    c2 = Complex(2)
    print(c1 + 1)
