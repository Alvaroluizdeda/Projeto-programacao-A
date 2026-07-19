from modelo.figuras import (Linha,Rabisco,Retangulo,Oval,Circulo,Poligono)
from tkinter import filedialog
import json


class Controlador:

    def __init__(self, visao, desenho):
        self.visao = visao
        self.desenho = desenho       
        self.figura_nova = None
        self.tipos = {"Linha": Linha,"Retângulo": Retangulo,"Oval": Oval,"Círculo": Circulo,}

        self.visao.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.visao.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.visao.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.visao.canvas.bind("<Button-3>", self.incluir_figura_nova)

        self.visao.botao_desfazer.config(command=self.desfazer)
        self.visao.botao_salvar.config(command = self.salvar)
        self.visao.botao_abrir.config(command = self.abrir)

    def iniciar_figura_nova(self, event): 
      
        tipo = self.visao.tipo_figura_var.get()
        cor = self.visao.cores_preenchimento[self.visao.cor_var.get()]
        cor_borda = self.visao.cores_bordas[self.visao.cor_borda_var.get()]
        largura = self.visao.larguras_borda[self.visao.largura_borda_var.get()]   
        if tipo == "Polígono":
            if self.figura_nova is None:
                self.figura_nova = Poligono([(event.x,event.y), (event.x,event.y)],cor,cor_borda,largura)
            else:
                self.figura_nova.adicionar_ponto(event.x,event.y)
            self.desenhar_figuras()
            return

        if tipo == "Rabisco":
            values = [(event.x,event.y)]
            self.figura_nova = Rabisco(values,cor,cor_borda,largura)
        else:
            values = (event.x,event.y,event.x,event.y)
            classe_figura = self.tipos[tipo]

            self.figura_nova = classe_figura(values,cor,cor_borda,largura)

    def atualizar_figura_nova(self, event):

        if self.figura_nova is None:
            return


        if isinstance(self.figura_nova, Poligono):
            self.figura_nova.atualizar_preview(event.x,event.y)

        else:
            self.figura_nova.atualizar(event.x,event.y)


        self.desenhar_figuras()

    def atualizar_preview_poligono(self, event):
        if not isinstance(self.figura_nova, Poligono):
           return 
        
        self.figura_nova.atualizar_preview(event.x,event.y)

        self.desenhar_figuras()


    def incluir_figura_nova(self, event): 
         if self.figura_nova is None:
            return
         if isinstance(self.figura_nova, Poligono):

            if event.num != 3:
                return

            self.figura_nova.finalizar()
         else:

            if event.num != 1:
                return
         if not self.figura_nova.incompleta():
            self.desenho.adicionar(self.figura_nova)

         self.figura_nova = None
         self.desenhar_figuras()
        
    def desenhar_figuras(self): 
        self.visao.canvas.delete("all")

        for figura in self.desenho.figuras:
            figura.desenhar(self.visao.canvas)

        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.visao.canvas, preview = True)

    ## Salva o desenho atual em um arquivo JSON(organizado pelo método), escolhido pelo usuário
    def desfazer(self):
        self.desenho.desfazer()
        self.desenhar_figuras()

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
            
        