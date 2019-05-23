object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 201
  ClientWidth = 447
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 176
    Top = 56
    Width = 31
    Height = 13
    Caption = 'Label1'
  end
  object Memo1: TMemo
    Left = 8
    Top = 88
    Width = 431
    Height = 89
    Lines.Strings = (
      'Memo1')
    TabOrder = 0
  end
  object Button1: TButton
    Left = 96
    Top = 32
    Width = 75
    Height = 25
    Caption = 'Button1'
    TabOrder = 1
    OnClick = Button1Click
  end
  object Edit1: TEdit
    Left = 177
    Top = 34
    Width = 121
    Height = 21
    TabOrder = 2
    Text = 'Edit1'
  end
  object Eventos1: TEventos
    Nome = 'WGCostta'
    Status = Eventos1Status
    Left = 32
    Top = 24
  end
end
