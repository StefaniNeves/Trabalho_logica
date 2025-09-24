from formula import Formula

class Ramo:
    def __init__(self, formulas=None):
        self.formulas = formulas if formulas else []
        self.expanded = set()  # fórmulas já expandidas neste ramo
    
    def contem_contradicao(self):
        valores = {}
        for formula in self.formulas:
            if formula.is_atom():
                atomo = formula.atomo
                valor = formula.rotulo
                if atomo in valores:
                    if valores[atomo] != valor:
                        return True  # achou Tp e Fp no mesmo ramo
                else:
                    valores[atomo] = valor
        return False

    def esta_saturado(self):
        # saturado = só contém fórmulas atômicas
        return all(f.is_atom() for f in self.formulas)

    def __repr__(self):
        return "[" + ", ".join(str(f) for f in self.formulas) + "]"
