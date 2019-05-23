<?php
include "cabecalho.html";
include "conexao.php";

$sql = "SELECT * FROM atirador;";
$rs = mysqli_query($conexao, $sql);

?>
<html>
    <body class="container">
        <h1 class="prymary">ATIRADORES</h1>
        <br/> 
        <table class="table table-striped table-red table table-hover">
            <tr>
                <th>RA</th>
                <th>Nome</th>
                <th>CPF</th>
                <th>Nascimento</th>
                <th>Endereço</th>
                <th>Pontuação</th>
                <th></th>
                <th></th>
            </tr>
            <?php while ($linha = mysqli_fetch_array($rs)) {?>
                <tr>
                    <td><?php echo $linha['ra'] ?></td>
                    <td><?php echo $linha['nome'] ?></td>
                    <td><?php echo $linha['cpf'] ?></td>
                    <td><?php echo $linha['nascimento'] ?></td>
                    <td><?php echo $linha['endereco'] ?></td>
                    <td><?php echo $linha['pontuacao'] ?></td>
                    <td><button type="" class="btn btn-warning">Editar</button></td>
                    <td><button type="" class="btn btn-danger">Deletar</button></td>
                </tr>
            <?php }?> 
        </table>
    </body>
</html>