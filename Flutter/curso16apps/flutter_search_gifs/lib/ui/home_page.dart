import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

const url_melhores_gifs =
    "https://api.giphy.com/v1/gifs/trending?api_key=ETRUxGlwAKlCo4YAMLeY6R9HR2QebWrx&limit=25&rating=G";
const url_imagem =
    "https://developers.giphy.com/branch/master/static/header-logo-8974b8ae658f704a5b48a2d039b8ad93.gif";

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String _search, _url_pesquisa_mont;
  int _offSet = 0;
  Future<Map> _getGifs() async {
    http.Response response;

    if (_search == null)
      response = await http.get(url_melhores_gifs);
    else {
      _url_pesquisa_mont =
          "https://api.giphy.com/v1/gifs/search?api_key=ETRUxGlwAKlCo4YAMLeY6R9HR2QebWrx&q=$_search&limit=25&offset=$_offSet&rating=G&lang=pt";
      ;

      _search.isEmpty;
      print(_url_pesquisa_mont);
      response = await http.get(_url_pesquisa_mont);
    }
    return json.decode(response.body);
  }

  @override
  void initState() {
    super.initState();
    _getGifs().then((map) {
      print(map);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Image.network(url_imagem),
        centerTitle: true,
      ),
      backgroundColor: Colors.black12,
      body: Column(
        children: <Widget>[
          Padding(
            padding: EdgeInsets.all(10.0),
            child: TextField(
              decoration: InputDecoration(
                  labelText: "Pesquise Aqui",
                  labelStyle: TextStyle(color: Colors.white),
                  border: OutlineInputBorder()),
              style: TextStyle(color: Colors.white, fontSize: 18.0),
              textAlign: TextAlign.center,
              onSubmitted: (text) {
                setState(() {
                  _search = text;
                  text.isEmpty;
                });
              },
            ),
          ),
          //Ocupar todo o espaço do Builder
          Expanded(
            child: FutureBuilder(
                future: _getGifs(),
                builder: (context, snapshot) {
                  switch (snapshot.connectionState) {
                    case ConnectionState.waiting:
                    case ConnectionState.none:
                      return Container(
                        width: 200.0,
                        height: 200.0,
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                            valueColor:
                                AlwaysStoppedAnimation<Color>(Colors.white),
                            strokeWidth: 5.0),
                      );
                    default:
                      if (snapshot.hasError)
                        return Container();
                      else
                        return _createGifTable(context, snapshot);
                  }
                }),
          )
        ],
      ),
    );
  }

  Widget _createGifTable(BuildContext context, AsyncSnapshot snapshot) {
    return GridView.builder(
        padding: EdgeInsets.all(10.0),
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2, crossAxisSpacing: 10.0, mainAxisSpacing: 10.0),
        itemCount: snapshot.data["data"].length,
        itemBuilder: (context, index) {
          return GestureDetector(
              child: Image.network(
            snapshot.data["data"][index]["images"]["fixed_height_small"]["url"],
            height: 100.0,
            fit: BoxFit.cover,
          ));
        });
  }
}
