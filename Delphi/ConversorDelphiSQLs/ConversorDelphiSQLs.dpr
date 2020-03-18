program ConversorDelphiSQLs;

uses
  Vcl.Forms,
  GeradorSQLDelphi in 'GeradorSQLDelphi.pas' {sqlForDelphi},
  Vcl.Themes,
  Vcl.Styles,
  VSM.Conversor.SQL in 'FormatSql\VSM.Conversor.SQL.pas',
  VSM.Rest in 'FormatSql\VSM.Rest.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;

  Application.CreateForm(TsqlForDelphi, sqlForDelphi);
  Application.Run;
end.
