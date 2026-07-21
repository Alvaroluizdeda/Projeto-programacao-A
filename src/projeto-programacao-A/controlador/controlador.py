from modelo.figuras import (Linha,Rabisco,Retangulo,Oval,Circulo,Poligono)
from tkinter import filedialog
import json
from controlador.ferramentas import (FerramentaLinha,FerramentaRabisco,FerramentaRetangulo,FerramentaOval,FerramentaCirculo,FerramentaPoligono )


class Controlador:

    def __init__(self, visao, desenho):
        self.ferramentas = {
            "Linha": FerramentaLinha(self),
            "Rabisco": FerramentaRabisco(self),
            "Retângulo": FerramentaRetangulo(self),
            "Oval": FerramentaOval(self),
            "Círculo": FerramentaCirculo(self),
            "Polígono": FerramentaPoligono(self)

        }

        self.visao = visao
        self.desenho = desenho       
        self.figura_nova = None
        
        self.visao.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.visao.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.visao.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.visao.canvas.bind("<Button-3>", self.incluir_figura_nova)

        self.visao.botao_desfazer.config(command=self.desfazer)
        self.visao.botao_salvar.config(command = self.salvar)
        self.visao.botao_abrir.config(command = self.abrir)

    def iniciar_figura_nova(self, event): 
        tipo = self.visao.tipo_figura_var.get()
        
        self.ferramenta = self.ferramentas[tipo]

        self.ferramenta.iniciar(event)
        
    def atualizar_figura_nova(self, event):
        self.ferramenta.atualizar(event)

    def incluir_figura_nova(self, event): 
        self.ferramenta.finalizar(event)
         
        
    def desenhar_figuras(self): 
        self.visao.canvas.delete("all")

        for figura in self.desenho.figuras:
            figura.desenhar(self.visao.canvas)

        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.visao.canvas, preview = True)

    
    def desfazer(self):
        self.desenho.desfazer()
        self.desenhar_figuras()

    ## Salva o desenho atual em um arquivo JSON(organizado pelo método), escolhido pelo usuário
    def salvar(self):
        caminho = filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("Arquivos JSON", "*.json")])

        if not caminho:
            return
        
        figuras = []

        for figura in self.desenho.figuras:
            figuras.append({
                "tipo": type(figura).__name__,
                "values": figura.values,
                "cor": figura.cor,
                "cor_borda": figura.cor_borda,
                "largura": figura.largura
            })
        
        dados = {
            "figuras": figuras
        }

       

        with open(caminho, "w", encoding = "utf-8") as arquivo:
         json.dump(dados, arquivo, indent = 4, ensure_ascii = False)

    def abrir(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])

        if not caminho:
            return
        
        with open(caminho, "r", encoding = "utf-8") as arquivo:
            dados = json.load(arquivo)

        self.desenho.limpar()

        tipos = {
            "Linha": Linha,
            "Rabisco": Rabisco,
            "Retangulo": Retangulo,
            "Oval": Oval,
            "Circulo": Circulo,
            "Poligono": Poligono
        }

        for figura in dados["figuras"]:
            classe = tipos[figura["tipo"]]

            nova_figura = classe(figura["values"], figura["cor"], figura["cor_borda"], figura["largura"])

            self.desenho.adicionar(nova_figura)

            self.desenhar_figuras()
            
        