# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import PedeCPF
import Tecla
import Tempo
import Alerta
import Tela



def F8():
    log.EscreverLog('Entra Função F8')
    Tecla.F8()
    if Variaveis.DocFiscal == "NFCE":
       Tela.Alerta('Alerta Nfce em Homologação','Não teve Alerta NFCE')
    log.EscreverLog('Sai Função F8')

    if Variaveis.DocFiscal == "NFE":
       Tela.Alerta('Alerta NFE em Homologação','Não teve Alerta NFE')
    log.EscreverLog('Sai Função F8')
