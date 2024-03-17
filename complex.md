## Требования к интерфейсу

Комплексные числа - числа вида $a + bi$, где $a$, $b$ - вещественные числа, $i$ - мнимая единица, то есть число, для которого выполняется равенство $i^2 = -1$.

В этом задании вам потребуется реализовать класс Complex, экземпляры которого представляют собой комплексные числа.

Конструктор Complex должен принимать два параметра: `real`, отражающий вещественную часть числа, и `imag`, отражающий множитель числа $i$. Оба параметра должны поддерживать позиционные и ключевые аргументы и иметь значение по умолчанию 0:


```python
Complex()                   # эквивалентно 0+0i 
Complex(1)                  # эквивалентно 1+0i 
Complex(1, 2)               # эквивалентно 1+2i
Complex(imag=3)             # эквивалентно 0+3i
Complex(pos=-2, imag=-5)    # эквивалентно -2+(-5i)
```

Экземпляры Complex должны поддерживать следующие операции:

- сложение (`+`)
- вычитание (`-`)
- умножение (`*`)
- деление (`/`)
- проверка равенства (`==`, `!=`)

Эти операции должны поддерживаться между любыми экземплярами `Complex` или встроенных типов `int` и `float`.

Вывод экземпляра 

## Теоретическая справка

Пусть $x = a + bi$ и $y = c + di$ &mdash; комплексные числа, тогда cложение и вычитание $x$ и $y$ представимы так:

$$
\begin{align*}
(a + bi) + (c + di) &= (a + c) + (b + d)i \\
(a + bi) - (c + di) &= (a - c) + (b - d)i
\end{align*}
$$

Пусть $c = r + 0i$ &mdash; вещественное число, тогда аналогичные операции между $x$ и $c$ представимы так:

$$
\begin{align*}
(a + bi) + (r + 0i) &= (a + r) + bi \\
(a + bi) - (r + 0i) &= (a - r) + bi
\end{align*}
$$

Произведение комплексных чисел:

$$
\begin{align*}
(a + bi) \cdot (c + di) &= ac + bci + adi + bdi^2 \\
                    &= (ac - bd) + (bc + ad)i
\end{align*}
$$

для вещественных чисел:

$$
(a + bi) \cdot r = ra + rbi
$$

Деление комплексных чисел:

$$
\begin{align*}
\frac{a + bi}{c + di}   &= \frac{(a + bi)(c - di)}{(c + di)(c - di)} \\
                        &= \frac{(a + bi)(c - di)}{c^2 + d^2} \\
                        &= \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i
\end{align*}
$$

для вещественных чисел:
$$
\frac{a + bi}{r} = \frac{a}{r} + \frac{b}{r}i
$$