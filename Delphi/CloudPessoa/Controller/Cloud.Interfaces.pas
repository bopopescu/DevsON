unit Cloud.Interfaces;
{  Utilizar a linguagem Delphi (Qualquer vers�o);
    Criar uma tela de cadastro de clientes, com os seguintes campos:
    Dados do Cadastro:

      Nome
      Identidade
      CPF
      Telefone
      Email
        Endere�o
        Cep
        Logradouro
        Numero
        Complemento
        Bairro
        Cidade
        Estado
        Pais
    Ao informar um Cep o sistema deve realizar a busca dos dados relacionados ao mesmo no seguinte endere�o: https://viacep.com.br/;
    A forma de consumo da API do via Cep, dever� ser utiliza JSON;
    Ao termino do cadastro o usu�rio dever� enviar um e-mail contendo as informa��es cadastrais e anexar um arquivo no formato XML com o mesmo conte�do;
    Os registros devem ficar salvo em mem�ria, n�o � necess�rio criar um banco de dados ou arquivo para o armazenamento dos dados;
    Disponibilizar o c�digo fonte do projeto no github;
}
interface

uses DBClient,
     Generics.Collections,
     Cloud.Pessoa;

type
  ICloudController = interface
    ['{D297498B-F1A8-4C82-B541-D5D11DA7FBAC}']
    function AddCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>) : Boolean;
    function IncluirFuncionario(Dados: array of variant): TCloudPessoa;
    procedure CriarCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>);
    procedure PreencherDataSet(var ClientDataSet: TClientDataSet;
                              FListaFuncionarios: TObjectList<TCloudPessoa>);
  end;

implementation

end.