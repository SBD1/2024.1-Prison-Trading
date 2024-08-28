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

	new.id = jogador_id;

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

	new.id = prisioneiro_id;

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

	new.id = informante_id;

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

	new.id = policial_id;

    RETURN NEW;

END;
$insert_policial$ LANGUAGE plpgsql;

CREATE TRIGGER policial_insert
BEFORE INSERT ON policial
FOR EACH ROW EXECUTE PROCEDURE insert_policial();
