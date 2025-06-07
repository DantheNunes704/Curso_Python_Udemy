# Exercício: Crie uma matriz que represente um key pad
"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for n in matriz:
    for d in n:
        print(d, end=" ");
    print()
    
print("\n\n", help(matriz));

"""

# Exercício das células:

matriz = [
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

matrizResposta = [];

"""
numRodadas = int(input());


for n in range(5):
    linha = [];
    for d in range(5):
        linha.append(int(input()));
    matriz.append(linha);
"""



vivos = 0;
mortos = 0;
for n in range(5):
    linha = [];
    for d in range(5):
        if n > 0:
            if matriz[n-1][d] == 1:
                vivos += 1;
            else:
                mortos += 1
            
        if d > 0:
            if matriz[n][d-1] == 1:
                vivos += 1;
            else:
                mortos += 1;
                
        if n < 4:
            if matriz[n+1][d] == 1:
                vivos += 1;
            else:
                mortos += 1
            
        if d < 4:
            if matriz[n][d+1] == 1:
                vivos += 1;
            else:
                mortos += 1;
                
        if n > 0 and d > 0:
            if matriz[n-1][d-1] == 1:
                vivos += 1;
            else:
                mortos += 1;
        
        if n > 0 and d < 4:
            if matriz[n-1][d+1] == 1:
                vivos += 1;
            else:
                mortos += 1;
                
                
        if n < 4 and d < 4:
            if matriz[n+1][d+1] == 1:
                vivos += 1;
            else:
                mortos += 1;
                
        if n < 4 and d > 0:
            if matriz[n+1][d-1] == 1:
                vivos += 1;
            else:
                mortos += 1;
                
        if matriz[n][d] == 1 and (vivos < 2 or vivos > 3):
            linha.append(0);
        elif matriz[n][d] == 1 and (vivos == 2 or vivos == 3):
            linha.append(1);
        elif matriz[n][d] == 0 and vivos == 3:
            linha.append(1);
        else:
            linha.append(0);
        vivos = 0;
        mortos = 0;
    matrizResposta.append(linha);
            

                
for linhas in matrizResposta:
    for elemento in linhas:
        print(elemento, end=" ");
    print();
        