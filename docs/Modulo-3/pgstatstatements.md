<center>

# pg_stat_statements

</center>

---

<CENTER>

# O que é?

</CENTER>

> é uma extensão do PostgreSQL que fornece informações sobre o desempenho das consultas SQL executadas no banco de dados. Ele ajuda a monitorar e analisar as consultas para identificar quais delas estão consumindo mais recursos e quanto tempo estão levando para ser executadas.

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
<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |       Descrição       | Autores                                               |
|:----------:|:------:|:---------------------:|-------------------------------------------------------|
| 08/09/2024 | `1.0`  | Criação do documento. | [Breno Alexandre](https://github.com/brenoalexandre0) |

</div>
