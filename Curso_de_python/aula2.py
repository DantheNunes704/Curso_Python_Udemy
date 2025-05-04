# A função "print" é usada para exibir algo na tela. Para isso, basta passar uma valor dentro dos parêntesis
# dessa função (O que é passado dentro dos parêntesis chamam-se "argumentos")

print("Isso é um argumento")

def explicaSep():
    """
        A função print separa cada item concatenado dentro dela acrescentado um espaço para cara item, 
        dessa maneira:
    """

    print(12, 34)

    """
        Porém, podemos mudar isso definindo no final da função print um separador que gostariamos de usar:
    """

    print(12, 34, 56, sep="-")
    print(12, 34, 56, sep="=")
    print(12, 34, 56, sep="")

    """
        Nesse contexto, o "sep" seria um Keyword Argument, parâmetro nomeado. Ainda há outro
        argumento nomeado, o "end", que define os caracteres que termina o que o print exibe
        default: end="\n"
    """

    print(12, 34, sep=" ", end=" oi\n")

print(explicaSep())