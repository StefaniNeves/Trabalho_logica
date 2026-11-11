# Tableaux Analítico – Implementação em Python

## 📘 Descrição do Projeto

Este projeto consiste na implementação de um **Tableaux Analítico para lógica proposicional**, baseado na estrutura apresentada no livro:

> SILVA, F. S. C.; FINGER, M. e MELO, A. C. V. *Lógica para Computação*. 1ª ed., 2006.  

O objetivo é automatizar o processo de verificação da **validade** ou **satisfatibilidade** de fórmulas proposicionais, utilizando a técnica de **Tableaux**.

---

## ⚙️ Decisões de Implementação

### 1) Linguagem Utilizada
Implementar em **Python**, pela sua simplicidade e expressividade em manipulação de árvores, listas e estruturas de dados dinâmicas.  

---

### 2) Representação das Fórmulas
- [ ] Definir como as fórmulas serão representadas internamente (árvore sintática ou estruturas aninhadas).  
- [ ] Implementar funções para parsing de strings em fórmulas.  

---

### 3) Estruturas de Dados para os Ramos
- [ ] Implementar a estrutura de ramos do tableau (listas/vetores de fórmulas).  
- [ ] Garantir armazenamento de fórmulas abertas, fórmulas beta e caminhos.  

---

### 4) Regras do Tableau
- [ ] Implementar as regras **α (determinísticas)** e **β (não determinísticas)**.  
- [ ] Criar funções auxiliares para expansão.  

---

### 5) Motor do Algoritmo (Execução do Tableau)
- [ ] Integrar regras, ramos e fórmulas no motor de execução.  
- [ ] Definir a estratégia de expansão (priorizar α, depois β).  

---

### 6) Funções Auxiliares
- [ ] Implementar detecção de contradições dentro dos ramos.  
- [ ] Criar controle da lista de fórmulas não processadas.  
- [ ] Organizar o código em módulos (`formula.py`, `rules.py`, `tableaux.py`).  

---

### 7) Testes e Validação
- [ ] Criar casos de teste simples e compostos.  
- [ ] Validar fechamento de ramos e identificação de fórmulas satisfatíveis/insatisfatíveis.  

---

### 8) Documentação
- [ ] Elaborar este README.  
- [ ] Produzir relatório final e exemplos de execução.

      
## 👩‍💻 Minha Contribuição- Stéfani Rodrigues Neves 

O projeto foi desenvolvido em equipe, com divisão de responsabilidades entre os integrantes. Minha participação foi voltada à implementação de dois módulos principais:

- **regras.py:** desenvolvimento da classe `Regras`, responsável pela implementação das regras de expansão alfa (α) e beta (β) utilizadas no método Tableaux Analítico.
- **formula.py:** desenvolvimento da classe `Formula`, responsável pela representação das fórmulas proposicionais, identificação dos operadores lógicos e manipulação dos rótulos de verdadeiro (T) e falso (F).

Além dessas implementações, participei do desenvolvimento colaborativo do projeto, contribuindo para a construção da solução em equipe.

