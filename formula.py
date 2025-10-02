class Formula:
    def __init__(self, tipo, rotulo, esquerda=None, direita=None, atomo=None):
        self.tipo = tipo       # A = átomo, N = negação, C = conjunção, D = disjunção, I = implicação, E = equivalência
        self.rotulo = rotulo   # T ou F
        self.esquerda = esquerda
        self.direita = direita
        self.atomo = atomo

    def __repr__(self):
        if self.tipo == 'A':
            return f"{self.rotulo}{self.atomo}"
        if self.tipo == 'N':
            return f"{self.rotulo}¬({self.esquerda})"
        if self.tipo in ['C', 'D', 'I', 'E']:
            simbolos = {'C': '∧', 'D': '∨', 'I': '→', 'E': '↔'}
            return f"{self.rotulo}({self.esquerda} {simbolos[self.tipo]} {self.direita})"
        return f"{self.rotulo}?"

    def is_atom(self):
        return self.tipo == 'A'

    # atalhos pra criar cópias com rótulos diferentes
    def as_T(self):
        return Formula(self.tipo, 'T', self.esquerda, self.direita, self.atomo)

    def as_F(self):
        return Formula(self.tipo, 'F', self.esquerda, self.direita, self.atomo)
