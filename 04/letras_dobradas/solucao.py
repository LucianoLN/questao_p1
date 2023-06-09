n = int(input())
com = 0
p_repete = []
p_naorepete = []

for a in range(n):
    palavra = input()
    p_naorepete.append(palavra)

    
    for i in range(len(palavra) - 1):
        if palavra[i] == palavra[i + 1]:
            p_repete.append(palavra)
            p_naorepete.remove(palavra)
            com += 1
            break

sem = n - com

print(f'{com} palavra(s) com letras dobradas:')
if len(p_repete) > 0:
    for p in p_repete:
        print(p)

print('---')


print(f'{sem} palavra(s) sem letras dobradas:')
if len(p_naorepete) > 0:
    for p in p_naorepete:
        print(p)

