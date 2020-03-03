import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

final String contactTable = "contactTable";
final String idCol = "idCol";
final String nomeCol = "nomeCol";
final String emailCol = "emailCol";
final String telefoneCol = "telefoneCol";
final String imagemCol = "imagemCol";

class ContactHelper {
  //Singleton
  final String sSqlCreate = "CREATE TABLE $contactTable("
      "$idCol INTEGER PRIMARY KEY,"
      "$nomeCol TEXT,"
      "$emailCol TEXT,"
      "$telefoneCol TEXT,"
      "$imagemCol TEXT"
      ")";
  static final ContactHelper _instance = Contact.internal();

  factory ContactHelper() => _instance;

  ContactHelper.internal();

  Database _db;
  get db {
    if (_db != null) {
      return _db;
    } else {
      _db = initDb();
    }
  }

  initDb() async {
    final databasesPath = await getDatabasesPath();
    final path = join(databasesPath, "contact.db");

    openDatabase(path, version: 1,
        onCreate: (Database db, int newerVersion) async {
      await db.execute(sSqlCreate);
    });
  }
}

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
