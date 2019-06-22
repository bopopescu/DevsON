unit uCategoriaModel;

interface

uses System.SysUtils;

type
  TCategoria = class
  private
    getDescricao: String;
    FCodigo: Integer;

    procedure SetDescricao(const Value: String);

  public
    property Codigo: Integer read FCodigo write FCodigo;
    property Descricao: String read getDescricao write SetDescricao;
  end;

implementation

{ TCategoria }

procedure TCategoria.SetDescricao(const Value: String);
begin
  if Value = EmptyStr then
    raise EArgumentException.Create('''Descri��o''precisa ser preenchido!');
  getDescricao := Value;

end;

end.
