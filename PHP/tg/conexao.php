<?php

$bdServidor = "localhost";
$bdUsuario = "root";
$bdSenha = "";
$bdBanco = "tg";


$conexao = mysqli_connect("$bdServidor", "$bdUsuario", "$bdSenha", "$bdBanco");

    // Testando conexão com banco de dados.
    if(!$conexao){
        echo "Erro ao se conectar com banco de dados!";
    }