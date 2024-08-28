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

	new.id = jogador_id;

	RAISE NOTICE 'Id do jogador é: %', jogador_id;

    RETURN NEW;

END;
$insert_jogador$ LANGUAGE plpgsql;

CREATE TRIGGER jogador_insert
BEFORE INSERT ON jogador
FOR EACH ROW EXECUTE PROCEDURE insert_jogador();

---------------------------------------------------------------

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

	new.id = prisioneiro_id;

	RAISE NOTICE 'Id do prisioneiro é: %', prisioneiro_id;

    RETURN NEW;

END;
$insert_prisioneiro$ LANGUAGE plpgsql;

CREATE TRIGGER prisioneiro_insert
BEFORE INSERT ON prisioneiro
FOR EACH ROW EXECUTE PROCEDURE insert_prisioneiro();

---------------------------------------------------------------

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

	new.id = informante_id;

    RAISE NOTICE 'Id do informante é: %', informante_id;

    RETURN NEW;

END;
$insert_informante$ LANGUAGE plpgsql;

CREATE TRIGGER informante_insert
BEFORE INSERT ON informante
FOR EACH ROW EXECUTE PROCEDURE insert_informante();

---------------------------------------------------------------

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

	new.id = policial_id;

	RAISE NOTICE 'Id do policial é: %', policial_id;

    RETURN NEW;

END;
$insert_policial$ LANGUAGE plpgsql;

CREATE TRIGGER policial_insert
BEFORE INSERT ON policial
FOR EACH ROW EXECUTE PROCEDURE insert_policial();

---------------------------------------------------------------

CREATE FUNCTION insert_pessoa()
RETURNS trigger AS $insert_pessoa$
DECLARE
	id_pessoa INTEGER;
	tipo_pessoa TipoPessoa;
	teste INTEGER;
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