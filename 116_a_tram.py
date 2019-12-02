num_of_stops = int(input())

current_val = min_capacity = 0

for i in range(num_of_stops):
    travelers = list(map(int, input().split()))
    current_val = current_val - travelers[0] + travelers[1]
    if current_val > min_capacity:
        min_capacity = current_val

print(min_capacity)
