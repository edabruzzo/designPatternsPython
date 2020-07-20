
class Orcamento(object):
    def __init__(self):
        self.__itens = []

    @property
    def valor(self):

        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total


    def obter_itens(self):
        return tuple(self.__itens)

    def quantidade_itens(self):
        return len(self.__itens)

    def adicionaItem(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor


    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome