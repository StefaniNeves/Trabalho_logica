class Ramo:
    def __init__(self, formulas=None):
        self.formulas = formulas or []
        self.expanded = set()  # guardo strings das fórmulas já expandidas

    def contem_contradicao(self):
        vistos = {}
        for f in self.formulas:
            if f.is_atom():
                if f.atomo in vistos and vistos[f.atomo] != f.rotulo:
                    return True
                vistos[f.atomo] = f.rotulo
        return False

    def esta_saturado(self):
        return all(f.is_atom() for f in self.formulas)

    def __repr__(self):
        return "[" + ", ".join(str(f) for f in self.formulas) + "]"
