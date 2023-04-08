def preencherInventario(lista):
    resp="S"
    while resp == "S":
        equipamento = [(input("Equipamento: ")),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome..........: ", elemento[0])
        print("Valor..........: ", elemento[1])
        print("Serial..........: ", elemento[2])
        print("Departamento..........: ", elemento[3])

def localizaPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial..: ", elemento[2])

def depreciarPorNome(lista):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == lista [0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * 0.9
            print("Novo valor: ", elemento[1])

def excluiPorSerial(lista):
    serial = int(input("\nDigite o serial do equipamento à ser excluído: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
            print("O Equipamento foi removido com sucesso.")

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

