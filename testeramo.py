from formula import Formula
from ramo import Ramo

# --- Teste de contradição ---
ramo1 = Ramo([Formula('A','T','p'), Formula('A','F','p')])
print("Ramo1:", ramo1)
print("Contradição?", ramo1.contem_contradicao())  # True
print("Saturado?", ramo1.esta_saturado())         # True (todas atômicas)

# --- Teste de saturação com fórmula composta ---
p = Formula('A','T','p')
q = Formula('A','T','q')
conj = Formula('C','T', esquerda=p, direita=q)
ramo2 = Ramo([conj])
print("\nRamo2:", ramo2)
print("Contradição?", ramo2.contem_contradicao())  # False
print("Saturado?", ramo2.esta_saturado())