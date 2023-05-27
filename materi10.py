def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))


def power_recursion(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1/power_recursion(a, -b)
    else:
        return a*power_recursion(a, b-1)


a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

print("="*20)
print("Hasil: ", power_recursion(a, b))


def print_fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        deretan = print_fibo(n - 1)
        angka_setelahnya = deretan[-1] + deretan[-2]
        deretan += [angka_setelahnya]
        return deretan

n = int(input("Masukkan panjang deret Fibonacci: "))
result = print_fibo(n)

print("="*59)
print("Hasil: ",result)