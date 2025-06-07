listaAux = input().split(" ");
album = int(listaAux[0]);
carimbadas = int(listaAux[1]);
compradas = int(listaAux[2]);

mostraCarimbadas = [];
jaCompradas = [];

listaAux = input().split(" ");

for n in range(carimbadas):
    mostraCarimbadas.append(int(listaAux[n]));
listaAux = input().split(" ");
for n in range(compradas):
    jaCompradas.append(int(listaAux[n]));

repetidas = []
resposta = carimbadas;



for m in range(len(jaCompradas)):
    if jaCompradas[m] in mostraCarimbadas and repetidas.count(jaCompradas[m]) == 0 :
        resposta -= 1;
        repetidas.append(jaCompradas[m])
    
print(resposta);