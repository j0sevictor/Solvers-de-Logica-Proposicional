solution: dict[int, bool] = dict()

def main():
    clauses = cnfFormula()
    clauses.sort(key= lambda k: len(k), reverse=True)

    if dpll(clauses):
        print('Sat')
        print(solution)
    else:
        print('Unsat')

def dpll(clauses: list[set[int]]) -> bool:
    TransformacaoBooleana(clauses)

    if len(clauses) == 0: return True
    if checarContradicao(clauses): return False

    var:int = heuristc(clauses)

    cpyClauses = copyClauses(clauses)
    cpyClauses.append(set({var}))
    addVarValoration(var, True)
    if dpll(cpyClauses): return True

    cpyClauses = copyClauses(clauses)
    cpyClauses.append(set({-var}))
    addVarValoration(var, False)
    if dpll(cpyClauses): return True

def TransformacaoBooleana(clauses: list[set[int]]):
    while len(clauses) > 0 and len(clauses[-1]) == 1:
        unit = clauses.pop(-1).pop()
        addVarValoration(unit, True)
        for clause in clauses:
            if unit in clause:
                clauses.remove(clause)
            elif -unit in clause:
                clause.remove(-unit)

        clauses.sort(key= lambda k: len(k), reverse=True)

def copyClauses(clauses: list[set[int]]) -> list[set[int]]:
    newClauses: list[set[int]] = list()
    for clause in clauses:
        newClauses.append(clause.copy())

    return newClauses

def cnfFormula() -> list[set[int]]:
    clauses = list()

    with open('DPLL/inputs/cnf2.txt', 'r') as formulae:
        lines = formulae.readlines()
        for line in lines:
            if line.startswith('c') or line.startswith('p'): continue

            clause = set()
            for var in line.split(sep=' '):
                varInt = int(var)
                if varInt != 0:
                    clause.add(varInt)
            clauses.append(clause)
    return clauses

def checarContradicao(clauses: list[set[int]]) -> bool:
    return len(clauses[-1]) == 0

def addVarValoration(var: int, valoration: bool):
    global solution
    if var > 0:
        solution[var] = valoration
    elif var < 0:
        solution[-var] = not valoration

def heuristc(clauses: list[set[int]]) -> int:
    for elem in clauses[-1]:
        return elem

if __name__ == '__main__':
    main()