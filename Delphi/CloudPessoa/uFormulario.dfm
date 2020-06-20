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
    Height = 443
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
    object DBGrid2: TDBGrid
      Left = 8
      Top = 269
      Width = 169
      Height = 123
      DataSource = DataSource
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
    object DBGrid1: TDBGrid
      Left = 8
      Top = 56
      Width = 169
      Height = 197
      DataSource = DataSource
      Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
      TabOrder = 1
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
      Left = 222
      Top = 228
      Width = 113
      Height = 25
      Caption = 'Cadastrar Pessoa'
      TabOrder = 2
      OnClick = btnAddPessoaClick
    end
    object btnAtualizarPessoa: TButton
      Left = 458
      Top = 229
      Width = 75
      Height = 25
      Caption = 'Alterar Pessoa'
      TabOrder = 3
      OnClick = btnAtualizarPessoaClick
    end
    object btnCadEndereco: TButton
      Left = 493
      Top = 376
      Width = 101
      Height = 25
      Caption = 'Cadastrar Endere'#231'o'
      TabOrder = 4
      OnClick = btnCadEnderecoClick
    end
    object btnDelPessoa: TButton
      Left = 367
      Top = 227
      Width = 75
      Height = 25
      Caption = 'Deletar Pessoa'
      TabOrder = 5
      OnClick = btnDelPessoaClick
    end
    object btnEnvioEmail: TButton
      Left = 605
      Top = 418
      Width = 101
      Height = 25
      Caption = 'Enviar Pessoa por E-mail'
      TabOrder = 6
      OnClick = btnEnvioEmailClick
    end
    object CampoCPF: TEdit
      Left = 431
      Top = 94
      Width = 127
      Height = 21
      ReadOnly = True
      TabOrder = 7
    end
    object CampoEmail: TEdit
      Left = 431
      Top = 132
      Width = 127
      Height = 21
      ReadOnly = True
      TabOrder = 8
    end
    object CampoID: TEdit
      Left = 243
      Top = 56
      Width = 43
      Height = 21
      ReadOnly = True
      TabOrder = 9
    end
    object CampoIdentidade: TEdit
      Left = 243
      Top = 94
      Width = 92
      Height = 21
      ReadOnly = True
      TabOrder = 10
    end
    object CampoNome: TEdit
      Left = 367
      Top = 56
      Width = 302
      Height = 21
      ReadOnly = True
      TabOrder = 11
    end
    object CampoTelefone: TEdit
      Left = 243
      Top = 132
      Width = 92
      Height = 21
      ReadOnly = True
      TabOrder = 12
    end
    object edtEmailDestino: TEdit
      Left = 472
      Top = 422
      Width = 126
      Height = 21
      TabOrder = 13
    end
  end
  object DataSource: TDataSource
    DataSet = ClientDataSet
    Left = 72
    Top = 128
  end
  object ClientDataSet: TClientDataSet
    PersistDataPacket.Data = {
      330000009619E0BD0100000018000000010000000000030000003300044E6F6D
      6501004900000001000557494454480200020064000000}
    Active = True
    Aggregates = <>
    Params = <>
    AfterScroll = ClientDataSetAfterScroll
    Left = 72
    Top = 101
    object ClientDataSetNome: TStringField
      FieldName = 'Nome'
      Size = 100
    end
  end
end
