<?php
include "cabecalho.html";
?>
<html>
        <form action="insereGuarda.php" method="POST">
            <div class="container">
                <label>RA:</label>
                <input class="form-control" type="text" name="ra"/>
            
                <label>Nome:</label>
                <input class="form-control" type="text" name="nome"/>
            
                <label>Data:</label>
                <input class="form-control" type="date" name="data"/>
                <br><br>
                <button type="submit" class="btn btn-success">Gravar</button>
                <button type="reset" class="btn btn-danger">Limpar</button>
             
            </div>
</html>