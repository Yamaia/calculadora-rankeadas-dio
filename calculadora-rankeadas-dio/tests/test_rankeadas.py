import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from rankeadas import (  # noqa: E402
    calcular_rankeada,
    calcular_saldo,
    classificar_nivel,
    classificar_nivel_por_laco,
)

CASOS = [
    (0, "Ferro"), (9, "Ferro"), (10, "Ferro"),
    (11, "Bronze"), (20, "Bronze"),
    (21, "Prata"), (50, "Prata"),
    (51, "Ouro"), (80, "Ouro"),
    (81, "Diamante"), (90, "Diamante"),
    (91, "Lendário"), (100, "Lendário"),
    (101, "Imortal"), (500, "Imortal"),
]


class TestRankeadas(unittest.TestCase):
    def test_saldo(self):
        self.assertEqual(calcular_saldo(30, 10), 20)
        self.assertEqual(calcular_saldo(5, 8), -3)

    def test_if_elif(self):
        for vitorias, esperado in CASOS:
            with self.subTest(vitorias=vitorias):
                self.assertEqual(classificar_nivel(vitorias), esperado)

    def test_versao_com_laco(self):
        for vitorias, esperado in CASOS:
            with self.subTest(vitorias=vitorias):
                self.assertEqual(classificar_nivel_por_laco(vitorias), esperado)

    def test_mensagem_final(self):
        self.assertEqual(
            calcular_rankeada(30, 10),
            "O Herói tem de saldo de **20** está no nível de **Prata**",
        )

    def test_saldo_negativo(self):
        self.assertEqual(
            calcular_rankeada(5, 8),
            "O Herói tem de saldo de **-3** está no nível de **Ferro**",
        )

    def test_criterio_saldo(self):
        # 120 vitórias e 90 derrotas: saldo 30 -> Prata (por saldo), Imortal (por vitórias)
        self.assertIn("**Prata**", calcular_rankeada(120, 90, criterio="saldo"))
        self.assertIn("**Imortal**", calcular_rankeada(120, 90))

    def test_entradas_invalidas(self):
        with self.assertRaises(ValueError):
            calcular_rankeada(-1, 0)
        with self.assertRaises(ValueError):
            calcular_rankeada(1, -1)
        with self.assertRaises(ValueError):
            calcular_rankeada(1, 1, criterio="xyz")


if __name__ == "__main__":
    unittest.main()
