num = int(input())
stones = input()

counter = 0
for i in range(num - 1):
    if stones[i] == stones[i+1]:
        counter += 1
print(counter)
