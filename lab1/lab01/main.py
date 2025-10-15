""" Лаба 1. Git, Python. Реализовать алгоритм Евклида. 
Алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел """

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Введите число №1\n"))
    num2 = int(input("Введите число №2\n"))
    print(f'НОД({num1};{num2}) = {gcd(num1, num2)}')


if __name__ == "__main__":
    main()
