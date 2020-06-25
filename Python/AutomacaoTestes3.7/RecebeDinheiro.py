# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
from random import choice
import Tecla
import Tela
import Tempo


def RecebeDinheiro():
    log.EscreverLog("Função RecebeDinheiro")
    try:
        log.EscreverLog("Forma Paganento")
        Variaveis.Tempo = ( Variaveis.TempoAddFinalVenda +  10)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_FORMAPAGTOOFF]", Variaveis.Tempo)
        log.EscreverLog("Abriu Forma Paganento")
        Recebe = choice([0, 1, 2])

        Recebe = 0

        if Recebe == 1 or Recebe == 2:
            Tempo.Click()
            log.EscreverLog('Zerando Forma Dinheiro')
            autoit.control_set_text("[Class:TFRM_FORMAPAGTOOFF]", "TRzNumericEdit3", 0)
            Tecla.Enter()
            log.EscreverLog('Forma Pagamento Cheque')

        if Recebe == 2:
            Tempo.Click()
            log.EscreverLog('Zerando Forma Cheque')
            autoit.control_set_text("[Class:TFRM_FORMAPAGTOOFF]", "TRzNumericEdit2", 0)
            Tecla.Enter()
            log.EscreverLog('Forma Pagamento Cartão')

        if Recebe == 0:
            log.EscreverLog('Forma Pagamento Dinheiro')

        Tempo.TeclaAcao()

        autoit.control_click("[Class:TFRM_FORMAPAGTOOFF]", "TVSMColorButton2")
        log.EscreverLog("Confirma Forma Pagamento")

        Tecla.TempoM()

        if Recebe == 1:
            try:
                Variaveis.Tempo = (10)
                log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
                autoit.win_wait_active("[Class:TFRM_CHEQUE]", Variaveis.Tempo)
                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzButtonEdit2",str(Variaveis.CPF))
                Tecla.Enter()

                autoit.control_click("[Class:TFRM_CHEQUE]", "TRzNumericEdit1")
                Tecla.TempoM()
                Tecla.LimpaTexto()
                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzNumericEdit1",'18')

                Tecla.Enter()

                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzNumericEdit5",'1')

                Tecla.Enter()

                autoit.control_click("[Class:TFRM_CHEQUE]", "TVSMColorButton3")
                Tecla.TempoM()



            except:
                log.EscreverLog('Timer ' + str(Variaveis.TAlertaR))


        if Recebe == 2:
            try:
                Variaveis.Tempo = (10)
                log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
                autoit.win_wait_active("[Class:TFRM_SELECIONACARTAO]", Variaveis.Tempo)
                autoit.control_set_text("[Class:TFRM_SELECIONACARTAO]", "TRzEdit1",'00000')
                Tecla.TempoM()

                autoit.control_click("[Class:TFRM_SELECIONACARTAO]", "TVSMColorButton2")
                Tecla.TempoM()
            except:
                log.EscreverLog('Timer ' + str(Variaveis.TAlertaR))

        zica = 0
        if zica == 1:
            try:
                log.EscreverLog('Timer ' + str(Variaveis.TTela))
                autoit.win_wait_active("[Class:TFRM_REJEICAONFE2]", Variaveis.TTela)
                log.EscreverLog('Tratamento de Rejeições')
                Tecla.TempoM()
                autoit.control_click("[Class:TFRM_SELECIONACARTAO]", "TVSMColorButton2")
                Tecla.TempoL()
                Tela.TelaAlerta('Nota Rejeitada','Sem Alerta')
                for x in range(0,3):
                    Tecla.Esc()
            except:
                log.EscreverLog('Nota Aceita')


        log.EscreverLog("Fecha Forma Paganento")
    except:
        log.EscreverLog("Venda Prazo ou Convenio não Abre Forma Pagamento")
    log.EscreverLog("Sai Função RecebeDinheiro")
    Tempo.TelaAcao()