<center>

# pgAgent

</center>

---

<CENTER>

# O que é?

</CENTER>

> É um plugin utilizado para executar funções periodicamente, utilizamos o mesmo para chamar funções de movimentação de prisioneiros,
> popular itens do mapa, reduzir tempo de vida de jogador e criar motins.
> 
> pgAgent é um plugin externo, caso esteja no **Windows** é possivel ser adquirido através do **Aplication Stack Builder**, que está disponível
> na instalação do PostgreSQL.

---

<center>

# Funções

</center>

## Movimenta prisioneiros

> Essa função deve ser acionada a acada 5 minutos.

````sql
SELECT movimenta_prisioneiros();
````

---

## Reduzir tempo de vida e Popula itens

> Essa função deve ser acionada a acada 10 minutos.

````sql
BEGIN;
    SELECT reduzir_tempo_vida();
    SELECT popula_itens();
COMMIT;
````

---

## Inicia motim

> Essa função deve ser acionada a acada 30 minutos.

````sql
SELECT inicia_motim();
````

## Finaliza motim

> Essa função deve ser acionada a acada 33 minutos.

````sql
SELECT finaliza_motim();
````

---
<center>

# Jobs

</center>

## Movimenta prisioneiros

> Na criação do job de movimentação de prisioneiros é obrigatorio obter o sequinte sql no final.

````sql
DO $$
DECLARE
jid integer;
    scid integer;
BEGIN
-- Creating a new job
INSERT INTO pgagent.pga_job(
    jobjclid, jobname, jobdesc, jobhostagent, jobenabled
) VALUES (
             1::integer, '5 min'::text, ''::text, ''::text, true
         ) RETURNING jobid INTO jid;

-- Steps
-- Inserting a step (jobid: NULL)
INSERT INTO pgagent.pga_jobstep (
    jstjobid, jstname, jstenabled, jstkind,
    jstconnstr, jstdbname, jstonerror,
    jstcode, jstdesc
) VALUES (
             jid, 'codigo'::text, true, 's'::character(1),
             ''::text, 'Prison-Trading'::name, 'f'::character(1),
             'SELECT movimenta_prisioneiros();'::text, ''::text
         ) ;

-- Schedules
-- Inserting a schedule
INSERT INTO pgagent.pga_schedule(
    jscjobid, jscname, jscdesc, jscenabled,
    jscstart,     jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths
) VALUES (
             jid, 'TIMER'::text, ''::text, true,
             '2024-09-05 00:00:00 -03:00'::timestamp with time zone,
             -- Minutes
             '{t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f,t,f,f,f,f}'::bool[]::boolean[],
             -- Hours
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Week days
             '{t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Month days
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Months
             '{t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[]
         ) RETURNING jscid INTO scid;
END
$$;
````

---

## Reduzir tempo de vida e Popula itens

> Na criação do job de reduzir tempo de vida e popula itens é obrigatorio obter o sequinte sql no final.

````sql
DO $$
DECLARE
jid integer;
    scid integer;
BEGIN
-- Creating a new job
INSERT INTO pgagent.pga_job(
    jobjclid, jobname, jobdesc, jobhostagent, jobenabled
) VALUES (
             1::integer, '10 min'::text, ''::text, ''::text, true
         ) RETURNING jobid INTO jid;

-- Steps
-- Inserting a step (jobid: NULL)
INSERT INTO pgagent.pga_jobstep (
    jstjobid, jstname, jstenabled, jstkind,
    jstconnstr, jstdbname, jstonerror,
    jstcode, jstdesc
) VALUES (
             jid, 'codigo'::text, true, 's'::character(1),
             ''::text, 'Prison-Trading'::name, 'f'::character(1),
             'BEGIN; 
             SELECT reduzir_tempo_vida();
             SELECT popula_itens();
         COMMIT;'::text, ''::text
         ) ;

-- Schedules
-- Inserting a schedule
INSERT INTO pgagent.pga_schedule(
    jscjobid, jscname, jscdesc, jscenabled,
    jscstart,     jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths
) VALUES (
             jid, 'timer'::text, ''::text, true,
             '2024-09-05 00:00:00 -03:00'::timestamp with time zone,
             -- Minutes
             '{t,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f}'::bool[]::boolean[],
             -- Hours
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Week days
             '{t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Month days
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Months
             '{t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[]
         ) RETURNING jscid INTO scid;
END
$$;
````

---

## Inicia motim

> Na criação do job de iniciar motim é obrigatorio obter o sequinte sql no final.

````sql
DO $$
DECLARE
jid integer;
    scid integer;
BEGIN
-- Creating a new job
INSERT INTO pgagent.pga_job(
    jobjclid, jobname, jobdesc, jobhostagent, jobenabled
) VALUES (
             1::integer, '30 min'::text, ''::text, ''::text, true
         ) RETURNING jobid INTO jid;

-- Steps
-- Inserting a step (jobid: NULL)
INSERT INTO pgagent.pga_jobstep (
    jstjobid, jstname, jstenabled, jstkind,
    jstconnstr, jstdbname, jstonerror,
    jstcode, jstdesc
) VALUES (
             jid, 'codigo'::text, true, 's'::character(1),
             ''::text, 'Prison-Trading'::name, 'f'::character(1),
             'SELECT inicia_motim();'::text, ''::text
         ) ;

-- Schedules
-- Inserting a schedule
INSERT INTO pgagent.pga_schedule(
    jscjobid, jscname, jscdesc, jscenabled,
    jscstart,     jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths
) VALUES (
             jid, 'timer'::text, ''::text, true,
             '2024-09-05 00:00:00-03'::timestamp with time zone,
             -- Minutes
             '{f,t,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f}'::bool[]::boolean[],
             -- Hours
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Week days
             '{t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Month days
             '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
             -- Months
             '{t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[]
         ) RETURNING jscid INTO scid;
END
$$;
````
---

## Finaliza motim

> Na criação do job de finaliza motim é obrigatorio obter o sequinte sql no final.

````sql
DO $$
DECLARE
    jid integer;
    scid integer;
BEGIN
-- Creating a new job
INSERT INTO pgagent.pga_job(
    jobjclid, jobname, jobdesc, jobhostagent, jobenabled
) VALUES (
    1::integer, '33 min'::text, ''::text, ''::text, true
) RETURNING jobid INTO jid;

-- Steps
-- Inserting a step (jobid: NULL)
INSERT INTO pgagent.pga_jobstep (
    jstjobid, jstname, jstenabled, jstkind,
    jstconnstr, jstdbname, jstonerror,
    jstcode, jstdesc
) VALUES (
    jid, 'codigo'::text, true, 's'::character(1),
    ''::text, 'Prison-Trading'::name, 'f'::character(1),
    'SELECT finaliza_motim();'::text, ''::text
) ;

-- Schedules
-- Inserting a schedule
INSERT INTO pgagent.pga_schedule(
    jscjobid, jscname, jscdesc, jscenabled,
    jscstart,     jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths
) VALUES (
    jid, 'timer'::text, ''::text, true,
    '2024-09-08 00:00:00-03'::timestamp with time zone, 
    -- Minutes
    '{f,f,f,t,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f}'::bool[]::boolean[],
    -- Hours
    '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Week days
    '{t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Month days
    '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Months
    '{t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[]
) RETURNING jscid INTO scid;
END
$$;
````

---
<center>

# Observações

</center>

> Para o job conseguir conectar sem problemas é necessário alterar o **METHOD** do **pg_hba.conf** para **trust**, 
> pois desse jeito não é preciso de senha do usuário postgresql.

---
<center>

# Resultado

</center>

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/pgagent.jpg?raw=true"/></div>
</div>

---
<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |       Descrição       | Autores                                          |
|:----------:|:------:|:---------------------:|--------------------------------------------------|
| 05/09/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |

</div>
