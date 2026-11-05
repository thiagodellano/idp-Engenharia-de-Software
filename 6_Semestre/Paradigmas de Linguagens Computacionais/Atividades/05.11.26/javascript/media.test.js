const assert = require("node:assert/strict");
const { Media } = require("./media");

const casos = [
  ["média 6 aprova e menção MM", () => { const m = new Media(6, 6, 6); assert.equal(m.media(), 6); assert.equal(m.situacao(), "Aprovado"); assert.equal(m.mencao(), "MM"); }],
  ["limite inferior MI", () => assert.equal(new Media(5.99, 5.99, 5.99).mencao(), "MI")],
  ["limites de menção", () => { assert.equal(new Media(8,8,8).mencao(), "MS"); assert.equal(new Media(9,9,9).mencao(), "SS"); }],
  ["recuperação substitui a menor nota", () => { const m = new Media(4, 6, 6, 10); assert.equal(m.media(), 22/3); assert.equal(m.situacao(), "Aprovado após recuperação"); }],
  ["recuperação ainda pode reprovar", () => assert.equal(new Media(4, 5, 6, 5).situacao(), "Reprovado após recuperação")],
  ["diferença acima de 3,33 reprova automaticamente", () => assert.equal(new Media(0, 4, 4).situacao(), "Reprovado automaticamente")],
  ["diferença igual a 3,33 permite recuperação", () => assert.equal(new Media(0, 3.33, 3.33).situacao(), "Recuperação necessária")],
  ["notas fora do intervalo são rejeitadas", () => assert.throws(() => new Media(-0.01, 5, 5), RangeError)],
  ["recuperação fora do intervalo é rejeitada", () => assert.throws(() => new Media(4, 5, 6, 10.01), RangeError)],
  ["média inicial aprovada não precisa de recuperação", () => assert.equal(new Media(6, 6, 6).situacao(), "Aprovado")],
];

for (const [nome, teste] of casos) { teste(); console.log(`✓ ${nome}`); }
console.log(`${casos.length} testes passaram.`);
