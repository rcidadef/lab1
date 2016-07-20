#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import time
import argparse
import subprocess

def coleta_amostras(command, path, p, sleep_time=1):
    # Remove os arquivos de amostras de execucoes anteriores
    if os.path.exists(path):
        os.remove(path)
    
    # Print para mostrar inicio da coleta
    print '########################################\n\n\n'
    print 'Iniciando coleta de amostras'
    print '\n\n\n########################################'
    
    count = 0
    while not p.poll() and p.returncode != 0:
        command1 = "top -bn 1 > tmp_top.out"
        subprocess.call(command1, shell=True)
        command2 = "grep {} tmp_top.out >> {}".format(command, path)
        subprocess.call(command2, shell=True)
        time.sleep(sleep_time)
        count += 1
        # Limitamos, para evitar encher o hd do raspberry.
        if count == 100000:
            break

    # Removes tmp file
    os.remove('tmp_top.out')
    
    # Print para mostrar final da coleta
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

    def execute(self, n):
        os.chdir('cactus/Cactus/')
        for i in range(n):
            p = subprocess.Popen(["./exe/cactus_WaveDemo", "../WaveDemo.par"])
            coleta_amostras("cactus_WaveDemo", "cactus.out.{}".format(i), p)

class Gcc:

    def install(self):
        pass

    def execute(self, n):
        os.chdir('gcc')
        
        for i in range(n):
            os.chdir('gcc_quicksort')
            os.system("gcc -o quicksort quicksort.c")
            p = subprocess.Popen(["./quicksort"])
            coleta_amostras("quicksort", "gcc_quicksort.out.{}".format(i), p)
            
            os.chdir('../gcc_buscabinaria')
            os.system("gcc -o buscabinaria BuscaBinaria.c")
            p = subprocess.Popen(["./buscabinaria"])
            coleta_amostras("buscabinaria", "gcc_buscabinaria.out.{}".format(i), p)
            
            os.chdir('../gcc_mergesort')
            os.system("gcc -o mergesort mergesort.c")
            p = subprocess.Popen(["./mergesort"])
            coleta_amostras("mergesort", "gcc_mergesort.out.{}".format(i), p)
            
            os.chdir('../gcc_ordinsert')
            os.system("gcc -o ordinsert ordenacaoPorInsecao.c")
            p = subprocess.Popen(["./ordinsert"])
            coleta_amostras("ordinsert", "gcc_ordinsert.out.{}".format(i), p)
            
            os.chdir('../gcc_ordselecao')
            os.system("gcc -o ordselecao ordporselecao.c")
            p = subprocess.Popen(["./ordselecao"])
            coleta_amostras("ordselecao", "gcc_ordselecao.out.{}".format(i), p)

            os.chdir('..')

class Perl:

    def execute(self, n):
        os.chdir('perl')
        sleep_time = 0.1
        
        for i in range(n):
            p = subprocess.Popen(["perl", "BuscaBinaria.perl"])
            coleta_amostras("perl", "../amostras/BuscaBinariaPerl.out.{}".format(i), p, sleep_time)

            p = subprocess.Popen(["perl", "mergeSort.pl"])
            coleta_amostras("perl", "../amostras/mergeSortPerl.out.{}".format(i), p, sleep_time)

            p = subprocess.Popen(["perl", "ordporselecao.perl"])
            coleta_amostras("perl", "../amostras/ordporselecaoPerl.out.{}".format(i), p, sleep_time)

            p = subprocess.Popen(["perl", "QuickSort.perl"])
            coleta_amostras("perl", "../amostras/QuickSortPerl.out.{}".format(i), p, sleep_time)

class Gobmk:
    
    def install(self):
        pass

    def execute(self, n):
        os.chdir("gobmk")
        for i in range(n):
            p = subprocess.Popen(
                "gnugo -l 2k80-gokifu-20160710-Kim_Sooyong-Lee_Changseok.sgf "
                "--output-flags dv --level 11 --replay both "
                "-o 2k80-gokifu-20160710-Kim_Sooyong-Lee_Changseok.sgf.output",
                shell=True)
            coleta_amostras("gnugo", "gobmk.out.{}".format(i), p)

class Bzip2:

    def install(self):
        pass

    def execute(self, n):
        os.chdir('bzip2')
        for i in range(n):
            p = subprocess.Popen("bzip2 -z \"Edvard Grieg - Peer Gynt Suites - 1 and 2.mp4\"", shell=True)
            coleta_amostras("bzip2", "../amostras/bzip2.compressao.out.{}".format(i), p)
            
            p = subprocess.Popen("bzip2 -d \"Edvard Grieg - Peer Gynt Suites - 1 and 2.mp4.bz2\"", shell=True)
            coleta_amostras("bzip2", "../amostras/bzip2.descompressao.out.{}".format(i), p)

def main():
    parser = argparse.ArgumentParser(description='Script para automatizar execucao do Lab1 - Avaliacao de Desempenho')
    
    parser.add_argument('-i', '--install', dest='install', action='store_true', required=False, help='Ativa instalação dos programas')
    parser.add_argument('-e', '--execute', dest='execute', action='store_true', required=False, help='Ativa execução dos programas')
    parser.add_argument('-p', '--programs', dest='programs', nargs='+', required=False, help='Lista de Programas (all para todos)')
    parser.add_argument('-n', '--number_of_executions', dest='n', type=int, default=1, help='Quantidade de execucoes do(s) programa(s).')

    result = parser.parse_args()
    
    if not os.path.exists('amostras'):
        os.system('mkdir amostras')

    mapa = {}
    # mapa['geral'] = Geral()
    mapa['cactus'] = Cactus()
    mapa['gobmk'] = Gobmk()
    mapa['gcc'] = Gcc()
    mapa['perl'] = Perl()
    mapa['bzip2'] = Bzip2()

    lista_programas = result.programs
    if result.programs == ['all']:
        lista_programas = ['geral',
                           'cactus',
                           'gcc',
                           'perl',
                           'bzip2',
                           'gobmk']

    for prog in lista_programas:
        if prog in mapa:
            if result.install:
                mapa[prog].install()
            if result.execute:
                mapa[prog].execute(result.n)
            os.chdir('..')

if __name__ == "__main__":
    main()
