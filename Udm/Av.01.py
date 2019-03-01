#Use for, split() e if para criar uma declaração que imprima as palavras que
# iniciam com 'S'
st = 'Print Only The Words That Start With S In This Sentence'.upper()
split_string = st.split()

for word in split_string:
    if word[0] == 'S':
        print(word)