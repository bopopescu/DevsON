# -*- coding: utf-8 -*-
import autoit
import os
import time

# Arquivo de log
arqLog = "aprendendo.txt"

def EscreverLog(sMesnagem):
    # type: (object) -> object
    data = time.asctime(time.localtime(time.time()))
    linha = "--> %s -  %s" % (data, sMesnagem)
    arq = open(arqLog, "a+")
    arq.write(linha + "\n")
    arq.close()
    print(linha)
