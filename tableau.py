from formula import Formula
from regras import Regras
from ramo import Ramo
import copy


class Tableau:
    def __init__(self, premissas=None, conclusoes=None):
        self.premissas = premissas if premissas else []
        self.conclusoes = conclusoes if conclusoes else []

        # Vetores principais
        self.branch = Ramo([])   # ramo atual
        self.stack = []          # pilha de ramos (backtracking)

        # inicializa o ramo raiz com premissas (T) e conclusões (F)
        for p in self.premissas:
            f = Formula(p.tipo, 'T', p.esquerda, p.direita, p.atomo)
            self.branch.formulas.append(f)
        for c in self.conclusoes:
            f = Formula(c.tipo, 'F', c.esquerda, c.direita, c.atomo)
            self.branch.formulas.append(f)

    def aplicar_regras(self, formula):
        """Aplica α ou β, se possível, mostrando passo a passo"""
        novas = Regras.expandir_alpha(formula)
        if novas:
            print(f"\nAplicando regra α em {formula}")
            for f in novas:
                print("   Adiciona:", f)
                self.branch.formulas.append(f)
            print("Ramo atual:", self.branch)
            return True

        novas = Regras.expandir_beta(formula)
        if novas:
            print(f"\nAplicando regra β em {formula}")
            # β gera ramificações → guardar na pilha
            for ramo in novas[1:]:
                copia = copy.deepcopy(self.branch)
                copia.formulas += ramo
                self.stack.append(copia)
                print("   Novo ramo (empilhado):", copia)

            # segue com a primeira ramificação no branch atual
            for f in novas[0]:
                print("   Adiciona:", f)
                self.branch.formulas.append(f)
            print("Ramo atual:", self.branch)
            return True

        return False

    def expandir(self):
        """Loop principal do tableau"""
        while True:
            # 1. Verifica contradição imediata
            if self.branch.contem_contradicao():
                print("\n*** Ramo fechado por contradição:", self.branch)
                if not self.stack:
                    return True  # todos os ramos fecharam
                self.branch = self.stack.pop()
                print("\n>>> Retomando ramo da pilha:", self.branch)
                continue

            # 2. Se o ramo só tem átomos (saturado)
            if self.branch.esta_saturado():
                if not self.stack:
                    print("\n*** Ramo aberto e saturado:", self.branch)
                    return False  # sobrou ramo aberto
                else:
                    self.branch = self.stack.pop()
                    print("\n>>> Retomando ramo da pilha:", self.branch)
                    continue

            # 3. Procura uma fórmula não atômica não expandida
            escolhida = None
            for f in self.branch.formulas:
                if not f.is_atom() and str(f) not in self.branch.expanded:
                    escolhida = f
                    break

            if escolhida:
                self.branch.expanded.add(str(escolhida))
                self.aplicar_regras(escolhida)
            else:
                # Nenhuma fórmula restante para expandir → saturado
                if not self.stack:
                    print("\n*** Ramo aberto e saturado:", self.branch)
                    return False
                else:
                    self.branch = self.stack.pop()
                    print("\n>>> Retomando ramo da pilha:", self.branch)

    def prova(self):
        print("Ramo inicial:", self.branch)
        resultado = self.expandir()
        if resultado:
            print("\nSequente válido (tableau fechado).")
        else:
            print("\nSequente inválido (ramo aberto encontrado).")
        print("Ramo final:", self.branch)
