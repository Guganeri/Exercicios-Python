from random import randint
computador = randint(0,10)
palpite = 1
print('=========== GAME ===========')
numero = int(input('Digite um numero: '))

while numero != computador:
    print('Quase!,tente novamente')
    palpite +=1
    if numero > computador:
        numero = int(input('Tente um palpite menor: '))
    else:
        numero = int(input('Tente um palpite maior: '))


print('Parabéns ! Na {} tentativa? Muito bom !!'.format(palpite))



