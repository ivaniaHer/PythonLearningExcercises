class Aritmetica:

    # No es posible tener dos métodos __init__ en la misma clase, pythgon solo reconoce el último definido.
    # def __init__(self, operando1):
    #     self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        print(f'{self.operando1} + {self.operando2} = {self.operando1 + self.operando2}')

    def multiplicar(self):
        print(f'{self.operando1} * {self.operando2} = {self.operando1 * self.operando2}')

aritmetica1 = Aritmetica(5,7)
aritmetica1.sumar()
aritmetica1.multiplicar()

aritmetica2 = Aritmetica(3)
aritmetica2.operando2 = 4
aritmetica2.sumar()
