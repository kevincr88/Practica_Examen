# --------------------------------------------------
# Creates main class
# --------------------------------------------------
class Geometria:
    def __init__(self, valores):
        self.valores = valores

    def area(self):
        pass

    def formula(self):
        pass

    def datos(self):
        pass


# --------------------------------------------------
# Creates derived classes with abstract methods
# --------------------------------------------------
class cuadrado(Geometria):
    def area(self):
        return self.valores[0] ** 2

    def formula(self):
        return 'Base * Base'

    def datos(self):
        return self.valores[0]


class rectangulo(Geometria):
    def area(self):
        return self.valores[0] * self.valores[1]

    def formula(self):
        return 'Base * Altura'

    def datos(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1])

class triangulo(Geometria):
    def area(self):
        return self.valores[0] * self.valores[1] / 2
    def formula(self):
        return '(Base * Altura)/2'
    def datos(self):
        return str(self.valores[0]) + ',' + str(self.valores[1]) + ',' + str(self.valores[2])
    def identificador(self):
        if (self.valores[0] == self.valores[1] and self.valores[2]==self.valores[1]):
            return print ('Es un tringulo equilatero')
        elif (self.valores[0]!= self.valores[1] and self.valores[1]!=self.valores[2]):
            return print ('Es un tringulo escaleno')
        else:
            print('Es un tringulo isoceles')



# --------------------------------------------------
# Using classes
# --------------------------------------------------
fig1 = cuadrado([3])
print('La formula del cuadrado es {0}.'.format(fig1.formula()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig1.datos(), fig1.area()))

print()

fig2 = rectangulo([3, 5])
print('La formula del rectángulo es {0}.'.format(fig2.formula()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig2.datos(), fig2.area()))

fig3 = triangulo([3,3,3])
print('La formula del tringulo es {0}.'.format(fig3.formula()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig3.datos(), fig2p.area()))
print(fig3.identificador())


