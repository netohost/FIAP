#Inventario

inventario = [] #Ao abrir a [] você está criando uam lista.
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()  #O \S\ é usado pra que o código não interrompa as strings.

for elemento in inventario:
    print(elemento)
