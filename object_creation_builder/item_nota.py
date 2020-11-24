# -*- coding: UTF-8 -*-
# nota_fiscal.py
from datetime import date
from observer.observadores import *

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
    def __init__(self,
                 razao_social,
                 cnpj, itens,
                 data_de_emissao=date.today(),
                 detalhes='TESTE',
                 observadores = [] ):

        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao

        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')

        self.__detalhes = detalhes

        for observador in observadores:
            observador(self)


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

#dependência circular
#from object_creation_builder.criador_nota_fiscal import Criador_de_nota_fiscal

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
        observadores=[envia_por_email, salva_no_banco, imprime]
        #detalhes='Referente à ...',
        #data_de_emissao=date.today()
    )