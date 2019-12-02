string = input()
string = string.lower()
new_string = ''
for char in string:
    if char in ('aeiouy'):
        continue
    else:
        new_string += '.' + char
print (new_string)
        
