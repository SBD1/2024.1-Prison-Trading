<center>

# Triggers

</center>

# O que é?

> *Triggers* são um recurso do SQL (Structured Query Language) que permite a execução automática de uma ação definida (como uma instrução `INSERT`, `UPDATE` ou `DELETE`) quando um evento específico ocorre em uma tabela ou visão. Elas são usadas para garantir a integridade dos dados, automatizar processos, e implementar regras de negócios diretamente no banco de dados, sem a necessidade de intervenção manual.

---

<center>

## Insert - Instância Item

</center>

> Objetivo é não permitir que a instância de item esteja em um estado inválido.

#### Restrições do código:

* Não permitir inventário e lugar ambos nulos.
* Não permitir inventário e lugar ambos possuirem valores, um item não pode está em um inventário e lugar ao mesmo tempo.

````sql
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
````

---

<center>

## Update - Instância Item

</center>

> Objetivo principal é permitir a adição e exclusão de itens no inventário de uma pessoa na tabela instancia_item, atualizando o tamanho_ocupado.
 
#### Restrições do código:

* Não permitir que um jogador pegue um item de uma sala que ele não está.
* Não permitir que ele drope um item em uma sala que ele não está.
* Não permitir inventário e lugar ambos nulos.
* Não permitir inventário e lugar ambos possuirem valores, um item não pode está em um inventário e lugar ao mesmo tempo.

```sql
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
```

---

<center>

## Delete - Instância Item

</center>

> Objetivo é impedir inconsistencias na hora de deletar instâncias de item, atualizando o inventário ocupado.

#### Restrições do código:

* Sem restrições

````sql
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

    RETURN NEW;
END;
$delete_instancia$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_item_delete
BEFORE DELETE ON instancia_item
FOR EACH ROW EXECUTE PROCEDURE delete_instancia();
````

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão |           Descrição            | Autores                                       |
|------------|--------|:------------------------------:|-----------------------------------------------|
| 26/07/2024 | `1.0`  |      Criação do documento.     | [Júlio Cesar](https://github.com/Julio1099)   |

</div>
