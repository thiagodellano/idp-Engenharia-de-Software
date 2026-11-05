import unittest
from media import Media


class TestMedia(unittest.TestCase):
    def test_aprovacao_no_limite(self): self.assertEqual(Media(6, 6, 6).situacao(), "Aprovado")
    def test_limites_mencoes(self):
        self.assertEqual(Media(5.99, 5.99, 5.99).mencao(), "MI")
        self.assertEqual(Media(6, 6, 6).mencao(), "MM")
        self.assertEqual(Media(8, 8, 8).mencao(), "MS")
        self.assertEqual(Media(9, 9, 9).mencao(), "SS")
    def test_recuperacao_substitui_menor(self):
        m = Media(4, 6, 6, 10)
        self.assertAlmostEqual(m.media(), 22 / 3)
        self.assertEqual(m.situacao(), "Aprovado após recuperação")
    def test_recuperacao_insuficiente(self): self.assertEqual(Media(4, 5, 6, 5).situacao(), "Reprovado após recuperação")
    def test_reprovacao_automatica(self): self.assertEqual(Media(0, 4, 4).situacao(), "Reprovado automaticamente")
    def test_limite_diferenca(self): self.assertEqual(Media(0, 3.33, 3.33).situacao(), "Recuperação necessária")
    def test_notas_invalidas(self):
        with self.assertRaises(ValueError): Media(-0.01, 5, 5)
        with self.assertRaises(ValueError): Media(4, 5, 6, 10.01)


if __name__ == "__main__": unittest.main()
