import random 
import time

start_time = time.time()
resultado = []
listaVariaveis = []
resultadoPossivel = []

class Node:
    def __init__(self, expression):
        self.expression = expression
        self.path = []
        self.left = None
        self.right = None
        self.parent = None
        self.direction = None
    def __repr__(self):
        return f"Node(expression={self.expression}, left={self.left}, right={self.right}))"

def main():
    clauses, numVariaveis, numClausues = cnfFormula()
    
    print(clauses, numVariaveis, numClausues)
    formula = prepararFormula(clauses)
    raiz = Node(formula)
    TransformacaoBooleana(raiz)
    if len(resultadoPossivel) > 0:
        print(resultadoPossivel)
    else:
        print("Esta fórmula não é satisfatível")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")


def cnfFormula() -> tuple:
    numVariables, numClauses = 0, 0

    with open('cnf.txt', 'r') as formulae:
        descStr = formulae.readline().split(sep=' ')
        numVariables, numClauses = int(descStr[-2]), int(descStr[-1])

        clauses = list()

        lines = formulae.readlines()
        for line in lines:
            clause = set()

            for var in  line.split(sep=' '):
                if '0' in var:
                    break
                clause.add(int(var))

            clauses.append(clause)
    
    return (clauses, numVariables, numClauses)

#def dpll(clauses: list[set]) -> bool:
    pass

#def simplifica(clauses: list[set]) -> set:
    pass

def prepararFormula(clauses):
    formula = []
    for clausulas in clauses:
        subform = []
        for literal in clausulas:
            if literal > 0:
                subform.append(f'x{literal}')
            elif literal < 0:
                subform.append(f'¬x{abs(literal)}')
        formula.append(subform)
    return formula    

def TransformacaoBooleana(node):
    global resultadoPossivel 
    
    if node is None:
        return 
    if len(node.expression) == 0:
        resultadoPossivel = node.path
    if node.expression is None:
        return 
    
    form = node.expression

    contr = checarContradicao(form)
    

    if contr:
        print("Contradição aqui")
        return 

    literais = []
    for formulas in form:
        for literal in formulas:
            if literal.startswith("¬") and literal[1:] not in literais:
                literais.append(literal[1:])
            elif not(literal.startswith("¬")) and literal not in literais:
                literais.append(literal)

    if len(literais) == 0:
        return 
    print(literais)


    randomLiteral = random.choice(literais)

    print("O escolhido foi: ", randomLiteral)

    if node.direction == "left":
        node.path.append(randomLiteral)
    if node.direction == "right":
        node.path.append(f'¬{randomLiteral}')
    if node.direction is None:
        node.path.append(randomLiteral)

    auxForm1 = [formulas[:] for formulas in form]
    print("auxForm1 antes da mudança", auxForm1)
    new_auxForm1 = []
    for formulas in auxForm1:
        if randomLiteral in formulas:
            pass
        elif f'¬{randomLiteral}' in formulas:
                if len(formulas) == 1:
                    pass
                else: 
                    new_formula = formulas[:]
                    new_formula.remove(f'¬{randomLiteral}')
                    new_auxForm1.append(new_formula)
        else:
                new_auxForm1.append(formulas)    
    auxForm1 = [subforms[:] for subforms in new_auxForm1]
    print("Este é o 1 após a mudança:", auxForm1)
    node.left = Node(auxForm1)
    node.left.path = [caminho[:] for caminho in node.path]
    node.left.direction = "left"

    auxForm2 = [formulas[:] for formulas in form]
    print("Este é o 2 antes da mudança", auxForm2)
    new_auxForm2 = []
    for formulas in auxForm2:
        if randomLiteral in formulas:
            if len(formulas) == 1:
                pass
            else: 
                new_formula = formulas[:]
                new_formula.remove(randomLiteral)
                new_auxForm2.append(new_formula)
        elif f'¬{randomLiteral}' in formulas or formulas == []:
            pass  
        else:
            new_auxForm2.append(formulas)
    auxForm2 = [subforms[:] for subforms in new_auxForm2]
    print("Este é o 2 após a mudança", auxForm2)
    node.right = Node(auxForm2)
    node.right.path = [caminho[:] for caminho in node.path]
    node.right.direction = "right"

    print(node.path)

    TransformacaoBooleana(node.right)
    TransformacaoBooleana(node.left)

def checarContradicao(expression):
    for subform in expression:
        if len(subform) == 1 and [f'¬{subform[0]}'] in expression:
            print("Razao da contradição: ", subform, [f'¬{subform[0]}'], expression)
            return True 
    return False

if __name__ == '__main__':
    main()