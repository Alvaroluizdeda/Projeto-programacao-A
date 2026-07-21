from abc import ABC
from modelo.figuras import (Linha,Rabisco,Retangulo,Oval,Circulo,Poligono)

#Classe pai abstrata "Ferramente" para ser o molde para as subclasse de cada ferramenta
class Ferramenta(ABC):
    def __init__(self,controlador):
        self.controlador = controlador
    
    tipo = None

    def iniciar(self,event):
        cor = self.controlador.visao.cores_preenchimento[self.controlador.visao.cor_var.get()]
        cor_borda = self.controlador.visao.cores_bordas[self.controlador.visao.cor_borda_var.get()]
        largura = self.controlador.visao.larguras_borda[self.controlador.visao.largura_borda_var.get()]   
        values = (event.x,event.y,event.x,event.y)
        self.controlador.figura_nova = self.tipo(values,cor,cor_borda,largura)

    def atualizar(self,event):
        if self.controlador.figura_nova is None:
            return
 
        self.controlador.figura_nova.atualizar(event.x,event.y)


        self.controlador.desenhar_figuras()

    def finalizar(self,event):
        if self.controlador.figura_nova is None:
            return
    
        if event.num != 1:
            return
        
        if not self.controlador.figura_nova.incompleta():
            self.controlador.desenho.adicionar(self.controlador.figura_nova)

        self.controlador.figura_nova = None
        self.controlador.desenhar_figuras()


#------------------------Subclasses----------------------------#

class FerramentaLinha(Ferramenta):
    tipo = Linha
    

class FerramentaRabisco(Ferramenta):
    def iniciar(self,event):
        cor = self.controlador.visao.cores_preenchimento[self.controlador.visao.cor_var.get()]
        cor_borda = self.controlador.visao.cores_bordas[self.controlador.visao.cor_borda_var.get()]
        largura = self.controlador.visao.larguras_borda[self.controlador.visao.largura_borda_var.get()]   
        values = [(event.x,event.y)]
        self.controlador.figura_nova = Rabisco(values,cor,cor_borda,largura)

    
class FerramentaRetangulo(Ferramenta):
    tipo = Retangulo


class FerramentaOval(Ferramenta):
    tipo = Oval

class FerramentaCirculo(Ferramenta):
    tipo = Circulo

class FerramentaPoligono(Ferramenta):
    def iniciar(self,event):
        cor = self.controlador.visao.cores_preenchimento[self.controlador.visao.cor_var.get()]
        cor_borda = self.controlador.visao.cores_bordas[self.controlador.visao.cor_borda_var.get()]
        largura = self.controlador.visao.larguras_borda[self.controlador.visao.largura_borda_var.get()]   
        
        if self.controlador.figura_nova is None:
            self.controlador.figura_nova = Poligono([(event.x,event.y),(event.x,event.y)],cor,cor_borda,largura)
        else:
            self.controlador.figura_nova.adicionar_ponto(event.x,event.y)
            
        self.controlador.desenhar_figuras()

    def atualizar(self,event):
        if self.controlador.figura_nova is None:
           return 
        
        self.controlador.figura_nova.atualizar_preview(event.x,event.y)

        self.controlador.desenhar_figuras()

    def finalizar(self,event):
        if self.controlador.figura_nova is None:
            return
     

        if event.num != 3:
            return

        self.controlador.figura_nova.finalizar()
        

        if not self.controlador.figura_nova.incompleta():
            self.controlador.desenho.adicionar(self.controlador.figura_nova)

        self.controlador.figura_nova = None
        self.controlador.desenhar_figuras()





