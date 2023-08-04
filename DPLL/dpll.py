def main():
    clauses, numVariaveis, numClausues = cnfFormula()
    print(clauses, numVariaveis, numClausues)


def cnfFormula() -> tuple:
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
    
    return (clauses, numVariables, numClauses)

def simplifica(cl):
    pass

if __name__ == '__main__':
    main()