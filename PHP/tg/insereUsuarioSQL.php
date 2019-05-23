<?php
include "conexao.php";


$user = $_POST['user'];
$senha = $_POST['senha'];


$sql = "INSERT INTO usuario (user, senha) VALUES 
('$user', '$senha');";


$resultado = mysqli_query($conexao, $sql);

    if(!$resultado){
        echo "Erro ao inserir usuario no banco de dados!";
    }