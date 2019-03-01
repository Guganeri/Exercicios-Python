#Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!"

st = 'Print every word in this sentence that has an even number of letters'
split_st = st.split()
for x in split_st:
    size = len(x)
    if size % 2 == 0:
        print(x,': É Par !!!')