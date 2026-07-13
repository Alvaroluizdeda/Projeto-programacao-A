from tkinter import *
from tkinter import ttk
from figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
   
    global figura_nova      
           
 
    tipo = tipo_figura_var.get()
    cor = cores[cor_var.get()]
    cor_borda = cores[cor_borda_var.get()]
    largura = espessuras[largura_borda_var.get()]    
    
    if tipo == "Polígono":

        if figura_nova is None:
            figura_nova = Poligono(
    [(event.x,event.y), (event.x,event.y)],
    cor,
    cor_borda,
    largura
)

        else:
            figura_nova.adicionar_ponto(event.x,event.y)


        desenhar_figuras()
        return
    
    
    tipos = {                  #generaliza os tipos que possuem a mesma lógica
        "Linha": Linha,    
        "Retângulo": Retangulo,
        "Oval": Oval,
        "Círculo": Circulo,
        "Polígono": Poligono
    }      




    if tipo == "Rabisco":
        values = [(event.x,event.y)]
        figura_nova = Rabisco(values,cor,cor_borda,largura)

    else:
        values = (event.x,event.y,event.x,event.y)
        classe_figura = tipos[tipo]

        figura_nova = classe_figura(values,cor,cor_borda,largura)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova is None:
        return


    if isinstance(figura_nova, Poligono):
        figura_nova.atualizar_preview(event.x,event.y)

    else:
        figura_nova.atualizar(event.x,event.y)


    desenhar_figuras()

# Quando mouse é solto
def incluir_figura_nova(event): 
    global figura_nova

    if figura_nova is None:
        return
    if isinstance(figura_nova, Poligono):

        if event.num != 3:
            return

        figura_nova.finalizar()
    else:

        if event.num != 1:
            return
    if not figura_nova.incompleta():
        figuras.append(figura_nova)

    figura_nova = None
    desenhar_figuras()

def desenhar_figuras(): 
  canvas.delete("all")

  for figura in figuras:
      figura.desenhar(canvas)

  if figura_nova is not None:
      figura_nova.desenhar(canvas, preview = True)

            
def desfazer():   # remove a última figura adicionada na lista figuras
    if figuras:
        figuras.pop() 
        desenhar_figuras()



#/*/*/*/*/*/*/ MAIN /*/*/*/*/*/*/

figuras = []       # Todas as figuras desenhadas

figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

#dicionarios de cores para os option menus
cores = {
    "Sem preenchimento": None,
    "Preto": "black",
    "Vermelho": "red",
    "Azul": "blue",
    "Verde": "green",
    "Amarelo": "yellow",
    "Laranja": "orange",
    "Roxo": "purple"
}


espessuras = {
    "Sem borda": None,
    "1": 1,
    "2": 2,
    "3": 3,
    "5": 5,
    "8": 8
}



# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 15, 'pady': 5} 


frame2 = ttk.Frame(frame)#criei outro frame pra separar os textos do canvas, mas não é necessário, só pra organização visual mesmo.
frame2.grid(column=0, row=0, sticky = EW)

#um botão para desfazer a última figura desenhada, que chama a função desfazer quando clica
label_desfazer = ttk.Label(frame2, text = "Botão de desfazer:")
label_desfazer.grid(column = 5,row = 0, sticky = W, **paddings)

botao_desfazer = ttk.Button(frame2, text="Desfazer",command=desfazer)
botao_desfazer.grid(column=5, row=1, sticky=W, **paddings)

#option menu & Label das espessuras e das cores das espessuras
cor_borda_var = StringVar(root)
cor_borda_var.set("Preto")

largura_borda_var = StringVar(root)
largura_borda_var.set("Sem borda")


#cor da borda
label_cor_borda = ttk.Label(frame2, text="Cor da borda:")
label_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

option_menu_cor_borda = ttk.OptionMenu( frame2,cor_borda_var, cor_borda_var.get(), *cores.keys())
option_menu_cor_borda.grid(column=2, row=1, sticky=W, **paddings)


#grossura da borda
label_largura_borda = ttk.Label(frame2, text="Grossura da borda:")
label_largura_borda.grid(column=3, row=0, sticky=W, **paddings)

option_menu_largura = ttk.OptionMenu(frame2,largura_borda_var, largura_borda_var.get(),*espessuras.keys())
option_menu_largura.grid(column=3, row=1, sticky=W, **paddings)


# option menu & Label das cores
cor_var = StringVar(root)
cor_var.set("Sem preenchimento")

label_cor = ttk.Label(frame2, text = "Cor de preenchimento:")
label_cor.grid(column = 1, row=0)

option_menu_cor = ttk.OptionMenu( frame2,cor_var, cor_var.get(), *cores.keys())
option_menu_cor.grid(column=1, row=1)



# option menu  & Label das figuras
tipo_figura_var = StringVar(root)
tipo_figura_var.set("Linha") 

label = ttk.Label(frame2,  text='Tipo da figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

option_menu = ttk.OptionMenu(frame2, tipo_figura_var, tipo_figura_var.get(),
                             'Linha', 'Rabisco','Retângulo','Oval','Círculo', 'Polígono')
option_menu.grid( column=0, row=1, sticky=W, **paddings)



# Área de desenho
canvas = Canvas(frame, bg='white', width=900, height=600)
canvas.grid(column=0, row=1, sticky=NSEW, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
canvas.bind("<Button-3>", incluir_figura_nova)

root.mainloop()
