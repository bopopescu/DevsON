unit Cloud.Dto.Pessoa;

interface

uses
  Vcl.Graphics,
  Cloud.Dto.Pessoa.Endereco,
  Generics.Collections;

type
  TCloudPessoa = class
  private
    Fid: integer;
    FNome: string;
    FIdentidade: string;
    FCPF: string;
    FTelefone: string;
    FEmail: string;
    FEndereco: TObjectList<TCloudEndereco>;
  public
    property ID: integer read Fid write Fid;
    property Nome: string read FNome write FNome;
    property Identidade: string read FIdentidade write FIdentidade;
    property CPF: string read FCPF write FCPF;
    property Telefone: string read FTelefone write FTelefone;
    property Email : string read FEmail write FEmail;
    property Endereco : TObjectList<TCloudEndereco> read FEndereco write FEndereco;
      constructor Create;
      destructor Destroy; override;
  end;

implementation

{ TCloudPessoa }

constructor TCloudPessoa.Create;
begin
   Endereco := TObjectList<TCloudEndereco>.Create;
end;

destructor TCloudPessoa.Destroy;
begin
   Endereco.Free;
  inherited;
end;

end.
