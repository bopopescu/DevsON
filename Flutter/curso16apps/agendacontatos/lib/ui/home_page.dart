import 'package:agendacontatos/helpers/contact_helper.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  ContactHelper helper = ContactHelper();

  //teste
  @override
  void initState() {
    super.initState();

    Contact c = Contact();
    c.nome = "WG";
    c.email = "wg@gmail.com";
    c.telefone = "184444444";
    c.imagem = "teste";

    helper.saveContact(c);

    helper.getAllContacts().then((list) {
      print(list);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
