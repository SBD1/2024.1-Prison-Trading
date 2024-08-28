<center>

# Triggers

</center>

# O que é?

> *Triggers* são um recurso do SQL (Structured Query Language) que permite a execução automática de uma ação definida (como uma instrução `INSERT`, `UPDATE` ou `DELETE`) quando um evento específico ocorre em uma tabela ou visão. Elas são usadas para garantir a integridade dos dados, automatizar processos, e implementar regras de negócios diretamente no banco de dados, sem a necessidade de intervenção manual.

---

<center>

## Update

</center>

```sql
CREATE FUNCTION update_instancia()
RETURNS trigger AS $update_instancia$
-- DECLARACAO DE VARIAVEIS
DECLARE
    inventario_atb INTEGER;
    item_atb INTEGER;
    inventario_ocupado_atb SMALLINT;
    tamanho_inventario_atb INTEGER;
    tamanho_item_atb INTEGER;
    total_atb SMALLINT;
	lugar_jogador_atb INTEGER;
BEGIN
    inventario_atb := NEW.inventario;
    item_atb := NEW.item;

    SELECT inventario_ocupado, tamanho INTO inventario_ocupado_atb, tamanho_inventario_atb
    FROM inventario
    WHERE id = inventario_atb;

    SELECT COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) INTO tamanho_item_atb
    FROM item ite
    LEFT JOIN arma arm
    ON arm.id = ite.id
    LEFT JOIN ferramenta fer
    ON fer.id = ite.id
    LEFT JOIN comida com
    ON com.id = ite.id
    LEFT JOIN medicamento med
    ON med.id = ite.id
    LEFT JOIN utilizavel uti
    ON uti.id = ite.id
    WHERE ite.id = item_atb;

    total_atb := inventario_ocupado_atb + tamanho_item_atb;

    IF total_atb > tamanho_inventario_atb THEN
    	RAISE EXCEPTION 'Espaço insuficiente no inventário. Atualização bloqueada. Total ocupado: % | Tamanho do item: % | Total atual: %', 
        inventario_ocupado_atb, tamanho_item_atb, total_atb;
	END IF;

	RAISE NOTICE 'Espaço disponível no inventário.';

    UPDATE inventario
    SET inventario_ocupado = total_atb
    WHERE id = inventario_atb;

	IF OLD.lugar IS DISTINCT FROM NEW.lugar THEN
        RAISE NOTICE 'O atributo regiao foi alterado de % para %', OLD.lugar, NEW.lugar;
		-- CARA PEGANDO ITEM NO CHAO

		SELECT lugar INTO lugar_jogador_atb
		FROM jogador
		WHERE id = NEW.pessoa;

		IF lugar_jogador_atb <> OLD.lugar THEN
			RAISE EXCEPTION 'Jogador não pode pegar o item, pois não está no mesmo lugar da instancia';
		END IF;

    END IF;

    RETURN NEW;

END;
$update_instancia$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_item_update
BEFORE UPDATE ON instancia_item
FOR EACH ROW EXECUTE PROCEDURE update_instancia();
```


<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão |           Descrição            | Autores                                       |
|------------|--------|:------------------------------:|-----------------------------------------------|
| 26/07/2024 | `1.0`  |      Criação do documento.     | [Júlio Cesar](https://github.com/Julio1099)   |