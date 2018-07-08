import sys
from QualificationRound.solution import Solution as qrSol;

if __name__ == '__main__':
    round = sys.argv[1]
    if round == 'qr':
        sol = qrSol()
    elif round == 'r1':
        sol = None
    else:
        print('Invalid Argument: Round')
        
    prob = sys.argv[2]
    if prob == '1':
        sol.p1()
    elif prob == '2':
        sol.p2()
    elif prob == '3':
        sol.p3()
    else:
        print('Invalid Argument: Problem')
