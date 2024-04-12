# Modelo Entidade-Relacionamento

O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de um banco de dados.

<div align="center">
<div align="center"><img src= "https://github.com/SBD1/2024.1-Prison-Trading/blob/main/docs/Images/MER.png?raw=true"/></div>
</div>

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

- Pessoa: <ins>id_pessoa</ins>, nome, item, lugar
  - Policial: grau_corrupcao
  - Prisioneiro: antecedentes_criminais, gangue
    - Jogador: respeito, tempo_vida
- Item: <ins>nome</ins>, utilizavel, lugar
- Lugar: <ins>nome</ins>, nivel_seguranca
- Gangue: <ins>nome</ins>, prisioneiro_lider 
- Negociaçao: data, lugar, itens (multivalorado)

## Relacionamento

- Pessoa - *possui* - Item
  - Cardinalidade: N - 0-N

- Pessoa - *está* - Lugar
  - Cardinalidade: 0-N - 1

- Item - *está* - Lugar
  - Cardinalidade: 0-N - 1 

- Jogador - *entra* - Gangue
  - Cardinalidade: 0-N - 0-N

- Prisioneiro - *esta* - Gangue
  - Cardinalidade: N - N  

- Jogador - *troca* - Pessoa
  - Cardinalidade: 1-N - 1-N

- Negociação - *envolve* - Item
  - Cardinalidade: 1-N - 1-N

- Negociação - *feita* - Lugar
  - Cardinalidade: 1-N - 1-N

- Gangue - *é liderada* - Prisioneiro
  - cardinalidade: N - 1    


# Histórico de versão 

| Data | Versão | Descrição | Autores |
|:------:|:--------:|-----------|-------|
| 10/04/2024 | `1.0` | Criação da primeira versão. | [João Antonio G.](https://github.com/joaoseisei)
| 10/04/2024 | `1.1` | Segunda Versão. | [Fernando Gabriel](https://github.com/show-dawn),      [Julio Cesar](https://github.com/julio1099)
| 11/04/2024 | `1.2` | Criação da terceira versão. | [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099),[Fernando Gabriel](https://github.com/show-dawn),         [Breno Alexandre](https://github.com/brenoalexandre0)
