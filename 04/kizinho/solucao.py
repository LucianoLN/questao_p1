num = input().split()
k = int(input())

seq = [int(n) for n in num]

cont = 0

for i in range(len(seq) - k):
    if seq[i] == seq[i + k] * 3 or seq[i] * 3 == seq[i + k]:
        cont += 1

print(cont)
