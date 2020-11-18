# -*- coding: UTF-8 -*-
# nota_fiscal.py
from datetime import date

class ItemNota(object):

    def __init__(self, valor, descricao):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    def valor(self):
        return self.__valor


class Nota_fiscal(object):

    # os parâmetros opcionais devem ser os últimos
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='TESTE'):

        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao

        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')

        self.__detalhes = detalhes

        @property
        def razao_social(self):
            return self.__razao_social

        @property
        def cnpj(self):
            return self.__cnpj

        @property
        def data_de_emissao(self):
            return self.__data_de_emissao

        @property
        def detalhes(self):
            return self.__detalhes



# nota_fiscal.py
# código das classes omitidos

if __name__ == '__main__':

    itens=[
        ItemNota(
            descricao='ITEM A',
            valor=100
        ),
        ItemNota(
            descricao='ITEM B',
            valor=200
        )
    ]

    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens,
        #detalhes='Referente à ...',
        #data_de_emissao=date.today()
    )




