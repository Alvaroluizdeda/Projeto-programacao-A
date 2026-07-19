from tkinter import *
from tkinter import ttk

#Classe visão responsável por gerenciar a interface.
class Visao:
    def __init__(self):
        self.root = Tk()
        
        self.criar_frames()
        self.criar_variaveis()
        self.criar_menu_tipo()
        self.criar_menu_cores()
        self.criar_menu_cores_borda()
        self.criar_menu_largura()
        self.criar_canvas()
        self.criar_botao_desfazer()
        self.criar_botao_salvar()
        self.criar_botao_abrir()
        self.frame.pack()

    #cria os frames.
    def criar_frames(self):
        self.frame = Frame(self.root)

        self.frame2 = ttk.Frame(self.frame)
        self.frame2.grid(column = 0, row = 0, sticky = EW)
    
    #cria as variáveis para serem usadas nos optionMenu.
    def criar_variaveis(self):
        self.cores_preenchimento = {
            "Sem preenchimento": None,
            "Preto": "black",
            "Vermelho": "red",
            "Azul": "blue",
            "Verde": "green",
            "Amarelo": "yellow",
            "Laranja": "orange",
            "Roxo": "purple"
        }

        self.cores_bordas = {
            "Sem cor na borda": None,
            "Preto": "black",
            "Vermelho": "red",
            "Azul": "blue",
            "Verde": "green",
            "Amarelo": "yellow",
            "Laranja": "orange",
            "Roxo": "purple"
        }

        self.larguras_borda = {
            "Sem borda": None,
            "1": 1,
            "2": 2,
            "3": 3,
            "5": 5,
            "8": 8
        }

        self.figuras = {
            "Linha",
            "Rabisco",
            "Retângulo",
            "Oval",
            "Círculo",
            "Polígono"

        }


        self.tipo_figura_var = StringVar(self.root)
        self.tipo_figura_var.set("Linha")
        
        self.cor_var = StringVar(self.root)
        self.cor_var.set("Sem preenchimento")

        self.cor_borda_var = StringVar(self.root)
        self.cor_borda_var.set("Sem cor na borda")

        self.largura_borda_var = StringVar(self.root)
        self.largura_borda_var.set("Sem borda")

    #cria os optionsMenus para cada funcionalidade.

    def criar_menu_tipo(self):
        self.label_tipo = ttk.Label(self.frame2,text = "Tipo da figura: ")
        self.label_tipo.grid(column = 0, row = 0, sticky = W, padx = 15, pady = 5)

        self.menu_tipo = ttk.OptionMenu(self.frame2,self.tipo_figura_var, self.tipo_figura_var.get(), *self.figuras) 
        self.menu_tipo.grid(column = 0, row = 1, sticky = W, padx = 15, pady = 5)

    def criar_menu_cores(self):
        self.label_cor = ttk.Label(self.frame2,text = "Cor de preenchimento: ")
        self.label_cor.grid(column = 1, row = 0, sticky = W, padx = 15, pady = 5)

        self.menu_cor = ttk.OptionMenu(self.frame2,self.cor_var,self.cor_var.get(), *self.cores_preenchimento.keys())
        self.menu_cor.grid(column = 1, row = 1, sticky = W, padx = 15,pady = 5)
    
    def criar_menu_cores_borda(self):
        self.label_cor_borda = ttk.Label(self.frame2, text = "Cor da borda: ")
        self.label_cor_borda.grid(column = 2, row = 0, sticky = W, padx = 15, pady = 5)

        self.menu_cor_borda = ttk.OptionMenu(self.frame2, self.cor_borda_var, self.cor_borda_var.get(), *self.cores_bordas.keys())
        self.menu_cor_borda.grid(column = 2, row = 1, sticky = W, padx = 15, pady = 5 )
    
    def criar_menu_largura(self):
        self.label_largura_borda = ttk.Label(self.frame2, text = "Grossura da borda: ")
        self.label_largura_borda.grid(column = 3, row = 0, sticky = W, padx = 15, pady = 5)

        self.menu_largura_borda = ttk.OptionMenu(self.frame2, self.largura_borda_var,self.largura_borda_var.get(), *self.larguras_borda.keys())
        self.menu_largura_borda.grid(column = 3, row = 1, sticky = W, padx = 15, pady = 5 )

    def criar_canvas(self):
        self.canvas = Canvas(self.frame,width = 900, height = 600, bg = "white")
        self.canvas.grid(column = 0, row = 1, sticky= NSEW, padx = 15, pady = 5)

    #cria o design do botão de desfazer, ainda sem o "command", esperando pelo controlador.
    def criar_botao_desfazer(self):
        self.label_desfazer = ttk.Label(self.frame2, text = "Botão de desfazer: ")
        self.label_desfazer.grid(column = 5, row = 0, sticky = W, padx = 15, pady = 5)

        self.botao_desfazer = ttk.Button(self.frame2, text = "Desfazer")
        self.botao_desfazer.grid(column = 5, row = 1, sticky = W, padx = 15, pady = 5)

    def criar_botao_salvar(self):
        self.label_salvar = ttk.Label(self.frame2, text = "Botão para salvar desenho: ")
        self.label_salvar.grid(column = 6, row = 0, sticky = W, padx = 15, pady = 5)

        self.botao_salvar = ttk.Button(self.frame2, text = "Salvar")
        self.botao_salvar.grid(column = 6, row = 1, sticky = W, padx = 15, pady = 5)

    def criar_botao_abrir(self):
        self.label_abrir = ttk.Label(self.frame2, text = "Botão para abrir desenho: ")
        self.label_abrir.grid(column = 7, row = 0, sticky = W, padx = 15, pady = 5)

        self.botao_abrir = ttk.Button(self.frame2, text = "abrir")
        self.botao_abrir.grid(column = 7, row = 1, sticky = W, padx = 15, pady = 5)




        
        
        
       
        
       