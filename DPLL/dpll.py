variaveis = dict()

def main():
    clauses = cnfFormula()
    clauses.sort(key= lambda k: len(k))

    if dpll(clauses):
        print('Sat')
        print(variaveis)
    else:
        print('Unsat')

def dpll(clauses: list[set[int]]) -> bool:
    TransformacaoBooleana(clauses)

    if len(clauses) == 0: return True
    if checarContradicao(clauses): return False

    var:int = 0
    for elem in clauses[0]:
        var = elem
        break
    
    cpyClauses = copyClauses(clauses)
    cpyClauses.insert(0, set({var}))
    addVarValoration(var, True)
    if dpll(cpyClauses): return True

    cpyClauses = copyClauses(clauses)
    cpyClauses.insert(0, set({-var}))
    addVarValoration(var, False)
    if dpll(cpyClauses): return True

def copyClauses(clauses: list[set[int]]) -> list[set[int]]:
    newClauses: list[set[int]] = list()
    for clause in clauses:
        newClauses.append(clause.copy())
    
    return newClauses


def cnfFormula() -> list[set[int]]:
    clauses = list()
    
    with open('DPLL/inputs/cnf2.txt', 'r') as formulae:
        formulae.readline()
        lines = formulae.readlines()
        for line in lines:
            clause = set()
            for var in line.split(sep=' '):
                varInt = int(var)
                if varInt != 0:
                    clause.add(varInt)     
            clauses.append(clause)
    return clauses

def TransformacaoBooleana(clauses: list[set[int]]):
    while len(clauses) > 0 and len(clauses[0]) == 1:
        unit = clauses.pop(0).pop()
        addVarValoration(unit, True)
        for clause in clauses[:]:
            if unit in clause:
                clauses.remove(clause)
            elif -unit in clause:
                clause.remove(-unit)
        
        clauses.sort(key= lambda k: len(k))   

def checarContradicao(clauses: list[set[int]]) -> bool:
    return (len(clauses[0]) == 0)

def addVarValoration(var: int, valoration: bool):
    global variaveis
    if var > 0:
        variaveis['x' + str(var)] = valoration
    elif var < 0:
        variaveis['x' + str(-var)] = not valoration

if __name__ == '__main__':
    main()