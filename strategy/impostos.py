
class ISS(object):

    #https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
    def calcular(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):

    #https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
    def calcular(self, orcamento):
        return orcamento.valor * 0.06
