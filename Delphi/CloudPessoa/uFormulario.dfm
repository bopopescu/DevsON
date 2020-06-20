object fFormulario: TfFormulario
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'Exemplo de preenchimento de campos com RTTI'
  ClientHeight = 456
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
  object LabelCodigo: TLabel
    Left = 200
    Top = 30
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
  object LabelNome: TLabel
    Left = 311
    Top = 30
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
    Top = 66
    Width = 60
    Height = 13
    Caption = 'Senioridade:'
  end
  object LabelDataNascimento: TLabel
    Left = 325
    Top = 66
    Width = 100
    Height = 13
    Caption = 'Data de Nascimento:'
  end
  object LabelCorUniforme: TLabel
    Left = 343
    Top = 106
    Width = 82
    Height = 13
    Caption = 'Cor do Uniforme:'
  end
  object CampoID: TEdit
    Left = 243
    Top = 27
    Width = 43
    Height = 21
    ReadOnly = True
    TabOrder = 0
  end
  object CampoNome: TEdit
    Left = 367
    Top = 27
    Width = 302
    Height = 21
    ReadOnly = True
    TabOrder = 1
  end
  object DBGrid1: TDBGrid
    Left = 8
    Top = 27
    Width = 169
    Height = 197
    DataSource = DataSource
    Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
    TabOrder = 2
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
  object DBGrid2: TDBGrid
    Left = 8
    Top = 240
    Width = 361
    Height = 197
    DataSource = DataSource
    Options = [dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete, dgCancelOnExit, dgTitleClick, dgTitleHotTrack]
    TabOrder = 3
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
    Top = 199
    Width = 113
    Height = 25
    Caption = 'Cadastrar Pessoa'
    TabOrder = 4
    OnClick = btnAddPessoaClick
  end
  object CampoIdentidade: TEdit
    Left = 243
    Top = 65
    Width = 92
    Height = 21
    ReadOnly = True
    TabOrder = 5
  end
  object CampoCPF: TEdit
    Left = 431
    Top = 65
    Width = 127
    Height = 21
    ReadOnly = True
    TabOrder = 6
  end
  object CampoTelefone: TEdit
    Left = 243
    Top = 103
    Width = 92
    Height = 21
    ReadOnly = True
    TabOrder = 7
  end
  object CampoEmail: TEdit
    Left = 431
    Top = 103
    Width = 127
    Height = 21
    ReadOnly = True
    TabOrder = 8
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
    Top = 72
    object ClientDataSetNome: TStringField
      FieldName = 'Nome'
      Size = 100
    end
  end
end