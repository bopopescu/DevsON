object DM_CATEGORIA: TDM_CATEGORIA
  OldCreateOrder = False
  Height = 256
  Width = 269
  object sqlPesquisar: TSQLDataSet
    CommandText = 
      'SELECT '#13#10'CODIGO,'#13#10'DESCRICAO'#13#10'FROM'#13#10'CATEGORIA'#13#10'WHERE'#13#10'(DESCRICAO ' +
      'LIKE :DESCRICAO_CAT)'
    MaxBlobSize = -1
    Params = <
      item
        DataType = ftUnknown
        Name = 'DESCRICAO_CAT'
        ParamType = ptInput
      end>
    SQLConnection = dmConexao.sqlConexao
    Left = 64
    Top = 24
    object sqlPesquisarCODIGO: TIntegerField
      FieldName = 'CODIGO'
      Required = True
    end
    object sqlPesquisarDESCRICAO: TStringField
      FieldName = 'DESCRICAO'
      Required = True
      Size = 100
    end
  end
  object dspPesquisar: TDataSetProvider
    DataSet = sqlPesquisar
    Left = 64
    Top = 104
  end
  object cdsPesquisar: TClientDataSet
    Aggregates = <>
    Params = <
      item
        DataType = ftString
        Name = 'DESCRICAO_CAT'
        ParamType = ptInput
      end>
    ProviderName = 'dspPesquisar'
    Left = 64
    Top = 172
    object cdsPesquisarCODIGO: TIntegerField
      FieldName = 'CODIGO'
      Required = True
    end
    object cdsPesquisarDESCRICAO: TStringField
      FieldName = 'DESCRICAO'
      Required = True
      Size = 100
    end
  end
  object CDS_CATEGORIAS: TClientDataSet
    Aggregates = <>
    Params = <>
    ProviderName = 'DSP_CATEGORIAS'
    Left = 168
    Top = 176
    object CDS_CATEGORIASCODIGO: TIntegerField
      FieldName = 'CODIGO'
      Required = True
    end
    object CDS_CATEGORIASDESCRICAO: TStringField
      FieldName = 'DESCRICAO'
      Required = True
      Size = 100
    end
  end
  object DSP_CATEGORIAS: TDataSetProvider
    DataSet = SQL_CATEGORIAS
    Left = 168
    Top = 112
  end
  object SQL_CATEGORIAS: TSQLDataSet
    Active = True
    CommandText = 'SELECT * FROM '#13#10'CATEGORIA'
    MaxBlobSize = -1
    Params = <>
    SQLConnection = dmConexao.sqlConexao
    Left = 168
    Top = 24
    object SQL_CATEGORIASCODIGO: TIntegerField
      FieldName = 'CODIGO'
      Required = True
    end
    object SQL_CATEGORIASDESCRICAO: TStringField
      FieldName = 'DESCRICAO'
      Required = True
      Size = 100
    end
  end
end
