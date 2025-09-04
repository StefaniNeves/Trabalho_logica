class Formula:
    def __init__(self, tipo, rotulo, esquerda=None, direita=None, atomo=None):
        
        self.tipo = tipo
        self.rotulo = rotulo
        self.esquerda = esquerda
        self.direita = direita
        self.atomo = atomo

    def __repr__(self):
        if self.tipo == 'A':
            return f"{self.rotulo}{self.atomo}"
        if self.tipo == 'N':
            return f"{self.rotulo}¬({self.esquerda})"
        if self.tipo in ['C', 'D', 'I']:
            simbolos = {'C': '∧', 'D': '∨', 'I': '→'}
            return f"{self.rotulo}({self.esquerda} {simbolos[self.tipo]} {self.direita})"
        return "Fórmula inválida"
        

    def is_atom(self):
         return self.tipo ==  'A'
     
    