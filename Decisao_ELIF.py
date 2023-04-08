nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()
if idade >= 65:
    print("O paciente " + nome + " possui atendimento priotário!")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente" + nome + " deve ser direcionado à sala reservada.")
else:
    print("O paciente " + nome + " não possui atendimento prioritário e deverá aguardar na sala comum.")