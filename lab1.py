#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import time
import argparse
import subprocess

def coleta_amostras(command, path, p):
    print '########################################\n\n\n'
    print 'Iniciando coleta de amostras'
    print '\n\n\n########################################'
    # Limitamos, para evitar encher o hd do raspberry.
    count = 0
    while not p.poll():
        command1 = "top -bn 1 > tmp_top.out"
        subprocess.call(command1, shell=True)
        command2 = "grep {} tmp_top.out >> {}".format(command, path)
        subprocess.call(command2, shell=True)
        time.sleep(2)
        count += 1
        if count == 100000:
            break
    print '########################################\n\n\n'
    print 'Parando coleta de amostras! Saida vazia!'
    print '\n\n\n########################################'

class Cactus:
    
    def __init__(self):
        pass

    def install(self):
        os.system("sudo apt-get install subversion")
        os.system("mkdir cactus")
        os.system("cd cactus")
        os.system("wget --no-check-certificate https://raw.github.com/gridaphobe/CRL/ET_2014_11/GetComponents")
        os.system("chmod 755 GetComponents")
        os.system("./GetComponents http://cactuscode.org/documentation/tutorials/wavetoydemo/WaveDemo.th")
        os.system("cd Cactus")
        os.system("y | make WaveDemo-config")
        os.system("y | make WaveDemo")
        os.system("y | make WaveDemo-testsuite")
        os.system("wget http://www.cactuscode.org/documentation/tutorials/wavetoydemo/WaveDemo.par")

    def execute(self):
        os.system("cd ./cactus/Cactus/")
        os.chdir('cactus/Cactus/')
        p = subprocess.Popen(["./exe/cactus_WaveDemo", "../WaveDemo.par"])
        coleta_amostras("cactus_WaveDemo", "cactus.out", p)


class Geral:
    
    def __init__(self):
        pass

    def install(self):
        os.system("")
        # Geral
        # sudo apt-get install git
        # sudo apt-get update
        # sudo apt-get upgrade
        # sudo apt-get install build-essential
        # sudo apt-get install gfortran

        # cd $1
        # mkdir amostras
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
    # mapa['geral'] = Geral()
    mapa['cactus'] = Cactus()

    lista_programas = result.programs
    if result.programs == ['all']:
        lista_programas = ['geral', 'cactus']

    for prog in lista_programas:
        if prog in mapa:
    		if result.install:
    			mapa[prog].install()
    		if result.execute:
    			mapa[prog].execute()


if __name__ == "__main__":
    main()
