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

INSERT INTO item_nao_fabricavel(id, tipo)
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
(26, 'utilizavel'),
(27, 'utilizavel'),
(28, 'medicamento'),
(29, 'medicamento'),
(30, 'medicamento'),
(31, 'comida'),
(32, 'comida'),
(33, 'comida'),
(34, 'comida'),
(35, 'comida'),
(36, 'comida'),
(37, 'utilizavel'),
(38, 'utilizavel'),
(39, 'utilizavel');


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

INSERT INTO utilizavel(id, nome, tamanho, descricao, raridade, quantidade, durabilidade)
VALUES
(14, 'Sabao', 1, 'Serve para remover sujeira e impurezas de superfícies e objetos, também é um material para fabricação de itens.', 0, 1, 1),
(15, 'Pedra', 1, 'A pedra serve para construção e também é um material para fabricação de itens.', 0, 3, 1),
(16, 'Graveto', 1, 'Produto de origem vegetal, é usado como material para fabricação de itens.', 0, 3, 1),
(17, 'Linha', 1, 'Fio fino e flexível utilizado como material para fabricação de itens.', 0, 3, 1),
(18, 'Pedaco pequeno de metal', 1, 'Material para fabricação de itens.', 1, 3, 1),
(19, 'Vidro', 1, 'Utilizado como material para fabricação de cerol.', 0, 1, 1),
(20, 'Pedaco grande de metal', 3, 'Material para fabricação de itens pesados.', 2, 1, 1),
(21, 'Alcool', 1, 'Utilizado como material para fabricação de coquetel molotov e garrafa quebrada.', 1, 1, 1),
(22, 'Tecido', 1, 'Utilizado como material para fabricação de explosivos.', 1, 3, 1),
(23, 'Garrafa de vidro', 2, 'Utilizado como material para fabricação de coquetel molotov e garrafa quebrada.', 1, 1, 1),
(24, 'Plastico', 1, 'Material versátil utilizado para várias criações.', 0, 3, 1),
(25, 'Isqueiro', 1, 'Dispositivo portátil utilizado para gerar fogo, podendo ser utilizado para queimar coisas.', 1, 1, 1),
(26, 'Lanterna', 1, 'Dispositivo portátil que emite luz.', 1, 1, 1),
(27, 'Cigarro', 1, 'Moeda de troca do jogo, além de poder ser utilizado para acalmar.', 1, 10, 1),
(37, 'Cracha', 1, 'Crachá de identificação, item ultra raro que pode ser usado para ativar a entrada.', 2, 1, 1),
(38, 'Chave Oficina A', 1, 'Chave usada para abrir a oficina A.', 2, 1, 1),
(39, 'Chave Oficina B', 1, 'Chave usada para abrir a oficina B.', 2, 1, 1);



INSERT INTO medicamento(id, nome, tamanho, descricao, raridade, cura, quantidade)
VALUES
(28, 'Anti-inflamatorio', 1, 'Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.', 2, 3, 5),
(29, 'Morfina', 1, 'Analgésico opiáceo potente utilizado para aliviar dores intensas.', 1, 10, 2),
(30, 'Bandagem', 1, 'Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo.', 0, 2, 5);

INSERT INTO comida(id, nome, tamanho, descricao, raridade, quantidade, recuperacao_vida)
VALUES
(31, 'Pao seco', 1, 'Um pão tão seco e duro, que parece que o próprio vendendor amassou ele.', 0, 1, 0),
(32, 'Pao', 1, 'Alimento básico feito a partir de farinha, água e fermento.', 0, 3, 1),
(33, 'Queijo', 1, 'Produto lácteo sólido feito a partir da coagulação do leite.', 0, 3, 1),
(34, 'Carne', 2, 'Tecido muscular de animais, como bovinos ou suínos, consumido como alimento.', 2, 1, 5),
(35, 'Peixe', 1, 'Tecido muscular de peixe, consumido como alimento.', 1, 2, 3),
(36, 'Laranja', 1, 'Fruta cítrica, suculenta e doce.', 0, 3, 1);

INSERT INTO missao (item_nao_fabricavel, lugar, regiao, nome, descricao)
VALUES
(38, 1, 1, 'Fuja da solitaria oeste', 'Escape da cela de isolamento leste sem ser pego.'),
(39, 9, 1, 'Fuja da solitaria leste', 'Escape da cela de isolamento oeste sem ser pego.'),
(30, 5, 1, 'Observar cela', 'Observe e memorize os detalhes da cela para planejar uma fuga.'),
(27, NULL, NULL, 'Escolher gangue', 'Escolha a gangue com a qual se aliar na prisão.'),
(NULL, NULL, NULL, 'explorar o mapa', 'Explore os locais no mapa da prisão, para um melhor entendimento do mesmo.'),
(34, NULL, NULL, 'Brigue com alguém', 'Inicie e participe de uma briga com outro prisioneiro.'),
(29, NULL, NULL, 'Vença uma briga', 'Vença uma briga.'),
(NULL, NULL, NULL, 'Fuja da prisão', 'Fuja da prisão.'),
(20, NULL, NULL, 'Encontre o informante', 'Encontre o informante.'),
(25, 25, 6, 'Venca um jogo de basquete', 'Vença um jogo de basquete.'),
(34, 24, 6, 'Fique maromba', 'Vá na academia.');

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

INSERT INTO Pessoa (tipo) VALUES
('jogador'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('prisioneiro'),
('policial'),
('policial'),
('policial'),
('policial'),
('policial'),
('informante'),
('informante');

INSERT INTO Inventario (pessoa, inventario_ocupado, tamanho) VALUES
(1, 0, 5),
(2, 4, 5),
(3, 3, 5),
(4, 3, 5),
(5, 4, 5),
(6, 3, 5),
(7, 2, 5),
(8, 3, 5),
(9, 2, 5),
(10, 2, 5),
(11, 3, 5),
(12, 2, 5),
(13, 2, 5),
(14, 2, 5),
(15, 2, 5),
(16, 2, 5),
(17, 3, 5),
(18, 3, 5),
(19, 2, 5),
(20, 4, 5);

INSERT INTO Prisioneiro (id, nome, habilidade_briga, vida, força, gangue, lugar) VALUES
(2, 'Rivas', 4, 9, 7, 'palhaco', 'Quadra De Basquete'),
(3, 'Filomano', 6, 7, 4, 'Polvos', 'celaB'),
(4, 'Fragas', 5, 11, 5, 'Palhacos', 'banheiroA'),
(5, 'Glaucão', 3, 6, 8, 'Polvos', 'mesaEsquerda'),
(6, 'Ucraniano', 7, 5, 6, 'Palhacos', 'celaC'),
(7, 'Rispomático', 6, 12, 6, 'Polvos', 'academiaSimples'),
(8, 'Manogaz', 4, 8, 5, 'Palhacos', 'celaG'),
(9, 'Dado', 5, 10, 6, 'Polvos', 'banheiroB'),
(10, 'Fabrilton', 4, 7, 5, 'Palhacos', 'mesaDireita'),
(11, 'Eneido', 6, 6, 6, 'Polvos', 'solitariaOeste'),
(12, 'Carlos', 5, 9, 7, 'Palhacos', 'arquibancada'),
(13, 'Silvio Serra', 6, 8, 5, 'Polvos', 'celaE');

INSERT INTO Policial (id, nome, lugar, corrupto) VALUES
(14, 'Italo Dimetrio', 'solitariaOeste', true),
(15, 'Sargento Nascimento', 'mesaDireita', false),
(16, 'Capitão Mathias', 'Quadra De Basquete', false),
(17, 'Capitão Brad', 'solitariaLeste', true),
(18, 'Lil Chico', 'arquibancada', true);

INSERT INTO Informante (id, nome, dano_infomante, lugar) VALUES
(19, 'Cubano', 200, 'banheiroC'),
(20, 'Chileno', 200, 'Enfermaria A');

INSERT INTO Jogador (id, nome, habilidade_briga, vida, força, tempo_vida, gangue, lugar, missao, nivel) VALUES
(1, 'Carimbo', 2, 5, 3, 10, null, 'celaA', null, 0);


INSERT INTO prisao(id, nome, descricao)
VALUES
(1, 'Basilio', 'Uma prisão cercada por muralhas altas, com uma floresta que separa ela da cidade mais próxima.');

INSERT INTO regiao(id, nome, prisao, descricao)
VALUES
(1, 'Celas', 1, 'Local onde estão as celas e solitárias dos prisioneiros.'),
(2, 'Banheiros', 1, 'Local onde os prisioneiros se banham.'),
(3, 'Enfermaria', 1, 'Local onde os prisioneiros podem se tratar/curar.'),
(4, 'Administracao', 1, 'Local onde tem o controle geral elétrico da prisão.'),
(5, 'Refeitorio', 1, 'Local onde os prisioneiros fazem suas refeições.'),
(6, 'Patio', 1, 'Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete e relaxar.'),
(7, 'Oficinas', 1, 'Local onde os prisioneiros trabalham e ganham um pouco de dinheiro.'),
(8, 'Exterior', 1, 'Localização fora da prisão.');

INSERT INTO lugar(id, nome, regiao, descricao, rota_final_fuga)
VALUES
(1, 'Solitaria  Oeste', 1, 'Sala escura para os prisioneiros indisciplinados. Na parede direita há uma mancha de cimento fresco.', false),
(2, 'Cela A', 1, 'Cela velha com 178 riscos na parede e o piso está rachado e com partes soltas.', false),
(3, 'Cela B', 1, 'Cela com uma beliche e há varias camisinhas de sabor pequi espalhadas embaixo dela.', false),
(4, 'Cela C', 1, 'Cela que fede a azeitona em conserva. Tem vários desenhos da folha de oliva e de azeitonas na parede.', false),
(5, 'Cela D', 1, 'Cela normal. Exceto pela montanha de pelos castanhos misturada com uma gosma preta no meio cela.', false),
(6, 'Cela E', 1, 'Cela com piso e paredes marrom. Barras enferrujadas. Camas marrom.', false),
(7, 'Cela F', 1, 'Cela com posteres de mulheres nuas nas paredes. O piso é da cor bege sujo. Há um buraco de rato na parede.', false),
(8, 'Cela G', 1, 'Cela normal. Tem 321 nomes escritos na parede. No teto há varios bonecos de palha pendurados pelo pescoço.', false),
(9, 'Solitaria Leste', 1, 'Sala escura para os prisioneiros indisciplinados. Ela fede a álcool por algum motivo.', false),
(10, 'Corredor Celas', 1, 'Corredor para se deslocar entre as celas e as solitárias.', false),
(11, 'Banheiro A', 2, 'Banheiro onde os prisioneiros tomam banho.', false),
(12, 'Banheiro B', 2, 'Banheiro onde os prisioneiros tomam banho.', false),
(13, 'Banheiro C', 2, 'Banheiro quebrado em manutenção com a porta trancada.', false),
(14, 'Banheiro D', 2, 'Banheiro onde os prisioneiros tomam banho.', false),
(15, 'Corredor Banheiros', 2, 'Corredor para se deslocar entre os banheiros e os corredores da enfermaria e do refeitório.', false),
(16, 'Sala A', 3, 'Sala com uma maca e armário com remédios e kits de primeiro-socorro.', false),
(17, 'Sala B', 3, 'Sala com uma maca e armário com remédios e kits de primeiro-socorro.', false),
(18, 'Sala C', 3, 'Sala com uma maca e armário com remédios e kits de primeiro-socorro.', false),
(19, 'Corredor Enfermaria', 3, 'Corredor para se deslocar entre as salas da enfermaria e a sala de controle.', false),
(20, 'Sala De Controle', 4, 'Sala onde tem o controle da prisão, no final do corredor da enfermaria. Há um uniforme policial do lado da mesa.', false),
(21, 'Mesa Esquerda', 5, 'Mesa onde a gangue 1 faz suas refeições.', false),
(22, 'Mesa Direita', 5, 'Mesa onde a gangue 2 faz suas refeições.', false),
(23, 'Corredor Refeitorio', 5, 'Corredor para se deslocar entre as mesas do refeitório e os corredores dos banheiros e do pátio.', false),
(24, 'Academia Simples', 6, 'Uma área com equipamentos simples de exercício.', false),
(25, 'Quadra De Basquete', 6, 'Quadra onde os prisioneiros jogam basquete para se distrair e se exercitar.', false),
(26, 'Arquibancada', 6, 'Arquibancada onde os prisioneiros podem conversar e assistir os jogos.', false),
(27, 'Area De Lazer', 6, 'Bancos onde os prisioneiros podem sentar e conversar. Há um área no chão com terra fresca.', false),
(28, 'Corredor Patio', 6, 'Corredor para se deslocar entre as áreas do pátio, as oficinas e entrada.', false),
(29, 'Oficina A', 7, 'Oficina de marcenaria onde os prisioneiros trabalham.', false),
(30, 'Oficina B', 7, 'Oficina de impressão de placas de carro onde os prisioneiros trabalham', false),
(31, 'Esgoto', 8, 'Local subterrâneo apertado que dá para fora da prisão.', true),
(32, 'Entrada', 8, 'Local onde os policias e prisioneiros entram e sai da prisão que dá no corredor do pátio.', true),
(33, 'Floresta', 8, 'Local cheio de árvores adjacente a prisão.', true);

INSERT INTO lugar_origem_destino (lugar_origem, regiao_origem, lugar_destino, regiao_destino)
VALUES
(1, 1, 2, 1),
(1, 1, 10, 1),
(2, 1, 1, 1),
(2, 1, 10, 1),
(3, 1, 10, 1),
(4, 1, 10, 1),
(5, 1, 10, 1),
(6, 1, 10, 1),
(7, 1, 10, 1),
(8, 1, 10, 1),
(9, 1, 10, 1),
(10, 1, 1, 1),
(10, 1, 2, 1),
(10, 1, 3, 1),
(10, 1, 4, 1),
(10, 1, 5, 1),
(10, 1, 6, 1),
(10, 1, 7, 1),
(10, 1, 8, 1),
(10, 1, 9, 1),
(10, 1, 15, 2),
(11, 2, 15, 2),
(12, 2, 15, 2),
(13, 2, 15, 2),
(13, 2, 31, 8),
(14, 2, 15, 2),
(15, 2, 10, 1),
(15, 2, 11, 2),
(15, 2, 12, 2),
(15, 2, 13, 2),
(15, 2, 14, 2),
(15, 2, 19, 3),
(15, 2, 23, 5),
(16, 3, 17, 3),
(16, 3, 19, 3),
(17, 3, 16, 3),
(17, 3, 18, 3),
(17, 3, 19, 3),
(18, 3, 17, 3),
(18, 3, 19, 3),
(19, 3, 15, 2),
(19, 3, 16, 3),
(19, 3, 17, 3),
(19, 3, 18, 3),
(19, 3, 20, 4),
(20, 4, 19, 3),
(21, 5, 23, 5),
(22, 5, 23, 5),
(23, 5, 15, 2),
(23, 5, 21, 5),
(23, 5, 22, 5),
(23, 5, 28, 6),
(24, 6, 25, 6),
(24, 6, 28, 6),
(25, 6, 24, 6),
(25, 6, 26, 6),
(25, 6, 28, 6),
(26, 6, 25, 6),
(26, 6, 27, 6),
(26, 6, 28, 6),
(27, 6, 26, 6),
(27, 6, 28, 6),
(27, 6, 33, 8),
(28, 6, 23, 5),
(28, 6, 24, 6),
(28, 6, 25, 6),
(28, 6, 26, 6),
(28, 6, 27, 6),
(28, 6, 29, 7),
(28, 6, 30, 7),
(28, 6, 32, 8),
(29, 7, 28, 6),
(30, 7, 28, 6),
(31, 8, 13, 2),
(32, 8, 28, 6),
(33, 8, 27, 6);


COMMIT;
```

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                | Autores                                                                                                                                       |
| :--------: | :----: | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 28/07/2024 | `1.0`  | Criação do documento.    | [João Antonio G.](https://github.com/joaoseisei)                                                                                              |
| 07/08/2024 | `1.1`  | Adiciona fabricacao.     | [João Antonio G.](https://github.com/joaoseisei)                                                                                              |
| 07/08/2024 | `1.2`  | adição parte do fernando | [Fernando Gabriel](https://github.com/show-dawn)                                                                                              |
| 07/08/2024 | `1.3`  | Adiciona parte do Júlio. | [Júlio Cesar](https://github.com/Julio1099)                                                                                                   |
| 10/08/2024 | `1.4`  | corrige dml              | [Júlio Cesar](https://github.com/Julio1099),[Fernando Gabriel](https://github.com/show-dawn),[João Antonio G.](https://github.com/joaoseisei) |
| 12/08/2024 | `1.5`  | Adiciona parte do bob.   | [Breno Alexandre](https://github.com/brenoalexandre0)                                                                                         |
| 13/08/2024 | `1.6`  | Edita parte do bob.      | [Breno Alexandre](https://github.com/brenoalexandre0)                                                                                         |
| 14/08/2024 | `1.4`  | corrige dml              | [João Antonio G.](https://github.com/joaoseisei),[Fernando Gabriel](https://github.com/show-dawn)                                             |

</div>
