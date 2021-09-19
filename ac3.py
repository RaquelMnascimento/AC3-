import abc
from unittest import TestCase, main

class Calculadora (object):

    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass


class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar (self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Divisao(Operacao):
    def executar (self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao):
    def executar (self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado



class Testes(TestCase):

     def test_soma(self):
        calculador = Calculadora()
        result = calculador.calcular(4,4, 'soma')
        self.assertEqual(result, 8)

     def test_subtracao(self):
        calculador2 = Calculadora()
        result2 = calculador2.calcular(4,4, 'subtrair')
        self.assertEqual(result2, 0)

    def test_divisao(self):
        calculador4 = Calculadora()
        result4 = calculador4.calcular(4,4, 'divisao')
        self.assertEqual(result4, 1)

     def test_multiplicacao(self):
        calculador3 = Calculadora()
        result3 = calculador3(4,4, 'multiplicacao'))
        self.assertEqual(result3, 16)


calculador = Calculadora()
x = calculador.calcular(2,3, 'soma')
print(x)

if __name__ == '__main__':

     main()
