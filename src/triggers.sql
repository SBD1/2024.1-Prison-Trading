-- --------------------------------------------------------------------------------------
-- Data de Criação ........: 28/08/2024                                                --
-- Autor(es) ..............:  Fernando Gabriel, João A. e Julio Cesar                  --
-- Versão .................: 1.0                                                       --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descrição ..............: Adiciona Triggers de pessoa.                              --
-- --------------------------------------------------------------------------------------


---------------------
---
---   PESSOA
---
---------------------

CREATE FUNCTION insert_pessoa()
RETURNS trigger AS $insert_pessoa$
DECLARE
	id_pessoa INTEGER;
	tipo_pessoa TipoPessoa;
BEGIN
	id_pessoa = NEW.id;
	tipo_pessoa = NEW.tipo;

	RAISE NOTICE 'Id da pessoa é: % | Tipo da pessoa é: %', id_pessoa, tipo_pessoa;

	PERFORM 1 FROM prisioneiro WHERE id = id_pessoa;
	IF FOUND THEN
		RAISE EXCEPTION 'A pessoa com o id % e tipo % está na tabela prisioneiro, ação negada.', id_pessoa, tipo_pessoa;
	END IF;

	PERFORM 1 FROM policial WHERE id = id_pessoa;
	IF FOUND THEN
		RAISE EXCEPTION 'A pessoa com o id % e tipo % está na tabela policial, ação negada.', id_pessoa, tipo_pessoa;
	END IF;

	PERFORM 1 FROM informante WHERE id = id_pessoa;
	IF FOUND THEN
		RAISE EXCEPTION 'A pessoa com o id % e tipo % está na tabela informante, ação negada.', id_pessoa, tipo_pessoa;
	END IF;

	PERFORM 1 FROM jogador WHERE id = id_pessoa;
	IF FOUND THEN
		RAISE EXCEPTION 'A pessoa com o id % e tipo % está na tabela jogador, ação negada.', id_pessoa, tipo_pessoa;
	END IF;

	RAISE NOTICE 'O % não aparece em nenhuma outra tabela, a tupla é unica inserção em pessoa concedida.', tipo_pessoa;

	RETURN NEW;
END;
$insert_pessoa$ LANGUAGE plpgsql;

CREATE TRIGGER pessoa_insert
BEFORE INSERT ON pessoa
FOR EACH ROW EXECUTE PROCEDURE insert_pessoa();

CREATE FUNCTION update_pessoa()
RETURNS trigger AS $update_pessoa$
BEGIN
	IF NEW IS DISTINCT FROM OLD THEN
		-- Não permite alterar atributos de pessoa, pois isso pode causar erros de integridade
		-- relacionados à generalização total exclusiva.
		RAISE EXCEPTION 'Não é possível alterar os atributos da pessoa (id ou tipo).';
	END IF;

    RETURN NEW;
END;
$update_pessoa$ LANGUAGE plpgsql;

CREATE TRIGGER pessoa_update
BEFORE UPDATE ON pessoa
FOR EACH ROW EXECUTE PROCEDURE update_pessoa();

CREATE FUNCTION delete_pessoa()
RETURNS trigger AS $delete_pessoa$
DECLARE
	id_pessoa INTEGER;
	tipo_pessoa TipoPessoa;
BEGIN
	id_pessoa = OLD.id;
	tipo_pessoa = OLD.tipo;

	DELETE FROM instancia_item
	WHERE pessoa = id_pessoa;

	RAISE NOTICE 'O comando deleteou todas as instâncias de item referenciando a pessoa com id %.',id_pessoa;

	DELETE FROM inventario
	WHERE pessoa = id_pessoa;

	RAISE NOTICE 'O comando deleteou o inventário da pessoa com id %.',id_pessoa;

	IF tipo_pessoa = 'prisioneiro' THEN

		DELETE FROM prisioneiro
		WHERE id = id_pessoa;

		RAISE NOTICE 'O comando deletou o prisioneiro vinculado.';

	ELSIF tipo_pessoa = 'policial' THEN

		DELETE FROM policial
		WHERE id = id_pessoa;

		RAISE NOTICE 'O comando deletou o policial vinculado.';

	ELSIF tipo_pessoa = 'informante' THEN

		DELETE FROM informante
		WHERE id = id_pessoa;

		RAISE NOTICE 'O comando deletou o informante vinculado.';

	ELSIF tipo_pessoa = 'jogador' THEN

		DELETE FROM jogador
		WHERE id = id_pessoa;

		RAISE NOTICE 'O comando deletou o jogador vinculado.';

	ELSE
		RAISE NOTICE 'O % não aparece em nenhuma outra tabela, a tupla é unica.', id_pessoa;
	END IF;

	RETURN OLD;
END;
$delete_pessoa$ LANGUAGE plpgsql;

CREATE TRIGGER pessoa_delete
BEFORE DELETE ON pessoa
FOR EACH ROW EXECUTE PROCEDURE delete_pessoa();

---------------------
---
---   JOGADOR
---
---------------------

CREATE FUNCTION insert_jogador()
RETURNS trigger AS $insert_jogador$
DECLARE
    jogador_id INTEGER;
BEGIN
	INSERT INTO pessoa (tipo)
	VALUES ('jogador')
	RETURNING id INTO jogador_id;

	INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
	VALUES (jogador_id, 0, 5);

    RAISE NOTICE 'Criação do inventário do jogador bem sucedida.';

	NEW.id = jogador_id;

	RAISE NOTICE 'Id do jogador é: %', jogador_id;

    RETURN NEW;

END;
$insert_jogador$ LANGUAGE plpgsql;

CREATE TRIGGER jogador_insert
BEFORE INSERT ON jogador
FOR EACH ROW EXECUTE PROCEDURE insert_jogador();

CREATE FUNCTION update_jogador()
RETURNS trigger AS $update_jogador$
BEGIN
	IF NEW.id <> OLD.id THEN
		-- Não deixa alterar id de jogador, se deixar tem q alterar pessoa, inventario e
		-- Instancias de item referenciando o inventario e pessoa.
		RAISE EXCEPTION 'Não é possível alterar o id do jogador.';
	END IF;

    RETURN NEW;

END;
$update_jogador$ LANGUAGE plpgsql;

CREATE TRIGGER jogador_update
BEFORE update ON jogador
FOR EACH ROW EXECUTE PROCEDURE update_jogador();


---------------------
---
---   PRISIONEIRO
---
---------------------

CREATE FUNCTION insert_prisioneiro()
RETURNS trigger AS $insert_prisioneiro$
DECLARE
    prisioneiro_id INTEGER;
BEGIN
	INSERT INTO pessoa (tipo)
	VALUES ('prisioneiro')
	RETURNING id INTO prisioneiro_id;

	INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
	VALUES (prisioneiro_id, 0, 5);

	RAISE NOTICE 'Criação do inventário do prisioneiro bem sucedida.';

	NEW.id = prisioneiro_id;

	RAISE NOTICE 'Id do prisioneiro é: %', prisioneiro_id;

    RETURN NEW;

END;
$insert_prisioneiro$ LANGUAGE plpgsql;

CREATE TRIGGER prisioneiro_insert
BEFORE INSERT ON prisioneiro
FOR EACH ROW EXECUTE PROCEDURE insert_prisioneiro();

CREATE FUNCTION update_prisioneiro()
RETURNS trigger AS $update_prisioneiro$
BEGIN
	IF NEW.id <> OLD.id THEN
		-- Não deixa alterar id de prisioneiro, se deixar tem q alterar pessoa, inventario e
		-- Instancias de item referenciando o inventario e pessoa.
		RAISE EXCEPTION 'Não é possível alterar o id do prisioneiro.';
	END IF;

    RETURN NEW;

END;
$update_prisioneiro$ LANGUAGE plpgsql;

CREATE TRIGGER prisioneiro_update
BEFORE update ON prisioneiro
FOR EACH ROW EXECUTE PROCEDURE update_prisioneiro();

---------------------
---
---   INFORMANTE
---
---------------------

CREATE FUNCTION insert_informante()
RETURNS trigger AS $insert_informante$
DECLARE
    informante_id INTEGER;
BEGIN
	INSERT INTO pessoa (tipo)
	VALUES ('informante')
	RETURNING id INTO informante_id;

	INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
	VALUES (informante_id, 0, 5);

    RAISE NOTICE 'Criação do inventário do informante bem sucedida.';

	NEW.id = informante_id;

    RAISE NOTICE 'Id do informante é: %', informante_id;

    RETURN NEW;

END;
$insert_informante$ LANGUAGE plpgsql;

CREATE TRIGGER informante_insert
BEFORE INSERT ON informante
FOR EACH ROW EXECUTE PROCEDURE insert_informante();

CREATE FUNCTION update_informante()
RETURNS trigger AS $update_informante$
BEGIN
	IF NEW.id <> OLD.id THEN
		-- Não deixa alterar id de informante, se deixar tem q alterar pessoa, inventario e
		-- Instancias de item referenciando o inventario e pessoa.
		RAISE EXCEPTION 'Não é possível alterar o id do informante.';
	END IF;

    RETURN NEW;

END;
$update_informante$ LANGUAGE plpgsql;

CREATE TRIGGER informante_update
BEFORE update ON informante
FOR EACH ROW EXECUTE PROCEDURE update_informante();

---------------------
---
---   POLICIAL
---
---------------------

CREATE FUNCTION insert_policial()
RETURNS trigger AS $insert_policial$
DECLARE
    policial_id INTEGER;
BEGIN
	INSERT INTO pessoa (tipo)
	VALUES ('policial')
	RETURNING id INTO policial_id;

	INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
	VALUES (policial_id, 0, 5);

    RAISE NOTICE 'Criação do inventário do informante bem sucedida.';

	NEW.id = policial_id;

	RAISE NOTICE 'Id do policial é: %', policial_id;

    RETURN NEW;

END;
$insert_policial$ LANGUAGE plpgsql;

CREATE TRIGGER policial_insert
BEFORE INSERT ON policial
FOR EACH ROW EXECUTE PROCEDURE insert_policial();

CREATE FUNCTION update_policial()
RETURNS trigger AS $update_policial$
BEGIN
	IF NEW.id <> OLD.id THEN
		-- Não deixa alterar id de policial, se deixar tem q alterar pessoa, inventario e
		-- Instancias de item referenciando o inventario e pessoa.
		RAISE EXCEPTION 'Não é possível alterar o id do policial.';
	END IF;

    RETURN NEW;

END;
$update_policial$ LANGUAGE plpgsql;

CREATE TRIGGER policial_update
BEFORE update ON policial
FOR EACH ROW EXECUTE PROCEDURE update_policial();

---------------------
---
---   INSTANCIA_ITEM
---
---------------------

CREATE FUNCTION insert_instancia()
RETURNS trigger AS $insert_instancia$
BEGIN
    IF NEW.lugar IS NULL AND NEW.inventario IS NULL THEN
        RAISE EXCEPTION 'Atualizando inventário e lugar como valores nulos.';
    ELSIF NEW.lugar IS NOT NULL AND NEW.inventario IS NOT NULL THEN
        RAISE EXCEPTION 'A instância não pode estar em um lugar e inventário ao mesmo tempo.';
    END IF;

    RETURN NEW;
END;
$insert_instancia$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_item_insert
BEFORE INSERT ON instancia_item
FOR EACH ROW EXECUTE PROCEDURE insert_instancia();

CREATE FUNCTION update_instancia()
RETURNS trigger AS $update_instancia$
DECLARE
    inventario_atb INTEGER;
    item_atb INTEGER;
    inventario_ocupado_atb SMALLINT;
    tamanho_inventario_atb INTEGER;
    tamanho_item_atb INTEGER;
    total_atb SMALLINT;
    lugar_jogador_atb INTEGER;

BEGIN
    IF NEW.lugar IS NULL AND NEW.inventario IS NULL THEN
        RAISE EXCEPTION 'Atualizando inventário e lugar como valores nulos.';
    ELSIF NEW.lugar IS NOT NULL AND NEW.inventario IS NOT NULL THEN
        RAISE EXCEPTION 'A instância não pode estar em um lugar e inventário ao mesmo tempo.';
    END IF;

    inventario_atb := NEW.inventario;
    item_atb := NEW.item;

    SELECT inventario_ocupado, tamanho INTO inventario_ocupado_atb, tamanho_inventario_atb
    FROM inventario
    WHERE id = inventario_atb;

    SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) INTO tamanho_item_atb
    FROM item ite
    LEFT JOIN arma arm ON arm.id = ite.id
    LEFT JOIN ferramenta fer ON fer.id = ite.id
    LEFT JOIN comida com ON com.id = ite.id
    LEFT JOIN medicamento med ON med.id = ite.id
    LEFT JOIN utilizavel uti ON uti.id = ite.id
    WHERE ite.id = item_atb;

    IF OLD.lugar IS DISTINCT FROM NEW.lugar THEN

        IF NEW.pessoa IS NOT NULL THEN
            SELECT lugar INTO lugar_jogador_atb
            FROM jogador
            WHERE id = NEW.pessoa;
            IF lugar_jogador_atb <> OLD.lugar THEN
                RAISE EXCEPTION 'Jogador não pode pegar o item, pois não está no mesmo lugar da instância.';
            END IF;
        ELSE
            SELECT lugar INTO lugar_jogador_atb
            FROM jogador
            WHERE id = OLD.pessoa;
            IF lugar_jogador_atb <> NEW.lugar THEN
                RAISE EXCEPTION 'Jogador não pode dropar o item, pois não está no mesmo lugar de onde vai dropar.';
            END IF;
        END IF;

    END IF;

    IF NEW.inventario IS NULL THEN
        SELECT inventario_ocupado INTO inventario_ocupado_atb
        FROM inventario
        WHERE id = OLD.inventario;

        total_atb := inventario_ocupado_atb - tamanho_item_atb;

        RAISE NOTICE 'Joguou Item fora - inventário ocupado: %', total_atb;

        UPDATE inventario
        SET inventario_ocupado = total_atb
        WHERE id = OLD.inventario;

    ELSIF NEW.inventario IS NOT NULL THEN

        total_atb := inventario_ocupado_atb + tamanho_item_atb;

        IF total_atb > tamanho_inventario_atb THEN
         	RAISE EXCEPTION 'Espaço insuficiente no inventário. Atualização bloqueada. Total ocupado: % | Tamanho do item: % | Total atual: %',
          	inventario_ocupado_atb, tamanho_item_atb, total_atb;
        END IF;

        RAISE NOTICE 'Pegou Item - inventário ocupado: %', total_atb;

        UPDATE inventario
        SET inventario_ocupado = total_atb
        WHERE id = inventario_atb;

    END IF;

    RETURN NEW;

END;
$update_instancia$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_item_update
BEFORE UPDATE ON instancia_item
FOR EACH ROW EXECUTE PROCEDURE update_instancia();

CREATE FUNCTION delete_instancia()
RETURNS trigger AS $delete_instancia$
DECLARE
    item_atb INTEGER;
    inventario_ocupado_atb SMALLINT;
    tamanho_item_atb INTEGER;
    total_atb SMALLINT;
BEGIN

    IF OLD.inventario IS NOT NULL THEN
        item_atb := OLD.item;

        SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) INTO tamanho_item_atb
        FROM item ite
        LEFT JOIN arma arm ON arm.id = ite.id
        LEFT JOIN ferramenta fer ON fer.id = ite.id
        LEFT JOIN comida com ON com.id = ite.id
        LEFT JOIN medicamento med ON med.id = ite.id
        LEFT JOIN utilizavel uti ON uti.id = ite.id
        WHERE ite.id = item_atb;

        SELECT inventario_ocupado INTO inventario_ocupado_atb
        FROM inventario
        WHERE id = OLD.inventario;

        total_atb := inventario_ocupado_atb - tamanho_item_atb;

        RAISE NOTICE 'Joguou Item fora - inventário ocupado: %', total_atb;

        UPDATE inventario
        SET inventario_ocupado = total_atb
        WHERE id = OLD.inventario;

    END IF;

    RETURN OLD;
END;
$delete_instancia$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_item_delete
BEFORE DELETE ON instancia_item
FOR EACH ROW EXECUTE PROCEDURE delete_instancia();

---------------------
---
---   FERRAMENTA
---
---------------------

CREATE FUNCTION insert_ferramenta()
RETURNS trigger AS $insert_ferramenta$
DECLARE
    ferramenta_id INTEGER;
BEGIN
    -- Inserir na tabela item_fabricavel e capturar o id gerado
    INSERT INTO item_fabricavel (id, tipo)
    VALUES (1, 'ferramenta')
    RETURNING id INTO ferramenta_id;

    -- Atribuir o id gerado ao NEW.id
    NEW.id := ferramenta_id;
	
    -- Mensagens de confirmação
    RAISE NOTICE 'Criação da ferramenta bem sucedida.';
    RAISE NOTICE 'Id da ferramenta é: %', ferramenta_id;

    RETURN NEW;
END;
$insert_ferramenta$ LANGUAGE plpgsql;

CREATE TRIGGER ferramenta_insert
BEFORE INSERT ON ferramenta
FOR EACH ROW EXECUTE FUNCTION insert_ferramenta();

---------------------
---
---   ARMA
---
---------------------

CREATE FUNCTION insert_arma()
RETURNS trigger AS $insert_arma$
DECLARE
    arma_id INTEGER;
BEGIN
    INSERT INTO item_fabricavel (id, tipo)
    VALUES (1, 'arma')
    RETURNING id INTO arma_id;

    NEW.id := arma_id;

    RAISE NOTICE 'Criação da arma bem sucedida.';
    RAISE NOTICE 'Id da arma é: %', arma_id;

    RETURN NEW;
END;
$insert_arma$ LANGUAGE plpgsql;

CREATE TRIGGER arma_insert
BEFORE INSERT ON arma
FOR EACH ROW EXECUTE FUNCTION insert_arma();

---------------------
---
---   COMIDA
---
---------------------

CREATE FUNCTION insert_comida()
RETURNS trigger AS $insert_comida$
DECLARE
    comida_id INTEGER;
BEGIN
    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (1, 'comida')
    RETURNING id INTO comida_id;

    NEW.id := comida_id;

    RAISE NOTICE 'Criação da comida bem sucedida.';
    RAISE NOTICE 'Id da comida é: %', comida_id;

    RETURN NEW;
END;
$insert_comida$ LANGUAGE plpgsql;

CREATE TRIGGER comida_insert
BEFORE INSERT ON comida
FOR EACH ROW EXECUTE FUNCTION insert_comida();

---------------------
---
---   MEDICAMENTO
---
---------------------

CREATE FUNCTION insert_medicamento()
RETURNS trigger AS $insert_medicamento$
DECLARE
    medicamento_id INTEGER;
BEGIN
    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (1, 'medicamento')
    RETURNING id INTO medicamento_id;

    NEW.id := medicamento_id;
	
    RAISE NOTICE 'Criação da medicamento bem sucedida.';
    RAISE NOTICE 'Id da medicamento é: %', medicamento_id;

    RETURN NEW;
END;
$insert_medicamento$ LANGUAGE plpgsql;

CREATE TRIGGER medicamento_insert
BEFORE INSERT ON medicamento
FOR EACH ROW EXECUTE FUNCTION insert_medicamento();

---------------------
---
---   UTILIZAVEL
---
---------------------

CREATE FUNCTION insert_utilizavel()
RETURNS trigger AS $insert_utilizavel$
DECLARE
    utilizavel_id INTEGER;
BEGIN
    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (1, 'utilizavel')
    RETURNING id INTO utilizavel_id;

    NEW.id := utilizavel_id;
	
    RAISE NOTICE 'Criação da utilizavel bem sucedida.';
    RAISE NOTICE 'Id da utilizavel é: %', utilizavel_id;

    RETURN NEW;
END;
$insert_utilizavel$ LANGUAGE plpgsql;

CREATE TRIGGER utilizavel_insert
BEFORE INSERT ON utilizavel
FOR EACH ROW EXECUTE FUNCTION insert_utilizavel();

---------------------
---
---   ITEM_FABRICAVEL
---
---------------------

CREATE FUNCTION insert_item_fabricavel()
RETURNS trigger AS $insert_item_fabricavel$
DECLARE
	id_item_fabricavel INTEGER;
	tipo_item_fabricavel TipoItemFabricavel;
BEGIN
	INSERT INTO item (tipo)
	    VALUES ('fabricavel')
	    RETURNING id INTO id_item_fabricavel;
	tipo_item_fabricavel = NEW.tipo;
	NEW.id = id_item_fabricavel;
	
	RAISE NOTICE 'Id do item_fabricavel é: % | Tipo do item_fabricavel é: %', id_item_fabricavel, tipo_item_fabricavel;

	PERFORM 1 FROM ferramenta WHERE id = id_item_fabricavel;
	IF FOUND THEN
		RAISE EXCEPTION 'O item fabricavel com o id % e tipo % está na tabela ferramenta, ação negada.', id_item_fabricavel, tipo_item_fabricavel;
	END IF;

	PERFORM 1 FROM arma WHERE id = id_item_fabricavel;
	IF FOUND THEN
		RAISE EXCEPTION 'O item fabricavel com o id % e tipo % está na tabela arma, ação negada.', id_item_fabricavel, tipo_item_fabricavel;
	END IF;

	RAISE NOTICE 'O % não aparece em nenhuma outra tabela, a tupla é unica inserção em item_fabricavel concedida.', tipo_item_fabricavel;

	RETURN NEW;
END;
$insert_item_fabricavel$ LANGUAGE plpgsql;

CREATE TRIGGER item_fabricavel_insert
BEFORE INSERT ON item_fabricavel
FOR EACH ROW EXECUTE PROCEDURE insert_item_fabricavel();

---------------------
---
---   ITEM_NAO_FABRICAVEL
---
---------------------

CREATE FUNCTION insert_item_nao_fabricavel()
RETURNS trigger AS $insert_item_nao_fabricavel$
DECLARE
	id_item_nao_fabricavel INTEGER;
	tipo_item_nao_fabricavel TipoItemNaoFabricavel;
BEGIN
	 INSERT INTO item (tipo)
		VALUES ('nao fabricavel')
		RETURNING id INTO id_item_nao_fabricavel;
	tipo_item_nao_fabricavel = NEW.tipo;
	NEW.id = id_item_nao_fabricavel;
	
	RAISE NOTICE 'Id do item_nao_fabricavel é: % | Tipo do item_nao_fabricavel é: %', id_item_nao_fabricavel, tipo_item_nao_fabricavel;

	PERFORM 1 FROM comida WHERE id = id_item_nao_fabricavel;
	IF FOUND THEN
		RAISE EXCEPTION 'O item nao fabricavel com o id % e tipo % está na tabela comida, ação negada.', id_item_nao_fabricavel, tipo_item_nao_fabricavel;
	END IF;

	PERFORM 1 FROM medicamento WHERE id = id_item_nao_fabricavel;
	IF FOUND THEN
		RAISE EXCEPTION 'O item nao fabricavel com o id % e tipo % está na tabela medicamento, ação negada.', id_item_nao_fabricavel, tipo_item_nao_fabricavel;
	END IF;

	PERFORM 1 FROM utilizavel WHERE id = id_item_nao_fabricavel;
	IF FOUND THEN
		RAISE EXCEPTION 'O item nao fabricavel com o id % e tipo % está na tabela utilizavel, ação negada.', id_item_nao_fabricavel, tipo_item_nao_fabricavel;
	END IF;

	RAISE NOTICE 'O % não aparece em nenhuma outra tabela, a tupla é unica inserção em item_nao_fabricavel concedida.', tipo_item_nao_fabricavel;

	RETURN NEW;
END;
$insert_item_nao_fabricavel$ LANGUAGE plpgsql;

CREATE TRIGGER item_nao_fabricavel_insert
BEFORE INSERT ON item_nao_fabricavel
FOR EACH ROW EXECUTE FUNCTION insert_item_nao_fabricavel();

---------------------
---
---   ITEM
---
---------------------

CREATE FUNCTION insert_item()
RETURNS trigger AS $insert_item$
DECLARE
    id_item INTEGER;
	tipo_item TipoItem;
BEGIN
	id_item = NEW.id;
	tipo_item = NEW.tipo;
	
	RAISE NOTICE 'Id do item é: % | Tipo do item é: %', id_item, tipo_item;

	PERFORM 1 FROM item_fabricavel WHERE id = id_item;
	IF FOUND THEN
		RAISE EXCEPTION 'O item com o id % e tipo % está na tabela item_fabricavel, ação negada.', id_item, tipo_item;
	END IF;

	PERFORM 1 FROM item_nao_fabricavel WHERE id = id_item;
	IF FOUND THEN
		RAISE EXCEPTION 'O item com o id % e tipo % está na tabela item_nao_fabricavel, ação negada.', id_item, tipo_item;
	END IF;

	RAISE NOTICE 'O % não aparece em nenhuma outra tabela, a tupla é unica inserção em item concedida.', tipo_item;
	
    RETURN NEW;
END;
$insert_item$ LANGUAGE plpgsql;

CREATE TRIGGER item_insert
BEFORE INSERT ON item
FOR EACH ROW EXECUTE PROCEDURE insert_item();

---------------------
---
---   LIVRO_FABRICACAO
---
---------------------

DROP TRIGGER IF EXISTS update_livro_fabricacao ON fabricacao;
CREATE OR REPLACE FUNCTION update_livro_fabricacao()
RETURNS trigger AS $update_livro_fabricacao$
BEGIN
    IF NEW.id <> OLD.id THEN
        RAISE EXCEPTION 'Não é possível alterar o id e o nome do livro_fabricacao.';
    END IF;

    RETURN NEW;

END;
$update_livro_fabricacao$ LANGUAGE plpgsql;

CREATE TRIGGER update_livro_fabricacao
    BEFORE update
    ON fabricacao
    FOR EACH ROW
EXECUTE PROCEDURE update_livro_fabricacao();
