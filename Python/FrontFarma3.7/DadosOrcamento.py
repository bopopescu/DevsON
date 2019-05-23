# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla


def DadosOrcamento():
    log.EscreverLog('Funçao Dados Orcamento')
    try:
        log.EscreverLog('Tela Orcamento')
        log.EscreverLog('Tempo. ' + str(Variaveis.TTela) + 'segundos')
        autoit.win_wait_active("[Class:TFRM_PERSONALCUPOM]", Variaveis.TTela)

        log.EscreverLog('Orcamento Ativo')
        Tecla.TempoR()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit7", "Wellington de Pauda da Silva")
        log.EscreverLog('Inseriu Nome')

        Tecla.Enter()
        Tecla.TempoR()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit6", "Rua Londrina 141")
        Tecla.Enter()
        Tecla.TempoR()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit2", "Jardim Parana")
        Tecla.Enter()
        Tecla.TempoR()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit5", "19807505")
        Tecla.Enter()
        Tecla.TempoR()
        log.EscreverLog("Cidade")
        autoit.send("A")
        autoit.win_wait_active("[Class:TFRM_LOCALIZAR]", Variaveis.TTela)
        Tecla.TempoR()
        autoit.send("SSIS")
        for x in range(0,3):
            Tecla.Enter()

        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TVSMDBEditTelefone1", "1897590628")
        for x in range(0,2):
            Tecla.Enter()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit4", "39177789806")
        Tecla.Enter()
        autoit.control_send("[Class:TFRM_PERSONALCUPOM]", "TRzDBEdit3", "473493895")

        Tecla.F10()
    except:
        log.EscreverLog('Nao chamou a tela orcamento')
    log.EscreverLog("Sai Funçao Dados Orcamento")
