import json

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    print(dicionario)
    #for chave, dados in dic.items():
        #print(chave + " " + str(dados))