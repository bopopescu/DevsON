object sqlForDelphi: TsqlForDelphi
  Left = 0
  Top = 0
  Caption = 'VSMConversorUtils 2.0'
  ClientHeight = 599
  ClientWidth = 1196
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  OldCreateOrder = False
  OnClose = FormClose
  OnCreate = FormCreate
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 15
  object Panel2: TPanel
    Left = 0
    Top = 0
    Width = 1196
    Height = 599
    Align = alClient
    Color = clWhite
    ParentBackground = False
    TabOrder = 0
    object Label2: TLabel
      Left = 12
      Top = 552
      Width = 55
      Height = 15
      Caption = 'Resultado:'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -12
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
    end
    object lblArquivo: TLabel
      Left = 69
      Top = 553
      Width = 9
      Height = 15
      Caption = '...'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clHotLight
      Font.Height = -12
      Font.Name = 'Segoe UI'
      Font.Style = [fsBold]
      ParentFont = False
    end
    object btnClear: TVSMColorButton
      Left = 884
      Top = 552
      Width = 150
      Height = 40
      Cursor = crHandPoint
      Action = ACT_CLEAR
      Color = 2359519
      Font.Charset = ANSI_CHARSET
      Font.Color = clWhite
      Font.Height = -15
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
      TabOrder = 1
      BorderColor = 2359519
      Caption = 'Limpar [DEL]'
      Glyph.Data = {
        89504E470D0A1A0A0000000D4948445200000018000000180806000000E0773D
        F8000000097048597300000EC400000EC401952B0E1B000001544944415478DA
        B594CD4A43311085D36AADB8D37DA5605DF92C0AFE3DA3B4AE5DD49F853E822F
        E142504114AFD0C6933623619C939B501C389B7B93F94ECECDDC8EF7DEFD6775
        08A00BCD2B7B997B2C401FBA804E2A0157D039F499036C4263E830BA592F6CFE
        0DF5A0EB68ECC30204E793D87CF10E9A15409AD83CAC0FCD6EA06339490AB884
        CE8C06398838D735858EC27B1D51936C10478EC425CDBDB1BECBBE41A82F6843
        6DD071E958644D30B2963663D7B489102BAE3989C5A7CEDB002CAED4318DA514
        60C56501FEC4520348E3B200D4790D805D45D7E6BE04A06F8B1551761873809C
        735D14C200B9219A25B1B40DA3092819A2926134012C166B8872C3F80B11C016
        F408EDB9967F0B39AD5EFF061D404FE90946D01D3420B1B0D271BDBBE52FFFC1
        8A681FBA8576492CAC242E697ECFBE819C24408685CDA59EA153719E0384DA81
        5E2A01DBD0AB7E58F2AB58A97E006E64A6D19B152ADE0000000049454E44AE42
        6082}
      GlyphMargin = 8
      PressedBorderColor = 2359519
      PressedColor = clMaroon
      PressedFontColor = clWhite
      SelectedBorderColor = 2359519
      SelectedColor = 2359519
      SelectedFontColor = clWhite
      BadgeProperties.Color = 2359519
      BadgeProperties.Top = True
      BadgeProperties.Right = True
      BadgeProperties.FontSize = 11
      BadgeProperties.FontColor = 16184821
      BadgeProperties.FontFamily = 'Segoe UI'
      BadgeProperties.FontStyle = 1
    end
    object btnCopy: TVSMColorButton
      Left = 1040
      Top = 552
      Width = 150
      Height = 40
      Cursor = crHandPoint
      Action = ACT_COPY
      Color = 4178176
      Font.Charset = ANSI_CHARSET
      Font.Color = clWhite
      Font.Height = -15
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
      TabOrder = 0
      BorderColor = 4178176
      Caption = 'Copiar [Ctrl+C]'
      Glyph.Data = {
        89504E470D0A1A0A0000000D4948445200000018000000180806000000E0773D
        F8000000097048597300000EC400000EC401952B0E1B000000CB4944415478DA
        ED94C90EC2300C441B02A22CFFFFA52C17A8B1A5B8B2825D3B283D80B034EAA2
        649E3D5D12000C6B56FA037E0E70419DD702DC506339DFF40650E727149BA5A2
        6D0F009BCB9A50B9C70477D45E740D45D98A882E9E345AC0FC8A3A56B1BCED95
        0010C7C98190F94174CDFB72BD9000A918D6654D42B18CD5BD39730DA04DC023
        3F503BA5F341AC598C547B06D6249C79A8730BC010A8F24DCA3DF0CC2D801597
        04782F810BB0E29AF745CC3D801617FF02C215F992E58226F3288021CDE62D80
        8FEBFB012F793779D5FCFAEC970000000049454E44AE426082}
      GlyphMargin = 8
      PressedBorderColor = 4178176
      PressedColor = clGreen
      PressedFontColor = 4178176
      SelectedColor = 4178176
      SelectedFontColor = clWhite
      BadgeProperties.Color = 2359519
      BadgeProperties.Top = True
      BadgeProperties.Right = True
      BadgeProperties.FontSize = 11
      BadgeProperties.FontColor = 16184821
      BadgeProperties.FontFamily = 'Segoe UI'
      BadgeProperties.FontStyle = 1
    end
    object Panel4: TPanel
      Left = 5
      Top = 330
      Width = 1184
      Height = 218
      Caption = 'Panel4'
      TabOrder = 2
      object MemoResultado: TRzMemo
        Left = 1
        Top = 1
        Width = 1182
        Height = 216
        Align = alClient
        Enabled = False
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clTeal
        Font.Height = -12
        Font.Name = 'Segoe UI'
        Font.Style = []
        ParentFont = False
        TabOrder = 0
        FrameColor = clWhite
      end
    end
    object pgSQLDelphi: TPageControl
      Left = 1
      Top = 1
      Width = 1194
      Height = 312
      ActivePage = TabSheet1
      Align = alTop
      Style = tsFlatButtons
      TabOrder = 3
      object TabSheet1: TTabSheet
        Caption = 'Conversor SQL e Delphi'
        object Panel1: TPanel
          Left = 0
          Top = 0
          Width = 1186
          Height = 279
          Align = alClient
          Color = clWhite
          ParentBackground = False
          TabOrder = 0
          object Label1: TLabel
            Left = 10
            Top = 236
            Width = 169
            Height = 30
            Caption = 'Necess'#225'rio trocar os Par'#226'metros'#13#10' do Delphi para execu'#231#227'o'
          end
          object Label3: TLabel
            Left = 9
            Top = 2
            Width = 73
            Height = 15
            Caption = 'Texto Original'
          end
          object MemoSQL: TRzMemo
            Left = 5
            Top = 17
            Width = 1176
            Height = 214
            Color = clWhite
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -12
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
            TabOrder = 0
          end
          object btnSQL: TVSMColorButton
            Left = 1030
            Top = 236
            Width = 150
            Height = 40
            Cursor = crHandPoint
            Action = ACT_SQLDELPHI
            Color = 7884599
            Font.Charset = ANSI_CHARSET
            Font.Color = clWhite
            Font.Height = -15
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
            TabOrder = 7
            BorderColor = 7884599
            Caption = 'SQL p/ Delphi'
            Glyph.Data = {
              89504E470D0A1A0A0000000D4948445200000018000000180803000000D7A9CD
              CA0000000373424954080808DBE14FE00000000970485973000000A6000000A6
              01DD7DFF380000001974455874536F667477617265007777772E696E6B736361
              70652E6F72679BEE3C1A00000183504C5445FFFFFF00FFFF8080FF66CCCC6DB6
              DB66B3E670AFDF78B4E175B5DF6DB6E44F95CA6FB3DD73B5DE70B7DF64A2D16F
              B7DE60A6D270B4E06EB4E24A99C671B5E372B3DE4C97C671B3DE72B6DF72B4E0
              71B3DE71B5DF70B4E071B5E170B5DF71B5E05EA4D371B4DF5BA4D04D98C671B4
              E071B4DF4D97C771B4E071B4E072B4E071B4E072B3E070B4E14D98C671B4E071
              B3E071B5DF72B4E171B5E14C98C671B4DF4D98C658A1CF71B4E071B4E071B4E0
              56A0CE57A0CE71B4E0579FCD71B4E04B98C671B4E071B5E1559FCC71B4E056A0
              CE549ECC71B4E070B2E071B4E0549ECC71B4E05FA6D3539ECC71B4E0519DCA68
              ADD971B4E04C98C6529CCA71B4E0519BC9519CC9529CCA71B4E0509BC9519CCA
              71B4E171B4E0539DCB569FCD64AAD771B4E071B4E04C98C64D98C64D99C74E9A
              C84F9AC8509BC9519CC9529CCA5768745AA2D05D7B8F5EA6D35FA6D35FA7D461
              A8D567ACD967ADD968ADD968ADDA699EC169AEDB6AAFDB6BA2C66CB0DC6CB0DD
              6CB1DD6DB1DD6EB2DE6FAFD970B0DB70B3DF71B4E0A53CE75B0000006174524E
              5300010205070A1011181C1D1E1F20212728292C2D2D2F3636383A46484B5659
              5A5C5F627E85888C8C8E9293949899A3A5B2B8B9BDC2C8C9CCCDD0D5D5DBDDDD
              DFE1E2E7E7E8EAEAEBEBECEDEEEFF1F2F3F4F5F7F8FAFAFAFAFBFBFBFCFDFDFD
              FDFEEF7EF984000001694944415478DA75D14B4B02511407F0FFCC389AA38EA3
              8EA2508956E2B62024249270DDA24DB669DD27893E45BB1611684411B4102128
              8B2C13C2452F2531DCD8432775526B9EE6A2CEE2DEB9E737E79E330C014C70D6
              CF76D5E67119A78BE58FC7369420004F9403591E27ED36397151A8E88050145F
              34E962D4577369410766A56B80858716A91B1DB0E4EE1BBD840E99CC00A221B0
              0E35DBA37AD486A8C3FC2438BB0A35B6E9DE6CEBB06C87D7A44293E998B71AAF
              1A24CCE4188663F7F61FC81DF635185CA5C64E51ABB0302C2D3FE4EFDFBEA5AD
              55D77AACFA58E9138152EA7D50A4C05A503DEC5F291BEDACA9E05D9716D108EC
              E5E57C60A67AA6423801081D27F0946C00FE58E0E0520122E6F3882D8A1F01B2
              0F021399C2F69D0206477DC12FDDECA6B5BEE9ACA8350717977E92899727C349
              A5D4D1A702D8C8A8546AE2643A2D3EFF0210F43ACD545FE8CE49331CBF0C811E
              7C388E64E10F807976F1E8FC2F8035485D033F9CF16019326BF6550000000049
              454E44AE426082}
            GlyphMargin = 8
            PressedBorderColor = clWhite
            PressedFontColor = 7884599
            SelectedColor = 7884599
            SelectedFontColor = clWhite
            BadgeProperties.Color = 2359519
            BadgeProperties.Top = True
            BadgeProperties.Right = True
            BadgeProperties.FontSize = 11
            BadgeProperties.FontColor = 16184821
            BadgeProperties.FontFamily = 'Segoe UI'
            BadgeProperties.FontStyle = 1
          end
          object btnDelphi: TVSMColorButton
            Left = 873
            Top = 236
            Width = 150
            Height = 40
            Cursor = crHandPoint
            Action = ACT_DELPHISQL
            Color = clWhite
            Font.Charset = ANSI_CHARSET
            Font.Color = 2359519
            Font.Height = -15
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
            TabOrder = 6
            BorderColor = clWhite
            Caption = 'Delphi->SQL  '
            Glyph.Data = {
              89504E470D0A1A0A0000000D4948445200000020000000200806000000737A7A
              F4000000017352474201D9C92C7F000007ED4944415478DA9D575B7013E715FE
              7625AD245F7441C6C618631BE3C1C40103BE20436B2681929A24B46E6C4A3349
              A77D48F3047D485F12D24932036FED24A54F8569D3994293D6212509898170E9
              745A626C0B4AB00DB8C6E08BF0154BB27559ED45DBF3AF2C23E4C898FC339A95
              F4EFEEF9CE77BE73F9393CC66AA9AEB61A787E996030D8E96AE1394E60FFC734
              4D5263315152D5005D479B3B3B238B7D27B708A364872B321B0C5566A3B1CEC8
              F3D5EC373DE8A0EDACD9DB821AE0D7346D4089C53AA38AF25554553D3160604F
              4747EC5B0368D9B489174CA606AB20FCC8C871B5647C8DD16030A57B88404051
              559940DC5234AD3D22491F1390D63D9D9D6941A405409E3BC8E3FD768BE51764
              389F68E01F275C14961801190988E21162E43085C5BF28001FD5D40844F70E32
              FECB0C41D8614831CCF1F4938FFF9551520283D53AB717191A221A3498962C81
              120840F6FBA1284A2C2C49E74445F91D69E45C534787B420804FDDEE5D5982F0
              1B0250CE82FFE04E0EE6BC3C38AAAB111D1B83343E8ED56FBC016B71B1BECDFE
              BBF3EEBB703DF5146CEBD723323888E0CD9B085CBD8A607F3FC2C1E08D9024FD
              6A775BDB17690130DA89F2BF91E7DF33241937399DC8AEA880A3B616B6CA4A8C
              9E3CA90328DEB74FDF8B4912EE9F3F0F7F672756BDF61A0C9999FA736A2402DF
              A54BF01E3F8ED0D090464C7C4921F9717238E68C30C19905E1CD2519196FA5D2
              6E5BB70ECB5F7C11F68D1B2113B583478EC0525080E57BF782331810E8E8C0E4
              C58BC8DDB50BD9746F62A9E130EEBCF71EFCEDEDFA77957431150EBF23C9F2C1
              268F27360780A51AE57683C36AFD035D0B923DCFDBBD1BC19E1EE43EF71C9C6E
              B71EE7F153A7E0DCB24567233A3AAA3392B5762D5CDBB6E9A18A91E7A1BE3E0C
              1E3DAA872179910EBCFE48E45599B2A389B2839B155E89CD6239906932FD3CA1
              7616EF82975ED2E3E93D760C36F23E67FB76847A7B11F07890FBECB330DA6C98
              387D1A868C0C38081C6F3643999ED6013246980E982853B383B4F0FE74347A88
              04794707F099DBDD9429086F594DA62713373AEBEA50B27F3F38A311DE0F3ED0
              29CF23A3E2D71E447BBB61AF5C074E8BC177E51AB26ADC3016AE82C61B3172E2
              04C60880343191364523B2DC1594A477C499998F38565E4978072D46E33E1315
              9944AA598B8A74955B56ACC0484B0B782982FCCA5268B20CCD9E032E9B0A21C5
              5F0BCD800FFAE8AD414CF50DE3F6879FE8E25B6811FD32A5E5EF49906F721FD7
              D696382C963F5B4CA67A46071355DEF3CFC3E47040154514FEF46528D7DB8149
              2F8C65158025131C19D34C6620B710102CF1B74623E0FAFE8BB14F4ED2735148
              2111633D77A1A9F38B200B8A28CBFFF28BE2CFB85375751B88FE93C4405122F6
              2C95589161E9B3CCBD0116A30A642FD10B90E6CCA3EF4E5D6C0F07970C4D0C83
              EBB9AC839A68BF82810BED50A2F237B2400C0C90167EC8B56EDDEAB61A8DA7A9
              F0D8D986B5B010AB5F7F1D19A5A598E9EE86E9B607D68A0D71BA9971C7D2F96F
              23EF1943DCE43DC095AF0BCF77F60BF47F761E7238FA8D00A83C07228AF27DEE
              CCD6ADF564FC027D0C6C83B758E0DCBC19B90D0DB0AD5C06F4778173D1553043
              5B51C604F2F09BA6EF13F5D7286729242BD7C401DE1FC1CC85565D0FE274381D
              00951AD5D3F30064969521BFA90933D7AFC39523C0B6A59E5A9C046D792915FF
              ECD9206A71AF47EF8223DA51460C3176126109FA21B65D44EFD1BF207C7F7A61
              00A9216005A5FCD021BDBC72975B61DCF41D70FE4968651BE34D4855E286A7C6
              E2025C45996B7ED090208600DA536F5EC58D3F7E88E0986FE110A48A50C8C941
              7E632332D7AC41D6C44D70EBB790975E68E5357100A100B85B1E1222A5617145
              1C04650542E4E9CC14E4512FC48141448687E0FDEA1AA269424022BC4B226C9C
              978646BB1DB9CF3CA303B1CBE3B07C7727B8F16168AB2BE32108CFE8E9A67F37
              0AD0880DF1DE08C223E398BEEB4588AEB2284125F52B9232AF12CE4BC3D442C4
              994CC87FE1052CDDB913FCE00D98735CE419D1E8CC85565201BD7D786F83FBDF
              15800A52A8A71B77CEFC5B8F754C51B198355B880E5321FAB5AE1A9A019AB292
              4AB1EE3DD57EC793E570B968EEB4510D8884A0ADADD10B115B1C798EC9116839
              CB11FECF79F8AE5EC758575FDAB44B5EB3A5F86D9A0D4E3C684666F301D242BC
              19919AB39F78022B5F7905C27017CCA56BE92E4A123FC5738AD850C95395061B
              2D006D7B23A5E21494DEAF71EFF33318B9726B41E37A3392E5F7A745F141336A
              A9A9E1059E7FA81DF382A04F3B822661657D35AC3162C2470D46A4F463C20A12
              0017B1B1A7195AE97A9D21F5522BBA8FFC15115F302D004A3D6F20B51DB3F5F7
              AA2A9E8478800692B79307123618152C75219FB46060653DB9B6F31CB49DB5C0
              D33FA00262D7B5E2FBD361DC3E7B19341BCF339E184828050F36CF4ECA8F1CC9
              046AC7F9349810332C7749D41A683407091619D4FFA3852ED87EB2375E0F7803
              E47F7E8AFE632DF00F8EA51A5F78244B2C12640309F2B764B89C8160C6081053
              2EA2AC15B354A57A6022600C809A25A0F8E5660835DBF4DAA0B69DC5C0F1164C
              F40E251B67E01F3D94CE0A72C1B13C751904238AEAAB90BB63BBFEB6D1D633F0
              B677CD6503A33D319653FCCF353F6A2C4F0E0781D8472179F5510793AC3C27EC
              05399819F561FADEE49CDABFD5C124793161120876346BA4A3D9E6C73C9A5DA6
              A3D93F126A4F6763D18753126115554B379D8A6BF8850FA71D44771B4DBF1EF6
              BB7901E38B029002E6E1E33925894E379BB613C773551D6DF678167D3CFF3F13
              30175F6621A9E10000000049454E44AE426082}
            GlyphMargin = 8
            PressedBorderColor = 2359519
            PressedColor = 2359519
            PressedFontColor = clWhite
            SelectedBorderColor = 2359519
            SelectedColor = clWhite
            SelectedFontColor = 2359519
            DisableColor = 2359519
            BadgeNumber = 2
            Style = cbsRed
            BadgeProperties.Color = clLime
            BadgeProperties.Top = False
            BadgeProperties.Right = True
            BadgeProperties.FontSize = 11
            BadgeProperties.FontColor = 16184821
            BadgeProperties.FontFamily = 'Segoe UI'
            BadgeProperties.FontStyle = 1
          end
          object chkFullScrean: TCheckBox
            Left = 637
            Top = 259
            Width = 97
            Height = 17
            Caption = 'FullScreen'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -12
            Font.Name = 'Segoe UI'
            Font.Style = [fsBold]
            ParentFont = False
            TabOrder = 3
            OnClick = chkFullScreanClick
          end
          object chkRemoverX: TRzCheckBox
            Left = 238
            Top = 236
            Width = 353
            Height = 28
            Caption = 
              'REMOVER: "+" (Em caso de  pegar a SQL do Executor, '#13'pode desmarc' +
              'ar a op'#231#227'o pois j'#225' ter'#225' removido os + pelo Debug)'
            Color = clWhite
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clGreen
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = [fsBold]
            ParentColor = False
            ParentFont = False
            State = cbUnchecked
            TabOrder = 1
          end
          object chkGerarArquivo: TCheckBox
            Left = 772
            Top = 259
            Width = 97
            Height = 17
            Caption = 'Gerar Arquivo'
            Checked = True
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -12
            Font.Name = 'Segoe UI'
            Font.Style = [fsBold]
            ParentFont = False
            State = cbChecked
            TabOrder = 5
          end
          object chkUpper: TCheckBox
            Left = 772
            Top = 236
            Width = 97
            Height = 17
            Caption = 'Case Sensitive'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -12
            Font.Name = 'Segoe UI'
            Font.Style = [fsBold]
            ParentFont = False
            TabOrder = 4
          end
          object chkFormatarSQL: TCheckBox
            Left = 637
            Top = 236
            Width = 133
            Height = 17
            Caption = 'Formatar SQL (Beta)'
            Checked = True
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clRed
            Font.Height = -12
            Font.Name = 'Segoe UI'
            Font.Style = [fsBold]
            ParentFont = False
            State = cbChecked
            TabOrder = 2
            OnClick = chkFullScreanClick
          end
        end
      end
      object TabSheet2: TTabSheet
        Caption = 'Gerador de Templates'
        ImageIndex = 1
        object Panel3: TPanel
          Left = 0
          Top = 0
          Width = 1186
          Height = 279
          Align = alClient
          Caption = 'Panel3'
          Color = clWhite
          ParentBackground = False
          TabOrder = 0
          object Label4: TLabel
            Left = 6
            Top = 6
            Width = 99
            Height = 13
            Caption = 'Nome do Template:'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
          end
          object Label5: TLabel
            Left = 8
            Top = 29
            Width = 52
            Height = 13
            Caption = 'Descri'#231#227'o:'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
          end
          object Label6: TLabel
            Left = 6
            Top = 53
            Width = 78
            Height = 13
            Caption = 'C'#243'digo Delphi:'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
          end
          object Label7: TLabel
            Left = 5
            Top = 178
            Width = 440
            Height = 52
            Caption = 
              'Os nomes ou variaveis que deseja que seja subsituido ao Inserir,' +
              ' colocar no c'#243'digo'#13#10' como |classname|, exemplo: class MyClass, c' +
              'olocar class |classname|.'#13#10'Salvar o conte'#250'do do resultado com o ' +
              'nome gerado e .xml, na pasta:'#13#10'C:\Program Files (x86)\Embarcader' +
              'o\Studio\18.0\ObjRepos\en\Code_Templates\Delphi'
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
          end
          object edtDescricaoTemplate: TRzEdit
            Left = 144
            Top = 28
            Width = 295
            Height = 21
            Text = ''
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            MaxLength = 70
            ParentFont = False
            TabOrder = 1
          end
          object edtNomeTemplate: TRzEdit
            Left = 143
            Top = 2
            Width = 121
            Height = 21
            Text = ''
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            MaxLength = 20
            ParentFont = False
            TabOrder = 0
          end
          object memoCodigoTemplate: TRzMemo
            Left = 3
            Top = 72
            Width = 960
            Height = 96
            Font.Charset = DEFAULT_CHARSET
            Font.Color = clWindowText
            Font.Height = -11
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
            TabOrder = 2
          end
          object VSMColorButton2: TVSMColorButton
            Left = 812
            Top = 235
            Width = 150
            Height = 40
            Cursor = crHandPoint
            Action = ACT_TEMPLATE
            Color = 15963681
            Font.Charset = ANSI_CHARSET
            Font.Color = clWhite
            Font.Height = -15
            Font.Name = 'Segoe UI'
            Font.Style = []
            ParentFont = False
            TabOrder = 3
            BorderColor = 15963681
            Caption = 'Template'
            Glyph.Data = {
              89504E470D0A1A0A0000000D4948445200000018000000180806000000E0773D
              F8000000097048597300000EC400000EC401952B0E1B000000CB4944415478DA
              ED94C90EC2300C441B02A22CFFFFA52C17A8B1A5B8B2825D3B283D80B034EAA2
              649E3D5D12000C6B56FA037E0E70419DD702DC506339DFF40650E727149BA5A2
              6D0F009BCB9A50B9C70477D45E740D45D98A882E9E345AC0FC8A3A56B1BCED95
              0010C7C98190F94174CDFB72BD9000A918D6654D42B18CD5BD39730DA04DC023
              3F503BA5F341AC598C547B06D6249C79A8730BC010A8F24DCA3DF0CC2D801597
              04782F810BB0E29AF745CC3D801617FF02C215F992E58226F3288021CDE62D80
              8FEBFB012F793779D5FCFAEC970000000049454E44AE426082}
            GlyphMargin = 8
            PressedBorderColor = 14581772
            PressedColor = 13136651
            PressedFontColor = 14581772
            SelectedColor = 14581772
            SelectedFontColor = clWhite
            BadgeProperties.Color = 2359519
            BadgeProperties.Top = True
            BadgeProperties.Right = True
            BadgeProperties.FontSize = 11
            BadgeProperties.FontColor = 16184821
            BadgeProperties.FontFamily = 'Segoe UI'
            BadgeProperties.FontStyle = 1
          end
        end
      end
    end
  end
  object ActionList1: TActionList
    Left = 277
    Top = 65523
    object ACT_CLEAR: TAction
      Caption = 'ACT_CLEAR'
      ShortCut = 46
      OnExecute = ACT_CLEARExecute
    end
    object ACT_COPY: TAction
      Caption = 'ACT_COPY'
      ShortCut = 16451
      OnExecute = ACT_COPYExecute
    end
    object ACT_DELPHISQL: TAction
      Caption = 'ACT_DELPHISQL'
      OnExecute = ACT_DELPHISQLExecute
    end
    object ACT_SQLDELPHI: TAction
      Caption = 'ACT_SQLDELPHI'
      OnExecute = ACT_SQLDELPHIExecute
    end
    object ACT_TEMPLATE: TAction
      Caption = 'ACT_TEMPLATE'
      OnExecute = ACT_TEMPLATEExecute
    end
  end
end
