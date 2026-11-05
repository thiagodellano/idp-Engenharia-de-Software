class Media {
  static NOTA_MINIMA = 0;
  static NOTA_MAXIMA = 10;
  static MEDIA_APROVACAO = 6;
  static DIFERENCA_MAX_RECUPERACAO = 3.33;

  constructor(nota1, nota2, nota3, notaRecuperacao = null) {
    this.notas = [nota1, nota2, nota3].map((n) => Media.validarNota(n, "Nota"));
    this.notaRecuperacao = notaRecuperacao === null
      ? null : Media.validarNota(notaRecuperacao, "Nota de recuperação");
  }

  static validarNota(valor, nome) {
    if (typeof valor !== "number" || !Number.isFinite(valor) || valor < 0 || valor > 10)
      throw new RangeError(`${nome} deve ser um número entre 0 e 10.`);
    return valor;
  }

  menorIndice() { return this.notas.indexOf(Math.min(...this.notas)); }
  media() {
    const notas = [...this.notas];
    if (this.notaRecuperacao !== null) notas[this.menorIndice()] = this.notaRecuperacao;
    return notas.reduce((soma, n) => soma + n, 0) / 3;
  }
  situacao() {
    const mediaInicial = this.notas.reduce((s, n) => s + n, 0) / 3;
    if (mediaInicial >= Media.MEDIA_APROVACAO) return "Aprovado";
    if (Math.max(...this.notas) - Math.min(...this.notas) > Media.DIFERENCA_MAX_RECUPERACAO)
      return "Reprovado automaticamente";
    if (this.notaRecuperacao === null) return "Recuperação necessária";
    return this.media() >= Media.MEDIA_APROVACAO ? "Aprovado após recuperação" : "Reprovado após recuperação";
  }
  mencao() {
    const m = this.media();
    if (m < 6) return "MI";
    if (m < 8) return "MM";
    if (m < 9) return "MS";
    return "SS";
  }
  resultado() {
    return { media: this.media(), mencao: this.mencao(), situacao: this.situacao() };
  }
}

function executar() {
  const readline = require("node:readline").createInterface({ input: process.stdin, output: process.stdout });
  const perguntar = (texto) => new Promise((resolve) => readline.question(texto, resolve));
  (async () => {
    try {
      const notas = [];
      for (let i = 1; i <= 3; i++) notas.push(Number(await perguntar(`Nota ${i} (0 a 10): `)));
      const media = new Media(...notas);
      if (media.situacao() === "Recuperação necessária") {
        const recuperacao = Number(await perguntar("Nota da recuperação (substitui a menor nota): "));
        media.notaRecuperacao = Media.validarNota(recuperacao, "Nota de recuperação");
      }
      const r = media.resultado();
      console.log(`Média final: ${r.media.toFixed(2)}\nMenção: ${r.mencao}\nSituação: ${r.situacao}`);
    } catch (erro) { console.error(`Erro: ${erro.message}`); process.exitCode = 1; }
    finally { readline.close(); }
  })();
}

if (require.main === module) executar();
module.exports = { Media };
