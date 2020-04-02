unit VSMRestClientParamHeaderDto;

interface

type
  TVSMRestClientParamHeaderDto = class
  private
    FValor: String;
    FNome: String;
    procedure SetNome(const Value: String);
    procedure SetValor(const Value: String);

    public constructor create(nome, valor: string);

  published
    property nome: String read FNome write SetNome;
    property valor: String read FValor write SetValor;
  end;

implementation

{ TVSMRestClientParamHeaderDto }

constructor TVSMRestClientParamHeaderDto.create(nome, valor: string);
begin
   Self.nome := nome;
   Self.valor := valor;
end;

procedure TVSMRestClientParamHeaderDto.SetNome(const Value: String);
begin
  FNome := Value;
end;

procedure TVSMRestClientParamHeaderDto.SetValor(const Value: String);
begin
  FValor := Value;
end;

end.
