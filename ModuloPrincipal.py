from Capitulo3_Funcoes.IdentificaçãoDeFuncoes import *

minhaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")

print("Pesquisando")
localizaPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista)

print("Excluindo")
excluiPorSerial(minhaLista)
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)