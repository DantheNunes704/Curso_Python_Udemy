"""
    O python é uma linguagem com tipagem dinâmica e forte
    tipagem dinâmica: não é necessário informar o tipo da variável
"""

# String -> Um texto, uma cadeia (array) de caracteres
# Podemos usar Strings com aspas duplas ou simples

print("\nIsso é uma String")


# Caractere de escape (barra invertida \) Faz com que o interpretador ignore o próximo caractere, ou seja
# ele não interpreta o próximo caractere de forma literal
# exe:


print("\nOi, meu nome é: \"Danthe\"")

"""
    Ainda há a possibilidade de colocar o caractere (r) antes de uma string. Isso faz com que
    ela seja lida como uma "raw string" — ou seja, todos os caracteres de escape presentes
    na string serão interpretados literalmente, sem efeito especial.
    Exemplo:
"""

print("\n", r"C:\novo\feio")

"""
    Caso não houvesse esse caractere antes da string, o interpretador entenderia o "\n"
    como uma quebra de linha, imprimindo o restante na linha seguinte. Isso não seria ideal
    em situações como quando queremos representar caminhos de arquivos no Windows, por exemplo.
"""

"""
    Uma String também pode ser interpretada dentro de aspas simples. Nesse caso, não há com que se 
    preocupar se seu objetivo é escrever algo dentro de uma String com aspas duplas, pois 
    elas não são reconhecidas como o fim da String: 
"""

print('\nMeu nome é: "Rodrigo"')
