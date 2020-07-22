from chain_of_responsibility.orcamento import Orcamento, Item

from chain_of_responsibility.descontos import Desconto_por_valor, Desconto_por_cinco_itens, Sem_desconto_Fim_Cadeia

class CalculadorDescontos(object):

    def calculaDesconto(self, orcamento):

        desconto = Desconto_por_cinco_itens(Desconto_por_valor(Sem_desconto_Fim_Cadeia())).calcula(orcamento)

        print('Desconto = '+str(desconto))


if __name__ == '__main__':

    orcamentoA = Orcamento()
    orcamentoA.adicionaItem(Item(nome='X', valor=501))
    orcamentoB = Orcamento()
    orcamentoB.adicionaItem(Item(nome='X', valor=400))
    orcamentoC = Orcamento()
    orcamentoC.adicionaItem(Item('Item A', 100.0))
    orcamentoC.adicionaItem(Item('Item B', 50.0))
    orcamentoC.adicionaItem(Item('Item C', 400.0))
    orcamentoC.adicionaItem(Item('Item D', 100.0))
    orcamentoC.adicionaItem(Item('Item E', 100.0))

    CalculadorDescontos().calculaDesconto(orcamentoA)
    CalculadorDescontos().calculaDesconto(orcamentoB)
    CalculadorDescontos().calculaDesconto(orcamentoC)