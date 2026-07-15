from desenho import Desenho

desenho = Desenho()

print(f"Inicial: {desenho.figuras}")

desenho.adicionar("Linha")
desenho.adicionar("Círculo")
desenho.adicionar("Retângulo")

print(f"Após adicionar: {desenho.figuras}")

desenho.desfazer()

print(f"Após desfazer: {desenho.figuras}")

desenho.limpar()
print(f"Após limpar: {desenho.figuras}")