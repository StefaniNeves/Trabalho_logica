from formula import Formula

if __name__ == "__main__":
    p = Formula('A', 'T', atomo='p')
    print("Fórmula p:", p)               
    print("É atômica?", p.is_atom())     

    q = Formula('A', 'F', atomo='q')
    print("\nFórmula q:", q)             
    print("É atômica?", q.is_atom())     

    not_p = Formula('N', 'T', esquerda=p)
    print("\nFórmula ¬p:", not_p)        
    print("É atômica?", not_p.is_atom()) 

    conj = Formula('C', 'T', esquerda=p, direita=q)
    print("\nFórmula (p ∧ q):", conj)    
    print("É atômica?", conj.is_atom())  

    implic = Formula('I', 'F', esquerda=conj, direita=not_p)
    print("\nFórmula (p ∧ q) → ¬p:", implic)
    print("É atômica?", implic.is_atom())