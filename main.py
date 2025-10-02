from formula import Formula
from tableau import Tableau

def teste_transitividade():
    print("\nExemplo 1: Transitividade (VÁLIDO)")
    # (p → q) → ((q → r) → (p → r))
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    r = Formula('A', '', atomo='r')

    conclusoes = [Formula('I', '', 
                    esquerda=Formula('I', '', esquerda=p, direita=q),
                    direita=Formula('I', '', 
                        esquerda=Formula('I', '', esquerda=q, direita=r),
                        direita=Formula('I', '', esquerda=p, direita=r)
                    )
                )]

    t = Tableau([], conclusoes)
    t.prova()


def teste_negacao_implicacao():
    print("\nExemplo 2: Negação de implicação (INVÁLIDO)")
    # ⊢ ¬((p ∨ q) → (r ∧ s))
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    r = Formula('A', '', atomo='r')
    s = Formula('A', '', atomo='s')

    disj = Formula('D', '', esquerda=p, direita=q)
    conj = Formula('C', '', esquerda=r, direita=s)
    imp = Formula('I', '', esquerda=disj, direita=conj)

    conclusoes = [Formula('N', '', esquerda=imp)]

    t = Tableau([], conclusoes)
    t.prova()


def teste_equivalencia():
    print("\nTeste 3: Equivalência (VÁLIDO)")
    # (p ↔ q) ∧ (q ↔ r) ⊢ (p ↔ r)
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    r = Formula('A', '', atomo='r')

    eq1 = Formula('E', '', esquerda=p, direita=q)
    eq2 = Formula('E', '', esquerda=q, direita=r)
    eq3 = Formula('E', '', esquerda=p, direita=r)

    premissas = [Formula('C', '', esquerda=eq1, direita=eq2)]
    conclusoes = [eq3]

    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_conjuncao():
    print("\nExemplo 4: Conjunção (VÁLIDO)")
    # p ∧ q ⊢ p
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    premissas = [Formula('C', '', esquerda=p, direita=q)]
    conclusoes = [p]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_conjuncao_invalido():
    print("\nExemplo 5: Conjunção (INVÁLIDO)")
    # p ⊢ p ∧ q
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    premissas = [p]
    conclusoes = [Formula('C', '', esquerda=p, direita=q)]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_disjuncao():
    print("\nExemplo 6: Disjunção (VÁLIDO)")
    # p ⊢ p ∨ q
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    premissas = [p]
    conclusoes = [Formula('D', '', esquerda=p, direita=q)]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_disjuncao_invalido():
    print("\nExemplo 7: Disjunção (INVÁLIDO)")
    # p ∨ q ⊢ p
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    premissas = [Formula('D', '', esquerda=p, direita=q)]
    conclusoes = [p]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_dupla_negacao():
    print("\nExemplo 8: Dupla Negação (VÁLIDO)")
    # p ⊢ ¬¬p
    p = Formula('A', '', atomo='p')
    nn = Formula('N', '', esquerda=Formula('N', '', esquerda=p))
    premissas = [p]
    conclusoes = [nn]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_dupla_negacao_invalido():
    print("\nExemplo 9: Dupla Negação (INVÁLIDO)")
    # ¬¬p ⊢ q
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    nn = Formula('N', '', esquerda=Formula('N', '', esquerda=p))
    premissas = [nn]
    conclusoes = [q]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_demorgan():
    print("\nExemplo 10: De Morgan (VÁLIDO)")
    # ¬(p ∧ q) ⊢ ¬p ∨ ¬q
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    conj = Formula('C', '', esquerda=p, direita=q)
    premissas = [Formula('N', '', esquerda=conj)]
    conclusoes = [Formula('D', '', esquerda=Formula('N', '', esquerda=p),
                                     direita=Formula('N', '', esquerda=q))]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_demorgan_invalido():
    print("\nExemplo 11: De Morgan (VÁLIDO)")
    # ¬(p ∨ q) ⊢ ¬p ∧ ¬q
    p = Formula('A', '', atomo='p')
    q = Formula('A', '', atomo='q')
    disj = Formula('D', '', esquerda=p, direita=q)
    premissas = [Formula('N', '', esquerda=disj)]
    conclusoes = [Formula('C', '', esquerda=Formula('N', '', esquerda=p),
                                     direita=Formula('N', '', esquerda=q))]
    t = Tableau(premissas, conclusoes)
    t.prova()


def teste_terceiro_excluido():
    print("\nExemplo 12: Terceiro Excluído (VÁLIDO)")
    # ⊢ p ∨ ¬p
    p = Formula('A', '', atomo='p')
    conclusoes = [Formula('D', '', esquerda=p, direita=Formula('N', '', esquerda=p))]
    t = Tableau([], conclusoes)
    t.prova()


if __name__ == "__main__":
    teste_transitividade()
    teste_negacao_implicacao()
    teste_equivalencia()
    teste_conjuncao()
    teste_conjuncao_invalido()
    teste_disjuncao()
    teste_disjuncao_invalido()
    teste_dupla_negacao()
    teste_dupla_negacao_invalido()
    teste_demorgan()
    teste_demorgan_invalido()
    teste_terceiro_excluido()
