#PROCURANDO UMA STRING DENTRO DE OUTRA STRING.
nome = str(input("Qual o seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))
