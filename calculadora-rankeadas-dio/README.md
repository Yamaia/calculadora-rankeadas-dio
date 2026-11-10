# 🎮 Calculadora de Partidas Rankeadas

Projeto do desafio da **DIO** que calcula o saldo de partidas rankeadas de um jogador (vitórias - derrotas) e informa o seu nível, de *Ferro* a *Imortal*.

Desenvolvido por Yamaia, desenvolvedor Python, como parte do meu portfólio no GitHub.

## 🎯 Objetivo

Criar uma **função** que recebe a quantidade de vitórias e derrotas de um jogador, guarda o saldo (`vitórias - derrotas`) em uma variável e exibe:

```
O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**
```

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **Variáveis** | `saldo_vitorias`, `nivel`, `historico`, constantes `FAIXAS` e `NIVEL_FINAL` |
| **Operadores** | subtração (saldo), comparação (`<=`, `<`), `or`, f-strings |
| **Estruturas de decisão** | `if / elif / else` em `classificar_nivel` e na escolha do critério |
| **Laços de repetição** | `while` (menu e validação de entrada) e `for` (tabela de faixas e resumo) |
| **Funções** | `calcular_saldo`, `classificar_nivel`, `classificar_nivel_por_laco`, `calcular_rankeada`, `ler_inteiro`, `main` |

## 📊 Tabela de níveis

| Vitórias | Nível |
|---|---|
| até 10 | Ferro |
| 11 a 20 | Bronze |
| 21 a 50 | Prata |
| 51 a 80 | Ouro |
| 81 a 90 | Diamante |
| 91 a 100 | Lendário |
| 101 ou mais | Imortal |

## ⚖️ Decisões de projeto

1. **Nível calculado pelas vitórias.** O enunciado manda calcular o saldo como `vitórias - derrotas`, mas a tabela de níveis é escrita em função das *vitórias*. Segui o enunciado: o **saldo é exibido** na mensagem e o **nível sai das vitórias**.
2. **Critério opcional.** Como a mensagem fala em "saldo", a função aceita `criterio="saldo"` para classificar pelo saldo (saldo negativo vira Ferro). O padrão continua sendo `"vitorias"`.
3. **Valor 10 na fronteira.** O enunciado diz "menor do que 10" para Ferro e começa Bronze em 11, deixando exatamente **10** sem regra. Incluí 10 em **Ferro**, mantendo faixas contínuas (cada nível vai até o seu limite superior, inclusive).
4. **Saldo negativo é permitido.** Quem perde mais do que vence tem saldo negativo, e isso é exibido normalmente.

## 🗂️ Estrutura

```
calculadora-rankeadas-dio/
├── src/
│   └── rankeadas.py        # código principal
├── tests/
│   └── test_rankeadas.py   # testes automatizados
├── .gitignore
└── README.md
```

## ▶️ Como executar

Requisito: Python 3.8+ (sem dependências externas).

```bash
git clone https://github.com/<seu-usuario>/calculadora-rankeadas-dio.git
cd calculadora-rankeadas-dio
python src/rankeadas.py
```

### Exemplo de uso

```
==================================================
   🎮  CALCULADORA DE PARTIDAS RANKEADAS  🎮
==================================================

Quantidade de vitórias: 30
Quantidade de derrotas: 10

O Herói tem de saldo de **20** está no nível de **Prata**

Calcular outro jogador? (s/n): n

--- Resumo da sessão ---
1. Vitórias:   30  Derrotas:   10  Saldo:    20
```

### Usando a função em outro código

```python
from rankeadas import calcular_rankeada

resultado = calcular_rankeada(vitorias=55, derrotas=20)
print(resultado)
# O Herói tem de saldo de **35** está no nível de **Ouro**
```

## ✅ Testes

```bash
python -m unittest discover -s tests -v
```

Cobrem todos os **valores de fronteira** (10, 11, 20, 21, 50, 51, 80, 81, 90, 91, 100, 101), saldo negativo, os dois critérios, entradas inválidas e o formato da mensagem.

## 🔍 Como funciona

1. **`calcular_saldo`** – subtrai derrotas das vitórias.
2. **`classificar_nivel`** – cadeia `if/elif/else` comparando com o limite de cada faixa, do menor para o maior.
3. **`classificar_nivel_por_laco`** – versão orientada a dados: percorre `FAIXAS` com `for`.
4. **`calcular_rankeada`** – função principal: valida, calcula o saldo, classifica e monta a mensagem.
5. **`main`** – menu em `while` que permite calcular vários jogadores e mostra um resumo.

## 🚀 Ideias de evolução

- Calcular taxa de vitória (winrate) em porcentagem
- Salvar o histórico de jogadores em JSON/CSV
- API com FastAPI e interface em React
- Ranking com vários jogadores ordenados por saldo

## 📚 Aprendizados

- Separar o cálculo (função pura) da interação com o usuário
- Tratar **casos de fronteira** e ambiguidades do enunciado
- Testes automatizados com `unittest` e `subTest`

## 🔗 Referências

- [Desafio DIO](https://www.dio.me/)
- [Documentação Python](https://docs.python.org/3/)
