Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш строки s. В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:

![aChzKSA9IChzXzFhXntuLTF9ICsgc18yYV57bi0yfSArIFxkb3RzICsgc197bi0xfWEgKyBzX3tufSkgXCBtb2QgXCBt](https://github.com/kkhitalenko/secrets/assets/115172229/e78bed3f-f475-4777-a5b0-e0de86096199)


## Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 10^9) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 10^6), состоящая из больших и маленьких латинских букв.

## Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.

## Пример 1
| Ввод                     | Вывод                      | 
| ------------------------ |:--------------------------:|
| 123                      | 97                         |
| 100003                   |                            |
| a                        |                            |



## Пример 2
| Ввод                     | Вывод                      | 
| ------------------------ |:--------------------------:|
| 123                      | 6080                       |
| 100003                   |                            |
| hash                     |                            |

## Пример 3
| Ввод                     | Вывод                      | 
| ------------------------ |:--------------------------:|
| 123                      | 56156                      |
| 100003                   |                            |
| HaSH                     |                            |

