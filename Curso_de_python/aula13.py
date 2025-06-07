# formatação de Strings
# f-string, ou "formatted string literal" (literal de string formatada)

'''
    f-string é uma forma de formatar strings em Python, introduzida no Python 3.6.
    Ela permite inserir variáveis e expressões diretamente dentro da string, usando chaves {}.
    Para utilizá-la, basta colocar a letra f antes das aspas da string.
    Exemplo: nome = "Ana"; print(f"Olá, {nome}!") -> saída: Olá, Ana.
    É mais legível e eficiente do que concatenação ou o método format().
'''

nome = "Bruno";
idade = 9;

print(f"{nome} tem {idade:.2f} anos");
