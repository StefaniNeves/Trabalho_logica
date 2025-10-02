from formula import Formula

class Regras:
    @staticmethod
    def expandir_alpha(f):
        # regras alpha
        if (f.tipo, f.rotulo) == ('C', 'T'):
            return [f.esquerda.as_T(), f.direita.as_T()]
        if (f.tipo, f.rotulo) == ('D', 'F'):
            return [f.esquerda.as_F(), f.direita.as_F()]
        if (f.tipo, f.rotulo) == ('I', 'F'):
            return [f.esquerda.as_T(), f.direita.as_F()]
        if (f.tipo, f.rotulo) == ('N', 'T'):
            return [f.esquerda.as_F()]
        if (f.tipo, f.rotulo) == ('E', 'T'):  # p ↔ q como (p→q) ∧ (q→p)
            p, q = f.esquerda, f.direita
            return [Formula('I','T',p,q), Formula('I','T',q,p)]
        return []

    @staticmethod
    def expandir_beta(f):
        # regras beta
        if (f.tipo, f.rotulo) == ('C', 'F'):
            return [[f.esquerda.as_F()], [f.direita.as_F()]]
        if (f.tipo, f.rotulo) == ('D', 'T'):
            return [[f.esquerda.as_T()], [f.direita.as_T()]]
        if (f.tipo, f.rotulo) == ('I', 'T'):
            return [[f.esquerda.as_F()], [f.direita.as_T()]]
        if (f.tipo, f.rotulo) == ('N', 'F'):
            return [[f.esquerda.as_T()]]
        if (f.tipo, f.rotulo) == ('E', 'F'):  # p ↔ q falso → ou (p ∧ ¬q) ou (¬p ∧ q)
            p, q = f.esquerda, f.direita
            return [
                [p.as_T(), q.as_F()],
                [p.as_F(), q.as_T()]
            ]
        return []
