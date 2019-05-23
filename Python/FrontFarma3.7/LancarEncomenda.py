# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import ProdutoEncomenda


def LancarEncomenda():
    log.EscreverLog('Funçao Lancar Encomenda')
    log.EscreverLog("Entra loop Produtos")
    for Arry in Variaveis.AProdEncomenda:
        ProdutoEncomenda.Produto(Arry[0],Arry[1],Arry[2],Arry[3])
        log.EscreverLog('Loop')
    log.EscreverLog("Sai loop Produtos")
    log.EscreverLog('Sai Funçao Tem Promoçao')