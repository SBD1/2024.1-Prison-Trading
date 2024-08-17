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

