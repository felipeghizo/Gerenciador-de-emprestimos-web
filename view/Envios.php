<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../css/style_envios.css"/>
    <title>Envios</title>
</head>
<body>
    <section id="Topo">
        <div id="layer"></div>
        <div class="center">
            <header>
                <div class="clear"></div>
                <div id="logo">
                    <h1>Bancos de dados EAG</h1>
                </div>
                <div id="Menu">
                    <ul>
                        <a href="Cameras.html"><li>Câmeras</li></a>
                        <a href="Clientes.html"><li>Clientes</li></a>
                        <a href="Historico.html"><li>Histórico</li></a>
                        <a href="Envios.html"><li>Envios</li></a>  
                    </ul>
                </div>
                <div class="clear"></div>
            </header>
        </div>
    </section>
    <section id="Main">
        <div id="botoes">
            <ul>
                <li><input type="button" value="Adicionar teste"></li>
                <li><input type="button" value="Encerrar teste"></li>
                <li><input type="button" value="Editar teste"></li>
                <li><input type="button" value="Visualizar dados"></li>
            </ul>
        </div>
        <div id="info">
            <div id="table-tittle">
                <div id="look-for-info">
                    <input type="text" placeholder="Dados">
                    <input type="button" value="Procurar">
                </div>
                <h3>Envios</h3>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Cliente</th>
                        <th>Câmera</th>
                        <th>Acesso</th>
                    </tr>
                </thead>
                <tbody>
                <?php
                    // Configurações do banco de dados
                    require_once '../dao/Conexao.php';
                    require_once '../modelo/Cliente.php';

                    $banco = "envio";
                    $ip = "10.100.68.253";
                    $senha = "Camerasip135.";

                    $cliente = new Cliente();

                    try {
                        // Cria a conexão
                        $conexao = new Conexao($banco, $ip, $senha);
                        $pdo = $conexao->getConexao();
                    
                        // Consulta SQL
                        $sql = "SELECT clienteid, cameraid, acesso FROM envios";
                        $stmt = $pdo->query($sql);
                    
                        // Busca todos os resultados
                        $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
                    
                        // Verifica se há resultados
                        if (count($results) > 0) {
                            echo '<table border="1">
                                    <thead>
                                        <tr>
                                            <th>Cliente</th>
                                            <th>Câmera</th>
                                            <th>Acesso</th>
                                        </tr>
                                    </thead>
                                    <tbody>';
                            
                            foreach ($results as $row) {
                                echo '<tr>';
                                echo '<td>' . $cliente->getNomeID(intval(htmlspecialchars($row['clienteid']))) . '</td>';
                                echo '<td>' . htmlspecialchars($row['cameraid']) . '</td>';
                                echo '<td>' . htmlspecialchars($row['acesso']) . '</td>';
                                echo '</tr>';
                            }
                            
                            echo '  </tbody>
                                  </table>';
                        } else {
                            echo "Nenhum registro encontrado";
                        }
                    
                    } catch (PDOException $e) {
                        echo 'Erro: ' . $e->getMessage();
                    }
                    ?>
                </tbody>
            </table>
        </div>
    </section>
</body>
<footer>
    <p>Todos os direitos reservados.</p>
</footer>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
<script type="text/javascript" src="js/menu_mobile.js"></script>
</html>