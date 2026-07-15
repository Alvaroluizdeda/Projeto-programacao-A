#Classe Desenho, responsável pelo desenho completo, ou seja, sem listas de figuras no main agora.
class Desenho:
    def __init__(self):
        self.figuras = []

    def adicionar(self,figura):
        self.figuras.append(figura)
    
    def desfazer(self):
        if self.figuras:
            self.figuras.pop()

    def limpar(self):
        self.figuras.clear()
