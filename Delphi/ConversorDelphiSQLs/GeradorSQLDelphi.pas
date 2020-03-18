unit GeradorSQLDelphi;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, RzEdit, Vcl.ExtCtrls, Vcl.ComCtrls, RzLabel, Vcl.Mask, System.Actions,
  Vcl.ActnList, VSMColorButton, Easysize, System.Generics.Collections, RzButton, RzRadChk;


type
  TsqlForDelphi = class(TForm)
    MemoSQL: TRzMemo;
    MemoResultado: TRzMemo;
    Label1: TLabel;
    Panel1: TPanel;
    Label2: TLabel;
    Label3: TLabel;
    pgSQLDelphi: TPageControl;
    TabSheet1: TTabSheet;
    TabSheet2: TTabSheet;
    edtNomeTemplate: TRzEdit;
    edtDescricaoTemplate: TRzEdit;
    memoCodigoTemplate: TRzMemo;
    Panel2: TPanel;
    Panel3: TPanel;
    btnClear: TVSMColorButton;
    btnCopy: TVSMColorButton;
    ActionList1: TActionList;
    ACT_CLEAR: TAction;
    ACT_COPY: TAction;
    btnSQL: TVSMColorButton;
    btnDelphi: TVSMColorButton;
    VSMColorButton2: TVSMColorButton;
    ACT_DELPHISQL: TAction;
    ACT_SQLDELPHI: TAction;
    ACT_TEMPLATE: TAction;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    chkUpper: TCheckBox;
    Panel4: TPanel;
    chkGerarArquivo: TCheckBox;
    lblArquivo: TLabel;
    chkFullScrean: TCheckBox;
    chkRemoverX: TRzCheckBox;
    chkFormatarSQL: TCheckBox;
    procedure FormShow(Sender: TObject);
    procedure ACT_CLEARExecute(Sender: TObject);
    procedure ACT_COPYExecute(Sender: TObject);
    procedure ACT_TEMPLATEExecute(Sender: TObject);
    procedure ACT_SQLDELPHIExecute(Sender: TObject);
    procedure ACT_DELPHISQLExecute(Sender: TObject);
    procedure chkFullScreanClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure FormCreate(Sender: TObject);
  private
   frmResizer: TFormResizer;
//    FListaDivergencias: TStringBuilder;
   procedure MontarSQLparaDelphi;
   procedure MontarDelphiParaSQL;
   function RemoveSujeirasDelphi(sArquivoTexto: String): string;
   function TratamentoSumCoalesceDelphi(sArquivoTexto: String): string;
   function RemoveFormatacoesDelphi(sArquivoTexto: String): string;
   function RetornaTratamentoSumCoalesceDelphi(sArquivoTexto: String): string;
   procedure FormatarSQLTentativa2(sArquivoTexto: String);
   function TextoContainsSELECT(sArquivoTexto: String): string;
   procedure GerarTemplateDelphi;
   procedure GerarArquivo(sCaminho, sTexto : String);
   procedure MontarArquivo(sTextoArquivo: String);
   function ReformatSQL(SQL: String): String;
   function Max(x, y: Integer): Integer;
    procedure SetListaDivergencias(const Value: TStringBuilder);
//   property       ListaDivergencias: TStringBuilder read FListaDivergencias write SetListaDivergencias;
    { Private declarations }
  public
 function Explode(Separator, Text: String): TStringList;
    { Public declarations }
  end;

var
  sqlForDelphi: TsqlForDelphi;

implementation

uses
  Vcl.Clipbrd, VSM.Conversor.SQL;

{$R *.dfm}

procedure TsqlForDelphi.ACT_CLEARExecute(Sender: TObject);
begin
   MemoResultado.Clear;
   MemoSQL.Clear;
   memoCodigoTemplate.Clear;
end;

procedure TsqlForDelphi.ACT_COPYExecute(Sender: TObject);
begin
   Clipboard.AsText := MemoResultado.Text;
end;

procedure TsqlForDelphi.ACT_DELPHISQLExecute(Sender: TObject);
begin
   MemoResultado.Clear;
   MontarDelphiParaSQL;
   MemoResultado.Enabled := True;
end;

procedure TsqlForDelphi.ACT_SQLDELPHIExecute(Sender: TObject);
begin
   MemoResultado.Clear;
   MontarSQLparaDelphi;
   MemoResultado.Enabled := True;
end;

procedure TsqlForDelphi.ACT_TEMPLATEExecute(Sender: TObject);
begin
   try
      if edtNomeTemplate.Text = EmptyStr then
      begin
         ShowMessage('Nome do Template deve ser informado');
         Exit;
      end;

      if edtDescricaoTemplate.Text = EmptyStr then
      begin
         ShowMessage('Descri��o do Template deve ser informado');
         Exit;
      end;

      if memoCodigoTemplate.Text = EmptyStr then
      begin
         ShowMessage('C�digo para o Template deve ser informado');
         Exit;
      end;

      GerarTemplateDelphi;
      MemoResultado.Enabled := True;
   except
      ShowMessage('Ocorreu um erro');
   end;
end;

procedure TsqlForDelphi.chkFullScreanClick(Sender: TObject);
begin
   if chkFullScrean.Checked then
   begin
      frmResizer := TFormResizer.Create(Self);
      frmResizer.Name := 'frmResizer';
      frmResizer.ResizeFonts := True;
      frmResizer.MinFontSize := 7;
      frmResizer.MaxFontSize := 18;
      frmResizer.InitializeForm;
      frmResizer.FullScreen;
      frmResizer.ResizeAll;
      chkFullScrean.Enabled := False;
   end
   else
   begin
      if Assigned(frmResizer) then
         frmResizer.Free;
   end;
end;



procedure TsqlForDelphi.FormClose(Sender: TObject; var Action: TCloseAction);
begin
//   ListaDivergencias.Free;
end;

procedure TsqlForDelphi.FormCreate(Sender: TObject);
begin
//   ListaDivergencias := TStringBuilder.Create;
end;

procedure TsqlForDelphi.FormShow(Sender: TObject);
begin
   pgSQLDelphi.ActivePage := TabSheet1;
end;

procedure TsqlForDelphi.GerarArquivo(sCaminho, sTexto : String);
var
   Arquivo : TStringList;
begin
    Arquivo := TStringList.Create;
    try
        Arquivo.Add(sTexto);
        Arquivo.SaveToFile(sCaminho);
    finally
         Arquivo.Free;
    end;
end;

procedure TsqlForDelphi.GerarTemplateDelphi;
var
   sNome, sDescricao, sTempArquivo : string;
   i : Integer;
begin
   try
      sNome := StringReplace(edtNomeTemplate.Text,' ', EmptyStr, [rfReplaceAll]);
      sDescricao := edtDescricaoTemplate.Text;
      MemoResultado.Clear;

      for i := 0 to Pred(memoCodigoTemplate.Lines.Count) do
      begin
         MemoResultado.Lines.Add('|*|'  + memoCodigoTemplate.Lines.Strings[i]);
      end;

      sTempArquivo := StringReplace(TemplatePadrao,'#SUBSTITUIR01#',sNome,[rfReplaceAll, rfIgnoreCase]);
      sTempArquivo := StringReplace(sTempArquivo,'#SUBSTITUIR02#',sDescricao,[rfReplaceAll, rfIgnoreCase]);

      sTempArquivo := sTempArquivo + MemoResultado.Text + TemplatePadraoFim ;

      MemoResultado.Clear;
      MemoResultado.Text := sTempArquivo;
      GerarArquivo('C:\Program Files (x86)\Embarcadero\Studio\18.0\ObjRepos\en\Code_Templates\Delphi\' + sNome + '.xml',sTempArquivo);
      lblArquivo.Caption := 'Arquivo gerado com sucesso em: \Embarcadero\Studio\18.0\ObjRepos\en\Code_Templates\Delphi';

   except
      raise;
   end;

end;


procedure TsqlForDelphi.MontarDelphiParaSQL;
var
   sTempSQL : string;
begin
//   ListaDivergencias.Clear;
   sTempSQL := RemoveSujeirasDelphi(MemoSQL.Text);
   sTempSQL := TratamentoSumCoalesceDelphi(sTempSQL);
   sTempSQL := RemoveFormatacoesDelphi(sTempSQL);
   sTempSQL := RetornaTratamentoSumCoalesceDelphi(sTempSQL);

   if chkFormatarSQL.Checked then
   begin
      FormatarSQLTentativa2(sTempSQL) ;
      MontarArquivo(MemoResultado.Text);
   end
   else
   begin
      MemoResultado.Text := sTempSQL;
      MontarArquivo(sTempSQL);
   end;
end;

procedure TsqlForDelphi.MontarArquivo(sTextoArquivo: String);
var
   sNomeArq : string;
begin
   if chkGerarArquivo.Checked then
   begin
      sNomeArq := DateTimeToStr(Now) ;
      sNomeArq := StringReplace(sNomeArq, ':', '', [rfReplaceAll]);
      sNomeArq := StringReplace(sNomeArq, '/', '', [rfReplaceAll]);
      sNomeArq := StringReplace(sNomeArq, ' ', '', [rfReplaceAll]);
      sNomeArq :=  'C:\OUROFARMA\logs\SQL_GERADOR_DELPHI_' + sNomeArq + '.sql';
      GerarArquivo(sNomeArq,sTextoArquivo);
      lblArquivo.Caption := sNomeArq ;
   end;
end;

procedure TsqlForDelphi.MontarSQLparaDelphi;
var
   Lista: TStringList;
   iRetorno:Integer;
   i, iPosicaoN,iPosicaoRecortar : integer ;
   sTempSQL, sTextoArquivo, sString2 : string;
//   srvConversor : TVSMFormataSQL;
   list : TStringList;
begin
//   sTextoArquivo := EmptyStr;
//   sTextoArquivo := ReformatSQL(MemoSQL.Text) ;

//   MemoSQL.Text := srvConversor.result;
//
//   for i := 0 to MemoSQL.Lines.Count -1 do
//   begin
//      iPosicaoN := Pos('#$A',MemoSQL.Lines.Strings[i]);
//      iPosicaoRecortar :=  MemoSQL.Lines.Strings[i].Length - iPosicaoN;
//      sString2 := copy(MemoSQL.Lines.Strings[i], 0, iPosicaoRecortar);
//   end;
//   list := TStringList.Create;
//
//   MemoResultado.Text := sTextoArquivo;
   if chkFormatarSQL.Checked then
   begin
      FormatarSQLTentativa2(MemoSQL.Text);
      MemoSQL.Text := MemoResultado.Text;
   end;

   for i := 0 to Pred(MemoSQL.Lines.Count) do
   begin
      sTempSQL := StringReplace(MemoSQL.Lines.Strings[i],'''','''''',[rfReplaceAll, rfIgnoreCase]);
      sTempSQL := StringReplace(sTempSQL,'`','',[rfReplaceAll, rfIgnoreCase]);
      sTempSQL := StringReplace(sTempSQL,'\','\\',[rfReplaceAll, rfIgnoreCase]);
      if not chkUpper.Checked then
         sTempSQL := UpperCase(sTempSQL);
      sTempSQL := ' '' ' + sTempSQL + ' '' + ' ;
      MemoResultado.Lines.Add(sTempSQL);
      sTextoArquivo := sTextoArquivo + sTempSQL;
   end;

   MontarArquivo(sTextoArquivo);
end;

function TsqlForDelphi.ReformatSQL(SQL: String): String;
var
  AllKeywords, ImportantKeywords, PairKeywords: TStringList;
  i, Run, KeywordMaxLen: Integer;
  IsEsc, IsQuote, InComment, InBigComment, InString, InKeyword, InIdent, LastWasComment: Boolean;
  c, p: Char;
  Keyword, PreviousKeyword, TestPair: String;
//  Datatypes: TDBDataTypeArray;
const
  WordChars = ['a'..'z', 'A'..'Z', '0'..'9', '_', '.'];
  WhiteSpaces = [#9, #10, #13, #32];
begin
  // Known SQL keywords, get converted to UPPERCASE
  AllKeywords := TStringList.Create;
//  AllKeywords.Text := MySQLKeywords.Text;
//  for i:=Low(MySQLFunctions) to High(MySQLFunctions) do begin
//    // Leave out operator functions like ">>", and the "X()" function so hex values don't get touched
//    if (MySQLFunctions[i].Declaration <> '') and (MySQLFunctions[i].Name <> 'X') then
//      AllKeywords.Add(MySQLFunctions[i].Name);
//  end;
////  Datatypes := Mainform.ActiveConnection.Datatypes;
//  for i:=Low(Datatypes) to High(Datatypes) do
//    AllKeywords.Add(Datatypes[i].Name);
  KeywordMaxLen := 0;
  AllKeywords.Text := MemoSQL.Text;
  for i:=0 to AllKeywords.Count-1 do
    KeywordMaxLen := Max(KeywordMaxLen, Length(AllKeywords[i]));

  // A subset of the above list, each of them will get a linebreak left to it
  ImportantKeywords := Explode(',', 'SELECT,FROM,LEFT,RIGHT,STRAIGHT,NATURAL,INNER,JOIN,WHERE,GROUP,ORDER,HAVING,LIMIT,CREATE,DROP,UPDATE,INSERT,REPLACE,TRUNCATE,DELETE');
  // Keywords which followers should not get separated into a new line
  PairKeywords := Explode(',', 'LEFT,RIGHT,STRAIGHT,NATURAL,INNER,ORDER,GROUP');

  IsEsc := False;
  InComment := False;
  InBigComment := False;
  LastWasComment := False;
  InString := False;
  InIdent := False;
  Run := 1;
  Result := '';
  SQL := SQL + ' ';
  SetLength(Result, Length(SQL)*2);
  Keyword := '';
  PreviousKeyword := '';
  for i:=1 to Length(SQL) do begin
    c := SQL[i]; // Current char
    if i > 1 then p := SQL[i-1] else p := #0; // Previous char

    // Detection logic - where are we?
    if c = '\' then IsEsc := not IsEsc
    else IsEsc := False;
    IsQuote := (c = '''') or (c = '"');
    if c = '`' then InIdent := not InIdent;
    if (not IsEsc) and IsQuote then InString := not InString;
    if (c = '#') or ((c = '-') and (p = '-')) then InComment := True;
    if ((c = #10) or (c = #13)) and InComment then begin
      LastWasComment := True;
      InComment := False;
    end;
    if (c = '*') and (p = '/') and (not InComment) and (not InString) then InBigComment := True;
    if (c = '/') and (p = '*') and (not InComment) and (not InString) then InBigComment := False;
    InKeyword := (not InComment) and (not InBigComment) and (not InString) and (not InIdent) and CharInSet(c, WordChars);

    // Creation of returning text
    if InKeyword then begin
      Keyword := Keyword + c;
    end else begin
      if Keyword <> '' then begin
        if AllKeywords.IndexOf(KeyWord) > -1 then begin
          while (Run > 1) and CharInSet(Result[Run-1], WhiteSpaces) do
            Dec(Run);
          Keyword := UpperCase(Keyword);
          if Run > 1 then begin
            // SELECT, WHERE, JOIN etc. get a new line, but don't separate LEFT JOIN with linebreaks
            if LastWasComment or ((ImportantKeywords.IndexOf(Keyword) > -1) and (PairKeywords.IndexOf(PreviousKeyword) = -1)) then
//              Keyword := CRLF + Keyword
            else if (Result[Run-1] <> '(') then
              Keyword := ' ' + Keyword;
          end;
          LastWasComment := False;
        end;
        PreviousKeyword := Trim(Keyword);
        Insert(Keyword, Result, Run);
        Inc(Run, Length(Keyword));
        Keyword := '';
      end;
      if (not InComment) and (not InBigComment) and (not InString) and (not InIdent) then begin
        TestPair := Result[Run-1] + c;
        if (TestPair = '  ') or (TestPair = '( ') then begin
          c := Result[Run-1];
          Dec(Run);
        end;
        if (TestPair = ' )') or (TestPair = ' ,') then
          Dec(Run);
      end;
      Result[Run] := c;
      Inc(Run);
    end;

  end;

  // Cut overlength
  SetLength(Result, Run-2);
end;

function TsqlForDelphi.Max(x, y: Integer): Integer;
begin
  if x > y then Result := x else Result := y;
end;

function TsqlForDelphi.Explode(Separator, Text: String): TStringList;
var
  i: Integer;
  Item: String;
begin
  // Explode a string by separator into a TStringList
  Result := TStringList.Create;
  while true do begin
    i := Pos(Separator, Text);
    if i = 0 then begin
      // Last or only segment: Add to list if it's the last. Add also if it's not empty and list is empty.
      // Do not add if list is empty and text is also empty.
      if (Result.Count > 0) or (Text <> '') then
        Result.Add(Text);
      break;
    end;
    Item := Trim(Copy(Text, 1, i-1));
    Result.Add(Item);
    Delete(Text, 1, i-1+Length(Separator));
  end;
end;

function TsqlForDelphi.RemoveFormatacoesDelphi(sArquivoTexto: String): string;
begin
   if chkRemoverX.Checked then
   begin
      sArquivoTexto := StringReplace(sArquivoTexto,') +',')',[rfReplaceAll, rfIgnoreCase]);
      sArquivoTexto := StringReplace(sArquivoTexto,')+',')',[rfReplaceAll, rfIgnoreCase]);
      sArquivoTexto := StringReplace(sArquivoTexto,'#+',' ',[rfReplaceAll, rfIgnoreCase]);
      sArquivoTexto := StringReplace(sArquivoTexto,'+#',' ',[rfReplaceAll, rfIgnoreCase]);
      sArquivoTexto := StringReplace(sArquivoTexto,'+ #',' ',[rfReplaceAll, rfIgnoreCase]);
      sArquivoTexto := StringReplace(sArquivoTexto,'# +',' ',[rfReplaceAll, rfIgnoreCase]);
   end;

   // Jogada feita na Sujeira para remo��o correta.
   sArquivoTexto := StringReplace(sArquivoTexto,'%%','''',[rfReplaceAll, rfIgnoreCase]);
   Result := StringReplace(sArquivoTexto,'#',' ',[rfReplaceAll, rfIgnoreCase]);
end;

function TsqlForDelphi.RemoveSujeirasDelphi(sArquivoTexto: String): string;
begin
   sArquivoTexto := StringReplace(sArquivoTexto,'''#$D#$A#9''','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);  //Muda sujeira para remover depois
   sArquivoTexto := StringReplace(sArquivoTexto,'#$D#$A','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'#$D#','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'$A#9','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'''#9#9#9''',' #REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'''#9#9''','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'''#9''',' #REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'#9','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'$D','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'$A','#REMOVER#',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'''#REMOVER#''','',[rfReplaceAll, rfIgnoreCase]);  //Remove a sujeira com as aspas que ficaram
   sArquivoTexto := StringReplace(sArquivoTexto,'#REMOVER#','',[rfReplaceAll, rfIgnoreCase]);

   sArquivoTexto := StringReplace(sArquivoTexto,'''','##',[rfReplaceAll, rfIgnoreCase]);   // Remove aspas duplas para ## para manipular depois

   Result := StringReplace(sArquivoTexto,'####','%%',[rfReplaceAll, rfIgnoreCase]);
end;

function TsqlForDelphi.RetornaTratamentoSumCoalesceDelphi(sArquivoTexto: String): string;
begin
   sArquivoTexto := StringReplace(sArquivoTexto,'SUM2SUM','+ SUM',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'SUM3SUM','+ (SUM',[rfReplaceAll, rfIgnoreCase]);

   Result := StringReplace(sArquivoTexto,'COALESCE4COALESCE','+ COALESCE',[rfReplaceAll, rfIgnoreCase]);
end;

procedure TsqlForDelphi.SetListaDivergencias(const Value: TStringBuilder);
begin
//  FListaDivergencias := Value;
end;

function TsqlForDelphi.TextoContainsSELECT(sArquivoTexto: String): string;
var
   valorTextoDepois, valorTextoAte : string;
   iPosAntes, iPosDepois : Integer;
begin
   if sArquivoTexto.Contains('SELECT') then
   begin
//      ListaDivergencias.AppendLine('SELECT');
      iPosAntes := Length(sArquivoTexto);
      iPosDepois  :=  Pos('SELECT', sArquivoTexto)    ;

      valorTextoAte := Trim(copy(sArquivoTexto, 1, iPosDepois - 1));

//      ListaDivergencias.AppendLine(valorTextoAte);
   //a := length(edt_endereco.Text);
//b := pos(',', edt_endereco.Text);
//
//edt_numero.Text := Trim(copy(edt_endereco.Text, 1, b - 1)

      valorTextoDepois    :=  Trim(copy(valorTextoAte, Pos('SELECT', sArquivoTexto) + 1, Length(sArquivoTexto) -  Pos('SELECT', sArquivoTexto)));

//a := length(edt_endereco.Text);
//b := pos(',', edt_endereco.Text);
//
//edt_numero.Text := Trim(copy(edt_endereco.Text, b + 1, a - b));
//
//      ListaDivergencias.AppendLine(valorTextoDepois);
//
//      valorTextoDepois := Copy(sArquivoTexto , Pos('SELECT', sArquivoTexto) + 6, Length(sArquivoTexto));
//      ListaDivergencias.AppendLine(valorTextoAte);
//      Result := ListaDivergencias.ToString;
   end;

   if valorTextoDepois.Contains('SELECT') then
   begin
      Result := TextoContainsSELECT(valorTextoDepois);
   end;


   //      Sintaxe : function Pos(Substr: string; S: string): Integer;
//
//         var
//                  sNome: String;
//                  nPos1: Byte;
//                  nPos2: Byte;
//                  nPos3: Byte;
//         begin
//                  sNome := \'Antonio Celio Morais\';
//                  nPos1 := Pos(\'A\', sNome); // nPos1 ser� 1
//                  nPos2 := Pos(\'Mor\', sNome); // nPos2 ser� 15
//                  nPos3 := Pos(\'Marco\', sNome); // nPos3 sera 0
//         end;
end;

procedure TsqlForDelphi.FormatarSQLTentativa2(sArquivoTexto: String);
var
  Lista: TStringList;
  srvConversor : TVSMFormataSQL;
  iContador : Integer;
  sVarTexto : string;

begin
  MemoResultado.Clear;

  Lista := TStringList.Create;
  srvConversor := TVSMFormataSQL.Create;
  try
     sArquivoTexto := srvConversor.ConsumirSQL(UpperCase(sArquivoTexto));
//     sArquivoTexto := StringReplace(sArquivoTexto,'    ','',[rfReplaceAll, rfIgnoreCase]);
     sArquivoTexto := StringReplace(sArquivoTexto,'\n',';',[rfReplaceAll]);
     sArquivoTexto := StringReplace(sArquivoTexto,'"}','',[rfReplaceAll, rfIgnoreCase]);
     sArquivoTexto := StringReplace(sArquivoTexto,'{"result":"','      ',[rfReplaceAll, rfIgnoreCase]);


     Lista.Delimiter := ';';
     Lista.StrictDelimiter := True;
     Lista.DelimitedText := sArquivoTexto;

     MemoResultado.Lines.AddStrings(Lista);

//      for iContador := 0 to Pred(Lista.Count) do
//      begin
//         if not Lista[iContador].Contains(',') then
//         begin
//            sVarTexto := sVarTexto +  '' + Lista[iContador];
//            Lista[iContador] := '      ' + Lista[iContador];
//            continue;
//         end;
//
//         if sVarTexto <> EmptyStr then
//         begin
//            MemoResultado.Lines.Add(sVarTexto);
//            sVarTexto := '';
//         end
//         else
//            MemoResultado.Lines.Add(Lista[iContador]);
//
//
//
//
//      end;


  finally
     srvConversor.Free;
     Lista.Free;
  end;


end;

function ObterStringEmLinhas(StringOrigem: string;
                               QtdeCaracteresLin: integer): string;
  var
    i, p, q: integer;
    StringProc, s: string;
    Lista: TStringList;
  begin
    Result := EmptyStr;
    Lista  := TStringList.Create;
    try
        q := QtdeCaracteresLin + 1;
        i := 1;
        StringProc := Trim(StringOrigem);
        while StringProc <> EmptyStr do
          begin
            s := Copy(StringProc, i, q);
            if Length(s) < q then
              begin
                Lista.Add(s);
                Delete(StringProc, 1, q);
              end
            else
              begin
//                p := Pos(' ', ReverseString(s));
                Lista.Add(Copy(s, 1, q - p));
                Delete(StringProc, 1, q - p);
              end;
            StringProc := Trim(StringProc);
          end;
        Result := Lista.Text;
    finally
        Lista.Free;
    end;
  end;

function TsqlForDelphi.TratamentoSumCoalesceDelphi(sArquivoTexto: String): string;
begin
   sArquivoTexto := StringReplace(sArquivoTexto,'+SUM','SUM2SUM',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'+ SUM','SUM2SUM',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'+  SUM','SUM2SUM',[rfReplaceAll, rfIgnoreCase]);

   sArquivoTexto := StringReplace(sArquivoTexto,'+(SUM','SUM3SUM',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'+ (SUM','SUM3SUM',[rfReplaceAll, rfIgnoreCase]);
   sArquivoTexto := StringReplace(sArquivoTexto,'+  (SUM','SUM3SUM',[rfReplaceAll, rfIgnoreCase]);

   Result := StringReplace(sArquivoTexto,'+ COALESCE','COALESCE4COALESCE',[rfReplaceAll, rfIgnoreCase]);
end;

end.
