def coin(notas, total):
    count = [0 for k in range(total+1)]
    count[0] = 1

    for i in range(len(notas)):
        for j in range(notas[i], total + 1):
            count[j] += count[j - notas[i]]
            print (x[i][j])
    return count[total]


notas = [9,2,1]
# tam = len(valor)
total = 10
print(coin(notas, total))
