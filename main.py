from PIL import Image, ImageDraw, ImageFont
import csv
import os
from pathlib import Path

# Atenção: base de dados (Arquivo csv), imagens a serem escritas do certificado e o arquivo .ttf da fonte 
# devem estar na mesma pasta deste script! 


def escreverCertificado(nomePessoa, nomeArquivo):

    #definindo nome da pasta e do arquivo
    folder_name = "Certificados"
    file_name = f"{nomePessoa}.pdf"

    # criar a pasta
    os.makedirs(folder_name, exist_ok=True)
    file_path = Path(folder_name) / file_name

    # carrega a imagem de fundo
    bg_img = Image.open(nomeArquivo)

    # cria um objeto de desenho na imagem
    draw = ImageDraw.Draw(bg_img)

    # carrega a fonte do texto (IMPORTANTE: fonte tem que estar na mesma pasta do script)
    font = ImageFont.truetype('MilkyNice.ttf', size=52)

    # define o nome da pessoa
    name = nomePessoa

    # obtém as dimensões do texto
    text_width, text_height = draw.textbbox((0, 0), name, font=font)[2:]

    # define a posição do texto na imagem
    x = (bg_img.width - text_width) / 2
    y = (bg_img.height - text_height) / 2 + 60

    # desenha o texto na imagem
    # COR LARANJA: 
    # draw.text((x, y), name, font=font, fill=(248, 150, 37))
    # COR BRANCA: 
    draw.text((x, y), name, font=font, fill=(255, 255, 255))

    # salva a imagem como um novo arquivo pdf
    bg_img = bg_img.convert('RGB')
    bg_img.save(file_path, 'PDF')


#le o arquivo e cria o array de nomes
def pegaListaDeNomes(nome_arquivo):
    with open(nome_arquivo, "r", encoding='utf-8') as nomes_csv:
        nomes_lido = csv.reader(nomes_csv, delimiter=';')

        nomes = []
        chars = '[\']'

        #Manipula os dados para ficar em um array de nomes
        for linha in nomes_lido:
            linha1 = str(linha).translate(str.maketrans('', '', chars))
            linha_certa = str(linha1).split(';')
            nomes.append(linha_certa[0])

    return nomes


def gerarCertificados(baseDeDados, imagemCertificado):
    nomes = pegaListaDeNomes(baseDeDados)
    horas = 3

    for i in range(len(nomes)):
        escreverCertificado(nomes[i], imagemCertificado)

        # # pega a quantidade de nomes repetidos no csv e converte para quantidade de horas (para triagens)
        # if i+1 < len(nomes):
        #     if nomes[i] == nomes[i+1]:
        #         horas = horas + 3
        #         i = i + 1
        #         continue

        # escreverCertificado(nomes[i], f"{horas}h totais (1).png")
        # horas = 3


    print("Certificados gerados com sucesso! :)")


gerarCertificados("Nomes Certificado Membros - Relações Externas.csv", "Certificado Membros Relações Externas.png")
