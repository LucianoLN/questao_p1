mando = input()
ingresso = input().split()

count = 0
while count < len(ingresso) - 1:
    if ingresso[count][0] == mando:
        valor = 'ok'
        count += 1

    elif ingresso[count][0] != mando:
        if ingresso[count + 1][0] == mando:
            valor = 'erro'
            count += 1
            break

        elif ingresso[count + 1][0] != mando:
            valor = 'ok'
            count += 1

print(valor)

        

        
