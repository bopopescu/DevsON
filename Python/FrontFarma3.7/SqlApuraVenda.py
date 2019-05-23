# -*- coding: utf-8 -*-
import Variaveis
from DAO import FuncoesBD


def SqlApura():
    sSql = 'DROP TABLE IF EXISTS PYTHONVENDA;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''
            CREATE TABLE PYTHONVENDA
            SELECT 
            '01' AS  SEQ,
            TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            V.IDVENDA,
            'VENDA' AS TABELA,
            'CODCAIXA' AS CAMPO, 
            IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            'IDFECHAMENTO' AS CAMPO2, 
            IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            FROM MYFRONT.PYTHONCONFIG P
            INNER JOIN MYOURO.VENDA V ON V.NUMPREVENDA = P.NUMPREVENDA AND TIMESTAMP(V.DATALANC,V.HORATRANSMISSAO) >= P.DTACAO  
            WHERE 
            P.ACAO = 'BAIXAR PREVENDA'
            AND P.TC = %s AND P.PASSO = %s ;
            ''' %(str(Variaveis.Tc),str(Variaveis.Passo))

    FuncoesBD.SqlSlave(sSql)

    sSql =  'DROP TABLE IF EXISTS PYTHONENTREGA;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONENTREGA
                SELECT
                '02' AS  SEQ,
                TIMESTAMP(E.DATAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'ENTREGA' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2,
                
                'CODCAIXATROCOSAI' AS CAMPO3,
                IF(E.CODCAIXATROCOSAI > 0,'PREENCHIDO','') AS VALOR3,
                
                'IDFECHAMENTOTROCOPEND' AS CAMPO4,
                IF(E.IDFECHAMENTOTROCOPEND > 0,'PREENCHIDO','') AS VALOR4,
                
                'CODCAIXATROCOENT' AS CAMPO5,
                IF(E.CODCAIXATROCOENT > 0,'PREENCHIDO','') AS VALOR5
                
                FROM  MYOURO.ENTREGAS E
                INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''

    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONPENDENTES;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONPENDENTES
            SELECT
            '03' AS  SEQ,
            TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'PENDENTES' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            
            FROM  MYOURO.PENDENTES E
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''
    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONRECEBIMENTOS;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONRECEBIMENTOS
            SELECT
            '04' AS  SEQ,
            TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'RECEBIMENTOS' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(R.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            
            FROM  MYOURO.PAGOS E
            INNER JOIN MYOURO.RECEBIMENTO_ORIGEM RO ON RO.IDPAGO = E.IDPAGO
            INNER JOIN MYOURO.RECEBIMENTOS R ON R.IDRECEBIMENTO = RO.IDRECEBIMENTO
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''

    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONPAGOS;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONPAGOS
            SELECT
            '05' AS  SEQ,
            TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'PAGOS' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            
            
            'IDFECHAMENTOVENDA' AS CAMPO2,
            IF(E.IDFECHAMENTOVENDA > 0,'PREENCHIDO','') AS VALOR2,
            
            'IDFECHAMENTO' AS CAMPO3,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR3
            
            FROM  MYOURO.PAGOS E
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''

    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONCREDITOUTILIZACAO;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''
            CREATE TABLE PYTHONCREDITOUTILIZACAO
            SELECT
            '06' AS  SEQ,
            TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'CREDITOUTILIZACAO' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(CU.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(CU.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            
            FROM  MYOURO.PAGOS E
            INNER JOIN MYOURO.CREDITOUTILIZACAO CU ON CU.IDPAGO = E.IDPAGO
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''
    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONDEVOLUCAO;'

    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONDEVOLUCAO
            SELECT
            '07' AS  SEQ,
            TIMESTAMP(E.DATAHORADEVOLUC,E.HORADEVOLUC) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'DEVOLUCAO' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2,
            
            
            'CODCAIXACRED' AS CAMPO3,
            IF(E.CODCAIXACRED > 0,'PREENCHIDO','') AS VALOR3,
            
            
            'IDFECHAMENTOCREDITO' AS CAMPO4,
            IF(E.IDFECHAMENTOCREDITO > 0,'PREENCHIDO','') AS VALOR4
            
            FROM  MYOURO.DEVOLUCAO E
            INNER JOIN MYOURO.VENDAPRODUTOS VP ON VP.IDVENDAPRODUTOS = E.IDVENDAPRODUTOORIGEM
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = VP.IDVENDA;
            '''

    FuncoesBD.SqlSlave(sSql)

    sSql ='DROP TABLE IF EXISTS PYTHONNOTASDIVACAODEVOL;'
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''CREATE TABLE PYTHONNOTASDIVACAODEVOL
            SELECT
            '08' AS  SEQ,
            TIMESTAMP(D.DATAHORADEVOLUC,D.HORADEVOLUC) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'PAGOS' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            
            
            FROM  MYOURO.NOTASDIVACAODEVOL E
            INNER JOIN MYOURO.ITENSNOTASDIV I ON E.IDNOTASDIV = I.IDNOTASDIV  
            INNER JOIN MYOURO.DEVOLUCAO D ON I.IDDEVOLUCAO = D.IDDEVOLUCAO
            INNER JOIN MYOURO.VENDAPRODUTOS VP ON VP.IDVENDAPRODUTOS = D.IDVENDAPRODUTOORIGEM
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = VP.IDVENDA;
            '''

    FuncoesBD.SqlSlave(sSql)
    sSql ='DROP TABLE IF EXISTS PYTHONESTORNOS;'

    FuncoesBD.SqlSlave(sSql)
    sSql =  '''CREATE TABLE PYTHONESTORNOS
            SELECT
            '09' AS  SEQ,
            TIMESTAMP(E.DATAVENDA,E.HORAVENDA) AS DATAHORA,
            P.TC,
            P.PASSO,
            P.ACAO,
            P.NUMPREVENDA,
            'ENTREGA' AS TABELA,
            
            'CODCAIXA' AS CAMPO,
            IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
            
            'IDFECHAMENTO' AS CAMPO2,
            IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
            
            FROM  MYOURO.ESTORNOS E
            INNER JOIN MYFRONT.PYTHONVENDA P ON P.IDVENDA = E.IDVENDA;
            '''
    FuncoesBD.SqlSlave(sSql)

    sSql =  '''INSERT IGNORE INTO PYTHONCONFIG
                (
                DTACAO,
                TC,
                PASSO,
                ACAO,
                NUMPREVENDA,
                TABELA,
                CAMPO,
                VALOR
                )
                SELECT
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM 
                (
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONENCOMENDA P
                
                UNION 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONENCOMENDA P
                
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.RTABELA,
                P.RCAMPO,
                P.RVALOR
                FROM PYTHONENCOMENDA P
                
                UNION 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.RTABELA,
                P.RCAMPO2,
                P.RVALOR2
                FROM PYTHONENCOMENDA P
                
                
                union all 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONVENDA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONVENDA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONENTREGA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONENTREGA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO3,
                P.VALOR3
                FROM PYTHONENTREGA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO4,
                P.VALOR4
                FROM PYTHONENTREGA P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO5,
                P.VALOR5
                FROM PYTHONENTREGA P
                
                UNION ALL
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONPENDENTES P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONPENDENTES P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONRECEBIMENTOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONRECEBIMENTOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONPAGOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONPAGOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO3,
                P.VALOR3
                FROM PYTHONPAGOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONCREDITOUTILIZACAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONCREDITOUTILIZACAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONDEVOLUCAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONDEVOLUCAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO3,
                P.VALOR3
                FROM PYTHONDEVOLUCAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO4,
                P.VALOR4
                FROM PYTHONDEVOLUCAO P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONNOTASDIVACAODEVOL P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONNOTASDIVACAODEVOL P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO,
                P.VALOR
                FROM PYTHONESTORNOS P
                
                UNION ALL 
                
                SELECT 
                P.SEQ,
                P.DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                P.TABELA,
                P.CAMPO2,
                P.VALOR2
                FROM PYTHONESTORNOS P
                
                ) P
                ORDER BY
                P.TC,
                P.PASSO,
                P.NUMPREVENDA,
                P.SEQ,
                P.TABELA,
                P.DATAHORA,
                P.CAMPO;
            '''
    FuncoesBD.SqlSlave(sSql)