w, d, n = list(map(int, input().split()))

total = (w + n * w) / 2 * n
to_borrow = int(total) - d

print(to_borrow if to_borrow > 0 else 0)
