class Figura:  # classe pai para ser o molde para as outras subclasses(figuras)
    def __init__(self,values,cor,cor_borda,largura):
        self.cor = cor
        self.cor_borda = cor_borda
        self.largura = largura
        self.values = values

    def atualizar(self, x, y):
        x1,y1,x2,y2 = self.values
        self.values = (x1,y1,x,y)


    def desenhar(self, canvas , preview = False):
        raise NotImplementedError
    

    def incompleta(self,):
        x1,y1,x2,y2 = self.values
        return (x1,y1) == (x2,y2)

    
  
    
##----------Subclasses--------------##

class Linha(Figura): 
    def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        canvas.create_line(*self.values, fill = self.cor, width = self.largura, dash = dash)

class Rabisco(Figura): 
    def atualizar(self,x,y):
        self.values.append((x,y))


    def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        canvas.create_line(*self.values, fill = self.cor, width = self.largura, dash = dash)


    def incompleta(self):
        return len(self.values) <= 1



class Retangulo(Figura):
      def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        canvas.create_rectangle(*self.values, fill = self.cor,outline = self.cor_borda, width = self.largura, dash = dash)

    

class Oval(Figura):
      def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        canvas.create_oval(*self.values, fill = self.cor, outline = self.cor_borda,width = self.largura, dash = dash)

 
class Circulo(Figura):
      def ajustar_circulo(self):  #mesma lógica anterior do círculo
          x1,y1,x2,y2 = self.values
          lado = min(abs(x2-x1), abs(y2-y1))

          if x2 < x1:
              x2 = x1 - lado
          else:
              x2 = x1 + lado
        
          if y2 < y1:
              y2 = y1 - lado
          else:
              y2 = y1 + lado
          
          return(x1,y1,x2,y2)

      def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        values = self.ajustar_circulo()
        canvas.create_oval(*values,fill = self.cor,outline = self.cor_borda, width = self.largura, dash = dash)


class Poligono(Figura):
    def desenhar(self, canvas, preview = False):
        dash = (4,2) if preview else None

        canvas.create_polygon(*self.values, fill = self.cor, outline = self.cor_borda,width = self.largura, dash = dash)


   