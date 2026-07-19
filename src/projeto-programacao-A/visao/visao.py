from tkinter import *
from tkinter import ttk

#Classe visão responsável por gerenciar a interface.
class Visao:
    def __init__(self):
        self.root = Tk()
        
        self.frame,self.frame2 = self.criar_frames()
        (self.cores_preenchimento,self.cores_bordas,self.larguras_borda,self.figuras) = self.criar_OptionMenu()
        (self.tipo_figura_var,self.cor_var,self.cor_borda_var,self.largura_borda_var) = self.criar_variaveis()
        self.menu_tipo = self.criar_menu_tipo()
        self.menu_cor = self.criar_menu_cores()
        self.menu_cor_borda = self.criar_menu_cores_borda()
        self.menu_largura_borda = self.criar_menu_largura()
        self.canvas = self.criar_canvas()
        self.botao_desfazer = self.criar_botao_desfazer()
        self.botao_salvar = self.criar_botao_salvar()
        self.botao_abrir = self.criar_botao_abrir()
        self.frame.pack()

    #cria os frames.
    def criar_frames(self):
        frame = Frame(self.root)

        frame2 = ttk.Frame(frame)
        frame2.grid(column = 0, row = 0, sticky = EW)

        return frame,frame2
    
    #cria as opções dos OptionMenus.
    def criar_OptionMenu(self):
        cores_preenchimento = {
            "Sem preenchimento": None,
            "Preto": "black",
            "Vermelho": "red",
            "Azul": "blue",
            "Verde": "green",
            "Amarelo": "yellow",
            "Laranja": "orange",
            "Roxo": "purple"
        }

        cores_bordas = {
            "Sem cor na borda": None,
            "Preto": "black",
            "Vermelho": "red",
            "Azul": "blue",
            "Verde": "green",
            "Amarelo": "yellow",
            "Laranja": "orange",
            "Roxo": "purple"
        }

        larguras_borda = {
            "Sem borda": None,
            "1": 1,
            "2": 2,
            "3": 3,
            "5": 5,
            "8": 8
        }

        figuras = {
            "Linha",
            "Rabisco",
            "Retângulo",
            "Oval",
            "Círculo",
            "Polígono"

        }

        return(cores_preenchimento, cores_bordas, larguras_borda,figuras)
    
    #cria as variáveis para serem usadas nos OptionMenus.
    def criar_variaveis(self):
        tipo_figura_var = StringVar(self.root)
        tipo_figura_var.set("Linha")
        
        cor_var = StringVar(self.root)
        cor_var.set("Sem preenchimento")

        cor_borda_var = StringVar(self.root)
        cor_borda_var.set("Sem cor na borda")

        largura_borda_var = StringVar(self.root)
        largura_borda_var.set("Sem borda")

        return (tipo_figura_var, cor_var, cor_borda_var,largura_borda_var)

    #cria os optionsMenus para cada funcionalidade.

    def criar_menu_tipo(self):
        label_tipo = ttk.Label(self.frame2,text = "Tipo da figura: ")
        label_tipo.grid(column = 0, row = 0, sticky = W, padx = 15, pady = 5)

        menu_tipo = ttk.OptionMenu(self.frame2,self.tipo_figura_var, self.tipo_figura_var.get(), *self.figuras) 
        menu_tipo.grid(column = 0, row = 1, sticky = W, padx = 15, pady = 5)

        return menu_tipo

    def criar_menu_cores(self):
        label_cor = ttk.Label(self.frame2,text = "Cor de preenchimento: ")
        label_cor.grid(column = 1, row = 0, sticky = W, padx = 15, pady = 5)

        menu_cor = ttk.OptionMenu(self.frame2,self.cor_var,self.cor_var.get(), *self.cores_preenchimento.keys())
        menu_cor.grid(column = 1, row = 1, sticky = W, padx = 15,pady = 5)

        return menu_cor
    
    def criar_menu_cores_borda(self):
        label_cor_borda = ttk.Label(self.frame2, text = "Cor da borda: ")
        label_cor_borda.grid(column = 2, row = 0, sticky = W, padx = 15, pady = 5)

        menu_cor_borda = ttk.OptionMenu(self.frame2, self.cor_borda_var, self.cor_borda_var.get(), *self.cores_bordas.keys())
        menu_cor_borda.grid(column = 2, row = 1, sticky = W, padx = 15, pady = 5 )

        return menu_cor_borda
    
    def criar_menu_largura(self):
        label_largura_borda = ttk.Label(self.frame2, text = "Grossura da borda: ")
        label_largura_borda.grid(column = 3, row = 0, sticky = W, padx = 15, pady = 5)

        menu_largura_borda = ttk.OptionMenu(self.frame2, self.largura_borda_var,self.largura_borda_var.get(), *self.larguras_borda.keys())
        menu_largura_borda.grid(column = 3, row = 1, sticky = W, padx = 15, pady = 5 )

        return menu_largura_borda

    def criar_canvas(self):
        canvas = Canvas(self.frame,width = 900, height = 600, bg = "white")
        canvas.grid(column = 0, row = 1, sticky= NSEW, padx = 15, pady = 5)

        return canvas

    #cria o design do botão de desfazer, ainda sem o "command", esperando pelo controlador.
    def criar_botao_desfazer(self):
        label_desfazer = ttk.Label(self.frame2, text = "Botão de desfazer: ")
        label_desfazer.grid(column = 5, row = 0, sticky = W, padx = 15, pady = 5)

        botao_desfazer = ttk.Button(self.frame2, text = "Desfazer")
        botao_desfazer.grid(column = 5, row = 1, sticky = W, padx = 15, pady = 5)

        return botao_desfazer

    def criar_botao_salvar(self):
        label_salvar = ttk.Label(self.frame2, text = "Botão para salvar desenho: ")
        label_salvar.grid(column = 6, row = 0, sticky = W, padx = 15, pady = 5)

        botao_salvar = ttk.Button(self.frame2, text = "Salvar")
        botao_salvar.grid(column = 6, row = 1, sticky = W, padx = 15, pady = 5)

        return botao_salvar

    def criar_botao_abrir(self):
        label_abrir = ttk.Label(self.frame2, text = "Botão para abrir desenho: ")
        label_abrir.grid(column = 7, row = 0, sticky = W, padx = 15, pady = 5)

        botao_abrir = ttk.Button(self.frame2, text = "abrir")
        botao_abrir.grid(column = 7, row = 1, sticky = W, padx = 15, pady = 5)

        return botao_abrir




        
        
        
       
        
       