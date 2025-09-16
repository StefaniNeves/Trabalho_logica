from formula import Formula

class Regras:
     @staticmethod
     def expandir_alpha(formula):
    
            if formula.tipo == 'C' and formula.rotulo == 'T':
                
                    return [Formula(formula.esquerda.tipo, 'T', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo),
                        Formula(formula.direita.tipo, 'T', 
                                formula.direita.esquerda, 
                                formula.direita.direita, 
                                formula.direita.atomo)]

            if formula.tipo == 'D' and formula.rotulo == 'F':
                
                    return [Formula(formula.esquerda.tipo, 'F', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo),
                        Formula(formula.direita.tipo, 'F', 
                                formula.direita.esquerda, 
                                formula.direita.direita, 
                                formula.direita.atomo)]

            if formula.tipo == 'I' and formula.rotulo == 'F':
                
                return [Formula(formula.esquerda.tipo, 'T', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo),
                        Formula(formula.direita.tipo, 'F', 
                                formula.direita.esquerda, 
                                formula.direita.direita, 
                                formula.direita.atomo)]

            if formula.tipo == 'N' and formula.rotulo == 'T':
                
                return [Formula(formula.esquerda.tipo, 'F', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo)]

            return []

     @staticmethod
     def expandir_beta(formula):

            if formula.tipo == 'C' and formula.rotulo == 'F':
                
                return [[Formula(formula.esquerda.tipo, 'F', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo)],
                        [Formula(formula.direita.tipo, 'F', 
                                formula.direita.esquerda, 
                                formula.direita.direita, 
                                formula.direita.atomo)]]

            if formula.tipo == 'D' and formula.rotulo == 'T':
                
                return [[Formula(formula.esquerda.tipo, 'T', 
                                formula.esquerda.esquerda, 
                                formula.esquerda.direita, 
                                formula.esquerda.atomo)],
                        [Formula(formula.direita.tipo, 'T', 
                            formula.direita.esquerda, 
                            formula.direita.direita, 
                            formula.direita.atomo)]]

            if formula.tipo == 'I' and formula.rotulo == 'T':
            
                return [[Formula(formula.esquerda.tipo, 'F', 
                            formula.esquerda.esquerda, 
                            formula.esquerda.direita, 
                            formula.esquerda.atomo)],
                    [Formula(formula.direita.tipo, 'T', 
                            formula.direita.esquerda, 
                            formula.direita.direita, 
                            formula.direita.atomo)]]

            if formula.tipo == 'N' and formula.rotulo == 'F':
            
                return [[Formula(formula.esquerda.tipo, 'T', 
                            formula.esquerda.esquerda, 
                            formula.esquerda.direita, 
                            formula.esquerda.atomo)]]

            return []