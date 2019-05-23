object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 418
  ClientWidth = 456
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Button1: TButton
    Left = 144
    Top = 80
    Width = 75
    Height = 25
    Caption = 'Button1'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Edit1: TEdit
    Left = 144
    Top = 120
    Width = 121
    Height = 21
    TabOrder = 1
  end
  object MaskEdit1: TMaskEdit
    Left = 32
    Top = 208
    Width = 271
    Height = 25
    EditMask = '!\(999\)000-0000;1;_'
    MaxLength = 13
    TabOrder = 2
    Text = '(   )   -    '
  end
  object MaskEdit2: TMaskEdit
    Left = 168
    Top = 323
    Width = 120
    Height = 21
    EditMask = '###.###.###-##'
    MaxLength = 14
    TabOrder = 3
    Text = '   .   .   -  '
  end
  object Button2: TButton
    Left = 296
    Top = 272
    Width = 75
    Height = 25
    Caption = 'Button2'
    TabOrder = 4
  end
  object MaskEdit3: TMaskEdit
    Left = 32
    Top = 323
    Width = 120
    Height = 21
    EditMask = '999.999.999-99'
    MaxLength = 14
    TabOrder = 5
    Text = '   .   .   -  '
  end
  object RadioButton1: TRadioButton
    Left = 32
    Top = 300
    Width = 113
    Height = 17
    Caption = 'CPF'
    TabOrder = 6
  end
  object RadioButton2: TRadioButton
    Left = 168
    Top = 296
    Width = 113
    Height = 17
    Caption = 'CNPJ'
    TabOrder = 7
  end
end
