print ('\n')
print ('************** Minha casa minha divida, Programa bancario 2.0 ************************')
casa = float(input('\nDigite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos deseja dividir: '))


emMeses = anos*12
prestacao = casa/emMeses
print('Os valores mensais serão de {}reais'.format(prestacao))

minimo = salario*30 /100

print('Pra pagar uma casa de {} em {}anos a prestação será de R${}'.format(casa,anos,prestacao))
if prestacao <= minimo:
    print('Emprestimo concedido !')
else:
    print("Emprestimo negado !")