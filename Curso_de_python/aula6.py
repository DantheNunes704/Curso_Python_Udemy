# conversão de tipos, coersão
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float e bool
# Há formas de converter tipos de dados em 
# outros:
print(type(int('1')))

# Não há como concatenar dois diferentes tipos
# de variáveis em python, sendo necessária 
# fazer a conversão para tal:

# print('1' + 1) -> Dá um erro

print('1' + str(1))

# no caso do valor int e float sendo concatenados
# não seria preciso converter o tipo, pois o pyhon 
# já faz isso automaticamente, convertendo o menor
# para o maior tipo

print(type(1.1 + 1))

# Também há como converter uma outra variável 
# em boolean

print(bool(1.1))

# A coerão pode ocorrer de maneira implícita ou explícita
# Tipos de type casting:

estudante = True;
nome = "nicolas"
idade = 13;
altura = 1.60;

print(int(altura)) # -> A altura, que antes era float, perde sua parte decimal e vira um integer.
print(float(idade)) # -> idade, que antes era um integer, ganha uma parte decimal e vira float
print(bool(nome)) # -> Se quisermos converter uma string em um valor boolean, sempre que a string não for nula, o valor será True. Caso contrário será false

resposta = bool(input("Digite alguma coisa "));
if resposta:
    print("Você digitou algo");
elif not resposta:
    print("Você não digitou nada");
    
verdadeiro = bool(1) # -> sempre que o valor de uma variável fo não 0, essa variável será considerada como True, se for 0 será false
    
# Esse tipo de type casting é (explícito)
    


 

