name = input()
unique_chars = set(name)
print('CHAT WITH HER!' if len(unique_chars) % 2 == 0  else 'IGNORE HIM!')
