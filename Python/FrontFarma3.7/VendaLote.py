# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import Produto


def VendaLote():
    log.EscreverLog('Entra funcao Venda')
    time.sleep(Variaveis.TTela)
    log.EscreverLog('Tela Venda')
    log.EscreverLog('Clicar na Grid')
    autoit.control_click("[CLASS:TFRM_VENDAS]", "TVSMDBGrid3")
    time.sleep(Variaveis.TEnter)
    log.EscreverLog("Entra loop Produtos")
    for Arry in Variaveis.AProdutoLote:
        Produto.Produto(Arry[0],Arry[1],Arry[2],Arry[3])
        log.EscreverLog('Loop')
    log.EscreverLog('Sai funcao Venda')