<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../css/style.css"/>
    <title>Bancos de dados EAG</title>
</head>
<body>
    <section id="main">
        <div id="layer"></div>
            <div class="center">
                <header>
                    <div class="clear"></div>
                    <div id="logo">
                        <h1>Bancos de dados EAG</h1>
                    </div>
                    <div class="clear"></div>
                </header>
                <div id="conteudo_header">
                    <form method="post">
                        <div id="input_Banco">
                            <h3>banco:</h3>
                            <input id="Banco_connect" name="Banco_connect" type="text" placeholder="Nome do banco" required>
                        </div>
                        <div id="input_IP">
                            <h3>IP:</h3>
                            <input id="IP_connect" name="IP_connect" type="text" placeholder="000.000.000.000" required>
                        </div>
                        <div id="input_Senha">
                            <h3>Senha:</h3>
                            <input id="Senha_connect" name="Senha_connect" type="password" required>
                        </div>
                        <input type="submit" value="Procurar">
                    </form>
                    <?php
                        require_once '../dao/Conexao.php';
                        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                            $banco = $_POST['Banco_connect'];
                            $ip = $_POST['IP_connect'];
                            $senha = $_POST['Senha_connect'];

                            $conexao = new Conexao($banco, $ip, $senha);
                            $db = $conexao->getConexao();

                            if ($db) {
                                echo "Conexão bem-sucedida!";
                                header('Location: Menu.html');
                                exit; // Certifique-se de chamar exit após o redirecionamento
                            } else {
                                echo "Falha na conexão.";
                            }
                        }
                    ?>
                </div>
            </div>
        </section>
    </body>
<footer>
    <p>Todos os direitos reservados.</p>
</footer>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
<script type="text/javascript" src="js/menu_mobile.js"></script>
</html>