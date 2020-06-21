unit Cloud.Dto.Tabela;

interface
uses
   DBClient,
   Generics.Collections,
   System.RTTI,
   System.TypInfo;

   type
      TCloudTabela = class

      end;

      TVSMCloudTabelaHelper = class helper for TCloudTabela
         public
            class procedure PreencherDataSet<T : TCloudTabela>(var ClientDataSet: TClientDataSet;
                                                                FLista: TObjectList<T>;
                                                                sField : string = 'Nome');
      end;



implementation

{ TCloudTabela }

class procedure TVSMCloudTabelaHelper.PreencherDataSet<T>(var ClientDataSet: TClientDataSet; FLista: TObjectList<T>; sField : string = 'Nome');
var
  AuxValue: TValue;
  Contexto: TRttiContext;
  TipoRtti: TRttiType;
  PropriedadeNome: TRttiProperty;
  tabela: TCloudTabela;
begin
   ClientDataSet.Close;
   ClientDataSet.CreateDataSet;
   // Cria o contexto do RTTI
   Contexto := TRttiContext.Create;
   if (FLista = nil) or (FLista.Count = 0) then
      Exit;

   try
      // Obt�m as informa��es de RTTI da classe TFuncionario
      AuxValue := GetTypeData(PTypeInfo(TypeInfo(T)))^.ClassType.Create;
      TipoRtti := Contexto.GetType(AuxValue.AsObject.ClassInfo);

      // Obt�m um objeto referente � propriedade "Nome" da classe TFuncionario
      PropriedadeNome := TipoRtti.GetProperty(sField);

      // Percorre a lista de objetos, inserindo o valor da propriedade "Nome" do ClientDataSet
      for tabela in FLista do
         ClientDataSet.AppendRecord([PropriedadeNome.GetValue(tabela).AsString]);

      ClientDataSet.First;
   finally
      Contexto.Free;
   end;
end;

end.
