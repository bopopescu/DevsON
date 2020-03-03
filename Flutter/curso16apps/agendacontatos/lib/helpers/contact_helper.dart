import 'package:sqflite/sqflite.dart';

final String idCol = "idCol";
final String nomeCol = "nomeCol";
final String emailCol = "emailCol";
final String telefoneCol = "telefoneCol";
final String imagemCol = "imagemCol";

class contactHelper {}

class Contact {
  int id;
  String nome;
  String email;
  String telefone;
  String imagem;

  Contact.fromMap(Map map) {
    id = map[idCol];
    nome = map[nomeCol];
    email = map[emailCol];
    telefone = map[telefoneCol];
    imagem = map[imagemCol];
  }

  Map toMap() {
    Map<String, dynamic> map = {
      nomeCol: nome,
      emailCol: email,
      telefoneCol: telefone,
      imagemCol: imagem
    };
    if (id != null) {
      map[idCol] = id;
    }
    return map;
  }

  @override
  String toString() {
    return "Contato(id: $id, nome: $nome, email: $email, telefone: $telefone, imagem: $imagem";
  }
}
