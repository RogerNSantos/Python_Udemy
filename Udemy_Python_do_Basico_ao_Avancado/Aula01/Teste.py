
import os
from rembg import remove
from PIL import Image

# Diretório atual onde o código está sendo executado
diretorio_atual = os.getcwd()

# Lista de extensões de imagem suportadas
extensoes = ['.webp', '.jpeg', '.jpg', '.png']

# Itera sobre os arquivos no diretório atual
for filename in os.listdir(diretorio_atual):
    # Verifica se o arquivo tem uma extensão de imagem suportada
    if any(filename.lower().endswith(ext) for ext in extensoes):
        # Constrói o caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio_atual, filename)
        
        # Abre a imagem usando PIL e converte para RGBA para garantir transparência
        img = Image.open(caminho_arquivo).convert("RGBA")

        # Remove o fundo da imagem
        img_sem_fundo = remove(img)

        # Salva a imagem sem fundo em formato PNG
        img_sem_fundo.save('img_sem_fundo.png')
        
        # Se desejar parar a execução após encontrar a primeira imagem, descomente a linha abaixo
        # break
