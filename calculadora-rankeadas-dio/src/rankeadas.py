"""Calculadora de partidas Rankeadas.

Conceitos aplicados: variáveis, operadores, laços de repetição,
estruturas de decisão e funções.
"""

# Tabela de níveis: (limite superior de vitórias, nível).
# Regra: vitórias <= limite -> nível. Acima de 100 -> Imortal.
NIVEL_FINAL = "Imortal"
FAIXAS = [
    (10, "Ferro"),
    (20, "Bronze"),
    (50, "Prata"),
    (80, "Ouro"),
    (90, "Diamante"),
    (100, "Lendário"),
]


def calcular_saldo(vitorias: int, derrotas: int) -> int:
    """Saldo de Rankeadas = vitórias - derrotas (pode ser negativo)."""
    return vitorias - derrotas


def classificar_nivel(vitorias: int) -> str:
    """Retorna o nível do jogador com if/elif/else."""
    if vitorias < 0:
        raise ValueError("A quantidade de vitórias não pode ser negativa.")

    if vitorias <= 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return NIVEL_FINAL


def classificar_nivel_por_laco(vitorias: int) -> str:
    """Versão alternativa: percorre a tabela FAIXAS com um laço (for)."""
    if vitorias < 0:
        raise ValueError("A quantidade de vitórias não pode ser negativa.")

    for limite, nivel in FAIXAS:
        if vitorias <= limite:
            return nivel
    return NIVEL_FINAL


def calcular_rankeada(vitorias: int, derrotas: int, criterio: str = "vitorias") -> str:
    """Função principal do desafio.

    Recebe vitórias e derrotas, calcula o saldo e devolve a mensagem final.

    criterio:
      "vitorias" (padrão) -> o nível sai da tabela do enunciado, que usa vitórias;
      "saldo"             -> o nível sai do saldo (vitórias - derrotas), com
                             saldo negativo tratado como Ferro.
    """
    if vitorias < 0 or derrotas < 0:
        raise ValueError("Vitórias e derrotas não podem ser negativas.")

    saldo_vitorias = calcular_saldo(vitorias, derrotas)  # variável com o resultado

    if criterio == "vitorias":
        base = vitorias
    elif criterio == "saldo":
        base = max(saldo_vitorias, 0)
    else:
        raise ValueError("Critério inválido. Use 'vitorias' ou 'saldo'.")

    nivel = classificar_nivel(base)
    return f"O Herói tem de saldo de **{saldo_vitorias}** está no nível de **{nivel}**"


def ler_inteiro(mensagem: str) -> int:
    """Laço while que repete até o usuário digitar um inteiro não negativo."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            return int(entrada)
        print("  ⚠️  Digite apenas números inteiros não negativos.")


def main() -> None:
    print("=" * 50)
    print("   🎮  CALCULADORA DE PARTIDAS RANKEADAS  🎮")
    print("=" * 50)

    historico = []

    while True:
        vitorias = ler_inteiro("\nQuantidade de vitórias: ")
        derrotas = ler_inteiro("Quantidade de derrotas: ")

        mensagem = calcular_rankeada(vitorias, derrotas)
        historico.append((vitorias, derrotas, mensagem))
        print("\n" + mensagem)

        if input("\nCalcular outro jogador? (s/n): ").strip().lower() != "s":
            break

    print("\n--- Resumo da sessão ---")
    for i, (v, d, _) in enumerate(historico, start=1):
        print(f"{i}. Vitórias: {v:>4}  Derrotas: {d:>4}  Saldo: {v - d:>5}")


if __name__ == "__main__":
    main()
