#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

class Media {
    std::array<double, 3> notas;
    bool temRecuperacao;
    double recuperacao;
    static double validar(double n, const std::string& nome) {
        if (!std::isfinite(n) || n < 0 || n > 10) throw std::out_of_range(nome + " deve estar entre 0 e 10.");
        return n;
    }
    std::size_t menorIndice() const { return std::distance(notas.begin(), std::min_element(notas.begin(), notas.end())); }
public:
    Media(double n1, double n2, double n3, double rec = -1)
        : notas{validar(n1,"Nota"), validar(n2,"Nota"), validar(n3,"Nota")}, temRecuperacao(rec >= 0), recuperacao(0) {
        if (temRecuperacao) recuperacao = validar(rec, "Nota de recuperação");
    }
    double media() const {
        auto n = notas;
        if (temRecuperacao) n[menorIndice()] = recuperacao;
        return (n[0] + n[1] + n[2]) / 3.0;
    }
    std::string situacao() const {
        const double inicial = (notas[0] + notas[1] + notas[2]) / 3.0;
        if (inicial >= 6) return "Aprovado";
        auto [lo, hi] = std::minmax_element(notas.begin(), notas.end());
        if (*hi - *lo > 3.33 + 1e-9) return "Reprovado automaticamente";
        if (!temRecuperacao) return "Recuperação necessária";
        return media() >= 6 ? "Aprovado após recuperação" : "Reprovado após recuperação";
    }
    std::string mencao() const {
        double m = media();
        if (m < 6) return "MI"; if (m < 8) return "MM"; if (m < 9) return "MS"; return "SS";
    }
};

int main() {
    try {
        double a,b,c,rec;
        std::cout << "Informe três notas (0 a 10): ";
        if (!(std::cin >> a >> b >> c)) throw std::runtime_error("Entrada inválida.");
        Media m(a,b,c);
        if (m.situacao() == "Recuperação necessária") {
            std::cout << "Nota da recuperação (substitui a menor nota): ";
            if (!(std::cin >> rec)) throw std::runtime_error("Entrada inválida.");
            m = Media(a,b,c,rec);
        }
        std::cout << std::fixed << std::setprecision(2) << "Média final: " << m.media()
                  << "\nMenção: " << m.mencao() << "\nSituação: " << m.situacao() << '\n';
    } catch (const std::exception& e) { std::cerr << "Erro: " << e.what() << '\n'; return 1; }
}
