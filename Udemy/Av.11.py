def multiply(numeros):
    tot = 1
    for n in numeros:
        tot *= n
    return tot


print(multiply([1, 2, 3]))