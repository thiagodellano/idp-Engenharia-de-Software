#define main programa_main
#include "main.cpp"
#undef main
#include <cassert>
#include <iostream>

int main() {
    assert(Media(6,6,6).situacao() == "Aprovado");
    assert(Media(5.99,5.99,5.99).mencao() == "MI");
    assert(Media(8,8,8).mencao() == "MS"); assert(Media(9,9,9).mencao() == "SS");
    assert(std::abs(Media(4,6,6,10).media()-22.0/3.0)<1e-9);
    assert(Media(4,6,6,10).situacao() == "Aprovado após recuperação");
    assert(Media(4,5,6,5).situacao() == "Reprovado após recuperação");
    assert(Media(0,4,4).situacao() == "Reprovado automaticamente");
    assert(Media(0,3.33,3.33).situacao() == "Recuperação necessária");
    bool invalida=false; try { Media(-1,5,5); } catch (const std::out_of_range&) { invalida=true; } assert(invalida);
    invalida=false; try { Media(4,5,6,11); } catch (const std::out_of_range&) { invalida=true; } assert(invalida);
    std::cout << "10 testes passaram.\n";
}
