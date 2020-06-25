                                                                                                                                                                                                                                                                                                            # -*- coding: utf-8 -*-
import autoit
from random import choice
import os
import sys
import time
import Variaveis
import log

import PedeCPF
import RecebeDinheiro
import Crtx

import Tecla
import Tempo
import Alerta
import Tela


def FinalizaVenda(Doc,Tipo,Rec):

    log.EscreverLog('Função Finaliza Venda')

    Tela.FinalVenda()

    Tecla.F8FinalVenda()

    if Doc == "NFCE":
        Tela.Alerta('Confirmar Venda Nfce em Homologação','Sem Alerta')
    if Doc == "NFE":
        Tela.Alerta('Confirmar Venda Nfe em Homologação','Sem Alerta')

    Tela.PedeCPF()

    if Doc == "PREV":
        Tela.LancamentoNroPrevenda()

    if Rec == "S":
        RecebeDinheiro.RecebeDinheiro()

    if (Doc == "NFCE" or Doc == "NFE"):
        Tela.Alerta("Alerta De Contigencia", "Sem Alerta Contigencia")
        if Variaveis.TesteRapido =='N':
            Tela.ValidacaoNF_NFC()
            Tela.ValidacaoFinalVenda()
            Tela.Rejeicao()
            Tela.ComprovanteNFCe()
            Tela.ComprovanteDANFe()
            Tela.ValidacaoFinalVenda()

    log.EscreverLog("Sai Função Finaliza Venda")
    if Doc == "NFE":
        Tempo.Esc()
        log.EscreverLog("Imprimir NFe - {ESC}")
        Tela.ComprovanteDANFe()
    Tela.LancamentoVenda()

