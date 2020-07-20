from strategy.impostos import ISS, ICMS


class CalculadorImpostos(object):

    def calculaImposto(self, orcamento, strategy):
        print(strategy.calcular(orcamento))


if __name__ == '__main__':
    
    from strategy.orcamento import Orcamento

    calculador = CalculadorImpostos()
    orcamento = Orcamento(500)
    calculador.calculaImposto(orcamento, ISS())
    calculador.calculaImposto(orcamento, ICMS())
