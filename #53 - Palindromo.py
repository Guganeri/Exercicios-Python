frase = str(input("Digite uma frase qualquer: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(junto,inverso)
if junto == inverso:
    print("É palíndromo")
else:
    print("Não é palindromo")
