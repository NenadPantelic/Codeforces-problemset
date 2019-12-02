matrix = []
target_row = target_col = None
for i in range(5):
    entry =list(map(int, input().split()))
    if 1 in entry:
        target_row = i
        target_col = entry.index(1)
        print(abs(target_row - 2) + abs(target_col - 2))
        break


