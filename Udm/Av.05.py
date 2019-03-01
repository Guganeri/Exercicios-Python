# Escreva um programa que imprima os números inteiros de 1 a 100
# Para multiplos de três imprima = Fizz ao inves do número
# Para os multiplos de cinco imprima = Buzz
# Para os que são multiplos de três e cinco imprima = FizzBuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)