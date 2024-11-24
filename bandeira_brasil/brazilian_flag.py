from PIL import Image, ImageDraw

def criar_bandeira_brasil(largura):
    altura = int(largura * 14 / 20) 
    verde = (0, 155, 58) 
    amarelo = (255, 223, 0) 
    azul = (0, 39, 118)  

    imagem = Image.new("RGB", (largura, altura), verde)
    desenhador = ImageDraw.Draw(imagem)

    largura_losango = int((10 / 14) * altura)  
    altura_losango = int((7 / 14) * altura) 

    coordenadas_losango = [
        (largura // 2, altura // 2 - altura_losango // 2),  
        (largura // 2 + largura_losango // 2, altura // 2),  
        (largura // 2, altura // 2 + altura_losango // 2),  
        (largura // 2 - largura_losango // 2, altura // 2),  
    ]
    desenhador.polygon(coordenadas_losango, fill=amarelo)  

    diametro_circulo = int((3 / 5) * altura_losango)  
    canto_superior_esquerdo = (
        largura // 2 - diametro_circulo // 2,
        altura // 2 - diametro_circulo // 2,
    )
    canto_inferior_direito = (
        largura // 2 + diametro_circulo // 2,
        altura // 2 + diametro_circulo // 2,
    )
    desenhador.ellipse([canto_superior_esquerdo, canto_inferior_direito], fill=azul) 

    imagem.show()

if __name__ == "__main__":
    largura_bandeira = int(input("Digite a largura da bandeira: "))
    criar_bandeira_brasil(largura_bandeira)
