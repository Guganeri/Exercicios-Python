sexo = str(input('Digite seu sexo. (M) ou (F)')).strip().upper()[0]
while sexo not in 'FM':
    print('Incorreto ! Digite uma opção valida')
    sexo = str(input('Digite seu sexo. (M) ou (F)')).strip().upper()[0]

if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'

print('Registrado:{}'.format(sexo))




