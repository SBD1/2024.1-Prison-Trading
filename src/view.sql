-- --------------------------------------------------------------------------------------
-- Data de Criação ........: 30/08/2024                                                --
-- Autor(es) ..............: Breno A., Fernando Gabriel, João A. e Julio Cesar         --
-- Versão .................: 1.0                                                       --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descrição ..............: Adiciona view                                             --
-- --------------------------------------------------------------------------------------

BEGIN;

---------------------
---
---   DETALHES DO LUGAR DO JOGADOR
---
---------------------

CREATE VIEW detalhes_lugar AS
	SELECT lug.id, lug.nome, lug.descricao
	FROM jogador jog
	LEFT JOIN lugar lug ON lug.id = jog.lugar;

---------------------
---
---   DETALHES DA REGIÃO DO JOGADOR
---
---------------------

CREATE VIEW detalhes_regiao AS
	SELECT reg.id, reg.nome, reg.descricao
	FROM jogador jog
	LEFT JOIN regiao reg ON reg.id = jog.regiao;

---------------------
---
---   TABELA ORIGEM DESTINO DETALHADA COM NOMES
---
---------------------

CREATE VIEW lugares_ori_des_detalhado AS
	SELECT lug.id, lug.nome
	FROM lugar_origem_destino ori
	JOIN lugar lug ON ori.lugar_destino = lug.id
	JOIN regiao reg ON lug.regiao = reg.id
	ORDER BY lug.nome;

---------------------
---
---   TABELAS DE PESSOAS EM LUGARES
---
---------------------

CREATE VIEW pessoas_lugar AS
	WITH Pessoas AS (
		SELECT id, nome, lugar FROM jogador
		UNION ALL
		SELECT id, nome, lugar FROM policial
		UNION ALL
		SELECT id, nome, lugar FROM prisioneiro
		UNION ALL
		SELECT id, nome, lugar FROM informante
	)
	SELECT pes.id, pes.nome, tip.tipo
	FROM pessoas pes, pessoa tip
	WHERE pes.id = tip.id
	ORDER BY tip.tipo, pes.id;

---------------------
---
---   INSTANCIA COM NOMES DOS ITENS
---
---------------------

CREATE VIEW instancias_detalhadas AS
	SELECT ins.item,
			COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome,
			COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) AS tamanho
	FROM instancia_item ins
	LEFT JOIN arma arm ON arm.id = ins.item
	LEFT JOIN ferramenta fer ON fer.id = ins.item
	LEFT JOIN comida com ON com.id = ins.item
	LEFT JOIN medicamento med ON med.id = ins.item
	LEFT JOIN utilizavel uti ON uti.id = ins.item
	ORDER BY nome;

---------------------
---
---   ITENS NO INVENTÁRIO DA PESSOA
---
---------------------

CREATE VIEW itens_inventario AS
	SELECT inst.id, inv.id, inv.inventario_ocupado, inv.tamanho,
		COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
	FROM inventario AS inv
	JOIN instancia_item AS inst ON inv.id = inst.inventario
	LEFT JOIN arma AS arm ON arm.id = inst.item
	LEFT JOIN ferramenta AS fer ON fer.id = inst.item
	LEFT JOIN comida AS com ON com.id = inst.item
	LEFT JOIN medicamento AS med ON med.id = inst.item
	LEFT JOIN utilizavel AS uti ON uti.id = inst.item
	ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);

---------------------
---
---   TABELA DETALHANDO UM ITEM ESPECIFICO
---
---------------------

CREATE VIEW info_item AS
	SELECT
	    COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome,
	    COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) AS tamanho,
	    COALESCE(arm.descricao, fer.descricao, com.descricao, med.descricao, uti.descricao) AS descricao,
	    arm.dano AS dano,
	    fer.utilidade AS utilidade,
	    COALESCE(com.raridade, med.raridade, uti.raridade) AS raridade,
	    COALESCE(com.quantidade, med.quantidade, uti.quantidade) AS quantidade,
	    com.recuperacao_vida AS recuperacao_vida,
	    med.cura AS cura,
	    uti.durabilidade AS durabilidade,
	    CASE
	        WHEN arm.nome IS NOT NULL THEN 'arma'
	        WHEN fer.nome IS NOT NULL THEN 'ferramenta'
	        WHEN com.nome IS NOT NULL THEN 'comida'
	        WHEN med.nome IS NOT NULL THEN 'medicamento'
	        WHEN uti.nome IS NOT NULL THEN 'utilizavel'
	        ELSE 'desconhecido'
	    END AS tipo
	FROM item AS i
	LEFT JOIN arma AS arm ON arm.id = i.id
	LEFT JOIN ferramenta AS fer ON fer.id = i.id
	LEFT JOIN comida AS com ON com.id = i.id
	LEFT JOIN medicamento AS med ON med.id = i.id
	LEFT JOIN utilizavel AS uti ON uti.id = i.id;

---------------------
---
---   ITENS PARA FAZER UM CRAFT
---
---------------------

CREATE VIEW craft_item AS
	SELECT inst.item_fabricavel, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
	FROM lista_fabricacao AS inst
	LEFT JOIN arma AS arm ON arm.id = inst.item
	LEFT JOIN ferramenta AS fer ON fer.id = inst.item
	LEFT JOIN comida AS com ON com.id = inst.item
	LEFT JOIN medicamento AS med ON med.id = inst.item
	LEFT JOIN utilizavel AS uti ON uti.id = inst.item
	ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);

---------------------
---
---   CRAFTS DE UM LIVRO
---
---------------------

CREATE VIEW itens_livro_fabricacao AS
	SELECT fabricacao.livro_fabricacao, fabricacao.id, COALESCE(arma.nome, ferr.nome) AS nome
	FROM fabricacao
	LEFT JOIN arma arma ON fabricacao.item_fabricavel = arma.id
	LEFT JOIN ferramenta ferr ON fabricacao.item_fabricavel = ferr.id
	ORDER BY fabricacao.id;


GRANT SELECT ON itens_livro_fabricacao TO prison_trading_user;
GRANT SELECT ON craft_item TO prison_trading_user;
GRANT SELECT ON detalhes_lugar TO prison_trading_user;
GRANT SELECT ON detalhes_regiao TO prison_trading_user;
GRANT SELECT ON lugares_ori_des_detalhado TO prison_trading_user;
GRANT SELECT ON pessoas_lugar TO prison_trading_user;
GRANT SELECT ON instancias_detalhadas TO prison_trading_user;
GRANT SELECT ON itens_inventario TO prison_trading_user;
GRANT SELECT ON info_item TO prison_trading_user;

COMMIT;
