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


 

