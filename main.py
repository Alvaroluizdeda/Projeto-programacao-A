from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    tipos = {                  #generaliza os tipos que possuem a mesma lógica
        "Linha": "linha",      
        "Retângulo": "retangulo",
        "Oval": "oval",
        "Círculo": "circulo"
    }      

    global figura_nova                         

    tipo = tipo_figura_var.get()

    if tipo == "Rabisco":
        figura_nova = ("rabisco",[(event.x,event.y,)], cores[cor_var.get()]) #rabisco é o único que precisa de uma lista de pontos, por isso o caso especial.

    else:
        figura_nova = (tipos[tipo], (event.x,event.y,event.x,event.y), cores[cor_var.get()])

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    else : 
        tipo = figura_nova[0] #n fica mais fixo em linha, depende da figura dada na tupla agora.
        figura_nova = (tipo, (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cores[cor_var.get()])
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras(): # generaliza os casos com lógica repetida
    desenhos = {
        "linha": canvas.create_line,
        "retangulo": canvas.create_rectangle,
        "oval": canvas.create_oval
    }

    canvas.delete("all")

    for fig, values, cor in figuras:

        if fig == "rabisco":
            canvas.create_line(values, fill=cor)

        elif fig == "circulo":
            novo_values = desenhar_circulo(values)
            canvas.create_oval(
                *novo_values,
                outline=cor
            )

        else:
            desenhos[fig](
                *values,
                outline=cor
            )

def desenhar_figura_nova(): #mesma lógica dos dicts anteriores, organização e generalização.
    desenhos = {
        "linha": canvas.create_line,
        "retangulo": canvas.create_rectangle,
        "oval": canvas.create_oval
    }
    
    fig, values, cor = figura_nova
     
    if fig == "rabisco":
        canvas.create_line(values, dash = (4,2), fill = cor)

    elif fig == "circulo":
        novo_values = desenhar_circulo(values)
        canvas.create_oval(novo_values[0],novo_values[1],novo_values[2],novo_values[3], dash = (4,2), outline = cor)

    elif fig == "oval":
        canvas.create_oval(values[0],values[1],values[2],values[3], dash = (4,2), outline = cor)

    else:
        desenhos[fig](values[0],values[1],values[2],values[3], dash = (4,2), outline = cor)

      
    
def desenhar_circulo(values):  #caso especial do oval
    x1 = values[0]
    y1 = values[1]
    x2 = values[2]
    y2 = values[3]

    lado = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x2 = x1 - lado

    else:
        x2 = x1 + lado
    

    if y2 < y1:
        y2 = y1 -lado

    else:
        y2 = y1 + lado
    return (x1,y1,x2,y2)
    

def incompleta(figura):  #generalizei novamente, apenas deixando rabisco como caso especial.
    
    fig, values, _ = figura
    if fig == "rabisco":
        return len(values) <= 1
    
    else:
        return (values[0],values[1]) == (values[2],values[3])
    


def iniciar_figura_nova(event):

    tipos = {
        "Linha": "linha",
        "Retângulo": "retangulo",
        "Oval": "oval",
        "Círculo": "circulo"
    }

    global figura_nova

    tipo = tipo_figura_var.get()
    cor = cores[cor_var.get()]

    if tipo == "Rabisco":
        figura_nova = ("rabisco", [(event.x, event.y)], cor)
    else:
        figura_nova = (
            tipos[tipo],
            (event.x, event.y, event.x, event.y),
            cor
        )








#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)


cores = {
    "Preto": "black",
    "Vermelho": "red",
    "Azul": "blue",
    "Verde": "green",
    "Amarelo": "yellow",
    "Laranja": "orange",
    "Roxo": "purple"
}


# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

cor_var = StringVar(root)
cor_var.set("Preto")


option_menu_cor = ttk.OptionMenu(
    frame,
    cor_var,
    "Preto",
    *cores.keys()
)

option_menu_cor.grid(column=3, row=0, sticky=W, **paddings)




cor = cores[cor_var.get()]


# label
label = ttk.Label(frame,  text='Tipo da figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                            'Linha', 'Linha', 'Rabisco','Retângulo','Oval','Círculo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
