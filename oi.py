nome = input(str("Qual seu nome ?"))
print(f"oi {nome}") 

pergunta_cor = input(str("Me fale uma cor: "))
if pergunta_cor == "vermelho":
    print("Essa é a minha cor preferida")
else:
    print("essa cor é bonita")

pergunta_simp = input(str(f"{nome},voce sabe somar ou subtrair ?"))
if pergunta_simp == "sim":
    pergunta_mat = input(str(f"{nome}, você quer somar ou subtrair?"))
if pergunta_mat == "somar":
    prim_num = int(input(f"{nome}, digite o primeiro numero: "))
    seg_num = int(input(f"{nome}, digite o segundo numero: "))
    resultado = prim_num + seg_num
    print(f"o resultado da sua soma é {resultado}")
elif pergunta_mat == "subtrair":
    prim_num2 = int(input("digite o primeiro numero: "))
    seg_num2 = int(input("digite o segundo numero: "))
    resultado = prim_num2 - seg_num2
    print(f"o resultado da subtração é {resultado}")
elif pergunta_simp == "não":
    print(f"{nome}, que pena, estude mais e depois volte aqui!")
else:
    print(f"{nome} estude mais!")  