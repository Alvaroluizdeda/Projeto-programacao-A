from tkinter import Tk, Canvas
from figuras import Linha,Rabisco, Retangulo, Oval, Circulo, Poligono

root = Tk()

canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()

linha = Linha(
    (20, 20, 20, 20),
    "red",
    "black",
    4
)

rabisco = Rabisco(
    [(20, 20), (60, 40), (100,30), (150, 80), (200,100)],
    "blue",
    "black",
    4
)

retangulo = Retangulo(
    (250, 30, 450, 150),
    "yellow",
    "blue",
    5
)

oval = Oval(
    (50, 180, 220, 320),
    "green",
    "black",
    3
)

circulo = Circulo(
    (280, 180, 480, 300),
    "orange",
    "purple",
    4
)

poligono = Poligono((300,200,380,400,480,250),
                    "white",
                    "blue",
                    4
                                 
)

linha.desenhar(canvas)
rabisco.desenhar(canvas)
retangulo.desenhar(canvas)
oval.desenhar(canvas)
circulo.desenhar(canvas)
poligono.desenhar(canvas)

print(linha.values)

#linha.atualizar(250,150)
#linha.desenhar(canvas)

#print(linha.values)

print(linha.incompleta())

root.mainloop()