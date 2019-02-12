MaiorIdade = 0
Homens = 0
MulherMenor = 0
continuar = 'SIM'

while continuar in 'SIM':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    if sexo == 'm':
        Homens += 1
    if idade >= 18:
        MaiorIdade += 1
    if sexo == 'f' and idade < 20:
        MulherMenor += 1
    print('-'*20)
    continuar = str(input('Deseja continua? [S/N]')).upper()
    print('-'*20)

print('__ FIM __')
print(f'Maior idade geral:{MaiorIdade}')
print(f'Quantidade de homens cadastrados:{Homens}')
print(f'Mulhres menores de 20 anos:{MulherMenor}')
