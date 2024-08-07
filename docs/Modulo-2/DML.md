<center>

# Linguagem de Manipulação de Dados - DML

</center>

---
<Center>

# O que é?

</center>

> É um subconjunto da SQL (Structured Query Language) usado para manipular e interagir com os dados armazenados em um banco de dados.

---

```
BEGIN TRANSACTION;

INSERT INTO item(tipo)
VALUES
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel'),
('nao fabricavel');

INSERT INTO item_fabricavel(id, tipo)
VALUES
(1, 'ferramenta'),
(2, 'ferramenta'),
(3, 'ferramenta'),
(4, 'ferramenta'),
(5, 'ferramenta'),
(6, 'ferramenta'),
(7, 'arma'),
(8, 'arma'),
(9, 'arma'),
(10, 'arma'),
(11, 'arma'),
(12, 'arma'),
(13, 'arma');

INSERT INTO item_nao_fabricavel(id_item, tipo_nao_fabricavel)
VALUES
(14, 'utilizavel'),
(15, 'utilizavel'),
(16, 'utilizavel'),
(17, 'utilizavel'),
(18, 'utilizavel'),
(19, 'utilizavel'),
(20, 'utilizavel'),
(21, 'utilizavel'),
(22, 'utilizavel'),
(23, 'utilizavel'),
(24, 'utilizavel'),
(25, 'utilizavel'),
(26, 'utilizavel');
(27, 'utilizavel');
(28, 'medicamento');
(29, 'medicamento');
(30, 'medicamento');
(31, 'comida');
(32, 'comida');
(33, 'comida');
(34, 'comida');
(35, 'comida');
(36, 'comida');

INSERT INTO ferramenta(id, nome, tamanho, descricao, utilidade)
VALUES
(1, 'Chave de Fenda', 1, 'Ferramenta com ponta plana ou cruzada para apertar ou soltar parafusos.', 'Usada para desmontar objetos.'),
(2, 'Pa', 2, 'Ferramenta com lâmina larga e plana para cavar e mover materiais.', 'Ideal para escavar ou remover detritos.'),
(3, 'Martelo', 2, 'Ferramenta com cabeça pesada usada para bater pregos ou quebrar objetos.', 'Usado em construção e demolição.'),
(4, 'Picareta', 2, 'Ferramenta com uma extremidade pontiaguda e outra achatada, usada para quebrar superfícies duras.', 'Ideal para mineração ou demolição.'),
(5, 'Lock Pick', 1, 'Ferramenta fina e estreita usada para destrancar fechaduras sem chave.', 'Utilizada para abrir fechaduras de forma furtiva.'),
(6, 'Corda', 1, 'Cordão grosso feito de fibras entrelaçadas.', 'Usada para amarrar, puxar ou escalar.');

INSERT INTO arma(id, nome, tamanho, descricao, dano)
VALUES
(7, 'Faca', 2, 'Lâmina afiada e curta usada para cortar ou perfurar.', 3),
(8, 'Agulha', 1, 'Ferramenta fina e pontiaguda, geralmente usada para costura.', 1),
(9, 'Soco Ingles', 1, 'Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo.', 2),
(10, 'Faca Curta', 1, 'Pequena faca com lâmina curta, fácil de esconder.', 2),
(11, 'Coquetel Molotov', 1, 'Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.', 5),
(12, 'Corda com Cerol', 1, 'Corda revestida com vidro moído para causar cortes.', 3),
(13, 'Garrafa Quebrada', 1, 'Garrafa de vidro quebrada, usada como arma cortante.', 3);

INSERT INTO utilizavel(id, nome, tamanho, descricao_efeito, raridade, quantidade)
VALUES
(14, 'Sabao', 1, 'serve para remover sujeira e impurezas de superfícies e objetos, também é um material para fabricação de itens.', 0, 1),
(15, 'Pedra', 1, 'A pedra serve para construção e também é um material para fabricação de itens.', 0, 3),
(16, 'graveto', 1, 'Produto de origem vegetal, é usado como material para fabricação de itens.', 0, 3),
(17, 'linha', 1, 'fio fino e flexível utilizado como material para fabricação de itens.', 0, 3),          
(18, 'pedaco pequeno de metal', 1, 'Corda revestida com vidro moído para causar cortes.', 1, 3),          
(19, 'vidro', 1, 'utilizado como material para fabricação de cerol.', 0, 1),          
(20, 'pedaco grande de metal', 3, 'Garrafa de vidro quebrada, usada como arma cortante.', 2, 1),          
(21, 'alcool', 1, 'utilizado como material para fabricação de coctel molotov e garrafa quebrada.', 1, 1),          
(22, 'tecido', 1, 'Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.', 1, 3),          
(23, 'garrada de vidro', 2, 'utilizado como material para fabricação de coctel molotov e garrafa quebrada.', 1, 1),          
(24, 'plastico', 1, 'Corda revestida com vidro moído para causar cortes.', 0, 3),          
(25, 'Isqueiro', 1, 'Isqueiro é um dispositivo portátil utilizado para gerar fogo, podendo ser utilizado para queimar coisas.', 1, 1),          
(26, 'Lanterna', 1, 'Lanterna é um dispositivo portátil que emite luz.', 1, 1),          
(27, 'cigarro', 1, 'Moeda de troca do jogo, além de poder ser utilizado para acalmar.', 1, 10);         

INSERT INTO medicamento(id, nome, tamanho, descricao, raridade, cura, quantidade)
VALUES
(28, 'anti-inflamatorio', 1, 'Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.', 2, 3, 5),          
(29, 'Morfina', 1, 'Analgésico opiáceo potente utilizado para aliviar dores intensas.', 1, 10, 2),          
(30, 'Bandagem', 1, 'Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo.', 0, 2, 5);         

INSERT INTO comida(id, nome, tamanho, descricao, raridade, quantidade, cura)
VALUES
(31, 'Pao seco', 1 'um pão tão seco e duro, que parece que o proprio vandor amassou ele.', 0, 1, 0),
(32, 'Pao', 1 'alimento básico feito a partir de farinha, água e fermento.', 0, 3, 1),    
(33, 'Queijo', 1 'produto lácteo sólido feito a partir da coagulação do leite.', 0, 3, 1),    
(34, 'Carne', 2 'é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento.', 2, 1, 5),    
(35, 'Peixe', 1 'tecido muscular de peixe, consumido como alimento.', 1, 2, 3),    
(36, 'Laranja', 1 'fruta cítrica, suculenta e doce.', 0, 3, 1); 

INSERT INTO missao(id, item, lugar, nome, descricao)
VALUES
(1, 'chave oficina A', 1, 'Fuja da solitaria oeste', 'Escape da cela de isolamento leste sem ser pego.'),                           
(2, 'chave oficina B', 9, 'Fuja da solitaria leste', 'Escape da cela de isolamento oeste sem ser pego.'),                           
(3, 'BANDAGEM', 5, 'Observar cela', 'Observe e memorize os detalhes da cela para planejar uma fuga.'),             
(4, 'FACA PEQUENA', 'NULL', 'Escolher gangue', 'Escolha a gangue com a qual se aliar na prisão.'),                            
(5, 'NULL', 'NULL', 'explorar o mapa', 'Explore os locais no mapa da prisão, para um melhor entendimento do mesmo.'), 
(6, 'CARNE', 'NULL', 'Brigue com alguém', 'Inicie e participe de uma briga com outro prisioneiro.'),                     
(7, 'REMEDIO', 'NULL', 'Vença uma briga', 'Vença uma briga contra qualquer prisioneiro.'),                                                            
(8, 'NULL', 'NULL', 'Fuja da prisão', 'Fuja da prisão e reconquiste a sua liberdade.'),                                                             
(9, 'pedaco grande de metal', 'NULL', 'encontre o informante', 'encontre o informante que está infiltrado na prisão.'),                                                      
(10, 'Isqueiro', 24, 'vença um jogo de basquete', 'vença um jogo de basquete contra os outros presos.'),                                                  
(11, 'CARNE', 23, 'Fique maromba', 'Va na academia.');                                                             


INSERT INTO livro_fabricacao(nome)
VALUES
('Livro de Crafts EASY'),
('Livro de Crafts HARD');

INSERT INTO fabricacao (item_fabricavel, livro_fabricacao) 
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 2),
(11, 2),
(12, 2),
(13, 2);

INSERT INTO lista_fabricacao (item_fabricavel, fabricacao, item) 
VALUES
(1, 1, 18),
(1, 1, 24),
(2, 2, 16),
(2, 2, 20),
(2, 2, 17),
(3, 3, 15),
(3, 3, 16),
(4, 4, 20),
(4, 4, 16),
(4, 4, 22),
(5, 5, 16),
(5, 5, 18),
(6, 6, 24),
(7, 7, 20),
(7, 7, 22),
(8, 8, 18),
(9, 9, 14),
(9, 9, 22),
(10, 10, 18),
(10, 10, 22),
(11, 11, 23),
(11, 11, 21),
(11, 11, 22),
(12, 12, 6),
(12, 12, 19),
(13, 13, 23);

INSERT INTO instancia_item ( item, lugar, regiao, inventario, pessoa) 
VALUES
(1, 28, 6, NULL, NULL),
(2, 28, 6, NULL, NULL),
(3, 29, 6, NULL, NULL),
(4, 29, 6, NULL, NULL),
(5, 28, 6, NULL, NULL),
(6, 29, 6, NULL, NULL),
(7, 11, 2, NULL, NULL),
(8, 11, 2, NULL, NULL),
(9, 8, 1, NULL, NULL),
(10, 6, 1, NULL, NULL),
(11, 7, 1, NULL, NULL),
(12, 6, 1, NULL, NULL),
(13, 27, 5, NULL, NULL),
(14, 12, 2, NULL, NULL),
(15, 26, 5, NULL, NULL),
(16, 26, 5, NULL, NULL),
(17, 16, 3, NULL, NULL),
(18, 28, 6, NULL, NULL),
(19, 3, 1, NULL, NULL),
(20, 4, 1, NULL, NULL),
(21, 16, 3, NULL, NULL),
(22, 16, 3, NULL, NULL),
(23, 16, 3, NULL, NULL),
(24, 19, 3, NULL, NULL),
(25, 4, 1, NULL, NULL),
(26, 1, 1, NULL, NULL),
(27, 13, 5, NULL, NULL),
(28, 17, 3, NULL, NULL),
(29, 18, 3, NULL, NULL),
(30, 19, 3, NULL, NULL),
(31, 20, 4, NULL, NULL),
(32, 20, 4, NULL, NULL),
(33, 20, 4, NULL, NULL),
(34, 21, 4, NULL, NULL),
(35, 21, 4, NULL, NULL),
(36, 21, 4, NULL, NULL),
(14, 11, 2, NULL, NULL),
(15, 11, 2, NULL, NULL),
(16, 8, 1, NULL, NULL),
(17, 8, 1, NULL, NULL),
(18, 12, 2, NULL, NULL),
(19, 12, 2, NULL, NULL),
(20, 19, 3, NULL, NULL),
(21, 19, 3, NULL, NULL),
(22, 6, 1, NULL, NULL),
(23, 6, 1, NULL, NULL),
(24, 27, 5, NULL, NULL),
(25, 27, 5, NULL, NULL),
(26, 16, 3, NULL, NULL),
(27, 16, 3, NULL, NULL),
(14, 26, 5, NULL, NULL),
(15, 26, 5, NULL, NULL),
(16, 1, 1, NULL, NULL),
(17, 1, 1, NULL, NULL),
(18, 3, 1, NULL, NULL),
(19, 3, 1, NULL, NULL),
(20, 4, 1, NULL, NULL),
(21, 4, 1, NULL, NULL),
(22, 28, 6, NULL, NULL),
(23, 28, 6, NULL, NULL),
(1, NULL, NULL, 2, 2),
(20, NULL, NULL, 2, 2),
(2, NULL, NULL, 3, 3),
(18, NULL, NULL, 3, 3),
(10, NULL, NULL, 4, 4),
(2, NULL, NULL, 4, 4),
(20, NULL, NULL, 5, 5),
(33, NULL, NULL, 5, 5),
(3, NULL, NULL, 6, 6),
(36, NULL, NULL, 6, 6),
(17, NULL, NULL, 7, 7),
(12, NULL, NULL, 7, 7),
(10, NULL, NULL, 8, 8),
(4, NULL, NULL, 8, 8),
(9, NULL, NULL, 9, 9),
(31, NULL, NULL, 9, 9),
(27, NULL, NULL, 10, 10),
(5, NULL, NULL, 10, 10),
(23, NULL, NULL, 11, 11),
(21, NULL, NULL, 11, 11),
(24, NULL, NULL, 12, 12),
(10, NULL, NULL, 12, 12),
(16, NULL, NULL, 13, 13),
(9, NULL, NULL, 13, 13),
(27, NULL, NULL, 14, 14),
(25, NULL, NULL, 14, 14),
(26, NULL, NULL, 15, 15),
(28, NULL, NULL, 15, 15),
(25, NULL, NULL, 16, 16),
(30, NULL, NULL, 16, 16),
(23, NULL, NULL, 17, 17),
(21, NULL, NULL, 17, 17),
(23, NULL, NULL, 18, 18),
(22, NULL, NULL, 18, 18),
(11, NULL, NULL, 19, 19),
(28, NULL, NULL, 19, 19),
(12, NULL, NULL, 20, 20),
(20, NULL, NULL, 20, 20);

COMMIT;
```

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                | Autores                                          |
| :--------: | :----: | ------------------------ | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.    | [João Antonio G.](https://github.com/joaoseisei) |
| 07/08/2024 | `1.1`  | Adiciona fabricacao.     | [João Antonio G.](https://github.com/joaoseisei) |
| 07/08/2024 | `1.2`  | adição parte do fernando | [Fernando Gabriel](https://github.com/show-dawn) |


</div>