# Comentários em python: Quando o interpretador do python identifica esse símbolo "#" automaticamente
# a linha após o símbolo é ignorada

print(123) # A função "print" serve para exibir algo na tela

"""
    As DocStrings são três aspas abrindo e fechando um bloco de DocString. Isso é usado para "comentar" mais 
    de uma linha em python. Tecnicamente, não é considerado um comentário, pois diferentemente
    deles, pode ser acessada e exibida na tela estando dentro de uma função.
"""

def exibeDoc(a , b):
    """
        Exibe na tela a soma de dois números inteiros
    """
    return a+b

print(exibeDoc(1, 2))
print(exibeDoc.__doc__)