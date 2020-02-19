import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

const url_melhores_gifs =
    "https://api.giphy.com/v1/gifs/trending?api_key=ETRUxGlwAKlCo4YAMLeY6R9HR2QebWrx&limit=25&rating=G";
const url_pesquisa =
    "https://api.giphy.com/v1/gifs/search?api_key=ETRUxGlwAKlCo4YAMLeY6R9HR2QebWrx&q=_buscar&limit=25&offset=_itenspage&rating=G&lang=pt";

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
      _url_pesquisa_mont = url_pesquisa;
      _url_pesquisa_mont.replaceAll("_buscar", _search);
      _url_pesquisa_mont.replaceAll("_itenspage", _offSet.toString());
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
    return Container();
  }
}
