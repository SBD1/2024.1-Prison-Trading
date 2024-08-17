-- --------------------------------------------------------------------------------------
-- Data de Criação ........: 17/08/20224                                               --
-- Autor(es) ..............:  Fernando Gabriel, João A. e Julio Cesar                  --
-- Versão .................: 1.0                                                       --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descrição ..............: Provaveis comandos que serão utilizados.                  --
-- --------------------------------------------------------------------------------------


-- Briga

-- Consultar os status de um prisioneiro
SELECT nome, habilidade_briga, vida, forca
FROM prisioneiro
WHERE id = <PRISIONEIRO>;

-- Consultar os status de um jogador
SELECT habilidade_briga, vida, forca
FROM jogador
WHERE id = <JOGADOR>;

-- Caso perder a luta

-- Caso perca dano, atualiza a vida
UPDATE jogador
SET vida = 1
WHERE id = <JOGADOR>;

-- Transfere o jogador para a enfermaria
UPDATE jogador
SET lugar = 16, regiao = 3
WHERE id = <JOGADOR>;

-- Diminui 1 dia do tempo de vida
UPDATE jogador
SET tempo_vida = 9
WHERE id = <JOGADOR>;

-- Atualiza a vida do jogador
UPDATE jogador
SET vida = 5
WHERE id = <JOGADOR>;

-- Caso vença a briga

-- Perde vida
UPDATE prisioneiro
SET vida = 1
WHERE id = <JOGADOR>;

-- Transfere o prisioneiro pra enfermaria
UPDATE prisioneiro
SET lugar = 16, regiao = 3
WHERE id = <PRISIONEIRO>;

-- Usar remedio

-- Verifica se tem remedio no inventário.
SELECT ins.item, med.nome, ins.id
FROM instancia_item ins
LEFT JOIN medicamento med
ON med.id = ins.item
WHERE ins.inventario = <INVENTARIO>
ORDER BY med.nome;

-- Caso tenha remedio atualiza a vida do jogador
UPDATE jogador
SET vida = 5
WHERE id = <JOGADOR>;

-- Usar Comida

-- Verifica se tem comida no inventario
SELECT ins.item, com.nome, ins.id
FROM instancia_item ins
LEFT JOIN comida com
ON com.id = ins.item
WHERE ins.inventario = <INVENTARIO>
ORDER BY com.nome;

-- Caso tenha comida, atualiza a vida do jogador
UPDATE jogador
SET vida = 5
WHERE id = <JOGADOR>;

-- Realizar um craft

-- Ver uma fabricação especifica
SELECT lis.item, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM lista_fabricacao lis
LEFT JOIN arma arm
ON arm.id = lis.item
LEFT JOIN ferramenta fer
ON fer.id = lis.item
LEFT JOIN comida com
ON com.id = lis.item
LEFT JOIN medicamento med
ON med.id = lis.item
LEFT JOIN utilizavel uti
ON uti.id = lis.item
WHERE lis.fabricacao = <FABRICACAO>
ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);

-- Consultar se o jogador possui os itens requeridos
SELECT t.item, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM instancia_item t
LEFT JOIN arma arm
ON arm.id = t.item
LEFT JOIN ferramenta fer
ON fer.id = t.item
LEFT JOIN comida com
ON com.id = t.item
LEFT JOIN medicamento med
ON med.id = t.item
LEFT JOIN utilizavel uti
ON uti.id = t.item
WHERE t.inventario = <JOGADOR> AND nome = <MATERIA_PRIMA>
ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);

-- Acessar o inventario Para consultar se tem espaço
SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = <JOGADOR>;

--- Deletar uma instancia de Item (materia prima)
DELETE FROM Instancia_Item
WHERE id = <ITEM>;

--- Criar uma instancia de Item (inventario)
INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
VALUES
(5, NULL, NULL, 7, 7);

--- Atualizar um inventario ocupado de uma Pessoa
UPDATE Inventario 
SET inventario_ocupado = <TAMANHO>
WHERE id = <ITEM>
AND pessoa = <JOGADOR>;

-- Realizar uma troca

-- Acessar o inventario Para consultar se tem espaço
SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = <JOGADOR>;

-- Transfere o item de uma pessoa
UPDATE instancia_item
SET pessoa = <PESSOA>, inventario = <INVENTARIO>
WHERE id = <ID>;

-- NECESSITA DE UM TERCEIRO PRA FAZER O SWAP UM TEMPORARIO, PODE SER UTILIZADO EM PYTHON.

--- Atualizar um inventario ocupado de uma Pessoa
UPDATE Inventario
SET inventario_ocupado = <TAMANHO>
WHERE id = <ITEM>
AND pessoa = <JOGADOR>;

-- Acessar o inventario Para consultar se tem espaço
SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = <JOGADOR>;

-- Transfere o item de outra pessoa
UPDATE instancia_item
SET pessoa = <PESSOA>, inventario = <INVENTARIO>
WHERE id = <ID>;

--- Atualizar um inventario ocupado de uma Pessoa
UPDATE Inventario
SET inventario_ocupado = <TAMANHO>
WHERE id = <ITEM>
AND pessoa = <JOGADOR>;

-- Pegar um item no chao

-- Acessar o inventario Para consultar se tem espaço
SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = <JOGADOR>;

-- Pega o item
UPDATE instancia_item
SET lugar = NULL, regiao = NULL, pessoa = <PESSOA>, inventario = <INVENTARIO>
WHERE id = <ID>;

--- Atualizar um inventario ocupado de uma Pessoa
UPDATE Inventario
SET inventario_ocupado = <TAMANHO>
WHERE id = <ITEM>
AND pessoa = <JOGADOR>;

--- Movimentação

-- Verifica os lugares onde a pessoa pode ir
SELECT lug.id
FROM lugar_origem_destino ori
JOIN lugar lug ON ori.lugar_destino = lug.id
JOIN regiao reg ON lug.regiao = reg.id
WHERE ori.lugar_origem = <LUGAR>
ORDER BY lug.nome;

-- Move a pessoa de lugar
UPDATE Jogador
SET lugar = <LUGAR>, regiao = <REGIAO>
WHERE id = <JOGADOR>;

-- Ver pessoas relacionadas a sala

-- Ver a sala atual
SELECT lug.nome, lug.descricao
FROM jogador jog
LEFT JOIN lugar lug ON lug.id = jog.lugar
WHERE jog.id = <JOGADOR>;

-- Ver as pessoas ligadas a essa sala
WITH Pessoas AS (
    SELECT id, nome, lugar FROM jogador
    UNION ALL
    SELECT id, nome, lugar FROM policial
    UNION ALL
    SELECT id, nome, lugar FROM prisioneiro
    UNION ALL
    SELECT id, nome, lugar FROM informante
)
SELECT pes.nome, tip.tipo
FROM pessoas pes, pessoa tip
WHERE pes.id = tip.id AND pes.lugar = <LUGAR>
ORDER BY tip.tipo, pes.nome;

-- Ver os itens relacionados a uma sala

-- Ver a sala atual
SELECT lug.nome, lug.descricao
FROM jogador jog
LEFT JOIN lugar lug ON lug.id = jog.lugar
WHERE jog.id = <JOGADOR>;

-- Ver os itens ligados a essa sala
SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM instancia_item ins
LEFT JOIN arma arm ON arm.id = ins.item
LEFT JOIN ferramenta fer ON fer.id = ins.item
LEFT JOIN comida com ON com.id = ins.item
LEFT JOIN medicamento med ON med.id = ins.item
LEFT JOIN utilizavel uti ON uti.id = ins.item
WHERE ins.lugar = %s
ORDER BY nome;

-- Ver todas as fabricações de um item especifico
SELECT COALESCE(arm.nome, fer.nome) AS nome
FROM lista_fabricacao lis
LEFT JOIN arma arm
ON arm.id = lis.fabricacao
LEFT JOIN ferramenta fer
ON fer.id = lis.fabricacao
WHERE lis.item = 20
ORDER BY COALESCE(arm.nome, fer.nome);

-- Consultar um livro especifico
SELECT COALESCE(arm.nome, fer.nome) AS nome
FROM fabricacao fab
LEFT JOIN arma arm
ON arm.id = fab.item_fabricavel
LEFT JOIN ferramenta fer
ON fer.id = fab.item_fabricavel
WHERE fab.livro_fabricacao = 2
ORDER BY COALESCE(arm.nome, fer.nome);

--- missao

---Ver o lugar que uma missão X está.
SELECT lugar.nome, lugar.descricao
FROM missao, lugar
WHERE missao.lugar = lugar.id AND missao.id = <LUGAR>;

--- estando no lugar certo

---Atualizar missao de um Jogador

UPDATE jogador 
SET missao = <MISSAO>
WHERE id = <JOGADOR>;

---Ver o item que uma missão X vai dar.
SELECT COALESCE(com.nome, uti.nome, med.nome) AS nome, COALESCE(com.descricao, uti.descricao, med.descricao) AS descricao
FROM missao mis
LEFT JOIN comida com
ON mis.item_nao_fabricavel = com.id
LEFT JOIN utilizavel uti
ON mis.item_nao_fabricavel = uti.id
LEFT JOIN medicamento med
ON mis.item_nao_fabricavel = med.id
WHERE mis.id = <JOGADOR>;

--- Caso Complete a missão

---Acessar o inventario Para consultar se tem espaço 

SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = <JOGADOR>;

---Caso tenha espaço

--- Criar uma instancia de Item (inventario)

INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
VALUES
(5, NULL, NULL, 7, 7);

--- Atualizar um inventario ocupado de uma Pessoa

UPDATE Inventario 
SET inventario_ocupado = <TAMANHO>
WHERE id = <ITEM>
AND pessoa = <JOGADOR>;
