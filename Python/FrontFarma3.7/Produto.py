# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import SENHAFUNC
import TemPromocao
import AltW
import MarcarPosVenda
import InformarLote
import InformarPsico
import Tecla
import Tempo
import Tela

def Produto(Prod,Desc,Qtd,Lote):
    log.EscreverLog('Entrada Função lança produto')
    log.EscreverLog('Produto codigo: ' + str(Prod))
    autoit.send(Prod)
    Tecla.EnterProduto()
    if Variaveis.TesteRapido != 'S':
        Tela.Validacao()
        for x in range(0, 2):
            Tela.AlertaProduto('Espera Alerta', 'Sem Alerta')
        TemPromocao.TemPromocao()

    log.EscreverLog('Quantidade: ' + str((Qtd)))
    autoit.send(Qtd)
    Tecla.EnterProduto()

    if Desc != "0":
        AltW.AltW(Desc)
        for x in range(0,3):
            Tecla.Enter()
    else:
        Tecla.Enter()

    if Lote == "Pos":
        MarcarPosVenda.MarcarPosVenda()
    if Lote == "L":
        InformarLote.InformarLote(Qtd)
    if Lote == "P":
        InformarPsico.InformarPsico(Qtd)

    log.EscreverLog('Sai função Lança produto')