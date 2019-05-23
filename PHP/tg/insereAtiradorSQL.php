<?php
include "conexao.php";


$nome = $_POST['nome'];
$cpf = $_POST['cpf'];
$nascimento = $_POST['nascimento'];
$endereco = $_POST['endereco'];
$pontuacao = $_POST['pontuacao'];


$sql = "INSERT INTO atirador (nome, cpf, nascimento, endereco, pontuacao) VALUES 
('$nome', '$cpf', '$nascimento', '$endereco', '$pontuacao');";


$resultado = mysqli_query($conexao, $sql);

    if(!$resultado){
        echo "Erro ao inserir atiraddor no banco de dados!";
    }

//Depos da chamada do insereAtiradorSQL.php o mesmo é direcionado para listagem, ficando assim mais intuitivel ao usuário.
header('location: atiradores.php');

/*echo $nome;
echo $cpf;
echo $nascimento;
echo $endereco;
echo $pontuacao;
*/