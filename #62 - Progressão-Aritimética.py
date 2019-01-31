print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('{} ->'.format(termo),end='')
        termo += razao
        contador += 1
    print('PAUSA')
    print('Digite [0] se desejar sair')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print("FIM")
