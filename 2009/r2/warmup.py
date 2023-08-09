def square_digits(n):
    return sum( int(c)**2 for c in str(n) )

attractors = [1, 4, 16, 37, 58, 89, 145, 42, 20]

for n in range(1, 1000):
    m = n
    while m not in attractors:
        m = square_digits(m)

print("Done")