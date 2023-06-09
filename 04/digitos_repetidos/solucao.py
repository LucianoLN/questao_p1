n = int(input())

contador = 0

com = 0

for x in range(n):
    senha = input()
    
    for i in range(len(senha) - 1):
        if senha[i] == senha[i + 1]:
            com += 1
            break
        
    contador += 1

sem = n - com

print(f'com: {com}')
print(f'sem: {sem}')
