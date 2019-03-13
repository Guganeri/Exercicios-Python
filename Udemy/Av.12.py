def palindromo(s):
    s = s.replace(' ','')
    return s == s[::-1]

print(palindromo(' helleh'))