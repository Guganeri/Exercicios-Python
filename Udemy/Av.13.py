import string

def ispangram(str, alphabet = string.ascii_lowercase):
    num = len(alphabet)
    count = 0

    for i in alphabet:
        if i in str:
            count +=1

    return count == num

print(ispangram('the quick brown fox jumps over the lazy dog'))