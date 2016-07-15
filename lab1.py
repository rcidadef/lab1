# -*- coding: utf8 -*-
import os
import commands
import argparse

# def coleta_amostras(command, path):
#     while True:
#         command = "top -bn 1 | grep {0} >> {1}".format(command, path)
#         _, output = commands.getstatusoutput(command)
#         if not len(output):
#             break


# Geral
# sudo apt-get install git
# sudo apt-get update
# sudo apt-get upgrade
# sudo apt-get install build-essential
# sudo apt-get install gfortran

# cd $1
# mkdir amostras

# # CACTUS
# sudo apt-get install subversion
# mkdir cactus
cd cactus
# wget --no-check-certificate https://raw.github.com/gridaphobe/CRL/ET_2014_11/GetComponents
# chmod 755 GetComponents
# ./GetComponents http://cactuscode.org/documentation/tutorials/wavetoydemo/WaveDemo.th
cd Cactus
# y | make WaveDemo-config
# y | make WaveDemo
# y | make WaveDemo-testsuite
# wget http://www.cactuscode.org/documentation/tutorials/wavetoydemo/WaveDemo.par
# nohup ./exe/cactus_WaveDemo WaveDemo.par &
coleta_amostras cactus_WaveDemo $1cactus


class Cactus:
    def __init__(self):
        pass

    def install(self):
        os.system("")
        pass

    def execute(self):
        pass


class Geral
    def __init__(self):
        pass

    def install(self):
        os.system("")
        pass

    def execute(self):
        pass



def main():
    parser = argparse.ArgumentParser(description='Script para automatizar execucao do Lab1 - Avaliacao de Desempenho')
    parser.add_argument('-i', '--install', dest='install', action='store_true', required=False, help='Ativa instalação dos programas')
    parser.add_argument('-e', '--execute', dest='execute', action='store_true', required=False, help='Ativa execução dos programas')
    parser.add_argument('-p', '--programs', dest='programs', nargs='+', required=False, help='Lista de Programas (all para todos)')

    result = parser.parse_args()

    mapa = {}
    mapa['geral'] = Geral()
    mapa['cactus'] = Cactus()

    lista_programas = result.programs
    if result.programs == ['all']:
        lista_programas = ['geral', 'cactus']

    for prog in lista_programas:
        if result.install:
            mapa[prog].install()
        if result.execute:
            mapa[prog].execute()


if __name__ == "__main__":
    main()
