from modelo.desenho import Desenho
from visao.visao import Visao
from controlador.controlador import Controlador


def main():
    desenho = Desenho()
    visao = Visao()

    controlador = Controlador(visao, desenho)

    visao.root.mainloop()


if __name__ == "__main__":
    main()