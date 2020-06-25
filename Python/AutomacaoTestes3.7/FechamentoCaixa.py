# -*- coding: utf-8 -*-
#import Principal

import autoit
import time
import Variaveis
import log


import Documento
import Venda
import LancarEncomenda
import F8
import Cliente
import Vendedor
import FinalizaVenda
import Entrega
import DadosEntrega
import TrocoEntrega
import FechaDadosEntrega
import LocalizaCupom
import Devolucao
import Estorno
import PgtoAntecipado
import Crtx
import RecebeDinheiro
from DAO import FuncoesBD


def Lancamentos(Doc,Tipo,CodCli,Seq):

    Crtx.Crtx()
    Variaveis.Nro += 1

    if Variaveis.DocFiscal == 'PREV':
        Variaveis.Query = (
                            '''
                            INSERT IGNORE INTO PYTHONCONFIG
                            (ACAO,DTACAO,NUMPREVENDA,TC,PASSO) SELECT "LANÇA PREVENDA", NOW(), %s,%s,%s
                            ''' % (int(Variaveis.Nro), int(Variaveis.Tc), int(Variaveis.Passo)))
    else:
        Variaveis.Query = (
                            '''
                            INSERT IGNORE INTO PYTHONCONFIG
                            (ACAO,DTACAO,NUMPREVENDA,TC,PASSO) SELECT "VENDA", NOW(), %s,%s,%s
                            ''' % (int(Variaveis.Nro), int(Variaveis.Tc), int(Variaveis.Passo)))


    if (Seq == "999999"):
        LocalizaCupom.LocalizaCupom(1)
        log.EscreverLog("Devolução do cupom: " + str(Variaveis.NCupom))
        Devolucao.Devolucao(str(Variaveis.NCupom),0)
        LocalizaCupom.LocalizaCupom(2)
        log.EscreverLog("Devolução do cupom: " + str(Variaveis.NCupom))
        Devolucao.Devolucao(str(Variaveis.NCupom),1)

        if Variaveis.Nro == 1:
            LocalizaCupom.LocalizaCupom(0)
            log.EscreverLog("Estono de cupom: " + str(Variaveis.NCupom))
            Estorno.Estorno(str(Variaveis.NCupom))


    # 1 - Sem entrega
    if (Seq == "1" or Seq == "0"):
        FuncoesBD.SqlSlave(str(Variaveis.Query))
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 1 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)


        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 2 - Com entrega
    if (Seq == "2" or Seq == "0"):
        FuncoesBD.SqlSlave(str(Variaveis.Query))

        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 2 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)

        if CodCli != "0":
            Entrega.Entrega()
        else:
            DadosEntrega.DadosEntrega()

        FechaDadosEntrega.FechaDadosEntrega()

        Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 3 - Com entrega e Pgto Antecipado
    if (Seq == "3" or Seq == "0"):
        FuncoesBD.SqlSlave(str(Variaveis.Query))
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 3 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)


        if CodCli != "0":
            Entrega.Entrega()
        else:
            DadosEntrega.DadosEntrega()

        PgtoAntecipado.PgtoAntecipado()
        Rec = "S"
        if Doc == "PREV":
            Rec = "N"


        FechaDadosEntrega.FechaDadosEntrega()

        log.EscreverLog('Timer ' + str(Variaveis.TTela))
        time.sleep(Variaveis.TTela)

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 4 - Com entrega com troco
    if (Seq == "4" or Seq == "0") and Tipo == "V":
        FuncoesBD.SqlSlave(str(Variaveis.Query))
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 4 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)

        if CodCli != "0":
            Entrega.Entrega()
        else:
            DadosEntrega.DadosEntrega()

        TrocoEntrega.TrocoEntrega("150")
        FechaDadosEntrega.FechaDadosEntrega()
        Rec = "N"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 5 - Encomenda com Pgto Antecipado
    if (Seq == "5" or Seq == "0") and Tipo == "V":

        Variaveis.Query = (
            '''
            INSERT IGNORE INTO PYTHONCONFIG
            (ACAO,DTACAO,NUMPREVENDA,TC,PASSO) SELECT "ENCOMENDA", NOW(), %s,%s,%s
            ''' % (int(Variaveis.Nro), int(Variaveis.Tc), int(Variaveis.Passo)))

        FuncoesBD.SqlSlave(str(Variaveis.Query))

        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 4 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        LancarEncomenda.LancarEncomenda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)

        time.sleep(Variaveis.TEnter)
        autoit.send('{F8}')
        time.sleep(Variaveis.TEnter)
        try:
            autoit.win_wait_active("[Class:TFRM_DADOSENTREGAENCOMENDA]", Variaveis.TTela)
            time.sleep(Variaveis.TEnter)
            autoit.send('{F7}')
            time.sleep(Variaveis.TEnter)
            log.EscreverLog('F7')
        except:
            log.EscreverLog('Error')

        try:
            autoit.win_wait_active("[Class:TFRM_MOSTRARENCOMENDAS]", Variaveis.TTela)
            time.sleep(Variaveis.TEnter)
            autoit.control_click("[Class:TFRM_MOSTRARENCOMENDAS]", 'TRzBmpButton1')
            time.sleep(Variaveis.TEnter)
            log.EscreverLog('Confirma Pagamento Anteciapado')
        except:
            log.EscreverLog('Error')
        RecebeDinheiro.RecebeDinheiro()



    if (Seq == "99" or Seq == "0"):
        FuncoesBD.SqlSlave(str(Variaveis.Query))
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 1 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        log.EscreverLog('Timer ' + str(Variaveis.TCliente))
        time.sleep(Variaveis.TCliente)

        Vendedor.Vendedor(Doc, Tipo)

        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)

        Rec = "S"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)