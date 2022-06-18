class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá\n{id(self)}'


if __name__ == '__main__':
    john = Pessoa(nome='john')
    paulo = Pessoa(john, nome='Paulo')
    print(Pessoa.cumprimentar(paulo))
    print(id(paulo))
    print(paulo.cumprimentar())
    print(paulo.nome)
    print(paulo.idade)
    for filho in paulo.filhos:
        print(filho.nome)
    #print(paulo.filhos)
