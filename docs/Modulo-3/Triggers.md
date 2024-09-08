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
