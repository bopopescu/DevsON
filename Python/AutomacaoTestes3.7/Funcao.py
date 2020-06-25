# -*- coding: utf-8 -*-

import autoit
import time
import log
import Variaveis
import Tempo



def ContadorVenda(Doc, Tipo, CodCli, Seq):
    Variaveis.Nro += 1
    Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: "+ str(Seq) + " Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
    log.EscreverLog(Teste)
    Tempo.Dig()
