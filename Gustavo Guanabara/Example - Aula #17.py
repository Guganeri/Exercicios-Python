galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #exemplo de transferir uma copia de lista para outra lista, os dados são copiados e podem ser
    dado.clear()           #apagados da primeira lista "dado" pois após o append em galera as listas param de ter vinculo

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade')
