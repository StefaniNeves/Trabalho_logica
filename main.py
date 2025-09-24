from formula import Formula
from tableau import Tableau

def teste_valido():
    print("\n=== Teste 1: Sequente VÁLIDO ===")
    # Silogismo hipotético: p → q, q → r ⊢ p → r
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    r = Formula('A', '', atomo='r')

    premissas = [Formula('I', '', esquerda=p, direita=q),
                 Formula('I', '', esquerda=q, direita=r)]
    conclusoes = [Formula('I', '', esquerda=p, direita=r)]

    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_invalido():
    print("\n=== Teste 2: Sequente INVÁLIDO ===")
    # Exemplo: p ⊢ q (isso não é válido)
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')

    premissas = [p]
    conclusoes = [q]

    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_tautologia():
    print("\n=== Teste 3: Tautologia ===")
    # Lei do terceiro excluído: ⊢ p ∨ ¬p
    p = Formula('A', '', atomo='p')
    nao_p = Formula('N', '', esquerda=p)

    conclusoes = [Formula('D', '', esquerda=p, direita=nao_p)]

    t = Tableau([], conclusoes)
    t.prova()


if __name__ == "__main__":
    teste_valido()
    teste_invalido()
    teste_tautologia()
