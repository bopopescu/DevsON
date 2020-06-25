# -*- coding: utf-8 -*-

import Variaveis
import log
import Produto
from random import choice
import Tecla
import BuscaProduto
import Tempo

def Venda():
    log.EscreverLog('Funcao Venda')
    i = choice([1, 2, 3])
    if Variaveis.TesteRapido == 'Q':
        i = int(Variaveis.NQtdProd)
    cont = 1

    while cont <= i:
        log.EscreverLog('Produto ' + str(cont) + ' de ' +str(i))
        if Variaveis.TesteRapido == 'N':
            BuscaProduto.BuscaProduto()
            Qtd = choice([1,2])

        if Variaveis.TesteRapido == 'S':
            i = 1
            Qtd = 1
            Variaveis.AtwDesc = "0"

        if Variaveis.TesteRapido == 'Q':
            BuscaProduto.BuscaProduto()
            Qtd = 1
            Variaveis.AtwDesc = "0"

        if Variaveis.AtwDesc != 0:
            log.EscreverLog('Desconto no Alt+w de: ' + str(Variaveis.AtwDesc) + '%')

        Produto.Produto(str(Variaveis.CodProd), Variaveis.AtwDesc,str(Qtd), 'N')
        cont += 1
        Tempo.Dig()
        log.EscreverLog("Sai loop Produtos")

    log.EscreverLog('Sai Funcao Venda')
    Tecla.ClickGrid()
