opção = ""
nomes = []
quantidades = []
preços = []
total = []
i = 0
while opção != "sim":
    nome = input("diga o nome do produto ")
    nomes.append(nome)
    quantidade = int(input("diga quanto deste produto você leva "))
    while quantidade < 1:
        quantidade = int(input("quantidade invalida diga de novo "))

    quantidades.append(quantidade)
    preço = float(input("qual o preço por unidade do seu produto "))
    while preço < 0:
        preço = float(input("preço invalido diga novamente "))

    preços.append(preço)

    opção = input("deseja terminar a lista de conpras? ")

for i in range(len(nomes)):
    print("você comprou",quantidades[i], nomes[i])
    total.append(quantidades[i] * preços[i])

print("o valor total da compra é:",sum(total))