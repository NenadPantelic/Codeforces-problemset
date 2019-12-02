num = int(input())

x_vect = y_vect = z_vect = 0

for i in range(num):
    vectors = list(map(int, input().split()))
    x_vect += vectors[0]
    y_vect += vectors[1]
    z_vect += vectors[2]

if x_vect == y_vect == z_vect == 0:
    print ('YES')
else:
    print ('NO')
