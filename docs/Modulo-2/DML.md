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
('fabricavel');

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

```

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição             | Autores                                          |
|:----------:|:------:|-----------------------|--------------------------------------------------|
| 28/07/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |
| 07/08/2024 | `1.1`  | Adiciona fabricacao.  | [João Antonio G.](https://github.com/joaoseisei) |

</div>