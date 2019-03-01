def primo(num):
    """
    Método para checar se é primo
    """
    for n in range(2,num):
        if num % n == 0:
            print('Não é um numero primo !')
            break
        else:
            print('Primo')
primo(2)