""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
 um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
  usando este link (em minutos). """

import math
# Solicitando o tamanho do arquivo para usuário em megabytes
tamanhoArquivoMB = float(input('Informe o tamanho do arquivo em MB: '))

# Solicitando a velocodade do link de Internet em megabits por segundos
velocidadeInternetMBPS = float(input('Informe a velocidade de sua internet: '))

# Converte o tamanho do arquivo de megabytes para megabits
tamanhoArquivoMBITS = tamanhoArquivoMB * 8

# Calcula o tempo de download em segundos
tempoDowload = tamanhoArquivoMBITS / velocidadeInternetMBPS

# Converte o tempo de download para minutos
tempodOWLOADMinutos = tempoDowload / 60

# Exibindo o tempo de dowload aproximado em minutos
print(f'Tempo aproximado para DOWLOAD é {tempodOWLOADMinutos:.2f} minútos')
