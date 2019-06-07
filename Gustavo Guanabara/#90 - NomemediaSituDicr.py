aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]} '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'
print('-=' * 30)
for chave, valor in aluno.items():
    print(f' - {chave} é igual a {valor}')