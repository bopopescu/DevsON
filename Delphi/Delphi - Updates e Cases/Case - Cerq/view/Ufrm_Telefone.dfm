object frm_Telefone: Tfrm_Telefone
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu]
  BorderStyle = bsNone
  BorderWidth = 1
  Caption = 'frm_Telefone'
  ClientHeight = 147
  ClientWidth = 274
  Color = 7884599
  Font.Charset = ANSI_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  KeyPreview = True
  OldCreateOrder = False
  Position = poScreenCenter
  OnKeyPress = FormKeyPress
  PixelsPerInch = 96
  TextHeight = 15
  object Panel1: TPanel
    Left = 0
    Top = 124
    Width = 274
    Height = 23
    Align = alBottom
    Color = 7884599
    ParentBackground = False
    TabOrder = 0
  end
  object Panel2: TPanel
    Left = 0
    Top = 0
    Width = 274
    Height = 41
    Align = alTop
    Color = 7884599
    ParentBackground = False
    TabOrder = 1
    object Label3: TLabel
      Left = 70
      Top = 11
      Width = 134
      Height = 17
      Align = alCustom
      Alignment = taCenter
      Caption = 'Cadastro de telefones'
      Font.Charset = ANSI_CHARSET
      Font.Color = clWhite
      Font.Height = -13
      Font.Name = 'Segoe UI'
      Font.Style = [fsBold]
      ParentFont = False
    end
  end
  object Panel3: TPanel
    Left = 0
    Top = 41
    Width = 274
    Height = 83
    Align = alClient
    Color = 15920615
    ParentBackground = False
    TabOrder = 2
    object Label1: TLabel
      Left = 16
      Top = 4
      Width = 27
      Height = 15
      Caption = 'Tipo:'
    end
    object Label2: TLabel
      Left = 136
      Top = 4
      Width = 47
      Height = 15
      Caption = 'N'#250'mero:'
    end
    object EditNumeroTel: TEdit
      Left = 136
      Top = 23
      Width = 121
      Height = 23
      MaxLength = 11
      TabOrder = 1
    end
    object EditTipoTel: TEdit
      Left = 16
      Top = 23
      Width = 99
      Height = 23
      MaxLength = 20
      TabOrder = 0
    end
    object Salvar: TButton
      Left = 24
      Top = 50
      Width = 75
      Height = 25
      Caption = 'Salvar'
      TabOrder = 2
      OnClick = SalvarClick
    end
    object Cancelar: TButton
      Left = 160
      Top = 50
      Width = 75
      Height = 25
      Caption = 'Cancelar'
      TabOrder = 3
      OnClick = CancelarClick
    end
  end
  object DS_Telefone: TDataSource
    DataSet = DM_Dados.CDS_Telefone
    Left = 112
    Top = 102
  end
end
