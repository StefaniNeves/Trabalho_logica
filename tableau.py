from regras import Regras
from ramo import Ramo
import copy

class Tableau:
    def __init__(self, premissas=None, conclusoes=None):
        self.stack = []           # pilha de ramos 
        self.branch = Ramo([])    # ramo atual

        premissas = premissas or []
        conclusoes = conclusoes or []

        # premissas como verdadeiras, conclusões como falsas
        for p in premissas:
            self.branch.formulas.append(p.as_T())
        for c in conclusoes:
            self.branch.formulas.append(c.as_F())

    def aplicar_regras(self, f):
        #Tenta expandir α ou β

        # α = adiciona sempre no mesmo ramo
        novas = Regras.expandir_alpha(f)
        if novas:
            for nf in novas:
                self.branch.formulas.append(nf)
            return True

        # β = gera ramificações
        novas = Regras.expandir_beta(f)
        if novas:
            # primeira ramificação no ramo atual
            self.branch.formulas.extend(novas[0])

            # as demais ramificações vão para a pilha
            for ramo_extra in novas[1:]:
                copia = copy.deepcopy(self.branch)
                copia.formulas = self.branch.formulas[:-len(novas[0])] + ramo_extra
                copia.expanded = set(self.branch.expanded)  # manter histórico
                self.stack.append(copia)
            return True

        return False

    def expandir(self):
        """Expande até fechar ou achar contraexemplo"""
        while True:
            # 1. Contradição → ramo fechado
            if self.branch.contem_contradicao():
                print("Fechou:", self.branch)
                if not self.stack:
                    return True  # todos fecharam
                self.branch = self.stack.pop()
                continue

            # 2. Se está saturado (só átomos)
            if self.branch.esta_saturado():
                print("Aberto:", self.branch)
                if not self.stack:
                    return False  # sobrou aberto
                self.branch = self.stack.pop()
                continue

            # 3. Pega próxima fórmula não expandida
            escolhida = None
            for f in self.branch.formulas:
                if not f.is_atom() and str(f) not in self.branch.expanded:
                    escolhida = f
                    break

            if escolhida:
                self.branch.expanded.add(str(escolhida))
                self.aplicar_regras(escolhida)
            else:
                # nada a expandir → saturado
                print("Aberto:", self.branch)
                if not self.stack:
                    return False
                self.branch = self.stack.pop()

    def obter_contraexemplo(self):
        """Extrai um modelo dos átomos restantes do ramo aberto"""
        return {f.atomo: (f.rotulo == 'T')
                for f in self.branch.formulas if f.is_atom()}

    def prova(self):
        print("Ramo inicial:", self.branch)
        fechado = self.expandir()
        if fechado:
            print("Sequente válido.")
        else:
            print("Sequente inválido. Contraexemplo:", self.obter_contraexemplo())
