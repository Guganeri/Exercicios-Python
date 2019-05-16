gerallist = list()
alunolist = list()
while True:

    nome = str(input('Digite o nome'))
    alunolist.append(nome)

    nota = list(input('Digite a primeira nota: '))
    alunolist.append(nota[0])
    nota = list(input('Digite a segunda nota: '))
    alunolist.append(nota[1])
    gerallist.append(alunolist)
    break
