alt = float(input('Digite a sua altura'))
peso =float(input('Digite o seu peso'))

imc = peso / (alt*2)

if imc<=18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc<30:
    print('Sobrepeso')
else:
    print('Obesidade morbida')