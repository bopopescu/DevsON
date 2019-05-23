# -*- coding: utf-8 -*-
import random
import log
import Variaveis
from DAO import FuncoesBD
import easygui
import sys
import Tela
import Tecla

def ZerarVariaveis():
    Variaveis.Break         = 'N'
    Variaveis.CodLoja       = '0'
    Variaveis.CodTerminal   = '0'
    Variaveis.CodVendedor   = '0'
    Variaveis.PrevAuto      = 'N'
    Variaveis.NroPrevenda   = 0
    Variaveis.TesteRapido   = 'N'
    Variaveis.ControlarTroco= 'N'
    Variaveis.PedeCpf       = 'N'
    Variaveis.Recebe        = 'N'
    Variaveis.Troco         = 'N'
    Variaveis.UfLoja        = ''
    Variaveis.sCPF          = ''

def SelecionarBanco():
    msg = "Banco de Dados"
    title = "Selecione um banco para conectar"
    choices = ["1 | Luiz", "2 | Wagner ", "3 | Wellington", "4 | Sandra"]
    Lista = easygui.choicebox(msg, title, choices)
    sBanco = 'N'
    if Lista != None:
        sBanco = str((Lista[:Lista.find('|')].strip()))
    else:
        sBanco = '0'
    log.EscreverLog('Selecionando banco Central e Slave')
    if sBanco == '1':
        FuncoesBD.ComDBMaster = FuncoesBD.ComDBMaster1
        FuncoesBD.ComDBSlave = FuncoesBD.ComDBSlave1
        FuncoesBD.ComDBSlaveMyouro = FuncoesBD.ComDBSlaveMyouro1
    if sBanco == '2':
        FuncoesBD.ComDBMaster = FuncoesBD.ComDBMaster2
        FuncoesBD.ComDBSlave = FuncoesBD.ComDBSlave2
        FuncoesBD.ComDBSlaveMyouro = FuncoesBD.ComDBSlaveMyouro2
    if sBanco == '3':
        FuncoesBD.ComDBMaster = FuncoesBD.ComDBMaster3
        FuncoesBD.ComDBSlave = FuncoesBD.ComDBSlave3
        FuncoesBD.ComDBSlaveMyouro = FuncoesBD.ComDBSlaveMyouro3
    if sBanco == '4':
        FuncoesBD.ComDBMaster = FuncoesBD.ComDBMaster4
        FuncoesBD.ComDBSlave = FuncoesBD.ComDBSlave4
        FuncoesBD.ComDBSlaveMyouro = FuncoesBD.ComDBSlaveMyouro4
    log.EscreverLog('Selecionou o banco Opc: ' + str(sBanco))
    Tecla.ClickGrid()

def SelecionarLoja():
    log.EscreverLog('Função Selecionar CodLoja')
    sSql = "SELECT CODLOJA,NOMELOJA FROM MYOURO.LOJAS";
    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBMaster.Select(sSql)
    choices = ''
    if len(Resultado) > 0:
        for linha in Resultado:
            if len(choices) > 0:
                choices = choices + ','
            choices = choices + str(linha[0]) + ' | ' + str(linha[1])
        choices = choices.split(',')

        msg = "Operações"
        title = "O que deseja Realizar"
        Lista = easygui.choicebox(msg, title, choices)

        if Lista != None:
            Variaveis.CodLoja = str((Lista[:Lista.find('|')].strip()))
        else:
            Variaveis.CodLoja = '0'


        sSql =\
            '''
            SELECT
                C.UFCID
            FROM LOJAS L 
            INNER JOIN CIDADES C ON c.CODCID = L.CODCID
            WHERE L.CODLOJA = %s 
            ''' % (Variaveis.CodLoja)

        log.EscreverLog('Executando Sql:' + str(sSql))
        Resultado = FuncoesBD.ComDBMaster.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.UfLoja = "'" + str(Result[0]) + "'"
        log.EscreverLog('Fim da execução da Sql')





def SelecionarTErminal():
    log.EscreverLog('Função Terminal')
    msg = "Informe o Codigo Terminal Logado"
    title = "VSM - Automação"
    fieldNames = ["Código do Terminal"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    if fieldValues == None:
        sCod = 0
        sys.exit()
    else:
        sCod = int(''.join(fieldValues))  # Converte Vetor para String
        Variaveis.CodTerminal = str(sCod)

    if Variaveis.CodTerminal != '0':
        sSql = ('SELECT ' \
               'TT.AUTO_ATENDENTELOGADO ' \
               'FROM TERMINAIS T ' \
               'INNER JOIN TIPOTERMINAL TT ON TT.IDTIPOTERMINAL = T.IDTIPOTERMINAL ' \
               'WHERE ' \
               'T.CODLOJA = "%s" and  ' \
               'T.CODTERMINAL = "%s" ' % ((Variaveis.CodLoja), (Variaveis.CodTerminal)))

        log.EscreverLog('Executando Sql:' + str(sSql))
        Resultado = FuncoesBD.ComDBMaster.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.VendedorAutomatico = str(Result[0])
        log.EscreverLog('Fim da execução da Sql')


def SelecionarCliente():
    log.EscreverLog('Carrega Cliente A Vista ')
    sSql = \
        '''
                SELECT
                    C.CODCLI
                FROM CLIENTES C
                    INNER JOIN ENDCLI E ON E.CODCLI = C.CODCLI
                    INNER JOIN CIDADES CI ON CI.CODCID = E.CODCID
                WHERE
                    CI.UFCID = %s
                    AND C.BLOQUEIO = 'N'
                    AND C.TIPOCLI = 'V'
                    ORDER BY C.CODCLI DESC
                LIMIT 1
        ''' % (Variaveis.UfLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlaveMyouro.Select(sSql)
    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.CliV = str(Result[0])
    log.EscreverLog('Fim da execução da Sql')

    log.EscreverLog('Carrega Cliente A Especial ')
    sSql = \
        '''
                SELECT
                    C.CODCLI
                FROM CLIENTES C
                    INNER JOIN ENDCLI E ON E.CODCLI = C.CODCLI
                    INNER JOIN CIDADES CI ON CI.CODCID = E.CODCID
                WHERE
                    CI.UFCID = %s
                    AND C.BLOQUEIO = 'N'
                    AND C.TIPOCLI = 'E'
                    ORDER BY C.CODCLI DESC
                LIMIT 1
        ''' %(Variaveis.UfLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlaveMyouro.Select(sSql)
    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.CliE = str(Result[0])
    log.EscreverLog('Fim da execução da Sql')

    log.EscreverLog('Carrega Cliente a Prazo ')
    sSql = \
        '''
                SELECT
                    C.CODCLI
                FROM CLIENTES C
                    INNER JOIN ENDCLI E ON E.CODCLI = C.CODCLI
                    INNER JOIN CIDADES CI ON CI.CODCID = E.CODCID
                WHERE
                    CI.UFCID = %s
                    AND C.BLOQUEIO = 'N'
                    AND C.TIPOCLI = 'P'
                    ORDER BY C.CODCLI DESC
                LIMIT 1
        ''' %(Variaveis.UfLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlaveMyouro.Select(sSql)
    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.CliP = str(Result[0])
    log.EscreverLog('Fim da execução da Sql')

    log.EscreverLog('Carrega Cliente a Convenio ')
    sSql = \
        '''
                SELECT
                    C.CODCLI
                FROM CLIENTES C
                    INNER JOIN ENDCLI E ON E.CODCLI = C.CODCLI
                    INNER JOIN CIDADES CI ON CI.CODCID = E.CODCID
                WHERE
                    CI.UFCID = %s
                    AND C.BLOQUEIO = 'N'
                    AND C.TIPOCLI = 'C'
                    ORDER BY C.CODCLI DESC
                LIMIT 1
        ''' % (Variaveis.UfLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlaveMyouro.Select(sSql)
    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.CliC = str(Result[0])
    log.EscreverLog('Fim da execução da Sql')





def ControlaTroco():
    Variaveis.ControlarTroco = 'N'
    if Variaveis.CodLoja != '0':
        sSql = "SELECT ENTREGAS_CONTROLARTROCO FROM MYOURO.CONFIGLOJA WHERE CODLOJA = '%s' " %(Variaveis.CodLoja)
        log.EscreverLog('Executando Sql:' + str(sSql))
        Resultado = FuncoesBD.ComDBSlave.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.ControlarTroco = str(Result[0])
        log.EscreverLog('Fim da execução da Sql')

def PrevendaAuto():
    Variaveis.PrevAuto = 'N'
    if Variaveis.CodLoja != '0':
        sSql = "SELECT NUMPREVENDAAUTOMATICO FROM MYOURO.CONFIGLOJA WHERE CODLOJA = '%s' " %(Variaveis.CodLoja)
        log.EscreverLog('Executando Sql:' + str(sSql))
        Resultado = FuncoesBD.ComDBSlave.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.PrevAuto = str(Result[0])
        log.EscreverLog('Fim da execução da Sql')




def NroPrevenda():
    Variaveis.NroPrevenda = 0
    if Variaveis.CodLoja != '0':
        sSql = "SELECT MAX(VV.NUMPREVENDA) FROM MYFRONT.VENDAS VV WHERE VV.CODLOJA = '%s'" %(Variaveis.CodLoja)
        log.EscreverLog('Executando Sql:' + str(sSql))
        Resultado = FuncoesBD.ComDBSlave.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.NroPrevenda = (Result[0])
        log.EscreverLog('Fim da execução da Sql')


def PedeCpf():
    Variaveis.PedeCpf = 'S'
    sSql = "SELECT COALESCE(CF.STATUS,'S') " \
           "FROM myouro.LOJAS L " \
           "INNER JOIN myouro.CIDADES C ON C.CODCID = L.CODCID " \
           "LEFT JOIN myouro.CONFIGURACAO CF ON CF.CHAVE = CONCAT(C.UFCID,'_PEDECPF') " \
           "WHERE L.CODLOJA  = %s " % (Variaveis.CodLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlave.Select(str(sSql))

    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.PedeCpf = str(Result[0])


def GeraCpf():
    def calcula_digito(digs):
        s = 0
        qtd = len(digs)
        for i in range(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10: return 0
        return res

    n = [random.randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))
    #return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)
    Variaveis.sCPF = str("%d%d%d%d%d%d%d%d%d%d%d" % tuple(n))
    log.EscreverLog("CPF Gerado: " + str(Variaveis.sCPF))


def Operecao():
    if Variaveis.CodLoja != '0':
        Variaveis.DocFiscal = ''
        msg = "Operações"
        title = "O que deseja Realizar"
        choices = ["1 | Venda", "2 | Pre-vendas ", "3 | Baixa Pre-Venda", "4 | Lançamento de Fórmulas"]
        Lista = easygui.choicebox(msg, title, choices)

        if Lista != None:
            sOperacao = str((Lista[:Lista.find('|')].strip()))
        else:
            sOperacao = '0'

        if sOperacao == '4':
            log.EscreverLog('Executando trecho:' + str(sOperacao))
            exit()

        if sOperacao != '2':
            msg = "Documento Fiscal a Ser Utilizado"
            title = "Qual Documento Fiscal esta Configurado"
            choices = ["1 | Cupom Fiscal", "2 | Sat ", "3 | Nfc-e", "4 | Nfe", "5 | Modelo 2"]
            Lista = easygui.choicebox(msg, title, choices)
            if Lista != None:
                sDoc = str((Lista[:Lista.find('|')].strip()))
            else:
                sDoc = '0'
        else:
            sDoc = '6'

        if sDoc == '1':
            Variaveis.DocFiscal = 'ECF'

        if sDoc == '2':
            Variaveis.DocFiscal = 'SAT'

        if sDoc == '3':
            Variaveis.DocFiscal = 'NFCE'

        if sDoc == '4':
            Variaveis.DocFiscal = 'NFE'

        if sDoc == '5':
            Variaveis.DocFiscal = 'MOD2'

        if sDoc == '6':
            Variaveis.DocFiscal = 'PREV'

        Tecla.ClickGrid()




def TesteRapido():
    Variaveis.TesteRapido='N'
    Variaveis.NQtdProd = 0
    if Variaveis.CodLoja != '0':
        msg = "Tipo do Teste"
        title = "Optar por um Teste Rapido"

        if Variaveis.DocFiscal == 'NFCE':
            choices = ["1 | Informar um Produto e um Vendedor (Teste Rapido)", "2 | Validação com Varios Produtos (Teste Lento)","99 | Tratar Rejeiçoes"]
        else:
            choices = ["1 | Informar um Produto e um Vendedor (Teste Rapido)","2 | Informar Quantidade de produtos e um Vendedor (Teste Rapido 2)","3 | Validação com Varios Produtos (Teste Lento)"]

        Lista = easygui.choicebox(msg, title, choices)
        if Lista != None:
            sSelecao = str((Lista[:Lista.find('|')].strip()))
        else:
            sSelecao = '0'

        if sSelecao == '1':
            Variaveis.TesteRapido ='S'
        if sSelecao == '2':
            Variaveis.TesteRapido = 'Q'
        if sSelecao == '3':
            Variaveis.TesteRapido = 'N'
        if sSelecao == '99':
            Variaveis.TesteRapido = 'R'

        if Variaveis.DocFiscal =='NFCE' and Variaveis.TesteRapido == 'R' :
            Tela.TratamentoRejeicoes()
            Variaveis.TesteRapido = 'S'


        if Variaveis.TesteRapido =='S':
            msg = "Informe o Produto"
            title = "VSM - Automação"
            fieldNames = ["Informao Código do Produto"]
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues == None:
                sCod = 0
                sys.exit()
            else:
                sCod = int(''.join(fieldValues))  # Converte Vetor para String
            Variaveis.CodProd = str(sCod)

        if Variaveis.TesteRapido == 'Q':
            msg = "Informe a Quantidade de Produtos"
            title = "VSM - Automação"
            fieldNames = ["Informe a Quantidade"]
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues == None:
                sCod = 0
                sys.exit()
            else:
                sCod = int(''.join(fieldValues))  # Converte Vetor para String
            Variaveis.NQtdProd = str(sCod)

        sCod = 0
        if Variaveis.DocFiscal == 'NFE' or Variaveis.TesteRapido == 'Q':
            msg = "Informe o Cliente"
            title = "VSM - Automação"
            fieldNames = ["Informao Código do Cliente"]
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues == None:
                sCod = 0
                sys.exit()
            else:
                sCod = int(''.join(fieldValues))  # Converte Vetor para String

        Variaveis.Cli = str(sCod)


        if Variaveis.VendedorAutomatico =='N':
            msg = "Informe o Vendedor"
            title = "VSM - Automação"
            fieldNames = ["Informao Código do Vendedor"]

            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues == None:
                sCod = 0
                sys.exit()
            else:
                sCod = int(''.join(fieldValues))  # Converte Vetor para String
                Variaveis.VendedorAutomatico = 'N'
            Variaveis.CodVendedor = str(sCod)