<center>

# Modelo Entidade-Relacionamento

</center>

---


> O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de um banco de dados.

## Entidades 

- Pessoa
  - Policial
  - Prisioneiro
    - Jogador
- Item
- Lugar
- Gangue
- Negociação
 
## Atributos
- Pessoa: <ins>id_pessoa</ins>, nome, item(multivalorado), lugar, tipo
  - Policial: grau_corrupcao
  - Prisioneiro: antecedentes_criminais(multivalorado), gangue
    - Jogador: tempo_vida, <ins>r</ins>e<ins>s</ins>p<ins>e</ins>it<ins>o</ins>
- Item: <ins>nome</ins>, utilizavel, lugar
- Lugar: <ins>nome</ins>, nivel_seguranca
- Gangue: <ins>nome</ins>, lider, gangue_rival(multivalorada), prisioneiros(multivalorado)
- Negociaçao: data, lugar, itens (multivalorado)


## Relacionamento

- Pessoa - *Possui* - Item
  - Cardinalidade: N - 0-N
  - Papel: Possui - É posse

---

- Pessoa - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Item - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Jogador - *Troca* - Pessoa
  - Cardinalidade: 1 - 1-N
  - Papel: Troca - Troca

---

- Negociação - *Envolve* - Item
  - Cardinalidade: 1-N - N
  - Papel: Envolve - Está Envolvido

---

- Negociação - *Realiza* - Lugar
  - Cardinalidade: 1-N - 1-N
  - Papel: É Realizado - São Realizadas

---

- Jogador - *Entra* - Gangue
  - Cardinalidade: 0-1 - 0-1
  - Papel: Entra - Possui

---

- Prisioneiro - *Está* - Gangue
  - Cardinalidade: N - 1  
  -  Papel: Está - Possui

---

- Gangue - *É liderada* - Prisioneiro
  - Cardinalidade: 1 - 1
  - Papel: É Liderada - Lidera

---

- Gangue - *Rivaliza* - Gangue
  - Cardinalidade: 1-N - 1-N
  - Papel: Rivaliza - É Rival

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data | Versão | Descrição | Autores                                                                                                                                                                                                  |
|:------:|:--------:|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/04/2024 | `1.0` | Criação da primeira versão. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                         |
| 10/04/2024 | `1.1` | Segunda Versão. | [Fernando Gabriel](https://github.com/show-dawn), [Julio Cesar](https://github.com/julio1099)                                                                                                            |
| 11/04/2024 | `1.2` | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099), |
| 13/04/2024 | `1.3` | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099), |

</div>
