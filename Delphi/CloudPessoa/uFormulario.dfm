object fFormulario: TfFormulario
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'Exemplo de preenchimento de campos com RTTI'
  ClientHeight = 489
  ClientWidth = 714
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
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
    Height = 46
    Align = alTop
    Color = 7884599
    ParentBackground = False
    TabOrder = 0
    object lblTitulo: TLabel
      Left = 1
      Top = 1
      Width = 712
      Height = 44
      Align = alClient
      Alignment = taCenter
      Caption = 'Cadastro de Pessoas'
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
    Top = 46
    Width = 714
    Height = 246
    Align = alClient
    Color = clWhite
    ParentBackground = False
    TabOrder = 1
    object LabelNome: TLabel
      Left = 311
      Top = 59
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
      Left = 183
      Top = 95
      Width = 60
      Height = 13
      Caption = 'Senioridade:'
    end
    object LabelCodigo: TLabel
      Left = 200
      Top = 59
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
      Left = 343
      Top = 135
      Width = 82
      Height = 13
      Caption = 'Cor do Uniforme:'
    end
    object LabelDataNascimento: TLabel
      Left = 325
      Top = 95
      Width = 100
      Height = 13
      Caption = 'Data de Nascimento:'
    end
    object DBGrid1: TDBGrid
      Left = 8
      Top = 56
      Width = 169
      Height = 197
      DataSource = DS_PESSOAS
      Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
      TabOrder = 0
      TitleFont.Charset = DEFAULT_CHARSET
      TitleFont.Color = clWindowText
      TitleFont.Height = -11
      TitleFont.Name = 'Tahoma'
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
      Left = 584
      Top = 77
      Width = 113
      Height = 25
      Caption = 'Cadastrar Pessoa'
      TabOrder = 1
      OnClick = btnAddPessoaClick
    end
    object btnAtualizarPessoa: TButton
      Left = 583
      Top = 136
      Width = 75
      Height = 25
      Caption = 'Alterar Pessoa'
      TabOrder = 2
      OnClick = btnAtualizarPessoaClick
    end
    object btnDelPessoa: TButton
      Left = 583
      Top = 105
      Width = 75
      Height = 25
      Caption = 'Deletar Pessoa'
      TabOrder = 3
      OnClick = btnDelPessoaClick
    end
    object btnEnvioEmail: TButton
      Left = 590
      Top = 210
      Width = 101
      Height = 25
      Caption = 'Enviar Pessoa por E-mail'
      TabOrder = 4
      OnClick = btnEnvioEmailClick
    end
    object CampoCPF: TEdit
      Left = 431
      Top = 94
      Width = 127
      Height = 21
      ReadOnly = True
      TabOrder = 5
    end
    object CampoEmail: TEdit
      Left = 431
      Top = 132
      Width = 127
      Height = 21
      ReadOnly = True
      TabOrder = 6
    end
    object CampoID: TEdit
      Left = 243
      Top = 56
      Width = 43
      Height = 21
      ReadOnly = True
      TabOrder = 7
    end
    object CampoIdentidade: TEdit
      Left = 243
      Top = 94
      Width = 92
      Height = 21
      ReadOnly = True
      TabOrder = 8
    end
    object CampoNome: TEdit
      Left = 346
      Top = 56
      Width = 251
      Height = 21
      ReadOnly = True
      TabOrder = 9
    end
    object CampoTelefone: TEdit
      Left = 243
      Top = 132
      Width = 92
      Height = 21
      ReadOnly = True
      TabOrder = 10
    end
    object edtEmailDestino: TEdit
      Left = 457
      Top = 214
      Width = 126
      Height = 21
      TabOrder = 11
    end
  end
  object pnlEndereco: TPanel
    Left = 0
    Top = 292
    Width = 714
    Height = 197
    Align = alBottom
    Color = clWhite
    ParentBackground = False
    TabOrder = 2
    object lblBairro: TLabel
      Left = 534
      Top = 6
      Width = 32
      Height = 13
      Caption = 'Bairro:'
    end
    object lblCEP: TLabel
      Left = 198
      Top = 6
      Width = 23
      Height = 13
      Caption = 'CEP:'
    end
    object lblCidade: TLabel
      Left = 198
      Top = 90
      Width = 37
      Height = 13
      Caption = 'Cidade:'
    end
    object lblComplemento: TLabel
      Left = 316
      Top = 48
      Width = 69
      Height = 13
      Caption = 'Complemento:'
    end
    object lblEstado: TLabel
      Left = 336
      Top = 90
      Width = 37
      Height = 13
      Caption = 'Estado:'
    end
    object lblLogradouro: TLabel
      Left = 315
      Top = 6
      Width = 23
      Height = 13
      Caption = 'Rua:'
    end
    object lblNumero: TLabel
      Left = 198
      Top = 48
      Width = 41
      Height = 13
      Caption = 'N'#250'mero:'
    end
    object lblPais: TLabel
      Left = 396
      Top = 90
      Width = 23
      Height = 13
      Caption = 'Pa'#237's:'
    end
    object CampoBairro: TEdit
      Left = 534
      Top = 23
      Width = 121
      Height = 21
      ReadOnly = True
      TabOrder = 2
    end
    object CampoCidade: TEdit
      Left = 198
      Top = 107
      Width = 121
      Height = 21
      ReadOnly = True
      TabOrder = 5
    end
    object CampoComplemento: TEdit
      Left = 316
      Top = 65
      Width = 337
      Height = 21
      TabOrder = 4
    end
    object CampoEstado: TEdit
      Left = 336
      Top = 107
      Width = 46
      Height = 21
      ReadOnly = True
      TabOrder = 6
    end
    object CampoLogradouro: TEdit
      Left = 315
      Top = 23
      Width = 201
      Height = 21
      NumbersOnly = True
      ReadOnly = True
      TabOrder = 1
    end
    object CampoNumero: TEdit
      Left = 198
      Top = 65
      Width = 97
      Height = 21
      TabOrder = 3
    end
    object CampoPais: TEdit
      Left = 396
      Top = 107
      Width = 121
      Height = 21
      ReadOnly = True
      TabOrder = 7
    end
    object edtCep: TEdit
      Left = 193
      Top = 24
      Width = 97
      Height = 21
      NumbersOnly = True
      TabOrder = 0
    end
    object dbEnderencos: TDBGrid
      Left = 9
      Top = 18
      Width = 169
      Height = 174
      DataSource = DS_ENDERECOS
      Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
      TabOrder = 8
      TitleFont.Charset = DEFAULT_CHARSET
      TitleFont.Color = clWindowText
      TitleFont.Height = -11
      TitleFont.Name = 'Tahoma'
      TitleFont.Style = []
      Columns = <
        item
          Expanded = False
          FieldName = 'Nome'
          Title.Caption = 'Rua'
          Width = 135
          Visible = True
        end>
    end
    object btnCadEndereco: TButton
      Left = 468
      Top = 155
      Width = 101
      Height = 25
      Caption = 'Cadastrar Endere'#231'o'
      TabOrder = 9
      OnClick = btnCadEnderecoClick
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
    PersistDataPacket.Data = {
      330000009619E0BD0100000018000000010000000000030000003300044E6F6D
      6501004900000001000557494454480200020064000000}
    Active = True
    Aggregates = <>
    Params = <>
    AfterScroll = CDS_ENDERECOSAfterScroll
    Left = 103
    Top = 319
    object StringField1: TStringField
      FieldName = 'Nome'
      Size = 100
    end
  end
end
