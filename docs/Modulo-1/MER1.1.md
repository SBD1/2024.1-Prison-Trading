# Modelo Entidade-Relacionamento

O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de um banco de dados.

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

- Pessoa: <ins>Id_Pessoa</ins>, Nome, itemFavorito
  - Policial: Grau_Corrupção
  - Prisioneiro: Antecendentes_Criminais, Gangue_Afiliada
    - Jogador: Respeito, Tempo_Vida
- Item: <ins>Nome</ins>, Descrição, efeito
- Lugar: <ins>Nome</ins>, Descrição
- Gangue: <ins>Nome</ins>, Descrição
- Negociaçao: Dia

## Relacionamento

- Pessoa - *possui* - Item
  - Cardinalidade: 0-N - 1
- Pessoa - *está* - Lugar
  - Cardinalidade: 0-N - 1
- Prisioneiro - *entra* - Gangue
  - Cardinalidade: 0-N - 1-N
- Jogador - *troca* - Pessoa
  - Cardinalidade: 1 - 1
- Negociação - *envolve* - Item
  - Cardinalidade: 1 - 1
- Negociação - *feita* - Lugar
  - Cardinalidade: 1 - 1

# Histórico de versão 

| Data | Versão | Descrição | Autores |
|:------:|:--------:|-----------|-------|
| 10/04/2024 | `1.0` | Criação da primeira versão. | [João Antonio G.](https://github.com/joaoseisei)
| 10/04/2024 | `1.1` | Segunda Versão. | [Fernando Gabriel, Julio Cesar.](https://github.com/show-dawn, https://github.com/julio1099)
