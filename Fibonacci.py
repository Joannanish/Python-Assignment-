n = int(input("Enter the number of terms: "))
a, b = 0, 1
sequence = []

for _ in range(n):
    sequence.append(str(a))
    a, b = b, a + b

print(", ".join(sequence))
