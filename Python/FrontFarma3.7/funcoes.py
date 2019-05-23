# -*- coding: utf-8 -*-

import psutil as ps

def ProcessoWindows(sNome):
    retorno = False
    processos = [proc.name() for proc in ps.process_iter()]
    for processo in processos:
        if processo == sNome:
           retorno = True
           break
    return retorno



