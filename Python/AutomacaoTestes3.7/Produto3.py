# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import TemPromocao
import AltW
import MarcarPosVenda
import InformarLote
import InformarPsico

def Produto3(Prod,Qtd,Lote):
    log.EscreverLog('Função lança produto')
    log.EscreverLog(Prod)
    time.sleep(Variaveis.TDig)
    autoit.send(Prod)
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    TemPromocao.TemPromocao()
    time.sleep(Variaveis.TDig)
    autoit.send(Qtd)
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")

    if Lote == "Pos":
        MarcarPosVenda.MarcarPosVenda()
    if Lote == "L":
        InformarLote.InformarLote(Qtd)
    if Lote == "P":
        InformarPsico.InformarPsico(Qtd)

    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    log.EscreverLog('Sai função lança produto')