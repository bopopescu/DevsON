unit Principal;

interface

uses System.Classes;
//-------------COMPONENTE--------------

procedure register;
type
  TNotifyEvent = procedure (Sender : TObject) of Object;
	TEventos = class(TComponent)
	private
    FNome: String;
    FStatus: TNotifyEvent;
    procedure SetNome(const Value: String);
    procedure SetStatus(const Value: TNotifyEvent);

	public
		function TamanhoString(Value : String) : Integer;
    procedure OnStatus;

  { PUBLISHED ->  Se colocar nessa seção. ao compilar já ira aparecer nas Units }
	published
    property Nome :  String read FNome write SetNome;
    property Status : TNotifyEvent read FStatus write SetStatus;

	end;


implementation

{ TEventos }

procedure register;
	begin
		RegisterComponents('DelphiUpdates',[TEventos])
    {
    Onde DelphiUpdates seria a sessão e TEventos as classes liberadas
      Após registrar, botão direito no componente em ProjectManager, Compile e depois Install.. Criar um
      novo projeto ou formulário e utilizar o evento de Tool Palette
         }

	end;

procedure TEventos.OnStatus;
begin
    if Assigned(Status) then
        Status(Self);
end;

procedure TEventos.SetNome(const Value: String);
begin
  FNome := Value;
end;

procedure TEventos.SetStatus(const Value: TNotifyEvent);
begin
  FStatus := Value;
end;

function TEventos.TamanhoString(Value: String): Integer;
begin
    Nome := Value;
    Result := Length(Value);
    OnStatus;
end;

end.

