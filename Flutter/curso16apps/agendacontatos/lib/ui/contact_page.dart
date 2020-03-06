import 'dart:io';

import 'package:agendacontatos/helpers/contact_helper.dart';
import 'package:flutter/material.dart';

class ContactPage extends StatefulWidget {
  final Contact contact;
  ContactPage({this.contact}); // parametro opcional

  @override
  _ContactPageState createState() => _ContactPageState();
}

class _ContactPageState extends State<ContactPage> {
  final _nameController = TextEditingController();
  final _phoneController = TextEditingController();
  final _emailController = TextEditingController();

  bool _bUserEdit = false;

  Contact _editedContact;

  @override
  void initState() {
    super.initState();

    if (widget.contact == null) {
      _editedContact = Contact();
    } else {
      _editedContact = Contact.fromMap(widget.contact.toMap());

      _phoneController.text = _editedContact.telefone;
      _emailController.text = _editedContact.email;
      _nameController.text = _editedContact.nome;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.red,
        title: Text(_editedContact.nome ?? "Novo Contato"),
        centerTitle: true,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: Icon(Icons.save),
        backgroundColor: Colors.red,
      ),
      body: new SingleChildScrollView(
        scrollDirection: Axis.vertical,
        padding: const EdgeInsets.all(10.0),
        child: new Column(
          children: <Widget>[
            GestureDetector(
              child: Container(
                width: 140.0,
                height: 140.0,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  image: DecorationImage(
                      image: _editedContact.imagem != null
                          ? FileImage(File(_editedContact.imagem))
                          : AssetImage("images/person.png")),
                ),
              ),
            ),
            new TextField(
              controller: _nameController,
              decoration: InputDecoration(labelText: "Nome"),
              onChanged: (text) {
                _bUserEdit = true;
                setState(() {
                  _editedContact.nome = text;
                });
              },
            ),
            new TextField(
              controller: _emailController,
              decoration: InputDecoration(labelText: "e-mail"),
              onChanged: (text) {
                _bUserEdit = true;

                _editedContact.nome = text;
              },
              keyboardType: TextInputType.emailAddress,
            ),
            new TextField(
              controller: _phoneController,
              decoration: InputDecoration(labelText: "telefone"),
              onChanged: (text) {
                _bUserEdit = true;

                _editedContact.nome = text;
              },
              keyboardType: TextInputType.phone,
            ),
          ],
        ),
      ),
    );
  }
}