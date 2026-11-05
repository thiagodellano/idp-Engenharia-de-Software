class Media:
    MEDIA_APROVACAO = 6.0
    DIFERENCA_MAX_RECUPERACAO = 3.33

    def __init__(self, nota1, nota2, nota3, nota_recuperacao=None):
        self.notas = [self._validar(n, "Nota") for n in (nota1, nota2, nota3)]
        self.nota_recuperacao = (None if nota_recuperacao is None else
                                 self._validar(nota_recuperacao, "Nota de recuperação"))

    @staticmethod
    def _validar(valor, nome):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not 0 <= valor <= 10:
            raise ValueError(f"{nome} deve ser um número entre 0 e 10.")
        return float(valor)

    def _notas_finais(self):
        notas = self.notas.copy()
        if self.nota_recuperacao is not None:
            notas[notas.index(min(notas))] = self.nota_recuperacao
        return notas

    def media(self):
        return sum(self._notas_finais()) / 3

    def situacao(self):
        inicial = sum(self.notas) / 3
        if inicial >= self.MEDIA_APROVACAO:
            return "Aprovado"
        if max(self.notas) - min(self.notas) > self.DIFERENCA_MAX_RECUPERACAO + 1e-9:
            return "Reprovado automaticamente"
        if self.nota_recuperacao is None:
            return "Recuperação necessária"
        return ("Aprovado após recuperação" if self.media() >= self.MEDIA_APROVACAO
                else "Reprovado após recuperação")

    def mencao(self):
        m = self.media()
        if m < 6: return "MI"
        if m < 8: return "MM"
        if m < 9: return "MS"
        return "SS"

    def resultado(self):
        return {"media": self.media(), "mencao": self.mencao(), "situacao": self.situacao()}


def executar():
    try:
        notas = [float(input(f"Nota {i} (0 a 10): ")) for i in range(1, 4)]
        media = Media(*notas)
        if media.situacao() == "Recuperação necessária":
            media.nota_recuperacao = Media._validar(
                float(input("Nota da recuperação (substitui a menor nota): ")), "Nota de recuperação")
        resultado = media.resultado()
        print(f"Média final: {resultado['media']:.2f}\nMenção: {resultado['mencao']}\nSituação: {resultado['situacao']}")
    except (ValueError, EOFError) as erro:
        print(f"Erro: {erro}")
        raise SystemExit(1)


if __name__ == "__main__":
    executar()
