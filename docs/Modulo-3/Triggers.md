<center>

# Triggers e Stored Procedure

</center>

---

<center>

# O que é?

</center>

> Triggers são um recurso do SQL (Structured Query Language) que permite a execução automática de uma ação definida (como uma instrução `INSERT`, `UPDATE` ou `DELETE`) quando um evento específico ocorre em uma tabela ou visão. Elas são usadas para garantir a integridade dos dados, automatizar processos, e implementar regras de negócios diretamente no banco de dados, sem a necessidade de intervenção manual.

---
<center>

# Funções

</center>

> Funções programadas no próprio SQL para realizar atividades basicas do jogo como mover um jogador, pegar um item, realizar troca entre outros.

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/Functions.png?raw=true"/></div>
</div>

---
<center>

# Security Definer

</center>

> Triggers e funções que alteram tabelas que o `prison_trading_user` não possui acesso, como inserir um novo jogador, que precisa
> inserir uma pessoa na tabela pessoa primeiro, essas funções são de suma importancia para manter a integridade no banco.

[//]: # (> Obs: linha 1 e 2 envolvem a funções que necessitam de privilégio de superusuario, pois inserir novo craft referente a)

[//]: # (> inserir um item fabricavel e criar um craft dele precisa inserir na tabela fabricação que o `prison_trading_user` não possui)

[//]: # (> acesso, ademais a função realizar craft é assim para o jogador poder criar um craft de forma justa e não simplesmente inserir uma instância.)

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/SecurityDefiner.png?raw=true"/></div>
</div>

---
<center>

# Triggers Normais

</center>

> Triggers comuns que não precisam de permissão de um superusuario para serem executados.

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/triggers.png?raw=true"/></div>
</div>

---
<center>

# Permissões do prison_trading_user

</center>

> Permissões que o usuário pode ou não fazer
> 
> Vermelho: Não pode alterar diretamente.
> 
> Azul: Não possui direito de update nesses campos.

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/permissoes.png?raw=true"/></div>
</div>

---
<center>

# Código

</center>

````sql
-- --------------------------------------------------------------------------------------
-- Data de Criação ........: 08/09/2024                                                --
-- Autor(es) ..............: Breno A., Fernando Gabriel, João A. e Julio Cesar         --
-- Versão .................: 4.1                                                       --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descrição ..............: Adiciona Triggers e restrições                            --
-- --------------------------------------------------------------------------------------

BEGIN;

---------------------
---
---   USUÁRIO PADRÃO
---
---------------------

CREATE ROLE prison_trading_user WITH
    LOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    NOBYPASSRLS
    CONNECTION LIMIT -1
    PASSWORD '123';
COMMENT ON ROLE prison_trading_user IS 'Usuário padrão para acesso ao banco de dados do jogo prison trading';

---------------------
---
---   PERMISSÕES
---
---------------------

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO prison_trading_user;

REVOKE INSERT, UPDATE, DELETE ON pessoa FROM prison_trading_user;

REVOKE INSERT, UPDATE, DELETE ON item, item_fabricavel, item_nao_fabricavel FROM prison_trading_user;

REVOKE INSERT, UPDATE, DELETE ON lista_fabricacao FROM prison_trading_user;

REVOKE INSERT, DELETE ON fabricacao, inventario FROM prison_trading_user;

---------------------
---
---   PESSOA
---
---------------------

CREATE FUNCTION insert_pessoa()
    RETURNS trigger AS
$insert_pessoa$
DECLARE
    id_pessoa   INTEGER;
    tipo_pessoa TipoPessoa;
BEGIN
    id_pessoa := NEW.id;
    tipo_pessoa := NEW.tipo;

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

CREATE TRIGGER insert_pessoa
    BEFORE INSERT
    ON pessoa
    FOR EACH ROW
EXECUTE PROCEDURE insert_pessoa();

---------------------
---
---   JOGADOR
---
---------------------

CREATE FUNCTION insert_jogador()
    RETURNS trigger AS
$insert_jogador$
DECLARE
    jogador_id INTEGER;
BEGIN
    INSERT INTO pessoa (tipo)
    VALUES ('jogador')
    RETURNING id INTO jogador_id;

    INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
    VALUES (jogador_id, 0, 5);

    NEW.id := jogador_id;

    RAISE NOTICE 'Criação da pessoa e inventário foram um sucesso, id do jogador é: %', jogador_id;

    RETURN NEW;

END;
$insert_jogador$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_jogador
    BEFORE INSERT
    ON jogador
    FOR EACH ROW
EXECUTE PROCEDURE insert_jogador();

CREATE FUNCTION update_jogador()
    RETURNS trigger AS
$update_jogador$
DECLARE
    ismotin            BOOLEAN;
    itens_inventario   INTEGER[];
    tem_todos_os_itens BOOLEAN;
    itens_necessarios  INTEGER[] := '{}';
BEGIN
    IF NEW.id <> OLD.id THEN
        RAISE EXCEPTION 'Não é possível alterar o id do jogador.';
    END IF;

    IF NEW.lugar <> OLD.lugar THEN
        SELECT array_agg(item)
        INTO itens_inventario
        FROM instancia_item
        WHERE pessoa = NEW.id;

        IF NEW.lugar = 31 THEN
            itens_necessarios := ARRAY [2, 4, 26]; -- FUGA ESGOTO - itens: picareta, pá e lanterna

        ELSIF NEW.lugar = 32 THEN
            itens_necessarios := ARRAY [37]; -- FUGA DISFARÇADO ENTRADA - itens: crachá

        ELSIF NEW.lugar = 33 THEN
            itens_necessarios := ARRAY [26, 1, 3]; -- FUGA FLORESTA - itens: lanterna, chave de fenda e martelo

        ELSIF NEW.lugar = 29 THEN
            itens_necessarios := ARRAY [38]; -- OFICINA A - itens: chave oficina A

        ELSIF NEW.lugar = 30 THEN
            itens_necessarios := ARRAY [39]; -- OFICINA B - itens: chave oficina B

        ELSIF NEW.lugar = 20 THEN
            SELECT prisao.motim
            INTO ismotin
            FROM prisao
                     JOIN regiao ON regiao.prisao = prisao.id
                     JOIN lugar ON lugar.regiao = regiao.id
            WHERE lugar.id = NEW.lugar;

            IF ismotin THEN
                RAISE NOTICE 'Motim está ativo, o jogador conseguiu entrar na sala de controle.';
                RETURN NEW;
            ELSE
                RAISE NOTICE 'Motim não está ativo, o jogador não conseguiu entrar na sala de controle.';
                RETURN OLD;
            END IF;

        ELSIF NEW.lugar = 2 AND OLD.lugar = 1 THEN
            itens_necessarios := ARRAY [4]; -- SAIR DA SOLITÁRIA - Itens: picareta

        END IF;

        IF array_length(itens_necessarios, 1) IS NOT NULL THEN
            tem_todos_os_itens := itens_inventario @> itens_necessarios;

            IF tem_todos_os_itens THEN
                RAISE NOTICE 'O jogador possui todos os itens desejados ou o motim está ativo.';
            ELSE
                RAISE EXCEPTION 'O jogador não possui todos os itens desejados ou o motim não está ativo.';
            END IF;
        END IF;

        RAISE NOTICE 'Movimentação concedida.';
    END IF;

    RETURN NEW;
END;
$update_jogador$ LANGUAGE plpgsql;

CREATE TRIGGER update_jogador
    BEFORE update
    ON jogador
    FOR EACH ROW
EXECUTE PROCEDURE update_jogador();

CREATE FUNCTION delete_jogador_before()
    RETURNS trigger AS
$delete_jogador_before$
DECLARE
    id_jogador INTEGER;
BEGIN
    id_jogador := OLD.id;

    DELETE FROM instancia_item WHERE pessoa = id_jogador;

    DELETE FROM inventario WHERE pessoa = id_jogador;

    RAISE NOTICE 'Todas as instancias de item referenciando o jogador foram deletadas, inclusive seu inventário.';

    RETURN OLD;

END;
$delete_jogador_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_jogador_before
    BEFORE DELETE
    ON jogador
    FOR EACH ROW
EXECUTE PROCEDURE delete_jogador_before();

CREATE FUNCTION delete_jogador_after()
    RETURNS trigger AS
$delete_jogador_after$
BEGIN
    DELETE FROM pessoa WHERE id = OLD.id;

    RAISE NOTICE 'A pessoa da tabela caracterizadora foi deletada.';

    RETURN OLD;

END;
$delete_jogador_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_jogador_after
    AFTER DELETE
    ON jogador
    FOR EACH ROW
EXECUTE PROCEDURE delete_jogador_after();

---------------------
---
---   PRISIONEIRO
---
---------------------

CREATE FUNCTION insert_prisioneiro()
    RETURNS trigger AS
$insert_prisioneiro$
DECLARE
    prisioneiro_id INTEGER;
BEGIN
    INSERT INTO pessoa (tipo)
    VALUES ('prisioneiro')
    RETURNING id INTO prisioneiro_id;

    INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
    VALUES (prisioneiro_id, 0, 5);

    NEW.id := prisioneiro_id;

    RAISE NOTICE 'Criação da pessoa e inventário foram um sucesso, id do prisioneiro é: %', prisioneiro_id;

    RETURN NEW;

END;
$insert_prisioneiro$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER prisioneiro_insert
    BEFORE INSERT
    ON prisioneiro
    FOR EACH ROW
EXECUTE PROCEDURE insert_prisioneiro();

CREATE FUNCTION update_prisioneiro()
    RETURNS trigger AS
$update_prisioneiro$
BEGIN
    IF NEW.id <> OLD.id THEN
        -- Não deixa alterar id de prisioneiro, se deixar tem q alterar pessoa, inventario e
        -- Instancias de item referenciando o inventario e pessoa.
        RAISE EXCEPTION 'Não é possível alterar o id do prisioneiro.';
    END IF;

    RETURN NEW;

END;
$update_prisioneiro$ LANGUAGE plpgsql;

CREATE TRIGGER update_prisioneiro
    BEFORE update
    ON prisioneiro
    FOR EACH ROW
EXECUTE PROCEDURE update_prisioneiro();

CREATE FUNCTION delete_prisioneiro_before()
    RETURNS trigger AS
$delete_prisioneiro_before$
DECLARE
    id_prisioneiro INTEGER;
BEGIN
    id_prisioneiro := OLD.id;

    DELETE FROM instancia_item WHERE pessoa = id_prisioneiro;

    DELETE FROM inventario WHERE pessoa = id_prisioneiro;

    RAISE NOTICE 'Todas as instancias de item referenciando o prisioneiro foram deletadas, inclusive seu inventário.';

    RETURN OLD;

END;
$delete_prisioneiro_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_prisioneiro_before
    BEFORE DELETE
    ON prisioneiro
    FOR EACH ROW
EXECUTE PROCEDURE delete_prisioneiro_before();

CREATE FUNCTION delete_prisioneiro_after()
    RETURNS trigger AS
$delete_prisioneiro_after$
BEGIN
    DELETE FROM pessoa WHERE id = OLD.id;

    RAISE NOTICE 'A pessoa da tabela caracterizadora foi deletada.';

    RETURN OLD;

END;
$delete_prisioneiro_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_prisioneiro_after
    AFTER DELETE
    ON prisioneiro
    FOR EACH ROW
EXECUTE PROCEDURE delete_prisioneiro_after();

---------------------
---
---   INFORMANTE
---
---------------------

CREATE FUNCTION insert_informante()
    RETURNS trigger AS
$insert_informante$
DECLARE
    informante_id INTEGER;
BEGIN
    INSERT INTO pessoa (tipo)
    VALUES ('informante')
    RETURNING id INTO informante_id;

    INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
    VALUES (informante_id, 0, 5);

    NEW.id := informante_id;

    RAISE NOTICE 'Criação da pessoa e inventário foram um sucesso, id do informante é: %', informante_id;

    RETURN NEW;

END;
$insert_informante$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER informante_insert
    BEFORE INSERT
    ON informante
    FOR EACH ROW
EXECUTE PROCEDURE insert_informante();

CREATE FUNCTION update_informante()
    RETURNS trigger AS
$update_informante$
BEGIN
    IF NEW.id <> OLD.id THEN
        -- Não deixa alterar id de informante, se deixar tem q alterar pessoa, inventario e
        -- Instancias de item referenciando o inventario e pessoa.
        RAISE EXCEPTION 'Não é possível alterar o id do informante.';
    END IF;

    RETURN NEW;

END;
$update_informante$ LANGUAGE plpgsql;

CREATE TRIGGER update_informante
    BEFORE update
    ON informante
    FOR EACH ROW
EXECUTE PROCEDURE update_informante();

CREATE FUNCTION delete_informante_before()
    RETURNS trigger AS
$delete_informante_before$
DECLARE
    id_informante INTEGER;
BEGIN
    id_informante := OLD.id;

    DELETE FROM instancia_item WHERE pessoa = id_informante;

    DELETE FROM inventario WHERE pessoa = id_informante;

    RAISE NOTICE 'Todas as instancias de item referenciando o informante foram deletadas, inclusive seu inventário.';

    RETURN OLD;

END;
$delete_informante_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_informante_before
    BEFORE DELETE
    ON informante
    FOR EACH ROW
EXECUTE PROCEDURE delete_informante_before();

CREATE FUNCTION delete_informante_after()
    RETURNS trigger AS
$delete_informante_after$
BEGIN
    DELETE FROM pessoa WHERE id = OLD.id;

    RAISE NOTICE 'A pessoa da tabela caracterizadora foi deletada.';

    RETURN OLD;

END;
$delete_informante_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_informante_after
    AFTER DELETE
    ON informante
    FOR EACH ROW
EXECUTE PROCEDURE delete_informante_after();

---------------------
---
---   POLICIAL
---
---------------------

CREATE FUNCTION insert_policial()
    RETURNS trigger AS
$insert_policial$
DECLARE
    policial_id INTEGER;
BEGIN
    INSERT INTO pessoa (tipo)
    VALUES ('policial')
    RETURNING id INTO policial_id;

    INSERT INTO inventario (pessoa, inventario_ocupado, tamanho)
    VALUES (policial_id, 0, 5);

    NEW.id := policial_id;

    RAISE NOTICE 'Criação da pessoa e inventário foram um sucesso, id do policial é: %', policial_id;

    RETURN NEW;

END;
$insert_policial$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER policial_insert
    BEFORE INSERT
    ON policial
    FOR EACH ROW
EXECUTE PROCEDURE insert_policial();

CREATE FUNCTION update_policial()
    RETURNS trigger AS
$update_policial$
BEGIN
    IF NEW.id <> OLD.id THEN
        -- Não deixa alterar id de policial, se deixar tem q alterar pessoa, inventario e
        -- Instancias de item referenciando o inventario e pessoa.
        RAISE EXCEPTION 'Não é possível alterar o id do policial.';
    END IF;

    RETURN NEW;

END;
$update_policial$ LANGUAGE plpgsql;

CREATE TRIGGER update_policial
    BEFORE update
    ON policial
    FOR EACH ROW
EXECUTE PROCEDURE update_policial();

CREATE FUNCTION delete_policial_before()
    RETURNS trigger AS
$delete_policial_before$
DECLARE
    id_policial INTEGER;
BEGIN
    id_policial := OLD.id;

    DELETE FROM instancia_item WHERE pessoa = id_policial;

    DELETE FROM inventario WHERE pessoa = id_policial;

    RAISE NOTICE 'Todas as instancias de item referenciando o policial foram deletadas, inclusive seu inventário.';

    RETURN OLD;

END;
$delete_policial_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_policial_before
    BEFORE DELETE
    ON policial
    FOR EACH ROW
EXECUTE PROCEDURE delete_policial_before();

CREATE FUNCTION delete_policial_after()
    RETURNS trigger AS
$delete_policial_after$
BEGIN
    DELETE FROM pessoa WHERE id = OLD.id;

    RAISE NOTICE 'A pessoa da tabela caracterizadora foi deletada.';

    RETURN OLD;

END;
$delete_policial_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_policial_after
    AFTER DELETE
    ON policial
    FOR EACH ROW
EXECUTE PROCEDURE delete_policial_after();

---------------------
---
---   INVENTARIO
---
---------------------

CREATE FUNCTION update_inventario()
    RETURNS trigger AS
$update_inventario$
BEGIN
    IF NEW.tamanho <> OLD.tamanho OR NEW.inventario_ocupado <> OLD.inventario_ocupado THEN
        RAISE NOTICE 'Operação foi um sucesso.';
        RETURN NEW;
    ELSE
        RAISE EXCEPTION 'Só é possivel alterar o tamanho total do inventário.';
    END IF;

END;
$update_inventario$ LANGUAGE plpgsql;

CREATE TRIGGER update_inventario
    BEFORE update
    ON inventario
    FOR EACH ROW
EXECUTE PROCEDURE update_inventario();

---------------------
---
---   INSTANCIA_ITEM
---
---------------------

CREATE FUNCTION insert_instancia()
    RETURNS trigger AS
$insert_instancia$
DECLARE
    tamanho_inventario INTEGER;
    tamanho_item INTEGER;
BEGIN
    IF NEW.lugar IS NULL AND NEW.inventario IS NULL THEN
        RAISE EXCEPTION 'Atualizando inventário e lugar como valores nulos.';
    ELSIF NEW.lugar IS NOT NULL AND NEW.inventario IS NOT NULL THEN
        RAISE EXCEPTION 'A instância não pode estar em um lugar e inventário ao mesmo tempo.';
    END IF;

    IF NEW.pessoa IS NOT NULL AND NEW.inventario IS NOT NULL THEN

        SELECT inventario_ocupado INTO tamanho_inventario
        FROM inventario
        WHERE id = NEW.inventario;

        SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho)
        INTO tamanho_item
        FROM item ite
                 LEFT JOIN arma arm ON arm.id = ite.id
                 LEFT JOIN ferramenta fer ON fer.id = ite.id
                 LEFT JOIN comida com ON com.id = ite.id
                 LEFT JOIN medicamento med ON med.id = ite.id
                 LEFT JOIN utilizavel uti ON uti.id = ite.id
        WHERE ite.id = NEW.item;

        UPDATE inventario
        SET inventario_ocupado = tamanho_inventario + tamanho_item
        WHERE id = NEW.inventario;

    END IF;

    RETURN NEW;
END;
$insert_instancia$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_instancia
    BEFORE INSERT
    ON instancia_item
    FOR EACH ROW
EXECUTE PROCEDURE insert_instancia();

CREATE FUNCTION update_instancia()
    RETURNS trigger AS
$update_instancia$
DECLARE
    inventario_atb         INTEGER;
    item_atb               INTEGER;
    inventario_ocupado_atb SMALLINT;
    tamanho_inventario_atb INTEGER;
    tamanho_item_atb       INTEGER;
    total_atb              SMALLINT;
    lugar_jogador_atb      INTEGER;

BEGIN
    IF NEW.lugar IS NULL AND NEW.inventario IS NULL THEN
        RAISE EXCEPTION 'Atualizando inventário e lugar como valores nulos.';
    ELSIF NEW.lugar IS NOT NULL AND NEW.inventario IS NOT NULL THEN
        RAISE EXCEPTION 'A instância não pode estar em um lugar e inventário ao mesmo tempo.';
    END IF;

    inventario_atb := NEW.inventario;
    item_atb := NEW.item;

    SELECT inventario_ocupado, tamanho
    INTO inventario_ocupado_atb, tamanho_inventario_atb
    FROM inventario
    WHERE id = inventario_atb;

    SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho)
    INTO tamanho_item_atb
    FROM item ite
             LEFT JOIN arma arm ON arm.id = ite.id
             LEFT JOIN ferramenta fer ON fer.id = ite.id
             LEFT JOIN comida com ON com.id = ite.id
             LEFT JOIN medicamento med ON med.id = ite.id
             LEFT JOIN utilizavel uti ON uti.id = ite.id
    WHERE ite.id = item_atb;

    IF OLD.lugar IS DISTINCT FROM NEW.lugar THEN

        IF NEW.pessoa IS NOT NULL THEN
            SELECT lugar
            INTO lugar_jogador_atb
            FROM jogador
            WHERE id = NEW.pessoa;
            IF lugar_jogador_atb <> OLD.lugar THEN
                RAISE EXCEPTION 'Jogador não pode pegar o item, pois não está no mesmo lugar da instância.';
            END IF;
        ELSE
            SELECT lugar
            INTO lugar_jogador_atb
            FROM jogador
            WHERE id = OLD.pessoa;
            IF lugar_jogador_atb <> NEW.lugar THEN
                RAISE EXCEPTION 'Jogador não pode dropar o item, pois não está no mesmo lugar de onde vai dropar.';
            END IF;
        END IF;

    END IF;

    IF NEW.inventario IS NULL THEN
        SELECT inventario_ocupado
        INTO inventario_ocupado_atb
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

CREATE TRIGGER update_instancia
    BEFORE UPDATE
    ON instancia_item
    FOR EACH ROW
EXECUTE PROCEDURE update_instancia();

CREATE FUNCTION delete_instancia()
    RETURNS trigger AS
$delete_instancia$
DECLARE
    item_atb               INTEGER;
    inventario_ocupado_atb SMALLINT;
    tamanho_item_atb       INTEGER;
    total_atb              SMALLINT;
BEGIN

    IF OLD.inventario IS NOT NULL THEN
        item_atb := OLD.item;

        SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho)
        INTO tamanho_item_atb
        FROM item ite
                 LEFT JOIN arma arm ON arm.id = ite.id
                 LEFT JOIN ferramenta fer ON fer.id = ite.id
                 LEFT JOIN comida com ON com.id = ite.id
                 LEFT JOIN medicamento med ON med.id = ite.id
                 LEFT JOIN utilizavel uti ON uti.id = ite.id
        WHERE ite.id = item_atb;

        SELECT inventario_ocupado
        INTO inventario_ocupado_atb
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

CREATE TRIGGER delete_instancia
    BEFORE DELETE
    ON instancia_item
    FOR EACH ROW
EXECUTE PROCEDURE delete_instancia();

---------------------
---
---   ITEM
---
---------------------

CREATE FUNCTION insert_item()
    RETURNS trigger AS
$insert_item$
DECLARE
    id_item   INTEGER;
    tipo_item TipoItem;
BEGIN
    id_item := NEW.id;
    tipo_item := NEW.tipo;

    RAISE NOTICE 'Id do item é: % | Tipo do item é: %', id_item, tipo_item;

    PERFORM 1 FROM item_fabricavel WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela item_fabricavel, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM item_nao_fabricavel WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela item_nao_fabricavel, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM ferramenta WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela ferramenta, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM arma WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela arma, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM comida WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela comida, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM medicamento WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela medicamento, ação negada.', id_item, tipo_item;
    END IF;

    PERFORM 1 FROM utilizavel WHERE id = id_item;
    IF FOUND THEN
        RAISE EXCEPTION 'O item com o id % e tipo % está na tabela utilizavel, ação negada.', id_item, tipo_item;
    END IF;

    RAISE NOTICE 'O item % não aparece em nenhuma outra tabela, a tupla é unica inserção em item concedida.', tipo_item;

    RETURN NEW;
END;
$insert_item$ LANGUAGE plpgsql;

CREATE TRIGGER insert_item
    BEFORE INSERT
    ON item
    FOR EACH ROW
EXECUTE PROCEDURE insert_item();

---------------------
---
---   ITEM_FABRICAVEL
---
---------------------

CREATE FUNCTION insert_item_fabricavel()
    RETURNS trigger AS
$insert_item_fabricavel$
DECLARE
    id_item_fabricavel   INTEGER;
    tipo_item_fabricavel TipoItemFabricavel;
BEGIN
    tipo_item_fabricavel := NEW.tipo;
    id_item_fabricavel := NEW.id;

    RAISE NOTICE 'Id do item_fabricavel é: % | Tipo do item_fabricavel é: %', id_item_fabricavel, tipo_item_fabricavel;

    PERFORM 1 FROM ferramenta WHERE id = id_item_fabricavel;
    IF FOUND THEN
        RAISE EXCEPTION 'O item fabricavel com o id % e tipo % está na tabela ferramenta, ação negada.', id_item_fabricavel, tipo_item_fabricavel;
    END IF;

    PERFORM 1 FROM arma WHERE id = id_item_fabricavel;
    IF FOUND THEN
        RAISE EXCEPTION 'O item fabricavel com o id % e tipo % está na tabela arma, ação negada.', id_item_fabricavel, tipo_item_fabricavel;
    END IF;

    RAISE NOTICE 'O item % não aparece em nenhuma outra tabela, a tupla é unica inserção em item_fabricavel concedida.', tipo_item_fabricavel;

    RETURN NEW;
END;
$insert_item_fabricavel$ LANGUAGE plpgsql;

CREATE TRIGGER insert_item_fabricavel
    BEFORE INSERT
    ON item_fabricavel
    FOR EACH ROW
EXECUTE PROCEDURE insert_item_fabricavel();

---------------------
---
---   ITEM_NAO_FABRICAVEL
---
---------------------

CREATE FUNCTION insert_item_nao_fabricavel()
    RETURNS trigger AS
$insert_item_nao_fabricavel$
DECLARE
    id_item_nao_fabricavel   INTEGER;
    tipo_item_nao_fabricavel TipoItemNaoFabricavel;
BEGIN
    tipo_item_nao_fabricavel := NEW.tipo;
    id_item_nao_fabricavel := NEW.id;

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

    RAISE NOTICE 'O item % não aparece em nenhuma outra tabela, a tupla é unica inserção em item_nao_fabricavel concedida.', tipo_item_nao_fabricavel;

    RETURN NEW;
END;
$insert_item_nao_fabricavel$ LANGUAGE plpgsql;

CREATE TRIGGER insert_item_nao_fabricavel
    BEFORE INSERT
    ON item_nao_fabricavel
    FOR EACH ROW
EXECUTE FUNCTION insert_item_nao_fabricavel();

---------------------
---
---   FERRAMENTA
---
---------------------

CREATE FUNCTION insert_ferramenta()
    RETURNS trigger AS
$insert_ferramenta$
DECLARE
    ferramenta_id INTEGER;
BEGIN
    INSERT INTO item (tipo)
    VALUES ('fabricavel')
    RETURNING id INTO ferramenta_id;

    INSERT INTO item_fabricavel (id, tipo)
    VALUES (ferramenta_id, 'ferramenta');

    NEW.id := ferramenta_id;

    RAISE NOTICE 'Criação da ferramenta bem sucedida, id da ferramenta é: %', ferramenta_id;

    RETURN NEW;
END;
$insert_ferramenta$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_ferramenta
    BEFORE INSERT
    ON ferramenta
    FOR EACH ROW
EXECUTE PROCEDURE insert_ferramenta();

CREATE FUNCTION update_ferramenta()
    RETURNS trigger AS
$update_ferramenta$
BEGIN
    IF NEW.id <> OLD.id OR NEW.nome <> OLD.nome THEN
        RAISE EXCEPTION 'Não é possível alterar o id e nome da ferramenta.';
    END IF;

    RETURN NEW;

END;
$update_ferramenta$ LANGUAGE plpgsql;

CREATE TRIGGER update_ferramenta
    BEFORE update
    ON ferramenta
    FOR EACH ROW
EXECUTE PROCEDURE update_ferramenta();

CREATE FUNCTION delete_ferramenta_before()
    RETURNS trigger AS
$delete_ferramenta_before$
DECLARE
    rec_fabricacao lista_fabricacao%ROWTYPE;
BEGIN
    DELETE FROM instancia_item WHERE item = OLD.id;

    DELETE FROM lista_fabricacao WHERE item_fabricavel = OLD.id;

    DELETE FROM fabricacao WHERE item_fabricavel = OLD.id;

    RAISE NOTICE 'Todas as instâncias referenciando esse item foram deletadas, a fabricação do item foi deletada, jutamente com seu craft.';

    UPDATE missao
    SET item_nao_fabricavel = NULL
    WHERE item_nao_fabricavel = OLD.id;

    FOR rec_fabricacao IN
        SELECT *
        FROM lista_fabricacao
        WHERE item = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.fabricacao;

            DELETE
            FROM fabricacao
            WHERE id = rec_fabricacao.fabricacao;

            RAISE NOTICE 'Deletando a fabricação % e seu craft', rec_fabricacao.fabricacao;

        END LOOP;

    RETURN OLD;

END;
$delete_ferramenta_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_ferramenta_before
    BEFORE DELETE
    ON ferramenta
    FOR EACH ROW
EXECUTE PROCEDURE delete_ferramenta_before();

CREATE FUNCTION delete_ferramenta_after()
    RETURNS trigger AS
$delete_ferramenta_after$
BEGIN
    DELETE FROM item_fabricavel WHERE id = OLD.id;

    DELETE FROM item WHERE id = OLD.id;

    RAISE NOTICE 'O item da tabela caracterizadora foi deletado, juntamente com o item fabricavel da segunda tabela caracterizadora.';

    RETURN OLD;

END;
$delete_ferramenta_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_ferramenta_after
    AFTER DELETE
    ON ferramenta
    FOR EACH ROW
EXECUTE PROCEDURE delete_ferramenta_after();

---------------------
---
---   ARMA
---
---------------------

CREATE FUNCTION insert_arma()
    RETURNS trigger AS
$insert_arma$
DECLARE
    arma_id INTEGER;
BEGIN
    INSERT INTO item (tipo)
    VALUES ('fabricavel')
    RETURNING id INTO arma_id;

    INSERT INTO item_fabricavel (id, tipo)
    VALUES (arma_id, 'arma');

    NEW.id := arma_id;

    RAISE NOTICE 'Criação da arma bem sucedida, id da arma é: %', arma_id;

    RETURN NEW;
END;
$insert_arma$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_arma
    BEFORE INSERT
    ON arma
    FOR EACH ROW
EXECUTE PROCEDURE insert_arma();

CREATE FUNCTION update_arma()
    RETURNS trigger AS
$update_arma$
BEGIN
    IF NEW.id <> OLD.id OR NEW.nome <> OLD.nome THEN
        RAISE EXCEPTION 'Não é possível alterar o id e nome da arma.';
    END IF;

    RETURN NEW;

END;
$update_arma$ LANGUAGE plpgsql;

CREATE TRIGGER update_arma
    BEFORE update
    ON arma
    FOR EACH ROW
EXECUTE PROCEDURE update_arma();

CREATE FUNCTION delete_arma_before()
    RETURNS trigger AS
$delete_arma_before$
DECLARE
    rec_fabricacao lista_fabricacao%ROWTYPE;
BEGIN
    DELETE FROM instancia_item WHERE item = OLD.id;

    DELETE FROM lista_fabricacao WHERE item_fabricavel = OLD.id;

    DELETE FROM fabricacao WHERE item_fabricavel = OLD.id;

    RAISE NOTICE 'Todas as instâncias referenciando esse item foram deletadas, a fabricação do item foi deletada, jutamente com seu craft.';

    UPDATE missao
    SET item_nao_fabricavel = NULL
    WHERE item_nao_fabricavel = OLD.id;

    FOR rec_fabricacao IN
        SELECT *
        FROM lista_fabricacao
        WHERE item = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.fabricacao;

            DELETE
            FROM fabricacao
            WHERE id = rec_fabricacao.fabricacao;

            RAISE NOTICE 'Deletando a fabricação % e seu craft', rec_fabricacao.fabricacao;

        END LOOP;

    RETURN OLD;

END;
$delete_arma_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_arma_before
    BEFORE DELETE
    ON arma
    FOR EACH ROW
EXECUTE PROCEDURE delete_arma_before();

CREATE FUNCTION delete_arma_after()
    RETURNS trigger AS
$delete_arma_after$
BEGIN
    DELETE FROM item_fabricavel WHERE id = OLD.id;

    DELETE FROM item WHERE id = OLD.id;

    RAISE NOTICE 'O item da tabela caracterizadora foi deletado, juntamente com o item fabricavel da segunda tabela caracterizadora.';

    RETURN OLD;

END;
$delete_arma_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_arma_after
    AFTER DELETE
    ON arma
    FOR EACH ROW
EXECUTE PROCEDURE delete_arma_after();

---------------------
---
---   COMIDA
---
---------------------

CREATE FUNCTION insert_comida()
    RETURNS trigger AS
$insert_comida$
DECLARE
    comida_id INTEGER;
BEGIN
    INSERT INTO item (tipo)
    VALUES ('nao fabricavel')
    RETURNING id INTO comida_id;

    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (comida_id, 'comida');

    NEW.id := comida_id;

    RAISE NOTICE 'Criação da comida bem sucedida, id da comida é: %', comida_id;

    RETURN NEW;
END;
$insert_comida$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_comida
    BEFORE INSERT
    ON comida
    FOR EACH ROW
EXECUTE PROCEDURE insert_comida();


CREATE FUNCTION update_comida()
    RETURNS trigger AS
$update_comida$
BEGIN
    IF NEW.id <> OLD.id OR NEW.nome <> OLD.nome THEN
        RAISE EXCEPTION 'Não é possível alterar o id e nome da comida.';
    END IF;

    RETURN NEW;

END;
$update_comida$ LANGUAGE plpgsql;

CREATE TRIGGER update_comida
    BEFORE update
    ON comida
    FOR EACH ROW
EXECUTE PROCEDURE update_comida();

CREATE FUNCTION delete_comida_before()
    RETURNS trigger AS
$delete_comida_before$
DECLARE
    rec_fabricacao lista_fabricacao%ROWTYPE;
BEGIN
    DELETE FROM instancia_item WHERE item = OLD.id;

    RAISE NOTICE 'Todas as instâncias referenciando esse item foram deletadas, a missão que dropava esse item agora não possui drop';

    UPDATE missao
    SET item_nao_fabricavel = NULL
    WHERE item_nao_fabricavel = OLD.id;

    FOR rec_fabricacao IN
        SELECT *
        FROM lista_fabricacao
        WHERE item = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.fabricacao;

            DELETE
            FROM fabricacao
            WHERE id = rec_fabricacao.fabricacao;

            RAISE NOTICE 'Deletando a fabricação % e seu craft', rec_fabricacao.fabricacao;

        END LOOP;

    RETURN OLD;

END;
$delete_comida_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_comida_before
    BEFORE DELETE
    ON comida
    FOR EACH ROW
EXECUTE PROCEDURE delete_comida_before();

CREATE FUNCTION delete_comida_after()
    RETURNS trigger AS
$delete_comida_after$
BEGIN
    DELETE FROM item_nao_fabricavel WHERE id = OLD.id;

    DELETE FROM item WHERE id = OLD.id;

    RAISE NOTICE 'O item da tabela caracterizadora foi deletado, juntamente com o item não fabricavel da segunda tabela caracterizadora.';

    RETURN OLD;

END;
$delete_comida_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_comida_after
    AFTER DELETE
    ON comida
    FOR EACH ROW
EXECUTE PROCEDURE delete_comida_after();

---------------------
---
---   MEDICAMENTO
---
---------------------

CREATE FUNCTION insert_medicamento()
    RETURNS trigger AS
$insert_medicamento$
DECLARE
    medicamento_id INTEGER;
BEGIN
    INSERT INTO item (tipo)
    VALUES ('nao fabricavel')
    RETURNING id INTO medicamento_id;

    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (medicamento_id, 'medicamento');

    NEW.id := medicamento_id;

    RAISE NOTICE 'Criação da medicamento bem sucedida, id do medicamento é: %', medicamento_id;

    RETURN NEW;
END;
$insert_medicamento$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_medicamento
    BEFORE INSERT
    ON medicamento
    FOR EACH ROW
EXECUTE PROCEDURE insert_medicamento();

CREATE FUNCTION update_medicamento()
    RETURNS trigger AS
$update_medicamento$
BEGIN
    IF NEW.id <> OLD.id OR NEW.nome <> OLD.nome THEN
        RAISE EXCEPTION 'Não é possível alterar o id e nome do medicamento.';
    END IF;

    RETURN NEW;

END;
$update_medicamento$ LANGUAGE plpgsql;

CREATE TRIGGER update_medicamento
    BEFORE update
    ON medicamento
    FOR EACH ROW
EXECUTE PROCEDURE update_medicamento();

CREATE FUNCTION delete_medicamento_before()
    RETURNS trigger AS
$delete_medicamento_before$
DECLARE
    rec_fabricacao lista_fabricacao%ROWTYPE;
BEGIN
    DELETE FROM instancia_item WHERE item = OLD.id;

    RAISE NOTICE 'Todas as instâncias referenciando esse item foram deletadas, a missão que dropava esse item agora não possui drop';

    UPDATE missao
    SET item_nao_fabricavel = NULL
    WHERE item_nao_fabricavel = OLD.id;

    FOR rec_fabricacao IN
        SELECT *
        FROM lista_fabricacao
        WHERE item = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.fabricacao;

            DELETE
            FROM fabricacao
            WHERE id = rec_fabricacao.fabricacao;

            RAISE NOTICE 'Deletando a fabricação % e seu craft', rec_fabricacao.fabricacao;

        END LOOP;

    RETURN OLD;

END;
$delete_medicamento_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_medicamento_before
    BEFORE DELETE
    ON medicamento
    FOR EACH ROW
EXECUTE PROCEDURE delete_medicamento_before();

CREATE FUNCTION delete_medicamento_after()
    RETURNS trigger AS
$delete_medicamento_after$
BEGIN
    DELETE FROM item_nao_fabricavel WHERE id = OLD.id;

    DELETE FROM item WHERE id = OLD.id;

    RAISE NOTICE 'O item da tabela caracterizadora foi deletado, juntamente com o item não fabricavel da segunda tabela caracterizadora.';

    RETURN OLD;

END;
$delete_medicamento_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_medicamento_after
    AFTER DELETE
    ON medicamento
    FOR EACH ROW
EXECUTE PROCEDURE delete_medicamento_after();

---------------------
---
---   UTILIZAVEL
---
---------------------

CREATE FUNCTION insert_utilizavel()
    RETURNS trigger AS
$insert_utilizavel$
DECLARE
    utilizavel_id INTEGER;
BEGIN
    INSERT INTO item (tipo)
    VALUES ('nao fabricavel')
    RETURNING id INTO utilizavel_id;

    INSERT INTO item_nao_fabricavel (id, tipo)
    VALUES (utilizavel_id, 'utilizavel');

    NEW.id := utilizavel_id;

    RAISE NOTICE 'Criação da utilizavel bem sucedida, id do utilizavel é: %', utilizavel_id;

    RETURN NEW;
END;
$insert_utilizavel$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER insert_utilizavel
    BEFORE INSERT
    ON utilizavel
    FOR EACH ROW
EXECUTE PROCEDURE insert_utilizavel();

CREATE FUNCTION update_utilizavel()
    RETURNS trigger AS
$update_utilizavel$
BEGIN
    IF NEW.id <> OLD.id OR NEW.nome <> OLD.nome THEN
        RAISE EXCEPTION 'Não é possível alterar o id e nome do utilizavel.';
    END IF;

    RETURN NEW;

END;
$update_utilizavel$ LANGUAGE plpgsql;

CREATE TRIGGER update_utilizavel
    BEFORE update
    ON utilizavel
    FOR EACH ROW
EXECUTE PROCEDURE update_utilizavel();

CREATE FUNCTION delete_utilizavel_before()
    RETURNS trigger AS
$delete_utilizavel_before$
DECLARE
    rec_fabricacao lista_fabricacao%ROWTYPE;
BEGIN
    DELETE FROM instancia_item WHERE item = OLD.id;

    RAISE NOTICE 'Todas as instâncias referenciando esse item foram deletadas, a missão que dropava esse item agora não possui drop';

    UPDATE missao
    SET item_nao_fabricavel = NULL
    WHERE item_nao_fabricavel = OLD.id;

    FOR rec_fabricacao IN
        SELECT *
        FROM lista_fabricacao
        WHERE item = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.fabricacao;

            DELETE
            FROM fabricacao
            WHERE id = rec_fabricacao.fabricacao;

            RAISE NOTICE 'Deletando a fabricação % e seu craft', rec_fabricacao.fabricacao;

        END LOOP;

    RETURN OLD;

END;
$delete_utilizavel_before$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_utilizavel_before
    BEFORE DELETE
    ON utilizavel
    FOR EACH ROW
EXECUTE PROCEDURE delete_utilizavel_before();

CREATE FUNCTION delete_utilizavel_after()
    RETURNS trigger AS
$delete_utilizavel_after$
BEGIN
    DELETE FROM item_nao_fabricavel WHERE id = OLD.id;

    DELETE FROM item WHERE id = OLD.id;

    RAISE NOTICE 'O item da tabela caracterizadora foi deletado, juntamente com o item não fabricavel da segunda tabela caracterizadora.';

    RETURN OLD;

END;
$delete_utilizavel_after$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_utilizavel_after
    AFTER DELETE
    ON utilizavel
    FOR EACH ROW
EXECUTE PROCEDURE delete_utilizavel_after();

---------------------
---
---   LIVRO_FABRICACAO
---
---------------------

CREATE FUNCTION update_livro_fabricacao()
    RETURNS trigger AS
$update_livro_fabricacao$
BEGIN
    IF NEW.id <> OLD.id THEN
        RAISE EXCEPTION 'Não é possível alterar o id do livro de fabricação.';
    END IF;

    RETURN NEW;

END;
$update_livro_fabricacao$ LANGUAGE plpgsql;

CREATE TRIGGER update_livro_fabricacao
    BEFORE update
    ON livro_fabricacao
    FOR EACH ROW
EXECUTE PROCEDURE update_livro_fabricacao();

CREATE FUNCTION delete_livro_fabricacao()
    RETURNS trigger AS
$delete_livro_fabricacao$
DECLARE
    rec_fabricacao fabricacao%ROWTYPE;
BEGIN

    FOR rec_fabricacao IN
        SELECT *
        FROM fabricacao
        WHERE livro_fabricacao = OLD.id
        LOOP
            DELETE
            FROM lista_fabricacao
            WHERE fabricacao = rec_fabricacao.id;

            RAISE NOTICE 'Deletando o craft % da lista_fabricacao.', rec_fabricacao.id;

        END LOOP;

	DELETE
	FROM fabricacao
	WHERE livro_fabricacao = OLD.id;

    RAISE NOTICE 'Todas as fabricações vinculadas a esse livro foram deletadas.';

    RETURN OLD;

END;
$delete_livro_fabricacao$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER delete_livro_fabricacao
    BEFORE DELETE
    ON livro_fabricacao
    FOR EACH ROW
EXECUTE PROCEDURE delete_livro_fabricacao();

---------------------
---
---   FABRICACAO
---
---------------------

CREATE FUNCTION update_fabricacao()
    RETURNS trigger AS
$update_fabricacao$
BEGIN
    IF NEW.id <> OLD.id OR NEW.item_fabricavel <> OLD.item_fabricavel THEN
        RAISE EXCEPTION 'Não é possível alterar o id e o item fabricavel.';
    END IF;

    RETURN NEW;

END;
$update_fabricacao$ LANGUAGE plpgsql;

CREATE TRIGGER update_fabricacao
    BEFORE update
    ON fabricacao
    FOR EACH ROW
EXECUTE PROCEDURE update_fabricacao();

---------------------
---
---   LISTA_FABRICACAO
---
---------------------

CREATE FUNCTION inserir_novo_craft(
    novo_item_fabricavel INTEGER,
    novos_itens INTEGER[],
    livro_fabricacao_atb INTEGER
)
RETURNS VOID AS $$
DECLARE
    nova_fabricacao INTEGER;
    item_existente BOOLEAN;
    i INTEGER;
BEGIN
    PERFORM 1
    FROM fabricacao
    WHERE item_fabricavel = novo_item_fabricavel;
    IF FOUND THEN
        RAISE EXCEPTION 'item já tem craft.';
    END IF;
    INSERT INTO fabricacao (item_fabricavel, livro_fabricacao)
    VALUES (novo_item_fabricavel, livro_fabricacao_atb)
    RETURNING id INTO nova_fabricacao;

    SELECT EXISTS (
        SELECT 1
        FROM (
            SELECT item_fabricavel, ARRAY_AGG(item ORDER BY item) AS itens
            FROM lista_fabricacao
            GROUP BY item_fabricavel
        ) sub
        WHERE item_fabricavel <> novo_item_fabricavel
          AND itens = ARRAY(SELECT * FROM unnest(novos_itens) ORDER BY 1)
    ) INTO item_existente;

    IF item_existente THEN
        RAISE EXCEPTION 'Um craft com esses itens já existe para outro item fabricável.';
    END IF;

    FOREACH i IN ARRAY novos_itens LOOP
        INSERT INTO lista_fabricacao (item_fabricavel, fabricacao, item)
        VALUES (novo_item_fabricavel, nova_fabricacao, i);
    END LOOP;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

---------------------
---
---   ITEM - JOGADOR
---
---------------------

CREATE FUNCTION pegar_item_chao(jogador INTEGER, instancia INTEGER)
    RETURNS VOID AS
$pegar_item_chao$
DECLARE
    inventario_atb INTEGER;
BEGIN
    SELECT id INTO inventario_atb
    FROM inventario
    WHERE pessoa = jogador;

    UPDATE instancia_item
    SET lugar = NULL, regiao = NULL, inventario = inventario_atb, pessoa =  jogador
    WHERE id = instancia;
END;
$pegar_item_chao$ LANGUAGE plpgsql;

CREATE FUNCTION dropar_item_chao(jogador_atb INTEGER, instancia INTEGER)
    RETURNS VOID AS
$dropar_item_chao$
DECLARE
    lugar_atb INTEGER;
    regiao_atb INTEGER;
BEGIN
    SELECT lugar, regiao INTO lugar_atb, regiao_atb
    FROM jogador
    WHERE id = jogador_atb;

    UPDATE instancia_item
    SET lugar = lugar_atb, regiao = regiao_atb, inventario = NULL, pessoa =  NULL
    WHERE id = instancia;
END;
$dropar_item_chao$ LANGUAGE plpgsql;

CREATE FUNCTION realizar_craft(jogador_atb INTEGER, item_atb INTEGER)
    RETURNS VOID AS
$realizar_craft$
DECLARE
    possui_itens BOOLEAN;
    itens_jogador INTEGER[];
    itens_craft INTEGER[];
    inventario_atb INTEGER;
BEGIN
    SELECT id INTO inventario_atb
    FROM inventario
    WHERE pessoa = jogador_atb;

    SELECT array_agg(item) INTO itens_jogador
    FROM instancia_item
    WHERE pessoa = jogador_atb;

    SELECT array_agg(item) INTO itens_craft
    FROM lista_fabricacao
    WHERE fabricacao = item_atb;

    possui_itens := itens_jogador @> itens_craft;

    IF possui_itens THEN
        DELETE FROM instancia_item
        WHERE pessoa = jogador_atb
        AND item = ANY(itens_craft);

        INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
        VALUES (item_atb, NULL, NULL, jogador_atb, inventario_atb);

        RAISE NOTICE 'Craft realizado com sucesso.';
    ELSE
        RAISE NOTICE 'Jogador não possui todos os itens para realizar o craft.';
    END IF;

END;
$realizar_craft$ LANGUAGE plpgsql SECURITY DEFINER;

---------------------
---
---   PRISÃO
---
---------------------

CREATE FUNCTION update_prisao()
RETURNS trigger AS $update_prisao$
BEGIN
	IF OLD.id <> NEW.id THEN
		RAISE EXCEPTION 'Não pode alterar o id de uma região.';
	END IF;
	RETURN NEW;
END;
$update_prisao$ LANGUAGE plpgsql;

CREATE TRIGGER update_prisao
    BEFORE update
    ON prisao
    FOR EACH ROW
EXECUTE PROCEDURE update_prisao();

---------------------
---
---   REGIÃO
---
---------------------

CREATE FUNCTION update_regiao()
RETURNS trigger AS $update_regiao$
BEGIN
	IF OLD.id <> NEW.id  THEN
		RAISE EXCEPTION 'Não pode alterar o id de uma região.';
	END IF;
	RETURN NEW;
END;
$update_regiao$ LANGUAGE plpgsql;

CREATE TRIGGER update_regiao
    BEFORE update
    ON regiao
    FOR EACH ROW
EXECUTE PROCEDURE update_regiao();

---------------------
---
---   LUGAR
---
---------------------

CREATE FUNCTION update_lugar()
RETURNS trigger AS $update_lugar$
BEGIN
	IF OLD.id <> NEW.id OR NEW.rota_final_fuga <> OLD.rota_final_fuga THEN
		RAISE EXCEPTION 'Não pode alterar o id de nem a rota de fuga de um lugar.';
	END IF;
	RETURN NEW;
END;
$update_lugar$ LANGUAGE plpgsql;

CREATE TRIGGER update_lugar
    BEFORE update
    ON lugar
    FOR EACH ROW
EXECUTE PROCEDURE update_lugar();

---------------------
---
---   MOVIMENTAÇÃO DE JOGADOR
---
---------------------

CREATE OR REPLACE FUNCTION movimenta_jogador(jogador_id INTEGER, lugar_destino_atb INTEGER)
    RETURNS VOID AS
$movimenta_jogador$
DECLARE
    jogador_lugar_atual INTEGER;
    jogador_regiao_atual INTEGER;
BEGIN
    SELECT lugar, regiao INTO jogador_lugar_atual, jogador_regiao_atual
    FROM Jogador
    WHERE id = jogador_id;

    PERFORM 1
    FROM lugar_origem_destino ori
    JOIN lugar lug ON ori.lugar_destino = lug.id
    WHERE ori.lugar_origem = jogador_lugar_atual AND lug.id = lugar_destino_atb;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'O lugar digitado não está conectado com o atual.';
    END IF;

    SELECT id, regiao INTO jogador_lugar_atual, jogador_regiao_atual
    FROM lugar
    WHERE id = lugar_destino_atb;

    UPDATE Jogador
    SET lugar = jogador_lugar_atual, regiao = jogador_regiao_atual
    WHERE id = jogador_id;

    RAISE NOTICE 'Posição movida com sucesso para lugar % e regiao %.', jogador_lugar_atual, jogador_regiao_atual;

END;
$movimenta_jogador$ LANGUAGE plpgsql;

---------------------
---
---   REDUZIR TEMPO DE VIDA - 10 min
---
---------------------

CREATE FUNCTION reduzir_tempo_vida()
RETURNS void AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN SELECT id, tempo_vida FROM jogador LOOP
        IF rec.tempo_vida > 1 THEN
            UPDATE jogador
            SET tempo_vida = tempo_vida - 1
            WHERE id = rec.id;
        ELSE
            DELETE FROM jogador
            WHERE id = rec.id;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---   MOTIM - 30 min, 3 min de duração
---
---------------------

CREATE FUNCTION gerencia_motim()
RETURNS void AS $$
DECLARE
    lugar_motim INTEGER;
    regiao_motim INTEGER;
    valores INTEGER[] := ARRAY[10, 15, 19, 23, 28];
BEGIN
    lugar_motim := valores[1 + (random() * (array_length(valores, 1) - 1))::INT];

    SELECT regiao INTO regiao_motim
    FROM lugar
    WHERE id = lugar_motim;

    CREATE TEMP TABLE lugar_pessoas_original AS
    (
        SELECT id AS pessoa_id, lugar AS lugar_original, regiao AS regiao_original
        FROM prisioneiro
        UNION ALL
        SELECT id AS pessoa_id, lugar AS lugar_original, regiao AS regiao_original
        FROM policial
        UNION ALL
        SELECT id AS pessoa_id, lugar AS lugar_original, regiao AS regiao_original
        FROM informante
    );

    UPDATE prisao
    SET motim = true;

    UPDATE prisioneiro
    SET lugar = lugar_motim, regiao = regiao_motim;

    UPDATE policial
    SET lugar = lugar_motim, regiao = regiao_motim;

    UPDATE informante
    SET lugar = lugar_motim, regiao = regiao_motim;

    RAISE NOTICE 'Motim iniciado no lugar: %, com a região: %', lugar_motim, regiao_motim;

    PERFORM pg_sleep(180); -- 180 segundos = 3 minutos

    UPDATE prisioneiro
    SET lugar = l.lugar_original, regiao = l.regiao_original
    FROM lugar_pessoas_original l
    WHERE prisioneiro.id = l.pessoa_id;

    UPDATE policial
    SET lugar = l.lugar_original, regiao = l.regiao_original
    FROM lugar_pessoas_original l
    WHERE policial.id = l.pessoa_id;

    UPDATE informante
    SET lugar = l.lugar_original, regiao = l.regiao_original
    FROM lugar_pessoas_original l
    WHERE informante.id = l.pessoa_id;

    UPDATE prisao
    SET motim = false;

    DROP TABLE IF EXISTS lugar_pessoas_original;

    RAISE NOTICE 'Motim finalizado, todas as pessoas voltaram para seus lugares de origem';
END;
$$ LANGUAGE plpgsql;

---------------------
---
---   MOVIMENTAÇÃO DE PRISIONEIROS - 5 min
---
---------------------

CREATE FUNCTION movimenta_prisioneiros()
RETURNS void AS $$
DECLARE
    prisioneiro_record RECORD;
	proximo_lugar INTEGER;
	proxima_regiao INTEGER;
BEGIN
    FOR prisioneiro_record IN
        SELECT id, lugar
        FROM prisioneiro
    LOOP
		SELECT lugar_destino, regiao_destino INTO proximo_lugar, proxima_regiao
		FROM lugar_origem_destino
		WHERE regiao_destino <> 4 AND regiao_destino <> 8 AND lugar_origem = prisioneiro_record.lugar
		ORDER BY RANDOM() LIMIT 1;

		UPDATE prisioneiro
		SET regiao = proxima_regiao, lugar = proximo_lugar
		WHERE id = prisioneiro_record.id;

		RAISE NOTICE 'MOVENDO - Prisioneiro: % PARA Lugar: %, Regiao: %', prisioneiro_record.id, proximo_lugar, proxima_regiao;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---   POPULA ITENS - 10 min
---
---------------------

CREATE FUNCTION popula_itens()
RETURNS void AS $$
DECLARE
    comida_count INTEGER;
BEGIN
    -- INSERIR CRACHÁ
    PERFORM 1 FROM instancia_item WHERE regiao = 4 AND item = 37;
    IF NOT FOUND THEN
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES (37, 20, 4, NULL, NULL);
    END IF;

    -- COMIDA NA MESA DIREITA REFEITORIO
    SELECT COUNT(*) INTO comida_count
    FROM instancia_item
    WHERE lugar = 22 AND item > 30 AND item < 37;

    IF comida_count = 3 THEN
        -- Não insere nada
        NULL;
    ELSIF comida_count = 2 THEN
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL);
    ELSIF comida_count = 1 THEN
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES
            (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL);
    ELSE
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES
            (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 22, 5, NULL, NULL);
    END IF;

    -- COMIDA NA MESA ESQUERDA REFEITORIO
    SELECT COUNT(*) INTO comida_count
    FROM instancia_item
    WHERE lugar = 21 AND item > 30 AND item < 37;

    IF comida_count = 3 THEN
        -- Não insere nada
        NULL;
    ELSIF comida_count = 2 THEN
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL);
    ELSIF comida_count = 1 THEN
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES
            (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL);
    ELSE
        INSERT INTO instancia_item (item, lugar, regiao, inventario, pessoa)
        VALUES
            (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL),
            (FLOOR(random() * (36 - 31 + 1)) + 31, 21, 5, NULL, NULL);
    END IF;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---   BRIGA
---
---------------------

CREATE FUNCTION combate(
    jogador_id INTEGER,
    prisioneiro_id INTEGER
) RETURNS VOID AS $$
DECLARE
    jogador_vida INTEGER;
    jogador_forca INTEGER;
    jogador_habilidade INTEGER;
    jogador_hp INTEGER;
    jogador_dano INTEGER;

    prisioneiro_vida INTEGER;
    prisioneiro_forca INTEGER;
    prisioneiro_habilidade INTEGER;
    prisioneiro_hp INTEGER;
    prisioneiro_dano INTEGER;

    turno INTEGER;
	lugar_prisioneiro INTEGER;
	lugar_jogador INTEGER;
	tipo_pessoa TipoPessoa;
    habilidade_briga_atb INTEGER;
BEGIN
	SELECT tipo INTO tipo_pessoa
	FROM pessoa
	WHERE id = prisioneiro_id;
	IF tipo_pessoa <> 'prisioneiro' THEN
		RAISE NOTICE 'Brigou com quem nao devia e morreu.';
		UPDATE jogador
        SET vida = 5, lugar = 16, regiao = 3, tempo_vida = 1
        WHERE id = jogador_id;
		RETURN;
	END IF;

	SELECT lugar INTO lugar_prisioneiro
	FROM prisioneiro
	WHERE id = prisioneiro_id;

	SELECT lugar INTO lugar_jogador
	FROM jogador
	WHERE id = jogador_id;

	IF lugar_jogador <> lugar_prisioneiro THEN
	    RAISE EXCEPTION 'Jogador e prisioneiro estão em lugares direfentes.';
	END IF;
    SELECT vida, forca, habilidade_briga INTO jogador_vida, jogador_forca, jogador_habilidade
    FROM jogador
    WHERE id = jogador_id;

    SELECT vida, forca, habilidade_briga INTO prisioneiro_vida, prisioneiro_forca, prisioneiro_habilidade
    FROM prisioneiro
    WHERE id = prisioneiro_id;

    jogador_hp := jogador_vida * 10;
    jogador_dano := jogador_forca * jogador_habilidade;

    prisioneiro_hp := prisioneiro_vida * 10;
    prisioneiro_dano := prisioneiro_forca * prisioneiro_habilidade;

    WHILE jogador_hp > 0 AND prisioneiro_hp > 0 LOOP
        turno := (RANDOM() * 2)::INTEGER + 1;

        IF turno = 1 THEN
            prisioneiro_hp := prisioneiro_hp - jogador_dano;
            IF prisioneiro_hp > 0 THEN
                jogador_hp := jogador_hp - prisioneiro_dano;
            END IF;
        ELSE
            jogador_hp := jogador_hp - prisioneiro_dano;
            IF jogador_hp > 0 THEN
                prisioneiro_hp := prisioneiro_hp - jogador_dano;
            END IF;
        END IF;
    END LOOP;


    IF jogador_hp <= 0 THEN
        UPDATE jogador
        SET vida = 5, lugar = 16, regiao = 3, tempo_vida = tempo_vida - 1
        WHERE id = jogador_id;

        UPDATE prisioneiro
        SET vida = GREATEST(1, prisioneiro_hp / 10)
        WHERE id = prisioneiro_id;
    ELSE
        UPDATE jogador
        SET vida = GREATEST(1, jogador_hp / 10)
        WHERE id = jogador_id;

        UPDATE prisioneiro
        SET vida = 5, lugar = 16, regiao = 3
        WHERE id = prisioneiro_id;
    END IF;

	SELECT jogador.habilidade_briga INTO habilidade_briga_atb
    FROM jogador
    WHERE id = jogador_id;

	habilidade_briga_atb := habilidade_briga_atb + 1;

	IF habilidade_briga_atb <= 10 THEN
	    UPDATE jogador
        SET habilidade_briga = habilidade_briga_atb
        WHERE id = jogador_id;
    END IF;

END;
$$ LANGUAGE plpgsql;

---------------------
---
---   USAR ITENS
---
---------------------

CREATE FUNCTION consumir_item(jogador_id INT, item_instancia_id INT) RETURNS VOID AS $$
DECLARE
    tipo_item TipoItemNaoFabricavel;
    incremento_vida INTEGER;
    inventario_id INTEGER;
    vida_jogador INTEGER;
    item_id INTEGER;
BEGIN
    SELECT ii.inventario, ii.item
    INTO inventario_id, item_id
    FROM instancia_item ii
    WHERE ii.id = item_instancia_id;

    IF inventario_id IS NULL THEN
        RAISE EXCEPTION 'Item não encontrado no inventário do jogador.';
    END IF;

    SELECT CASE
        WHEN EXISTS (SELECT 1 FROM medicamento med WHERE med.id = item_id) THEN 'medicamento'
        WHEN EXISTS (SELECT 1 FROM comida com WHERE com.id = item_id) THEN 'comida'
        ELSE NULL
    END INTO tipo_item;

    IF tipo_item IS NULL THEN
        RAISE EXCEPTION 'O item informado não pode ser consumido.';
    END IF;

    IF tipo_item = 'medicamento' THEN
        SELECT m.cura
        INTO incremento_vida
        FROM medicamento m
        WHERE m.id = item_id;
    ELSIF tipo_item = 'comida' THEN
        SELECT c.recuperacao_vida
        INTO incremento_vida
        FROM comida c
        WHERE c.id = item_id;
    END IF;

    SELECT vida INTO vida_jogador
    FROM jogador
    WHERE id = jogador_id;

    UPDATE jogador
    SET vida = LEAST(vida_jogador + incremento_vida, 10)
    WHERE id = jogador_id;

    DELETE FROM instancia_item
    WHERE id = item_instancia_id;

    RAISE NOTICE 'Item consumido com sucesso e vida do jogador atualizada.';
END;
$$ LANGUAGE plpgsql;

---------------------
---
---  MALHAR NA ACADEMIA
---
---------------------

CREATE FUNCTION malhar_jogador(id_jogador INT)
RETURNS VOID AS $$
DECLARE
    forca_atual INTEGER;
    lugar_atual INTEGER;
    regiao_atual INTEGER;
BEGIN
    SELECT lugar, regiao
    INTO lugar_atual, regiao_atual
    FROM jogador
    WHERE id = id_jogador;

    IF lugar_atual = 24 AND regiao_atual = 6 THEN
        SELECT forca INTO forca_atual
        FROM jogador
        WHERE id = id_jogador;

        IF forca_atual >= 10 THEN
            RAISE NOTICE 'A força do jogador % já está no limite de 10. Não pode malhar mais.', id_jogador;
            RETURN;
        END IF;

        UPDATE jogador
        SET forca = forca_atual + 1
        WHERE id = id_jogador;

        RAISE NOTICE 'O jogador % malhou com sucesso! Força incrementada para %.', id_jogador, forca_atual + 1;
    ELSE
        RAISE EXCEPTION 'O jogador só pode malhar na Academia Simples (lugar 24, regiao 6).';
    END IF;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---  ESCOLHER GANGUE
---
---------------------

CREATE FUNCTION selecionar_gangue(id_jogador INT, nova_gangue TipoGangue)
RETURNS VOID AS $$
DECLARE
    gangue_atual TipoGangue;
BEGIN
    SELECT gangue INTO gangue_atual
    FROM jogador
    WHERE id = id_jogador;

    IF gangue_atual IS NOT NULL THEN
        RAISE EXCEPTION 'O jogador % já está em uma gangue e não pode trocar de gangue.', id_jogador;
    END IF;

    IF nova_gangue NOT IN ('palhaco', 'polvo') THEN
        RAISE EXCEPTION 'O valor % para a gangue não é válido. Os valores permitidos são ''palhaco'' e ''polvo''.', nova_gangue;
    END IF;

    UPDATE jogador
    SET gangue = nova_gangue
    WHERE id = id_jogador;

    RAISE NOTICE 'Jogador % agora faz parte da gangue %.', id_jogador, nova_gangue;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION remover_gangue(id_jogador INT)
RETURNS VOID AS $$
DECLARE 
    gangue_atual TipoGangue;
BEGIN
    SELECT gangue INTO gangue_atual
    FROM jogador
    WHERE id = id_jogador;

    IF gangue_atual IS NULL THEN
        RAISE NOTICE 'O jogador % não está em nenhuma gangue.', id_jogador;
        RETURN;
    END IF;

    UPDATE jogador
    SET gangue = NULL
    WHERE id = id_jogador;

    RAISE NOTICE 'A gangue do jogador % foi removida.', id_jogador;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---  TROCA
---
---------------------

CREATE FUNCTION realizar_troca(
    jogador_id INT,
    pessoa_id INT,
    item_jogador_id INT,
    item_pessoa_id INT
) RETURNS VOID AS $$
DECLARE
	tamanho_item_jogador SMALLINT;
	tamanho_item_pessoa SMALLINT;
	inventario_pessoa INTEGER;
	inventario_jogador INTEGER;
	is_corrupto_atb BOOLEAN;
	pessoa_tipo TipoPessoa;
BEGIN
	SELECT tipo INTO pessoa_tipo
    FROM pessoa
    WHERE id = pessoa_id;

    IF pessoa_tipo = 'informante' THEN
        UPDATE jogador
		SET tempo_vida = 1
		WHERE id = jogador_id;
		RETURN;
    END IF;

	IF pessoa_tipo = 'policial' THEN

        SELECT corrupto INTO is_corrupto_atb
		FROM policial
		WHERE id = pessoa_id;

		IF NOT is_corrupto_atb THEN

			UPDATE jogador
			SET tempo_vida = 1
			WHERE id = jogador_id;

			RETURN;

		END IF;

    END IF;


	SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) INTO tamanho_item_jogador
	FROM instancia_item ins
	LEFT JOIN arma arm ON arm.id = ins.item
	LEFT JOIN ferramenta fer ON fer.id = ins.item
	LEFT JOIN comida com ON com.id = ins.item
	LEFT JOIN medicamento med ON med.id = ins.item
	LEFT JOIN utilizavel uti ON uti.id = ins.item
	WHERE ins.id = item_jogador_id;

	SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) INTO tamanho_item_pessoa
	FROM instancia_item ins
	LEFT JOIN arma arm ON arm.id = ins.item
	LEFT JOIN ferramenta fer ON fer.id = ins.item
	LEFT JOIN comida com ON com.id = ins.item
	LEFT JOIN medicamento med ON med.id = ins.item
	LEFT JOIN utilizavel uti ON uti.id = ins.item
	WHERE ins.id = item_pessoa_id;

	IF tamanho_item_jogador = tamanho_item_pessoa THEN
		SELECT id INTO inventario_jogador
		FROM inventario
		WHERE pessoa = jogador_id;

		SELECT id INTO inventario_pessoa
		FROM inventario
		WHERE pessoa = pessoa_id;

		UPDATE instancia_item
		SET pessoa = pessoa_id, inventario = inventario_pessoa
		WHERE id = item_jogador_id;

		UPDATE instancia_item
		SET pessoa = jogador_id, inventario = inventario_jogador
		WHERE id = item_pessoa_id;

		UPDATE inventario
		SET inventario_ocupado = inventario_ocupado - tamanho_item_pessoa
		WHERE id = pessoa_id;

		UPDATE inventario
		SET inventario_ocupado = inventario_ocupado - tamanho_item_pessoa
		WHERE id = jogador_id;

	ELSE
		RAISE EXCEPTION 'Itens com tamanho diferente, troca negada.';
	END IF;

END;
$$ LANGUAGE plpgsql;

---------------------
---
---  MISSAO
---
---------------------

CREATE FUNCTION gerencia_missao(id_jogador INT)
RETURNS void AS $$
DECLARE
	tempoVida INTEGER;
	missaoAtual INTEGER;
    id_inventario INTEGER;
	linhas INTEGER;
	fuga1 BOOLEAN;
	fuga2 BOOLEAN;
	fuga3 BOOLEAN;
BEGIN
    -- Guarda tempo de vida e a missão atual
	SELECT missao, tempo_vida
	INTO missaoAtual, tempoVida
	FROM Jogador
	WHERE id = id_jogador;

    SELECT id INTO id_inventario
    FROM inventario
    WHERE pessoa = id_jogador;
	
	-- No primeiro dia o jogador terá as missões 5, 3 e 4
	IF tempoVida = 10 THEN
		-- Guarda quantas vezes o jogador andou pelo mapa
		SELECT rows INTO linhas
		FROM pg_stat_statements
		WHERE query ILIKE 'SELECT movimenta_jogador($' || id_jogador || '%';
		
		-- Checa se ele explorou o mapa ou não
		IF linhas < 52 THEN
			-- Inicialmente jogador terá a missão 5 (Explorar o mapa)
			UPDATE Jogador
			SET missao = 5
			WHERE id = id_jogador;
			
		ELSIF linhas = 52 THEN
			RAISE NOTICE 'Missão "Explorar o mapa" completa com sucesso!';
		END IF;

		IF linhas > 52 AND linhas <= 55 THEN
			-- Missão 3 (Observar cela)
			UPDATE Jogador
			SET missao = 3
			WHERE id = id_jogador;

 			-- Checa se o jogador está na Cela D
			PERFORM 1
			FROM Jogador
			WHERE id = id_jogador AND lugar = 5;
			IF FOUND THEN
				PERFORM pg_sleep(60);  -- Espera por 60 segundos
	    		RAISE NOTICE 'Missão "Observar cela" completa com sucesso!';
			END IF;

			-- Recompensa o jogador com uma bandagem
			INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
        	VALUES (30, NULL, NULL, id_jogador, id_inventario);
			RAISE NOTICE 'Você ganhou uma bandagem!';
		END IF;
			
		IF linhas > 55 THEN
			-- Missão 4 (Escolher gangue)
			UPDATE Jogador
			SET missao = 4
			WHERE id = id_jogador;

            PERFORM 1
            FROM Jogador
            WHERE id = id_jogador AND  gangue IN ('palhaco', 'polvo');
            IF FOUND THEN			
                RAISE NOTICE 'Missão "Escolher gangue" completa com sucesso!';
                
                -- Recompensa o jogador com um cigarro
                INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
                VALUES (27, NULL, NULL, id_jogador, id_inventario);
                RAISE NOTICE 'Você ganhou um cigarro!';
                -- Ficar sem missão
                UPDATE Jogador
                SET missao = NULL
                WHERE id = id_jogador;
            END IF;
		END IF;
	END IF;

	-- Outros dias
	IF tempoVida < 10 THEN
		-- Checa se o jogador está sem missão para resetar o quanto ele andou
		IF missaoAtual IS NULL THEN
			SELECT pg_stat_statements_reset();
		END IF;

		-- Guarda quantas vezes o jogador andou pelo mapa
		SELECT rows INTO linhas
		FROM pg_stat_statements
		WHERE query ILIKE 'SELECT movimenta_jogador($' || id_jogador || '%';
		
		IF linhas <= 52 THEN
			-- Missão 9 (Encontre o informante)
			UPDATE Jogador
			SET missao = 9
			WHERE id = id_jogador;
			
			-- Checa se o jogador ta no mesmo lugar do informante
			PERFORM 1
			FROM Jogador AS j
			INNER JOIN Informante AS i ON j.lugar = i.lugar;
			IF FOUND THEN
				RAISE NOTICE 'Missão "Encontre o informante" completa com sucesso!';
				-- Recompensa o jogador com um pedaço grande metal
				INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
		        VALUES (20, NULL, NULL, id_jogador, id_inventario);
				RAISE NOTICE 'Você ganhou um pedaço grande metal!';
			END IF;
        END IF;
        
		IF linhas > 52 THEN
			-- Missão 10 (Vença um jogo de basquete)
			UPDATE Jogador
			SET missao = 10
			WHERE id = id_jogador;
			
			-- Checa se o jogador está na Quadra de Basquete
			PERFORM 1
			FROM Jogador
			WHERE id = id_jogador AND lugar = 25;
			IF FOUND THEN
				RAISE NOTICE 'Missão "Vença um jogo de basquete" completa com sucesso!';
				-- Recompensa o jogador com um isqueiro
				INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
		        VALUES (25, NULL, NULL, id_jogador, id_inventario);
				RAISE NOTICE 'Você ganhou um isqueiro!';
			END IF;
		END IF;

		IF linhas > 60 THEN
			-- Missão 11 (Fique maromba)
			UPDATE Jogador
			SET missao = 11
			WHERE id = id_jogador;

			-- Checa se o jogador está na Academia Simples
			PERFORM 1
			FROM Jogador
			WHERE id = id_jogador AND lugar = 24;
			IF FOUND THEN
				-- Checa se o jogador malhou
				PERFORM 1
				FROM pg_stat_statements
				WHERE query ILIKE 'UPDATE jogador SET forca%';
				IF FOUND THEN
					RAISE NOTICE 'Missão "Fique maromba" completa com sucesso!';
					-- Recompensa o jogador com uma carne
					INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
			        VALUES (34, NULL, NULL, id_jogador, id_inventario);
					RAISE NOTICE 'Você ganhou uma carne!';
				END IF;
			END IF;
		ELSIF linhas > 65 THEN
			-- Missão 6 (Brigue com alguém)
			UPDATE Jogador
			SET missao = 6
			WHERE id = id_jogador;
			
			-- Checa se o jogador brigou
			PERFORM 1
			FROM pg_stat_statements
			WHERE query ILIKE 'UPDATE jogador SET vida%';
			IF FOUND THEN
				RAISE NOTICE 'Missão "Brigue com alguém" completa com sucesso!';
				-- Recompensa o jogador com uma carne
				INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
		        VALUES (34, NULL, NULL, id_jogador, id_inventario);
				RAISE NOTICE 'Você ganhou uma carne!';
			END IF;
		END IF;

		IF linhas > 70 THEN
			-- Missão 7 (Vença uma briga)
			UPDATE Jogador
			SET missao = 7
			WHERE id = id_jogador;

			-- Checa se o jogador venceu
			PERFORM 1
			FROM pg_stat_statements
			WHERE query ILIKE 'UPDATE jogador SET habilidade_briga%';
			IF FOUND THEN
				RAISE NOTICE 'Missão "Vença uma briga" completa com sucesso!';
				-- Recompensa o jogador com uma morfina
				INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
		        VALUES (29, NULL, NULL, id_jogador, id_inventario);
				RAISE NOTICE 'Você ganhou uma morfina!';
			END IF;
		END IF;

        -- Checa se o jogador está na solitária oeste
		PERFORM 1
		FROM Jogador
		WHERE id = id_jogador AND lugar = 1;
		IF FOUND THEN
			-- Missão 1 (Fuja da solitária oeste)
			UPDATE Jogador
			SET missao = 1
			WHERE id = id_jogador;
        END IF;
		-- Verifica se o jogador tem a missão 1 e está no corredor das celas
        PERFORM 1
		FROM Jogador
		WHERE id = id_jogador AND lugar = 2 AND missao = 1;
		IF FOUND THEN
			RAISE NOTICE 'Missão "Fuja da solitária oeste" completa com sucesso!';
			-- Recompensa o jogador com a Chave da Oficina A
			INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
			VALUES (38, NULL, NULL, id_jogador, id_inventario);
			RAISE NOTICE 'Você ganhou a Chave da Oficina A!';
		END IF;

        -- Checa se o jogador está na solitária leste
		PERFORM 1
		FROM Jogador
		WHERE id = id_jogador AND lugar = 9;
		IF FOUND THEN
			-- Missão 2 (Fuja da solitária leste)
			UPDATE Jogador
			SET missao = 2
			WHERE id = id_jogador;
		END IF;
		-- Verifica se o jogador tem a missão 2 e está no corredor das celas
        PERFORM 1
		FROM Jogador
		WHERE id = id_jogador AND lugar = 2 AND missao = 2;
		IF FOUND THEN
			RAISE NOTICE 'Missão "Fuja da solitária leste" completa com sucesso!';
			-- Recompensa o jogador com a Chave da Oficina B
			INSERT INTO instancia_item (item, lugar, regiao, pessoa, inventario)
			VALUES (39, NULL, NULL, id_jogador, id_inventario);
			RAISE NOTICE 'Você ganhou a Chave da Oficina B!';
		END IF;

		IF linhas > 100 THEN
			-- Missão 8 (Fuja da prisão)
			UPDATE Jogador
			SET missao = 8
			WHERE id = id_jogador;
        END IF;
		
		SELECT fuga_prisao_esgoto(id_jogador) INTO fuga1;
		SELECT fuga_prisao_floresta(id_jogador) INTO fuga2;
		SELECT fuga_prisao_disfarcado(id_jogador) INTO fuga3;
		IF fuga1 IS TRUE THEN
			RAISE NOTICE 'Você fugiu pelo esgoto! Parabéns!';
			RETURN;
		ELSIF fuga2 IS TRUE THEN
			RAISE NOTICE 'Você fugiu pela floresta! Parabéns!';
			RETURN;
		ELSIF fuga3 IS TRUE THEN
			RAISE NOTICE 'Você fugiu disfarçado pela entrada! Parabéns!';
			RETURN;
		END IF;
	END IF;
	RETURN;
END;
$$ LANGUAGE plpgsql;

---------------------
---
---  FUGAS PRISAO
---
---------------------

CREATE FUNCTION fuga_prisao_esgoto(id_jogador INT)
RETURNS BOOLEAN AS $$
BEGIN
	PERFORM 1
	FROM Jogador
	WHERE id = id_jogador AND lugar = 31;
	IF FOUND THEN
		RETURN true;
	END IF;
	RETURN false;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION fuga_prisao_floresta(id_jogador INT)
RETURNS BOOLEAN AS $$
BEGIN
	PERFORM 1
	FROM Jogador
	WHERE id = id_jogador AND lugar = 33;
	IF FOUND THEN
		RETURN true;
	END IF;
	RETURN false;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION fuga_prisao_disfarcado(id_jogador INT)
RETURNS BOOLEAN AS $$
BEGIN
	PERFORM 1
	FROM Jogador
	WHERE id = id_jogador AND lugar = 32;
	IF FOUND THEN
		RETURN true;
	END IF;
	RETURN false;
END;
$$ LANGUAGE plpgsql;

COMMIT;
````

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão |       Descrição       | Autores                                          |
|------------|--------|:---------------------:|--------------------------------------------------|
| 26/07/2024 | `1.0`  | Criação do documento. | [Júlio Cesar](https://github.com/Julio1099)      |
| 05/09/2024 | `1.1`  |  Atualiza triggers.   | [João Antonio G.](https://github.com/joaoseisei) |

</div>
