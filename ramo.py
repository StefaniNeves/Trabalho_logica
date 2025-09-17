from formula import Formula

class Ramo:
    def __init__(self, formulas):
        self.formulas = formulas  if formulas else []
    
    def contem_contradicao(self):
        valores = {}
        for formulas in self.formulas:
            if formula.is_atom():
                if formula.atomo in valores:
                    if valores[formula.atomo] != formula.valor:
                        return True
                else:
                    valores[formula.atomo] = formula.valor
        return False
    
    def esta_staurado(self):
        return all(f.id_atom() for f in self.formulas)
    def __repr__(self):
        return "[" + ",".join(str(f) for f in self.formulas) + "]"