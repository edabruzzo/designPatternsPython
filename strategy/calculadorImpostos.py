from strategy.impostos import ISS, ICMS, IKCV, ICPP


class CalculadorImpostos(object):

    def calculaImposto(self, orcamento, strategy):
        print(strategy.calcular(orcamento))


if __name__ == '__main__':
    
    from strategy.orcamento import Orcamento
    from chain_of_responsibility.orcamentoChain import OrcamentoChain, Item

    calculador = CalculadorImpostos()
    orcamento = Orcamento(500)

    #calculador.calculaImposto(orcamento, ISS())
    #calculador.calculaImposto(orcamento, ICMS())

    orcamentoC = OrcamentoChain()
    orcamentoC.adicionaItem(Item('Item A', 100.0))
    orcamentoC.adicionaItem(Item('Item B', 50.0))
    orcamentoC.adicionaItem(Item('Item C', 400.0))
    orcamentoC.adicionaItem(Item('Item D', 100.0))
    orcamentoC.adicionaItem(Item('Item E', 100.0))

    #calculador.calculaImposto(orcamento, ICPP())
    #calculador.calculaImposto(orcamento, IKCV())


    #Comportamento composto
    calculador.calculaImposto(orcamento, ISS(ICMS()))
    calculador.calculaImposto(orcamentoC, ICMS(IKCV()))
