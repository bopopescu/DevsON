unit Ufrm_Endereco;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.ExtCtrls, Vcl.StdCtrls, Data.DB,
  Vcl.Mask;

type
  Tfrm_Endereco = class(TForm)
    Label1: TLabel;
    EditTipoEnd: TEdit;
    Label2: TLabel;
    EditEndereco: TEdit;
    Label3: TLabel;
    EditNumeroEnd: TEdit;
    Label4: TLabel;
    EditCidade: TEdit;
    Label5: TLabel;
    btnSalvar: TButton;
    btnVoltar: TButton;
    Panel1: TPanel;
    Panel2: TPanel;
    Panel3: TPanel;
    Label6: TLabel;
    DS_Endereco: TDataSource;
    EditCep: TMaskEdit;
    procedure btnVoltarClick(Sender: TObject);
    procedure FormKeyPress(Sender: TObject; var Key: Char);
    procedure FormShow(Sender: TObject);
    procedure btnSalvarClick(Sender: TObject);
  private
    { Private declarations }
    procedure limpaCampos;
  public
    { Public declarations }
  end;

var
  frm_Endereco: Tfrm_Endereco;

implementation

{$R *.dfm}

uses U_DMDados, U_Funcoes, Datasnap.DBClient, Ufrm_Principal;

procedure Tfrm_Endereco.btnSalvarClick(Sender: TObject);
begin
  with DM_Dados do //utilizo o with para n�o precisar informar o DM_Dados no inicio de cada um
   begin

    if DS_Endereco.State in [dsInsert] then
      begin
        CDS_EndCliIDENDERECO.AsInteger := GetId('IDENDERECO','ENDCLI');
        CDS_EndCliIDCLIENTE.AsInteger := CDS_Clientesidcliente.AsInteger;
      end;

    CDS_EndClitipo.AsString := trim(EditTipoEnd.Text);
    CDS_EndCliendereco.AsString := trim(EditEndereco.Text);
    CDS_EndClinumero.AsString := trim(EditNumeroEnd.Text);
    CDS_EndClicidade.AsString := trim(EditCidade.Text);
    CDS_EndClicep.AsString := trim(EditCep.Text);



   end;

  //salvar ou incluir
  try
    TClientDataSet(DS_Endereco.DataSet).Post;
    TClientDataSet(DS_Endereco.DataSet).ApplyUpdates(0);

    Application.MessageBox('Registro Inserido com sucesso!','Inclus�o',MB_OK+MB_ICONINFORMATION);

    limpaCampos;
    TClientDataSet(DS_Endereco.DataSet).Open;
    close;
  except on E: Exception do
    raise Exception.Create('Erro ao salvar registro:'+E.Message);
  end;
end;



procedure Tfrm_Endereco.btnVoltarClick(Sender: TObject);
begin
    Close;
    frmPrincipal.DS_EndCli.DataSet.cancel;
    frmPrincipal.DS_TelCli.DataSet.cancel;
end;


procedure Tfrm_Endereco.FormKeyPress(Sender: TObject; var Key: Char);
begin
    if key = #27 then
      begin
        Close;
        frmPrincipal.DS_EndCli.DataSet.cancel;
        frmPrincipal.DS_TelCli.DataSet.cancel;
      end;
end;

procedure Tfrm_Endereco.FormShow(Sender: TObject);
begin
    EditTipoEnd.SetFocus;
end;


procedure Tfrm_Endereco.limpaCampos;
var
  I: Integer;
begin
  for I := 0 to ComponentCount -1 do
  begin
    if Components[i] is TCustomEdit then
      TCustomEdit(Components[i]).Clear;
  end;
end;

end.
