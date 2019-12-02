log_word = input()

i = 0
hello_word = 'hello'

for val in log_word:
    if val == hello_word[i]:
        i += 1
        if(i == 5): break

print('YES' if i == 5 else 'NO')
