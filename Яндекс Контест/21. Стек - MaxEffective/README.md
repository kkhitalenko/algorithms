Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке. Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop() также должны выполняться за константное время.

## Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

## Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».

## Пример 1
| Ввод                           | Вывод              | 
| -------------------------------|:------------------:|
| 10                             | error              | 
| pop                            | error              | 
| pop                            | 4                  |
| push 4                         | None               |
| push -5                        |                    |
| push 7                         |                    | 
| pop                            |                    |
| pop                            |                    |
| get_max                        |                    | 
| pop                            |                    |
| get_max                        |                    |


## Пример 2
| Ввод                           | Вывод                  | 
| -------------------------------|:----------------------:|
| 10                             | None                   | 
| get_max                        | error                  | 
| push - 6                       | None                   |
| pop                            | 2                      |
| pop                            |                        |
| get_max                        |                        | 
| push 2                         |                        | 
| get_max                        |                        |
| pop                            |                        | 
| push - 2                       |                        | 
| push - 6                       |                        |

