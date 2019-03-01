# Use a compreensão em listas para criar uma lista das primeiras letras de cada string abaixo

st = 'Create  lista of the first letters of every word in this string'
st_split = st.split()

print([letter[0] for letter in st_split])

for i in st_split:
    print(i[0],end=' ')