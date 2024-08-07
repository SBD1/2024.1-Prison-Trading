<center>

# Linguagem de Manipulação de Dados - DML

</center>

---

> O que é?

---

```

INSERT INTO item(tipo_item)
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

INSERT INTO item_fabricavel(id_item, tipo_fabricavel)
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

INSERT INTO ferramenta(id_item, nome_item, tamanho_item, descricao_item, utilidade_ferramenta)
VALUES
(1, 'Chave de Fenda', 1, 'Ferramenta com ponta plana ou cruzada para apertar ou soltar parafusos.', 'Usada para desmontar objetos.'),
(2, 'Pa', 2, 'Ferramenta com lâmina larga e plana para cavar e mover materiais.', 'Ideal para escavar ou remover detritos.'),
(3, 'Martelo', 2, 'Ferramenta com cabeça pesada usada para bater pregos ou quebrar objetos.', 'Usado em construção e demolição.'),
(4, 'Picareta', 2, 'Ferramenta com uma extremidade pontiaguda e outra achatada, usada para quebrar superfícies duras.', 'Ideal para mineração ou demolição.'),
(5, 'Lock Pick', 1, 'Ferramenta fina e estreita usada para destrancar fechaduras sem chave.', 'Utilizada para abrir fechaduras de forma furtiva.'),
(6, 'Corda', 1, 'Cordão grosso feito de fibras entrelaçadas.', 'Usada para amarrar, puxar ou escalar.');

INSERT INTO arma(id_item, nome_item, tamanho_item, descricao_item, dano_arma)
VALUES
(7, 'Faca', 2, 'Lâmina afiada e curta usada para cortar ou perfurar.', 3),
(8, 'Agulha', 1, 'Ferramenta fina e pontiaguda, geralmente usada para costura.', 1),
(9, 'Soco Ingles', 1, 'Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo.', 2),
(10, 'Faca Curta', 1, 'Pequena faca com lâmina curta, fácil de esconder.', 2),
(11, 'Coquetel Molotov', 1, 'Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.', 5),
(12, 'Corda com Cerol', 1, 'Corda revestida com vidro moído para causar cortes.', 3),
(13, 'Garrafa Quebrada', 1, 'Garrafa de vidro quebrada, usada como arma cortante.', 3);

INSERT INTO utilizavel(id_item, nome_item, tamanho_item, descricao_efeito, raridade, quantidade)
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

INSERT INTO medicamento(id_item, nome_item, tamanho_item, descricao, raridade, cura, quantidade)
VALUES
(28, 'anti-inflamatorio', 1, 'Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.', 2, 3, 5),          
(29, 'Morfina', 1, 'Analgésico opiáceo potente utilizado para aliviar dores intensas.', 1, 10, 2),          
(30, 'Bandagem', 1, 'Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo.', 0, 2, 5);         

INSERT INTO medicamento(id_item, nome_item, tamanho_item, descricao, raridade, quantidade, cura)
VALUES
(31, 'Pao seco', 1 'um pão tão seco e duro, que parece que o proprio vandor amassou ele.', 0, 1, 0),
(32, 'Pao', 1 'alimento básico feito a partir de farinha, água e fermento.', 0, 3, 1),    
(33, 'Queijo', 1 'produto lácteo sólido feito a partir da coagulação do leite.', 0, 3, 1),    
(34, 'Carne', 2 'é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento.', 2, 1, 5),    
(35, 'Peixe', 1 'tecido muscular de peixe, consumido como alimento.', 1, 2, 3),    
(36, 'Laranja', 1 'fruta cítrica, suculenta e doce.', 0, 3, 1);    

```

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                | Autores                                          |
| :--------: | :----: | ------------------------ | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.    | [João Antonio G.](https://github.com/joaoseisei) |
| 07/08/2024 | `1.1`  | adição parte do fernando | [Fernando Gabriel](https://github.com/show-dawn) |


</div>