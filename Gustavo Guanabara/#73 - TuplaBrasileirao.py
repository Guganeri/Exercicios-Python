campeonato = ('Palmeiras','Flamengo','Athletico-PR',
              'Atlético-MG', 'Avaí', 'Bahia', 'Botafogo', 'CSA', 'Ceará',
              'Chapecoense', 'Corinthians','São Paulo', 'Chapecoense', 'Fluminense', 'Santos', 'Internacional')

print('='*15,'Os 5 primeiros colocados são:','='*15)
print(campeonato[0:5])
print('='*15,'Os 4 últimos colocados são:','='*15)
print(campeonato[-4:])
print('='*50)
print('Times em ordem alfabetica:')
print(sorted(campeonato))
print('='*50)
print ('Colocação da chape')
print(f'O chapeconse esta na {campeonato.index("Chapecoense")+1}º posição')


