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
    cor = cores[cor_var.get()]
    cor_borda = cores[cor_borda_var.get()]
    largura = espessuras[largura_borda_var.get()]
    if tipo == "Rabisco":
        figura_nova = ("rabisco",[(event.x,event.y,)], cor, cor_borda, largura) #rabisco é o único que precisa de uma lista de pontos, por isso o caso especial.

    else:
        figura_nova = (tipos[tipo], (event.x,event.y,event.x,event.y), cor, cor_borda, largura)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    else : 
        tipo = figura_nova[0]  #n fica mais fixo em linha, depende da figura dada na tupla agora.
        cor = figura_nova[2]
        cor_borda = figura_nova[3]
        largura = figura_nova[4]
        figura_nova = (tipo, (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor, cor_borda, largura)

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

    for fig, values, cor, cor_borda, largura in figuras:

        if fig == "rabisco":
            canvas.create_line(*values, fill = cor, width = largura) #rabisco não pode ficar "sem preenchimento", igual à linha
        
        elif fig == "linha":
            canvas.create_line(*values, fill = cor, width = largura) #linha não pode ficar "sem preenchimento", igual à rabisco

        elif fig == "circulo":
            novo_values = desenhar_circulo(values)
            canvas.create_oval(*novo_values, fill=cor, outline=cor_borda, width=largura)

        else:
            desenhos[fig](*values,fill=cor,outline=cor_borda,width=largura)

def desenhar_figura_nova(): #mesma lógica dos dicts anteriores, organização e generalização.
    desenhos = {
        "linha": canvas.create_line,
        "retangulo": canvas.create_rectangle,
        "oval": canvas.create_oval
    }
    
    fig, values, cor, cor_borda, largura = figura_nova
     
    if fig == "rabisco":
        canvas.create_line(values, dash = (4,2), fill = cor,width=largura)
    
    elif fig == "linha":
        canvas.create_line(values, dash = (4,2), fill = cor,width=largura)

    elif fig == "circulo":
        novo_values = desenhar_circulo(values)
        canvas.create_oval(*novo_values, dash = (4,2), fill = cor)

    else:
        desenhos[fig](*values, dash = (4,2), fill=cor)

      
    
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
    
    fig, values, *_ = figura
    if fig == "rabisco":
        return len(values) <= 1
    
    else:
        return (values[0],values[1]) == (values[2],values[3])
    
def desfazer():
    if len(figuras) > 0:
        figuras.pop()  # remove a última figura adicionada na lista [figuras]
        desenhar_figuras()
#/*/*/*/*/*/*/ MAIN /*/*/*/*/*/*/

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

#dicionarios de cores e espessuras para os option menus
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
    "1": 1,
    "2": 2,
    "3": 3,
    "5": 5,
    "8": 8
}



# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 


frame2 = ttk.Frame(frame)#criei outro frame pra separar os textos do canvas, mas não é necessário, só pra organização visual mesmo.
frame2.grid(column=0, row=0, sticky=N)

#um botão para desfazer a última figura desenhada, que chama a função desfazer quando clica
botao_desfazer = ttk.Button(frame2, text="Desfazer",command=desfazer)

botao_desfazer.grid(column=0, row=8, sticky=W, **paddings)

#option menu & Label das espessuras e das cores das espessuras
cor_borda_var = StringVar(root)
cor_borda_var.set("Preto")

largura_borda_var = StringVar(root)
largura_borda_var.set("2")

#cor da borda
label_cor_borda = ttk.Label(frame2, text="Cor da borda:")
label_cor_borda.grid(column=0, row=4, sticky=W, **paddings)
option_menu_cor_borda = ttk.OptionMenu( frame2,cor_borda_var, cor_borda_var.get(), *cores.keys())
option_menu_cor_borda.grid(column=0, row=5, sticky=W, **paddings)

#borda
label_largura_borda = ttk.Label(frame2, text="Grossura da borda:")
label_largura_borda.grid(column=0, row=6, sticky=W, **paddings)
option_menu_largura = ttk.OptionMenu(frame2,largura_borda_var, largura_borda_var.get(),*espessuras.keys())
option_menu_largura.grid(column=0, row=7, sticky=W, **paddings)


# option menu & Label das cores
cor_var = StringVar(root)
cor_var.set("Sem preenchimento")

option_menu_cor = ttk.OptionMenu( frame2,cor_var, cor_var.get(), *cores.keys())
option_menu_cor.grid(column=0, row=3, sticky=W, **paddings)

label_cor = ttk.Label(frame2, text = "Cor de preenchimento:")
label_cor.grid(column = 0, row=2, sticky = W, **paddings)


# option menu  & Label das figuras
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame2, tipo_figura_var,
                            'Linha', 'Linha', 'Rabisco','Retângulo','Oval','Círculo')
option_menu.grid( column=0, row=1, sticky=W, **paddings)
label = ttk.Label(frame2,  text='Tipo da figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=1, row=0, sticky=NSEW, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()