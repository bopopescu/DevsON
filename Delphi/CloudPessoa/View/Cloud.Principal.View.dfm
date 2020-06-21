object CloudPrincipalView: TCloudPrincipalView
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'Gerenciador de Clientes'
  ClientHeight = 443
  ClientWidth = 714
  Color = clWhite
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Segoe UI'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  OnCreate = FormCreate
  OnDestroy = FormDestroy
  PixelsPerInch = 96
  TextHeight = 13
  object pnlTitulo: TPanel
    Left = 0
    Top = 0
    Width = 714
    Height = 38
    Align = alTop
    Color = 7884599
    ParentBackground = False
    TabOrder = 0
    object lblTitulo: TLabel
      Left = 1
      Top = 1
      Width = 712
      Height = 36
      Align = alClient
      Alignment = taCenter
      Caption = 'Gereciador de Clientes'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = 16184821
      Font.Height = -24
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
    end
  end
  object Panel1: TPanel
    Left = 0
    Top = 38
    Width = 714
    Height = 246
    Align = alClient
    ParentBackground = False
    ParentColor = True
    TabOrder = 1
    object LabelNome: TLabel
      Left = 244
      Top = 15
      Width = 31
      Height = 13
      Caption = 'Nome:'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -11
      Font.Name = 'Tahoma'
      Font.Style = []
      ParentFont = False
    end
    object LabelSenioridade: TLabel
      Left = 317
      Top = 64
      Width = 18
      Height = 13
      Caption = 'RG:'
    end
    object LabelCodigo: TLabel
      Left = 178
      Top = 14
      Width = 37
      Height = 13
      Caption = 'C'#243'digo:'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -11
      Font.Name = 'Tahoma'
      Font.Style = []
      ParentFont = False
    end
    object LabelCorUniforme: TLabel
      Left = 293
      Top = 112
      Width = 34
      Height = 13
      Caption = 'E-mail:'
    end
    object LabelDataNascimento: TLabel
      Left = 178
      Top = 66
      Width = 22
      Height = 13
      Caption = 'CPF:'
    end
    object Label1: TLabel
      Left = 178
      Top = 113
      Width = 47
      Height = 13
      Caption = 'Telefone:'
    end
    object Label3: TLabel
      Left = 548
      Top = 130
      Width = 142
      Height = 13
      Caption = 'Enviar Pessoa para o E-mail:'
    end
    object DBGrid1: TDBGrid
      Left = 1
      Top = 1
      Width = 169
      Height = 213
      Align = alLeft
      DataSource = DS_PESSOAS
      Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
      TabOrder = 0
      TitleFont.Charset = DEFAULT_CHARSET
      TitleFont.Color = clWindowText
      TitleFont.Height = -11
      TitleFont.Name = 'Segoe UI'
      TitleFont.Style = []
      Columns = <
        item
          Expanded = False
          FieldName = 'Nome'
          Width = 135
          Visible = True
        end>
    end
    object btnAddPessoa: TButton
      Left = 179
      Top = 177
      Width = 117
      Height = 25
      Caption = 'Cadastrar Cliente'
      TabOrder = 7
      OnClick = btnAddPessoaClick
    end
    object btnAtualizarPessoa: TButton
      Left = 425
      Top = 177
      Width = 117
      Height = 25
      Caption = 'Alterar Cliente'
      TabOrder = 8
      OnClick = btnAtualizarPessoaClick
    end
    object btnDelPessoa: TButton
      Left = 302
      Top = 177
      Width = 117
      Height = 25
      Caption = 'Deletar Cliente'
      TabOrder = 9
      OnClick = btnDelPessoaClick
    end
    object btnEnvioEmail: TButton
      Left = 548
      Top = 177
      Width = 158
      Height = 25
      Caption = 'Enviar Cliente por E-mail'
      TabOrder = 10
      OnClick = btnEnvioEmailClick
    end
    object CampoCPF: TEdit
      Left = 178
      Top = 84
      Width = 131
      Height = 21
      ReadOnly = True
      TabOrder = 3
    end
    object CampoEmail: TEdit
      Left = 290
      Top = 131
      Width = 244
      Height = 21
      ReadOnly = True
      TabOrder = 6
    end
    object CampoID: TEdit
      Left = 178
      Top = 37
      Width = 43
      Height = 21
      ReadOnly = True
      TabOrder = 1
    end
    object CampoIdentidade: TEdit
      Left = 318
      Top = 84
      Width = 213
      Height = 21
      ReadOnly = True
      TabOrder = 4
    end
    object CampoNome: TEdit
      Left = 243
      Top = 36
      Width = 288
      Height = 21
      ReadOnly = True
      TabOrder = 2
    end
    object CampoTelefone: TEdit
      Left = 178
      Top = 131
      Width = 106
      Height = 21
      ReadOnly = True
      TabOrder = 5
    end
    object edtEmailDestino: TEdit
      Left = 548
      Top = 149
      Width = 158
      Height = 21
      TabOrder = 11
    end
    object Panel2: TPanel
      Left = 1
      Top = 214
      Width = 712
      Height = 31
      Align = alBottom
      Color = clGray
      ParentBackground = False
      TabOrder = 12
      object Label2: TLabel
        Left = 1
        Top = 1
        Width = 710
        Height = 29
        Align = alClient
        Alignment = taCenter
        Caption = 'Endere'#231'o:'
        Color = clGray
        Font.Charset = DEFAULT_CHARSET
        Font.Color = 16184821
        Font.Height = -20
        Font.Name = 'Segoe UI'
        Font.Style = []
        ParentColor = False
        ParentFont = False
      end
    end
  end
  object pnlEndereco: TPanel
    Left = 0
    Top = 284
    Width = 714
    Height = 159
    Margins.Left = 0
    Margins.Top = 0
    Margins.Right = 0
    Margins.Bottom = 0
    Align = alBottom
    ParentBackground = False
    ParentColor = True
    TabOrder = 2
    StyleElements = []
    object lblBairro: TLabel
      Left = 537
      Top = 4
      Width = 33
      Height = 13
      Caption = 'Bairro:'
    end
    object lblCEP: TLabel
      Left = 178
      Top = 6
      Width = 22
      Height = 13
      Caption = 'CEP:'
    end
    object lblCidade: TLabel
      Left = 178
      Top = 90
      Width = 39
      Height = 13
      Caption = 'Cidade:'
    end
    object lblComplemento: TLabel
      Left = 305
      Top = 47
      Width = 75
      Height = 13
      Caption = 'Complemento:'
    end
    object lblEstado: TLabel
      Left = 305
      Top = 91
      Width = 38
      Height = 13
      Caption = 'Estado:'
    end
    object lblLogradouro: TLabel
      Left = 305
      Top = 5
      Width = 23
      Height = 13
      Caption = 'Rua:'
    end
    object lblNumero: TLabel
      Left = 178
      Top = 48
      Width = 44
      Height = 13
      Caption = 'N'#250'mero:'
    end
    object lblPais: TLabel
      Left = 360
      Top = 90
      Width = 23
      Height = 13
      Caption = 'Pa'#237's:'
    end
    object CampoBairro: TEdit
      Left = 537
      Top = 21
      Width = 169
      Height = 21
      ReadOnly = True
      TabOrder = 2
    end
    object CampoCidade: TEdit
      Left = 178
      Top = 107
      Width = 121
      Height = 21
      ReadOnly = True
      TabOrder = 5
    end
    object CampoComplemento: TEdit
      Left = 305
      Top = 64
      Width = 225
      Height = 21
      ReadOnly = True
      TabOrder = 4
    end
    object CampoEstado: TEdit
      Left = 305
      Top = 108
      Width = 46
      Height = 21
      ReadOnly = True
      TabOrder = 6
    end
    object CampoLogradouro: TEdit
      Left = 305
      Top = 22
      Width = 225
      Height = 21
      NumbersOnly = True
      ReadOnly = True
      TabOrder = 1
    end
    object CampoNumero: TEdit
      Left = 178
      Top = 67
      Width = 121
      Height = 21
      ReadOnly = True
      TabOrder = 3
    end
    object CampoPais: TEdit
      Left = 360
      Top = 107
      Width = 170
      Height = 21
      ReadOnly = True
      TabOrder = 7
    end
    object CampoCep: TEdit
      Left = 178
      Top = 25
      Width = 121
      Height = 21
      NumbersOnly = True
      ReadOnly = True
      TabOrder = 0
    end
    object dbEnderencos: TDBGrid
      Left = 1
      Top = 1
      Width = 169
      Height = 157
      Align = alLeft
      DataSource = DS_ENDERECOS
      Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
      TabOrder = 8
      TitleFont.Charset = DEFAULT_CHARSET
      TitleFont.Color = clWindowText
      TitleFont.Height = -11
      TitleFont.Name = 'Segoe UI'
      TitleFont.Style = []
      Columns = <
        item
          Expanded = False
          FieldName = 'CEP'
          Width = 135
          Visible = True
        end>
    end
    object btnCadEndereco: TButton
      Left = 548
      Top = 104
      Width = 158
      Height = 25
      Caption = 'Cadastrar Endere'#231'o'
      TabOrder = 9
      OnClick = btnCadEnderecoClick
    end
    object btnAtualizarEndereco: TButton
      Left = 548
      Top = 64
      Width = 158
      Height = 25
      Caption = 'Atualizar Cliente'
      TabOrder = 10
      OnClick = btnAtualizarEnderecoClick
    end
  end
  object DS_PESSOAS: TDataSource
    DataSet = CDS_PESSOAS
    Left = 72
    Top = 128
  end
  object CDS_PESSOAS: TClientDataSet
    PersistDataPacket.Data = {
      330000009619E0BD0100000018000000010000000000030000003300044E6F6D
      6501004900000001000557494454480200020064000000}
    Active = True
    Aggregates = <>
    Params = <>
    AfterScroll = CDS_PESSOASAfterScroll
    Left = 72
    Top = 101
    object CDS_PESSOASNome: TStringField
      FieldName = 'Nome'
      Size = 100
    end
  end
  object DS_ENDERECOS: TDataSource
    DataSet = CDS_ENDERECOS
    Left = 103
    Top = 346
  end
  object CDS_ENDERECOS: TClientDataSet
    Aggregates = <>
    Params = <>
    AfterScroll = CDS_ENDERECOSAfterScroll
    Left = 103
    Top = 319
    object CEP: TStringField
      FieldName = 'CEP'
      Size = 100
    end
  end
end
