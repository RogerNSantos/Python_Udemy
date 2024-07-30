"""import os
from PyPDF2 import PdfReader
import pandas as pd
from openpyxl import Workbook


def extrair_texto_pdf(pdf_file):
    try:
        # Verifica se o arquivo PDF existe na mesma pasta do script
        if not os.path.exists(pdf_file):
            raise FileNotFoundError

        # Abrir o arquivo PDF
        with open(pdf_file, 'rb') as file:
            reader = PdfReader(file)
            num_pages = len(reader.pages)  # Obtém o número de páginas

            # Extrair texto de todas as páginas
            texto_completo = ''
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                texto_completo += page.extract_text()

            return texto_completo
    except FileNotFoundError:
        print(f"Erro: Arquivo PDF não encontrado em '{pdf_file}'. Verifique o caminho e tente novamente.")
        return None


def converter_pdf_para_excel(pdf_file, excel_file):
    # Extrair texto do PDF
    texto_pdf = extrair_texto_pdf(pdf_file)

    if texto_pdf is None:
        return  # Encerrar se ocorreu erro ao extrair texto

    # Criar um DataFrame Pandas
    linhas = texto_pdf.split('\n')
    dados = [linha.split('\t') for linha in linhas if linha.strip()]
    df = pd.DataFrame(dados)

    # Salvar DataFrame como Excel
    df.to_excel(excel_file, index=False, header=False)

    print(f'Arquivo Excel gerado com sucesso: {excel_file}')


if __name__ == "__main__":
    # Nome do arquivo PDF de entrada e nome do arquivo Excel de saída
    pdf_file = 'Usuários BRB.pdf'  # Nome do seu arquivo PDF
    excel_file = 'saida.xlsx'  # Nome do arquivo Excel de saída

    # Converter PDF para Excel
    converter_pdf_para_excel(pdf_file, excel_file)"""

import tabula
import pandas as pd
import os

def pdf_to_excel(pdf_file):
    # Define o nome do arquivo de saída como o nome do arquivo de entrada com extensão .xlsx
    excel_file = os.path.splitext(pdf_file)[0] + '.xlsx'

    # Extrai tabelas do PDF usando tabula
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

    # Concatena todas as tabelas em um único DataFrame do pandas
    df = pd.concat(tables)

    # Salva o DataFrame como um arquivo Excel
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f'Arquivo Excel gerado com sucesso: {excel_file}')

if __name__ == "__main__":
    # Nome do arquivo PDF de entrada
    pdf_file = 'Usuários BRB.pdf'

    # Chama a função para converter o PDF em Excel
    pdf_to_excel(pdf_file)



