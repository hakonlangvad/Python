import time, random
from collections import Counter
import copy as cp

def Solver(board):
    t0 = time.time()
    sudoku_board = [
        [[[],[],[]],[[],[],[]],[[],[],[]]],
        [[[],[],[]],[[],[],[]],[[],[],[]]],
        [[[],[],[]],[[],[],[]],[[],[],[]]]
    ]

    sudoku_board[0][0][0] = board[0][0]
    sudoku_board[0][0][1] = board[1][0]
    sudoku_board[0][0][2] = board[2][0]
    sudoku_board[0][1][0] = board[0][1]
    sudoku_board[0][1][1] = board[1][1]
    sudoku_board[0][1][2] = board[2][1]
    sudoku_board[0][2][0] = board[0][2]
    sudoku_board[0][2][1] = board[1][2]
    sudoku_board[0][2][2] = board[2][2]

    sudoku_board[1][0][0] = board[3][0]
    sudoku_board[1][0][1] = board[4][0]
    sudoku_board[1][0][2] = board[5][0]
    sudoku_board[1][1][0] = board[3][1]
    sudoku_board[1][1][1] = board[4][1]
    sudoku_board[1][1][2] = board[5][1]
    sudoku_board[1][2][0] = board[3][2]
    sudoku_board[1][2][1] = board[4][2]
    sudoku_board[1][2][2] = board[5][2]

    sudoku_board[2][0][0] = board[6][0]
    sudoku_board[2][0][1] = board[7][0]
    sudoku_board[2][0][2] = board[8][0]
    sudoku_board[2][1][0] = board[6][1]
    sudoku_board[2][1][1] = board[7][1]
    sudoku_board[2][1][2] = board[8][1]
    sudoku_board[2][2][0] = board[6][2]
    sudoku_board[2][2][1] = board[7][2]
    sudoku_board[2][2][2] = board[8][2]
    
    while True:
        check = False
        for i in range(3):
            for y in range(3):
                for z in range(3):
                    for j in range(3):
                        number = sudoku_board[i][y][z][j]
                        if number == 0:
                            check = True
                            numbers_in_block = []
                            for a in range(3):
                                for b in range(3):
                                    if sudoku_board[i][y][a][b] != 0:
                                        numbers_in_block.append(sudoku_board[i][y][a][b])
                            potential_x = []
                            potential_y = []
                            for a in range(1,10):
                                if a not in numbers_in_block:
                                    for b in range(3):
                                        if b != y:
                                            if a in sudoku_board[i][b][z]:
                                                potential_x.append(a)
                            for b in range(3):
                                if b != i:
                                    for c in range(3):
                                        if sudoku_board[b][y][c][j] != 0 and sudoku_board[b][y][c][j] not in numbers_in_block:
                                            potential_y.append(sudoku_board[b][y][c][j])
                            potensielle = []
                            a = 1
                            while a < 10: 
                                if a not in potential_x and a not in potential_y and a not in numbers_in_block:
                                    potensielle.append(a)
                                a += 1
                            if len(potensielle) == 1:
                                sudoku_board[i][y][z][j] = potensielle[0]
                                print(sudoku_board[0][0][0],sudoku_board[0][1][0],sudoku_board[0][2][0])
                                print(sudoku_board[0][0][1],sudoku_board[0][1][1],sudoku_board[0][2][1])
                                print(sudoku_board[0][0][2],sudoku_board[0][1][2],sudoku_board[0][2][2],'\n')
                                print(sudoku_board[1][0][0],sudoku_board[1][1][0],sudoku_board[1][2][0])
                                print(sudoku_board[1][0][1],sudoku_board[1][1][1],sudoku_board[1][2][1])
                                print(sudoku_board[1][0][2],sudoku_board[1][1][2],sudoku_board[1][2][2],'\n')
                                print(sudoku_board[2][0][0],sudoku_board[2][1][0],sudoku_board[2][2][0])
                                print(sudoku_board[2][0][1],sudoku_board[2][1][1],sudoku_board[2][2][1])
                                print(sudoku_board[2][0][2],sudoku_board[2][1][2],sudoku_board[2][2][2],'\n')
        if check == False:
            break
    '''
    print(sudoku_board[0][0][0],sudoku_board[0][1][0],sudoku_board[0][2][0])
    print(sudoku_board[0][0][1],sudoku_board[0][1][1],sudoku_board[0][2][1])
    print(sudoku_board[0][0][2],sudoku_board[0][1][2],sudoku_board[0][2][2],'\n')
    print(sudoku_board[1][0][0],sudoku_board[1][1][0],sudoku_board[1][2][0])
    print(sudoku_board[1][0][1],sudoku_board[1][1][1],sudoku_board[1][2][1])
    print(sudoku_board[1][0][2],sudoku_board[1][1][2],sudoku_board[1][2][2],'\n')
    print(sudoku_board[2][0][0],sudoku_board[2][1][0],sudoku_board[2][2][0])
    print(sudoku_board[2][0][1],sudoku_board[2][1][1],sudoku_board[2][2][1])
    print(sudoku_board[2][0][2],sudoku_board[2][1][2],sudoku_board[2][2][2],'\n')
    '''
    t1 = time.time()
    return t1-t0

def Solver_2(board):
    
    t0 = time.time()
    while True:
        check = True
        for i in range(9):
            tall_brukt_x = []
            for x in range(3):
                for y in range(3):
                    if board[i][x][y] != 0:
                        tall_brukt_x.append(board[i][x][y])
            for j in range(3):
                tall_brukt_blokk = []
                rest = i % 3
                for x in range(3):
                    for k in range(3):
                        if board[i+x-rest][j][k] != 0:
                            tall_brukt_blokk.append(board[i+x-rest][j][k])
                for k in range(3):
                    if board[i][j][k] != 0:
                        pass
                    else:
                        check = False
                        tall_brukt_y = []
                        for n in range(9):
                            if board[n][j][k] != 0:
                                tall_brukt_y.append(board[n][j][k])
                        
                        # Sudoku-Test #
                        potentials = []
                        for x in range(1,10):
                            if x not in tall_brukt_blokk and x not in tall_brukt_x and x not in tall_brukt_y:
                                potentials.append(x)
                        if len(potentials) == 1:
                            board[i][j][k] = potentials[0]
                        else:
                            pass
        if check == True:
            break
    '''
    print(board[0][0],board[0][1],board[0][2])
    print(board[1][0],board[1][1],board[1][2])
    print(board[2][0],board[2][1],board[2][2],'\n')
    print(board[3][0],board[3][1],board[3][2])
    print(board[4][0],board[4][1],board[4][2])
    print(board[5][0],board[5][1],board[5][2],'\n')
    print(board[6][0],board[6][1],board[6][2])
    print(board[7][0],board[7][1],board[7][2])
    print(board[8][0],board[8][1],board[8][2],'\n')
    '''
    t1 = time.time()
    return t1-t0

def Solver_3(board):
    t0 = time.time()
    while True:
        check = True
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    if board[i][j][k] != 0:
                        pass
                    else:
                        check = False
                        tall_brukt_x = []
                        tall_brukt_y = []
                        tall_brukt_blokk = []

                        rest = i % 3
                        for x in range(3):
                            for y in range(3):
                                if board[i][x][y] != 0:
                                    tall_brukt_x.append(board[i][x][y])
                                if board[i+x-rest][j][y] != 0:
                                    tall_brukt_blokk.append(board[i+x-rest][j][y])

                        for n in range(9):
                            if board[n][j][k] != 0:
                                tall_brukt_y.append(board[n][j][k])
                                                
                        # Sudoku-Test #
                        potentials = []
                        for x in range(1,10):
                            if x not in tall_brukt_blokk and x not in tall_brukt_x and x not in tall_brukt_y:
                                potentials.append(x)
                        if len(potentials) == 1:
                            board[i][j][k] = potentials[0]
                            print('\n\n\n')
                            print(board[0][0],board[0][1],board[0][2])
                            print(board[1][0],board[1][1],board[1][2])
                            print(board[2][0],board[2][1],board[2][2],'\n')
                            print(board[3][0],board[3][1],board[3][2])
                            print(board[4][0],board[4][1],board[4][2])
                            print(board[5][0],board[5][1],board[5][2],'\n')
                            print(board[6][0],board[6][1],board[6][2])
                            print(board[7][0],board[7][1],board[7][2])
                            print(board[8][0],board[8][1],board[8][2],'\n')
                            
                        else:
                            pass
        if check == True:
            break
    
    print(board[0][0],board[0][1],board[0][2])
    print(board[1][0],board[1][1],board[1][2])
    print(board[2][0],board[2][1],board[2][2],'\n')
    print(board[3][0],board[3][1],board[3][2])
    print(board[4][0],board[4][1],board[4][2])
    print(board[5][0],board[5][1],board[5][2],'\n')
    print(board[6][0],board[6][1],board[6][2])
    print(board[7][0],board[7][1],board[7][2])
    print(board[8][0],board[8][1],board[8][2],'\n')
    
    t1 = time.time()
    return t1-t0

def Solver_4(board):
    t0 = time.time()
    counter = 0
    check_2 = 0
    check_3 = 0
    backup_old = 0
    backup = False
    while True: 
        check = True
        check_2 += 1
        ultimate_test = {}
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    
                    if board[i][j][k] != 0:
                        pass
                    else:
                        ##### Algoritme 1 #####

                        # Sjekker tall i blokk på rekke og rad i henhold til celle
                        # Super effektiv

                        check = False
                        tall_brukt_x = []
                        tall_brukt_y = []
                        tall_brukt_blokk = []

                        rest = i % 3
                        for x in range(3):
                            for y in range(3):
                                if board[i][x][y] != 0:
                                    tall_brukt_x.append(board[i][x][y])
                                if board[i+x-rest][j][y] != 0:
                                    tall_brukt_blokk.append(board[i+x-rest][j][y])

                        for n in range(9):
                            if board[n][j][k] != 0:
                                tall_brukt_y.append(board[n][j][k])
                                                                        
                        # Finner potensielle tall for celle
                        potentials = []
                        for x in range(1,10):
                            if x not in tall_brukt_blokk and x not in tall_brukt_x and x not in tall_brukt_y:
                                potentials.append(x)
                        if len(potentials) == 1: # Hvis det bare er ett potensielt tall legges den til sudokubrettet
                            board[i][j][k] = potentials[0]
                            check_2 = 0
                                                    
                        elif check_3 > 0:
                            ##### Algoritme 2 #####

                            # Denne algoritmen er litt tregere men til gjenjeld super smart. Brukes kun når algoritme 1 feiler
                            # Denne tar utgangspunkt i en hel blokk (3x3 celler) og ser på hvor mange potensielle tall det er, celle for celle, for hele blokken:
                            # Hvis den bare finner ett potensielt tall som ikke oppstår i noe annen celle i blokken, legges den til brettet

                            # Startposisjon Y-retning
                            if 0 <= i < 3:
                                y_0 = 0
                            elif 3 <= i < 6:
                                y_0 = 3
                            else:
                                y_0 = 6                      

                            tall_brukt_x1 = []
                            tall_brukt_x2 = []
                            tall_brukt_x3 = []
                            tall_brukt_y1 = []
                            tall_brukt_y2 = []
                            tall_brukt_y3 = []

                            # Finner brukte tall i alle x-rekkene
                            for z in range(3):
                                for x in range(3):
                                    for y in range(3):
                                        if board[y_0+z][x][y] != 0:
                                            if z == 0:
                                                tall_brukt_x1.append(board[y_0+z][x][y])
                                            elif z == 1:
                                                tall_brukt_x2.append(board[y_0+z][x][y])
                                            else:    
                                                tall_brukt_x3.append(board[y_0+z][x][y])
                            
                            # Finner brukte tall i alle y-rekkene
                            for z in range(3):
                                for n in range(9):
                                    if board[n][j][z] != 0:
                                        if z == 0:
                                            tall_brukt_y1.append(board[n][j][z])
                                        elif z == 1:
                                            tall_brukt_y2.append(board[n][j][z])
                                        else:
                                            tall_brukt_y3.append(board[n][j][z])

                            # Her legges alle potensielle tall til i en liste med tilhørende koordinater
                            totale_pot = {}
                            z = 0
                            while z < 3:
                                n = 0
                                while n < 3:
                                    pot = []
                                    tall = board[z+y_0][j][n]
                                    if tall != 0 and n < 2:
                                        n += 1
                                        continue
                                    elif tall != 0 and n == 2:
                                        n += 1
                                        z += 1
                                    else:
                                        if z == 0:
                                            if n == 0:                                           
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x1 and m not in tall_brukt_y1 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            elif n == 1:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x1 and m not in tall_brukt_y2 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            else:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x1 and m not in tall_brukt_y3 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                        elif z == 1:
                                            if n == 0:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x2 and m not in tall_brukt_y1 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            elif n == 1:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x2 and m not in tall_brukt_y2 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            else:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x2 and m not in tall_brukt_y3 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                        else:
                                            if n == 0:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x3 and m not in tall_brukt_y1 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            elif n == 1:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x3 and m not in tall_brukt_y2 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                            else:
                                                for m in range(1,10):
                                                    if m not in tall_brukt_x3 and m not in tall_brukt_y3 and m not in tall_brukt_blokk and m not in pot:
                                                        pot.append(m)
                                        if n < 2:
                                            n += 1
                                            if len(pot) != 0:
                                                totale_pot[z,j,n-1] = pot
                                                ultimate_test[z+y_0,j,n-1] = pot
                                        else:
                                            n += 1
                                            z += 1
                                            if len(pot) != 0:
                                                totale_pot[z-1,j,n-1] = pot
                                                ultimate_test[z-1+y_0,j,n-1] = pot
                                    
                            # Sjekker så hvilke(n) tall som bare oppstå én gang for en celle i en blokk
                            tall_liste = []
                            tall_counter = Counter()

                            for val in totale_pot.values():
                                for a in range(len(val)):
                                    tall_liste.append(val[a])
                            
                            for a in range(len(tall_liste)):
                                tall_counter[tall_liste[a]] += 1
                            
                            # Legger den så til på brettet hvis den bare oppstå én gang
                            for w,c in tall_counter.items():
                                if c == 1:
                                    for key,val in totale_pot.items():
                                        if w in val:
                                            i_1 = key[0]
                                            i_2 = key[1]
                                            i_3 = key[2]
                                            board[i_1+y_0][i_2][i_3] = w
                                            check_2 = 0
        counter += 1     
             
        if check_2 > 0 and check == False and check_3 > 1:
            ##### Algoritme 3 #####

            # Denne er ikke ønskelig å bruke så alt for ofte. Helst så sjeldent som mulig ettersom at den er treg. Trengs for vanskelige sudoku
            # Denne brukes når Algoritme 1 og Algoritme 2 feiler.
            # Hvis det skulle oppstå en situasjon i sudokuen hvor det ikke lenger er noe entydig svar for hvilke tall en skal legge inn på brettet,
            # Blir man nødt å "gjette" på et alternativt tall for å se hvordan det påvirker resten av sudokuen. Denne algoritmen gjør akkurat det


            # Første test: Finne de/den cellen(e) med færrest mulige alternativ. Helst bare to
            liste_over_pot = []
            antall_pot_celle = []
            for key, val in ultimate_test.items():
                liste_over_pot.append([key,val])
                antall_pot_celle.append(len(val))
            
            # Tar backup
            if backup == False:
                backup_old = cp.deepcopy(board) # Deepcopy
                backup = True # Denne skal kun ta backup én gang og det skjer første gangen Algoritme 1 og 2 feiler.
                
            
            # Finner så en vilkårlig celle med 2 eller flere alternativ
            if len(antall_pot_celle) != 0:
                minste_verdi = min(antall_pot_celle) # Finner minste antall alternativ for mulige tall for alle cellene på brettet
                antall_pot = 0
                for key, val in ultimate_test.items():
                    if len(val) == minste_verdi:
                        antall_pot += 1
                i = 0
                # Velger ut en tilfeldig celle som tilferedstiller minste alternativ for mulige tall
                y = random.randint(0,antall_pot-1)
                valg = random.randint(0,minste_verdi-1) # Hvilke av alternativene programmet skal velge
                for key, val in ultimate_test.items():
                    if len(val) == minste_verdi and i == y:
                        test_subject = val[valg] # Valgt tall (test_subject)
                        # Koordianter til cellen
                        x_1 = key[0]
                        x_2 = key[1]
                        x_3 = key[2]
                        # Legger så test_subject til brettet
                        board[x_1][x_2][x_3] = test_subject

                    if len(val) == minste_verdi:
                        i += 1

        # Hvis programmet setter seg fast. Henter fra backup og begynner på nytt
        if check_2 > 20 and backup == True: # check_2 > x bør ikke settes for lavt
            board = cp.deepcopy(backup_old)
            check_2 = 0 
        
        # Hvis Algoritme 1 feiler
        if check_2 > 1 and check_3 == 0:
            check_3 = 1
        # Hvis algoritme 2 feiler
        elif check_2 > 1 and check_3 == 1:
            check_3 = 2
            check_2 = 0

        # Når programmet har løst for alle cellene. Avsluttes loopen
        if check == True:
            break

    t1 = time.time()

    print(board[0][0],board[0][1],board[0][2])
    print(board[1][0],board[1][1],board[1][2])
    print(board[2][0],board[2][1],board[2][2],'\n')
    print(board[3][0],board[3][1],board[3][2])
    print(board[4][0],board[4][1],board[4][2])
    print(board[5][0],board[5][1],board[5][2],'\n')
    print(board[6][0],board[6][1],board[6][2])
    print(board[7][0],board[7][1],board[7][2])
    print(board[8][0],board[8][1],board[8][2],'\n')

    return t1-t0,counter

# MAINLOOP
if __name__ == "__main__":
    test_runner = 10 # Hvor mange ganger programmet skal løse sudokuen
    test_number = 0 # Ikke endre på denne
    time_table = [] 
    runder_tabbel = []
    while test_number < test_runner:

        board = [
            [[8,0,0],[0,0,0],[0,0,0]],
            [[0,0,3],[6,0,0],[0,0,0]],
            [[0,7,0],[0,9,0],[2,0,0]],

            [[0,5,0],[0,0,7],[0,0,0]],
            [[0,0,0],[0,4,5],[7,0,0]],
            [[0,0,0],[1,0,0],[0,3,0]],

            [[0,0,1],[0,0,0],[0,6,8]],
            [[0,0,8],[5,0,0],[0,1,0]],
            [[0,9,0],[0,0,0],[4,0,0]]     
        ]

        #time_return = Solver(board)
        #time_return = Solver_2(board)
        #time_return = Solver_3(board)
        time_return,counter = Solver_4(board)
        time_table.append(time_return)
        test_number += 1
        runder_tabbel.append(counter)

    # Testresultatet
    print('TEST RESULTS:')
    value = 0
    for i in range(test_runner):
        value += time_table[i]
    value = value / test_runner
    print(value)
    print('\nFærrest runder brukt:',min(runder_tabbel))
    print('Flest runder brukt:',max(runder_tabbel))
    input()