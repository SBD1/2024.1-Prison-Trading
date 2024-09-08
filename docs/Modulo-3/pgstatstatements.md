<center>

# pg_stat_statements

</center>

---

<CENTER>

## O que é?

</CENTER>

> É uma extensão do PostgreSQL que fornece informações sobre o desempenho das consultas SQL executadas no banco de dados. Ele ajuda a monitorar e analisar as consultas
> para identificar quais delas estão consumindo mais recursos e quanto tempo estão levando para ser executadas.

---

<center>

## Configurando

> Para adicionar a extensão a configuração pode ser feita no arquivo postgresql.conf, onde tem shared_preload_libraries.

</center>


````txt
shared_preload_libraries = 'pg_stat_statements'
````

<center>
  
> Após salvar a alteração deve-se reiniciar o servidor do PostgreSQL com os comandos abaixo.
> Alternativamente é possível reiniciar também abrindo o Gerenciador de Serviços 'services.msc', clicar com o direito no serviço PostgreSQL e selecionar 'Reiniciar'.

</center>

````txt
net stop postgresql-x64-<versão>
net start postgresql-x64-<versão>
````

<center>
  
> Criando a extensão no PostgreSQL.

</center>

````sql
CREATE EXTENSION pg_stat_statements;
````

<center>
  
> Resetar os dados para uso nas funções.

</center>

````sql
SELECT pg_stat_statements_reset();
````

---

<center>

## Funções

</center>

### Reseta dados

> Essa função deve ser acionada após tempo_vida do jogador ser menor que 10.

````sql
SELECT pg_stat_statements_reset();
````

### Quantidade de linhas que a função movimenta_jogador() foi chamada

> Guarda quantas vezes o jogador andou pelo mapa.

````sql
BEGIN
  SELECT rows INTO linhas
  FROM pg_stat_statements
  WHERE query ILIKE 'SELECT movimenta_jogador($' || id_jogador || '%';
END;
````

### Quantidade de linhas que a função UPDATE em Jogador foi chamada para alterar a força

> Checa se o jogador malhou.

````sql
BEGIN
  PERFORM 1
  FROM pg_stat_statements
  WHERE query ILIKE 'UPDATE jogador SET forca%';
END;
````

### Quantidade de linhas que a função UPDATE em Jogador foi chamada para alterar a vida

> Checa se o jogador brigou.

````sql
BEGIN
  PERFORM 1
  FROM pg_stat_statements
  WHERE query ILIKE 'UPDATE jogador SET vida%';
END;
````

### Quantidade de linhas que a função UPDATE em Jogador foi chamada para alterar a habilidade de briga

> Checa se o jogador venceu.

````sql
BEGIN
  PERFORM 1
  FROM pg_stat_statements
  WHERE query ILIKE 'UPDATE jogador SET habilidade_briga%';
END;
````

---
<center>

## Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |       Descrição       | Autores                                               |
|:----------:|:------:|:---------------------:|-------------------------------------------------------|
| 08/09/2024 | `1.0`  | Criação do documento. | [Breno Alexandre](https://github.com/brenoalexandre0) |

</div>
