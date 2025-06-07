# if -> Lê um valor booleano a a partir de uma expressão e executa ou não o código que está dentro de seu escopo
# elif -> Depende o if para ser escrito, significa "se não, se"
# else -> Sempre o último bloco. Não se pode ter um "else" sem um "if"
resposta = input("O que você quer fazer? ")
if resposta == "entrar":
    print("Você entrou");
elif resposta == "sair":
    print("Você saiu");
else:
    print("Você não dogotou nada");
# pass -> Serve apenas para que o código do bloco atual seja ignorado e não executado