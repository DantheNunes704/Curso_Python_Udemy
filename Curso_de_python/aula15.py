# A função input() serve para capturar a entrada do usuário
# Ela sempre retornará uma string. Podemos escrever algo que será mostrado para o usuário
nome = input("Qual o seu nome? ");
print(f'Seu nome é {nome}.');

# Antenção!!! Por conta da função input sempre retornar uma tring, não se pode somar diretamente. É necessária fazer a coersão para inteiro:
numero = int(input());
# Porém, fazer a coersão diretamente da função print pode causar problemas se o usuário digitar algum caractere como a letra "A"
# O correto seria fazer uma verificação se a variável pode ser um inteiro ou não