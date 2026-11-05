class Criterio:
    def __init__(self,Textopregunta,fil,col,val = None):
        self.pregunta = Textopregunta
        self.valoracion = 0
        self.fila = fil
        self.columna = col
        if val != None:
            if val > 0:
                self.valoracion = val - 1
            else:
                self.valoracion = val + 1

    def valorar(self,valor):
        if valor >= -8 and valor <= 8:
            self.valoracion = valor

    def media(self):
        return self.valoracion