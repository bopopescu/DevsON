object CloudPessoaView: TCloudPessoaView
  Left = 0
  Top = 0
  Caption = 'Cadastrar Cliente'
  ClientHeight = 193
  ClientWidth = 447
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Segoe UI'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object pnlTitulo: TPanel
    Left = 0
    Top = 0
    Width = 447
    Height = 46
    Align = alTop
    Color = 7884599
    ParentBackground = False
    TabOrder = 0
    object lblTitulo: TLabel
      Left = 1
      Top = 1
      Width = 445
      Height = 44
      Align = alClient
      Alignment = taCenter
      Caption = 'Cadastrar Endere'#231'o'
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
    Width = 447
    Height = 147
    Align = alClient
    Color = clWhite
    ParentBackground = False
    TabOrder = 1
    object Label1: TLabel
      Left = 11
      Top = 9
      Width = 33
      Height = 13
      Caption = 'Nome:'
    end
    object lblCPF: TLabel
      Left = 191
      Top = 9
      Width = 22
      Height = 13
      Caption = 'CPF:'
    end
    object lblEmail: TLabel
      Left = 190
      Top = 51
      Width = 34
      Height = 13
      Caption = 'E-mail:'
    end
    object lblRG: TLabel
      Left = 318
      Top = 9
      Width = 18
      Height = 13
      Caption = 'RG:'
    end
    object lblTelefone: TLabel
      Left = 11
      Top = 51
      Width = 47
      Height = 13
      Caption = 'Telefone:'
    end
    object btnCancelar: TButton
      Left = 365
      Top = 102
      Width = 75
      Height = 25
      Caption = 'Cancelar'
      TabOrder = 6
      OnClick = btnCancelarClick
    end
    object btnConfirmar: TButton
      Left = 284
      Top = 102
      Width = 75
      Height = 25
      Caption = 'Confirmar'
      TabOrder = 5
      OnClick = btnConfirmarClick
    end
    object edtEmail: TEdit
      Left = 190
      Top = 71
      Width = 247
      Height = 21
      TabOrder = 4
      OnExit = edtEmailExit
      OnKeyDown = edtEmailKeyDown
    end
    object edtNome: TEdit
      Left = 11
      Top = 26
      Width = 170
      Height = 21
      TabOrder = 0
      OnKeyDown = edtNomeKeyDown
    end
    object edtRG: TEdit
      Left = 318
      Top = 26
      Width = 121
      Height = 21
      NumbersOnly = True
      TabOrder = 2
      OnKeyDown = edtRGKeyDown
    end
    object edtCPF: TMaskEdit
      Left = 191
      Top = 26
      Width = 120
      Height = 21
      EditMask = '999.999.999-99;1;_'
      MaxLength = 14
      TabOrder = 1
      Text = '   .   .   -  '
      OnKeyDown = edtCPFKeyDown
    end
    object edtTelefone: TMaskEdit
      Left = 11
      Top = 71
      Width = 119
      Height = 21
      EditMask = '!\(99\)00000-0000;1;_'
      MaxLength = 14
      TabOrder = 3
      Text = '(  )     -    '
      OnKeyDown = edtTelefoneKeyDown
    end
  end
end
