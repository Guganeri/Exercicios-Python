#dados = dict()
dados = {'nome':'pedro', 'idade':25}


#del dados['idade']
print(dados.values()) #O que tem dentro da lista
print(dados.keys())   #O nome da lista literaria
print(dados.items())  #Print de todas as coisas

for k, v in dados.items():
    print(f'O {k} e {v}')

print('-=' *30)
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

for k, v in filme.items():
    print(f'O {k} é {v}')