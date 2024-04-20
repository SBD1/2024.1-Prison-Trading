# Modelo Entidade-Relacionamento

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
    - Jogador: <ins>r</ins>e<ins>s</ins>p<ins>e</ins>it<ins>o</ins>, tempo_vida
- Item: <ins>nome</ins>, utilizavel, lugar
- Lugar: <ins>nome</ins>, nivel_seguranca
- Gangue: <ins>nome</ins>, lider, gangue_rival(multivalorada), prisioneiros(multivalorado)
- Negociaçao: data, lugar, itens (multivalorado)


## Relacionamento

- Pessoa - *Possui* - Item
  - Cardinalidade: N - 0-N
  - Papel: Possui - É possuído

---

- Pessoa - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Item - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Jogador - *Entra* - Gangue
  - Cardinalidade: 0-1 - 0-1
  - Papel: Entra - Possui

---

- Prisioneiro - *Está* - Gangue
  - Cardinalidade: N - N  
  -  Papel: Está - Possui

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

- Gangue - *É liderada* - Prisioneiro
  - Cardinalidade: 1 - 1
  - Papel: É Liderada - Lidera

---

- Gangue - *Rivaliza* - Gangue
  - Cardinalidade: 1-N - 1-N
  - Papel: Rivaliza - É Rival

---

# Histórico de versão 

| Data | Versão | Descrição | Autores                                                                                                                                                                                                  |
|:------:|:--------:|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/04/2024 | `1.0` | Criação da primeira versão. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                         |
| 10/04/2024 | `1.1` | Segunda Versão. | [Fernando Gabriel](https://github.com/show-dawn), [Julio Cesar](https://github.com/julio1099)                                                                                                            |
| 11/04/2024 | `1.2` | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099), |
| 13/04/2024 | `1.3` | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099), |
