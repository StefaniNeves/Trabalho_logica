from formula import Formula
from regras import Regras

def testar_alpha():
    print("==== Testando Regras α (não ramificam) ====")

    # T(A ∧ B) → TA, TB
    p = Formula('A', 'T', atomo='p')
    q = Formula('A', 'T', atomo='q')
    conj = Formula('C', 'T', esquerda=p, direita=q)
    print("Expansão de T(p ∧ q):", Regras.expandir_alpha(conj))

    # F(A ∨ B) → FA, FB
    disj = Formula('D', 'F', esquerda=p, direita=q)
    print("Expansão de F(p ∨ q):", Regras.expandir_alpha(disj))

    # F(A → B) → TA, FB
    impl = Formula('I', 'F', esquerda=p, direita=q)
    print("Expansão de F(p → q):", Regras.expandir_alpha(impl))

    # T(¬A) → FA
    neg = Formula('N', 'T', esquerda=p)
    print("Expansão de T(¬p):", Regras.expandir_alpha(neg))


def testar_beta():
    print("\n==== Testando Regras β (ramificam) ====")

    # F(A ∧ B) → [FA] | [FB]
    p = Formula('A', 'T', atomo='p')
    q = Formula('A', 'T', atomo='q')
    conj = Formula('C', 'F', esquerda=p, direita=q)
    print("Expansão de F(p ∧ q):", Regras.expandir_beta(conj))

    # T(A ∨ B) → [TA] | [TB]
    disj = Formula('D', 'T', esquerda=p, direita=q)
    print("Expansão de T(p ∨ q):", Regras.expandir_beta(disj))

    # T(A → B) → [FA] | [TB]
    impl = Formula('I', 'T', esquerda=p, direita=q)
    print("Expansão de T(p → q):", Regras.expandir_beta(impl))

    # F(¬A) → [TA]
    neg = Formula('N', 'F', esquerda=p)
    print("Expansão de F(¬p):", Regras.expandir_beta(neg))


if __name__ == "__main__":
    testar_alpha()
    testar_beta()