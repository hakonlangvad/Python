import random

def Generer_kalender(n,antall,check):
    '''
    Genererer n antall flaksloddkalendere og lagrer disse i Flakskalendere.txt
    '''
    i = 0

    ######## Definere vinnerloddene ########
    vinnerlodd_liste = []
    if check == False:
        while i < antall: # antall vinnerlodd i en flakskalender
            vinnerlodd = random.randint(1,n) # Random vinerlodd. Kan være så stor som n antall kalender
            if vinnerlodd not in vinnerlodd_liste: # Sørger for at et vinnerlodd ikke kan oppstå 2 ganger
                vinnerlodd_liste.append(vinnerlodd)
            else:
                continue
            i += 1
        print('Vinnerloddene: ' + str(vinnerlodd_liste))
    
    elif check == True:
        i = 0
        y = 24
        antall_vinnerlodd = []
        while i < y:
            try:
                print('Skriv inn hvor mange vinnerlodd det er for',i+1,'desember')
                antall_vinnerlodd_lodd = input('')
                if antall_vinnerlodd_lodd == '':
                    antall_vinnerlodd_lodd = '1'
                vinnerlodd = random.randint(1,n)
                if vinnerlodd not in vinnerlodd_liste:
                    antall_vinnerlodd.append(int(antall_vinnerlodd_lodd))
                    vinnerlodd_liste.append(vinnerlodd)
                    i += 1
                else:
                    continue
            except:
                print('Du skrev inn noe feil. Prøv igjen')
                continue
    
    ######## Plassering for vinnerloddene ########
    i = 0
    plassering = []
    if check == False:
        while i < len(vinnerlodd_liste):
            plass = random.randint(0,n-1) # Velger hvilke kalender de ulike vinnerloddene skal være med i
            if plass not in plassering:
                plassering.append(plass) # Kan kun oppstå i én kalender
            else:
                continue
            i += 1
        print('Hvilke kalender de puttes i ' + str(plassering))
    else:
        ny_vinnerlodd_liste = []
        gammel_plassering = []
        for i in range(len(vinnerlodd_liste)):
            y = 0
            liste = []
            plass_liste = []
            while y < antall_vinnerlodd[i]:
                plass = random.randint(1,n) # Velger hvilke kalender de ulike vinnerloddene skal være med i
                if plass not in plassering and plass not in gammel_plassering:
                    #plassering.append(plass) # Kan kun oppstå i én kalender
                    liste.append(vinnerlodd_liste[i])
                    plass_liste.append(plass)
                    gammel_plassering.append(plass)
                else:
                    continue
                y += 1
            ny_vinnerlodd_liste.append(liste)
            plassering.append(plass_liste)
        gammel_vinnerlodd_liste = vinnerlodd_liste
        vinnerlodd_liste = ny_vinnerlodd_liste
        print('Antall vinnerlodd:',antall_vinnerlodd)
        print('Vinnerloddene:',gammel_vinnerlodd_liste)
        print('Plasseringene:',gammel_plassering)
    
    ######## Lager n antall kalendere ########
    i = 0
    julekalendere = []
    verdier_brukt = []
    while i < n:
        b = 0
        lodd_liste = []
        y = 0
        while b < 24:
            lodd = random.randint(1,n) # Loddene er et tall mellom 1 og n

            # Hvis kalender i skal ha et vinnerlodd puttes de med her
            if i in plassering and vinnerlodd_liste[y] not in lodd_liste and check == False:
                if plassering[y] == i:
                    lodd_liste.append(vinnerlodd_liste[y])
                elif lodd not in vinnerlodd_liste and lodd not in lodd_liste:
                    lodd_liste.append(lodd)
                    y += 1
                else:
                    continue
            
            # Ellers så lenge kalender i ikke har loddet fra før av legges den til her
            # Et lodd kan ikke oppstå 2 ganger i samme kalender
            elif lodd not in vinnerlodd_liste and lodd not in lodd_liste:
                if check == False:
                    lodd_liste.append(lodd)
                elif lodd not in gammel_vinnerlodd_liste and lodd not in lodd_liste:
                    lodd_liste.append(lodd)
                else:
                    continue
            else:
                continue
            b += 1
        julekalendere.append(lodd_liste)
        i += 1
    
    ######### Hvis vi har en multiple vinner liste ############

    if check == True:
        for i in range(len(vinnerlodd_liste)):
            for y in range(len(vinnerlodd_liste[i])):
                kalender_plassering = plassering[i][y]
                kalender = julekalendere[kalender_plassering-1]
                loddet = kalender[i]
                vinnerlodd = vinnerlodd_liste[i][y]
                kalender[i] = vinnerlodd

    ############# Bruks kun for testing #############
    '''
    for i in range(len(julekalendere)):
        if vinnerlodd_liste[0] in julekalendere[i]:
            print(julekalendere[i])'''
    
    '''
    for i in range(len(julekalendere)):
        for y in range(len(vinnerlodd_liste[i])):
            if vinnerlodd_liste[y] in julekalendere[i]:
                print(julekalendere[i])'''
    
    '''
    for i in range(len(julekalendere)):
        for y in range(len(vinnerlodd_liste)):
            if vinnerlodd_liste[y] in julekalendere[i]:
                print('Vinnerlodd:',vinnerlodd_liste[y],'Kalendernummer:',i+1,julekalendere[i])'''
                
    ######## Lagrer julekalenderne i Flakskalendere.txt ########
    with open('Kalendere\\Flakskalendere.txt','w') as f:
        f.write(str(n) + ' antall julekalendere') # Første linje i filen sier hvor mange kalendere som er generert
        if check == False:
            f.write('\nVinnerloddene fra 0-24 des: ' + str(vinnerlodd_liste)) # Andre linjen er vinnerloddene og hvilke luke disse oppstår i
        else:
            f.write('\nVinnerloddene fra 0-24 des: ' + str(gammel_vinnerlodd_liste))
        for i in range(len(julekalendere)):
            f.write('\n' + str(julekalendere[i])) # Resten av linjene er alle n julekalenedere
    print('Vellykket\n')
            
def Sjekk_vinnerlodd(dag,lodd):
    '''
    Sjekker om et vilkårlig flakslodd er et vinnerlodd i en gitt dag
    '''
    # Leser flakskalendere.txt
    with open('Kalendere\\Flakskalendere.txt','r') as f:
        lines = f.readlines()
    vinnerrekke = lines[1][28:]
    vinnerliste = []
    i = 1
    n = 1
    # Lager en ny liste med alle vinnertallene og hvilke dag disse tilhører
    while i < len(vinnerrekke):
        tall = vinnerrekke[i]
        if tall == ' ':
            n += 1
        elif tall == ',' or tall == ']':
            vinnerliste.append(vinnerrekke[n:i])
            i += 1
            n = i
            continue
        i += 1

    # Tester så om lodd og dag stemmer overens med vinnerlodd
    if vinnerliste[dag-1] == str(lodd):
        return True # Returnerer True om stemmer
    return False # Ellers False

def print_kalender():
    luker = []
    i = 0
    while i < 24:
        luke = random.randint(1,24)
        if luke not in luker:
            luker.append(luke)
            i += 1
    print(luker)
    with open('Kalendere\\Flakskalendere.txt','r') as f:
        kalendere = f.readlines()
    
    kalender_liste = []
    for i in range(2,len(kalendere)):
        kalenderrekke = kalendere[i][0:]
        liste = []
        i = 1
        n = 1
        while i < len(kalenderrekke):
            tall = kalenderrekke[i]
            if tall == ' ':
                n += 1
            elif tall == ',' or tall == ']':
                liste.append(kalenderrekke[n:i])
                i += 1
                n = i
                continue
            i += 1
        kalender_liste.append(liste)
    kalendere = kalender_liste

    n_1 = len(kalendere)
    n = len(str(n_1))
    for i in range(len(kalendere)):
        for y in range(len(kalendere[i])):
            tall = kalendere[i][y]
            if int(tall) < 10:
                nytt_tall = '0'*(n-1) + tall
            elif int(tall) < 100:
                nytt_tall = '0'*(n-2) + tall
            elif int(tall) < 1000:
                nytt_tall = '0'*(n-3) + tall
            elif int(tall) < 10000:
                nytt_tall = '0'*(n-4) + tall
            elif int(tall) < 10000:
                nytt_tall = '0'*(n-5) + tall
            kalendere[i][y] = nytt_tall

    with open ('Kalendere\\kalenderutskrift.txt','w') as g:
        g.write('\n\n\n\n')
        g.write(str(luker[0]) + '   ' + str(luker[1]) + '   ' + str(luker[2]) + '   ' + str(luker[3]) + '   ' + str(luker[4]) + '   ' + str(luker[5]) + '\n\n')
        g.write(str(luker[6]) + '   ' + str(luker[7]) + '   ' + str(luker[8]) + '   ' + str(luker[9]) + '   ' + str(luker[10]) + '   ' + str(luker[11]) + '\n\n')
        g.write(str(luker[12]) + '   ' + str(luker[13]) + '   ' + str(luker[14]) + '   ' + str(luker[15]) + '   ' + str(luker[16]) + '   ' + str(luker[17]) + '\n\n')
        g.write(str(luker[18]) + '   ' + str(luker[19]) + '   ' + str(luker[20]) + '   ' + str(luker[21]) + '   ' + str(luker[22]) + '   ' + str(luker[23]) + '\n\n')
        g.write('\n\n\n')
        for i in range(len(kalendere)):
            g.write('\n\n\n\n')
            g.write(kalendere[i][luker[0]-1] + '   ' + kalendere[i][luker[1]-1] + '   ' + kalendere[i][luker[2]-1] + '   ' + kalendere[i][luker[3]-1] + '   ' + kalendere[i][luker[4]-1] + '   ' + kalendere[i][luker[5]-1] + '\n\n')
            g.write(kalendere[i][luker[6]-1] + '   ' + kalendere[i][luker[7]-1] + '   ' + kalendere[i][luker[8]-1] + '   ' + kalendere[i][luker[9]-1] + '   ' + kalendere[i][luker[10]-1] + '   ' + kalendere[i][luker[11]-1] + '\n\n')
            g.write(kalendere[i][luker[12]-1] + '   ' + kalendere[i][luker[13]-1] + '   ' + kalendere[i][luker[14]-1] + '   ' + kalendere[i][luker[15]-1] + '   ' + kalendere[i][luker[16]-1] + '   ' + kalendere[i][luker[17]-1] + '\n\n')
            g.write(kalendere[i][luker[18]-1] + '   ' + kalendere[i][luker[19]-1] + '   ' + kalendere[i][luker[20]-1] + '   ' + kalendere[i][luker[21]-1] + '   ' + kalendere[i][luker[22]-1] + '   ' + kalendere[i][luker[23]-1] + '\n\n')
            g.write('\n\n\n')



if __name__ == "__main__":
    # Skriver ut kommandoer for brukeren
    print('Kommandoer:')
    print('"generer" + <antall kalendere> for å generere kalendere')
    print('"generer multiple" + <antall kalendere> for å generere og definere antall vinnerlodd')
    print('"sjekk" + <dag> for å sjekke om vinnerlodd')
    print('"print" for å skrive ut alle kalenderne i kalenderutskrift.txt')
    while True: # Mainloop
        try:
            # Brukeren skriver inn en kommando
            kommando = input('Skriv inn kommando < ')
            # Gyldige kommandoer
            gyldige_svar = ['generer','sjekk','generer multiple']
        
            if gyldige_svar[2] in kommando:
                antall = int(kommando[16:])
                premier = 24
                Generer_kalender(antall,premier,True)

            # For å generere flaksloddkalendere
            elif gyldige_svar[0] in kommando: 
                antall = int(kommando[7:])
                premier = 24
                Generer_kalender(antall,premier,False)

            # For å sjekke om et vilkårlig lodd er et vinnerlodd
            elif gyldige_svar[1] in kommando:
                dag = int(kommando[5:])
                lodd = int(input('Skriv inn loddnr '))
                resultat = Sjekk_vinnerlodd(dag,lodd)

                # Om loddet og dagen som er oppgitt er et vinnerlodd eller ikke:
                if resultat == True:
                    print('Dette er et gyldig vinnerlodd\n')
                else:
                    print('Dette loddet er ikke i listen over gyldige vinnerlodd. Kan hende at feil dato er oppgitt\n')

            # For å gjøre klar kalenderne til å skrives ut
            elif kommando.lower() == 'print':
                print_kalender()
            
            # Hvis brukeren skrev inn noe ugyldig
            else:
                raise Exception
        except Exception:
            print('Du skrev inn noe ugydig. Pørv igjen\n')
