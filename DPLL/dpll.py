def main():
    clauses = cnfFormula()
    clauses.sort(key= lambda k: len(k))
    print(clauses)


def cnfFormula() -> list[set]:
    numVariables, numClauses = 0, 0

    with open('DPLL\CNFFormula.txt', 'r') as formulae:
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
    
    return clauses

def dpll(clauses: list[set]) -> bool:
    pass

def simplifica(clauses: list[set]) -> set:
    for clause in clauses:
        if len(clause) == 1:
            pass


if __name__ == '__main__':
    main()