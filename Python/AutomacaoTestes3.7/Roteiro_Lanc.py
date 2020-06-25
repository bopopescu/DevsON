# -*- coding: utf-8 -*-

import Lancamentos
import Variaveis
import log
import Tempo
import Tecla


def Roteiro():
    log.EscreverLog('Função Roteiro')
    N = 3
    for X in range(0, N):
        Tecla.Esc()

    if Variaveis.Break == 'N':
        I = 0
        Variaveis.Loop = I

    I = Variaveis.Loop
    Variaveis.Break = 'N'

    for X in range(I, Variaveis.NVezes):
        log.EscreverLog('Lançando venda ' + str(X))
        Tecla.ClickGrid()
        Variaveis.TempoAdd = 0
        if Variaveis.TesteRapido =='S' or Variaveis.TesteRapido =='Q':
            if Variaveis.NCodCli == 0:
                Lancamentos.Lancamentos(Variaveis.DocFiscal, "V", Variaveis.Cli, str(1))
            else:
                Lancamentos.Lancamentos(Variaveis.DocFiscal, "P", Variaveis.Cli, str(1))
        else:
            Lancamentos.Lancamentos(Variaveis.DocFiscal, "V", Variaveis.CliV, str(1))
            Lancamentos.Lancamentos(Variaveis.DocFiscal, "E", Variaveis.CliE, str(1))
            Lancamentos.Lancamentos(Variaveis.DocFiscal, "P", Variaveis.CliP, str(1))
            Lancamentos.Lancamentos(Variaveis.DocFiscal, "C", Variaveis.CliC, str(1))
            

        Variaveis.Loop = I
        Tempo.Click()
