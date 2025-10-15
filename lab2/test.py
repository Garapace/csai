import pytest
from lib import *  # Импортируем функцию fibonacci (замените путь, если функция в другом файле)

def test_fibonacci_correct():
    # Проверяем корректный результат для первых 7 чисел Фибоначчи
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_incorrect_input():
    # Проверяем, что функция возвращает пустой список для отрицательного n
    assert fibonacci(-5) == []

def test_bubble_sort_correct():
    # Проверяем, что список сортируется по возрастанию
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_empty_list():
    # Проверяем, что пустой список возвращается как есть
    assert bubble_sort([]) == []

def test_calculator_correct_addition():
    # Проверяем корректный результат для сложения
    assert calculator(10, 5, '+') == 15

def test_calculator_division_by_zero():
    # Проверяем, что деление на ноль возвращает корректное сообщение об ошибке
    assert calculator(10, 0, '/') == "Ошибка: деление на ноль"
