# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'salve_class.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Joao', 33)
p2 = Pessoa('Janaina', 29)
p3 = Pessoa('Renan', 30)
dados = [vars(p1), vars(p2), p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        print('Fazendo o dump')
        json.dump(dados, arquivo, ensure_ascii=False, indent=2) #Dump é a forma de voce enviar os dados para o arquivo json


if __name__ == '__main__':
    print('Ele é o MAIN')
    fazer_dump()