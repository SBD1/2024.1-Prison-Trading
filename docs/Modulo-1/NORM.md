<center>

# Normalização

</center>

---

<center>

# O que é?

</center>

> Normalização é uma técnica criada para melhoria do projeto removendo as redundâncias, complexidades desnecessárias e inconsistências.

---

<center>

# Primeira Forma Normal

</center>

> Para estar na primeira forma normal todos os atributos são Monovalorados e Atômicos.
>
> O nosso projeto respeita a primeira forma normal, pois a partir da versão `2.0` removemos os atributos multivalorados de Pessoa e Gangue. Além disso, o projeto não possui atributos compostos.

---

<center>

# Segunda Forma Normal

</center>

> Deve estar na 1ª Forma Normal e os atributos comuns não dependem parcialmente de qualquer chave.
>
> Única entidade que apresentava esse erro era o Lugar:

### Lugar:
> descricao_lugar não depende parcialmente de qualquer chave.
> 
> lugar_anterior depende parcialmente da chave primária.

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/NORM0.png?raw=true"/></div>
</div>

> Criamos uma tabela associativa para o lugar atual e lugar anterior, ambas sendo chaves estrangeiras de Lugar, isso resolve o problema de um atributo comum depender da chave primária.


<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/NORM1.png?raw=true"/></div>
</div>

---

<center>

# Terceira Forma Normal

</center>

> Deve estar na 2ª. Forma Normal, os atributos comuns não dependem transitivamente de qualquer superchave.
> 
> Possivel erro pode estar em atributos derivados, no projeto existem 2 atributos derivados, o inventario_ocupado da tabela Inventario e respeito_jogador da Tabela Jogador.
> 
> Decidimos remover o respeito pois o mesmo era redundante, tempo_vida_jogador determinava respeito_jogador, preferimos remover esse elemento.
> 
> inventario_ocupado não possuia dependencia transivida de qualquer superchave.
> 
> Além disso não existe outros atributos comuns com dependencias transitivas de qualquer superchave.

---

<center>

# Forma Normal de Boyce-Codd

</center>

> Versão mais abrangente da 2ª. e 3ª Forma Normal. Além disso para estar na forma nomal de Boyce-Codd é necessário que:

* Não existam mais que uma chave candidata.

* Não existam pelo menos duas chaves candidatas compostas.

* Não exista intersceção entre chaves compostas.

> No nosso projeto não possuimos chaves candidatas muito menos chaves candidatas compostas, também não existe intersceção entre chaves compostas, como o projeto já estava na 2ª. e 3ª forma normal e ele satisfaz as condições específicas de Boyce-Codd então ele está na forma normal de Boyce-Codd.

---

<center>

# Quarta Forma Normal

</center>

> Última forma normal, necessário está na forma normal de Boyce-Codd, além disso não pode ter dependência multivalorada.
> 
> Embora `Instancia_Item` possa parecer ferir essa forma normal isso não se aplica, pois as chaves estrangeiras da instancia possuem valores únicos, não é possível uma instancia está em uma fabricacao e lugar ao mesmo tempo, isso garante a exclusividade.
> 
> Nenhuma Tabela possui dependência multivalorada, logo o projeto está na 4ª forma normal.

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição               | Autores                                                                                                                                          |
|:----------:|:------:|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 19/07/2024 | `1.0`  | Criação do documento.   | [João Antonio G.](https://github.com/joaoseisei)                                                                                                 |
| 20/07/2024 | `1.1`  | Normalização do projeto | [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |

</div>