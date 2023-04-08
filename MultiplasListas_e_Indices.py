#Criando as listas

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":              #Enquanto a resposta for "S" você continuará adicionando itens às listas.
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range (0, len(equipamentos)):   #para cada índice dentro do número de letras do equipamento
    print("\nEquipamento....: ", (indice+1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serial.........: ", seriais[indice])
    print("Departamento...: ", departamentos[indice])

    #print
    #Equipamento....: 2
    #Nome...........: Eq2
    #Valor..........: 2.5
    #Serial.........: 10213
    #Departamento...: T.i

