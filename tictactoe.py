Bräda = [' ' for x in range(10)]

def VäljBokstav(Bokstav,pos):
    Bräda[pos] = Bokstav

def YtanÄrTomm(pos):
    return Bräda[pos] == ' '

def PrintaBräda(Bräda):
    print('   |   |   ')
    print(' ' + Bräda[1] + ' | ' + Bräda[2] + ' | ' + Bräda[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + Bräda[4] + ' | ' + Bräda[5] + ' | ' + Bräda[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + Bräda[7] + ' | ' + Bräda[8] + ' | ' + Bräda[9])
    print('   |   |   ')

def ÄrBrädanFull(Bräda):
    if Bräda.count(' ') > 1:
        return False
    else:
        return True

def Vinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def DragAvSpelare():
    run = True
    while run:
        Drag = input("För att göra ett drag, välj mellan 1 till 9\n")
        try:
            Drag = int(Drag)
            if Drag > 0 and Drag < 10:
                if YtanÄrTomm(Drag):
                    run = False
                    VäljBokstav('X' , Drag)
                else:
                    print('Tyvärr är detta redan valt')
            else:
                print('Välj ett nummer mellan 1 till 9')

        except:
            print('Skriv ett nummer')

def DatorDrag():
    MöjligaDrag = [x for x , bokstav in enumerate(Bräda) if bokstav == ' ' and x != 0  ]
    Drag = 0

    for let in ['O' , 'X']:
        for i in MöjligaDrag:
            KopiaBräda = Bräda[:]
            KopiaBräda[i] = let
            if Vinnare(KopiaBräda, let):
                Drag = i
                return Drag

    FriaHörn = []
    for i in MöjligaDrag:
        if i in [1 , 3 , 7 , 9]:
            FriaHörn.append(i)

    if len(FriaHörn) > 0:
        Drag = selectRandom(FriaHörn)
        return Drag

    if 5 in MöjligaDrag:
        Drag = 5
        return Drag

    FriKant = []
    for i in MöjligaDrag:
        if i in [2,4,6,8]:
            FriKant.append(i)

    if len(FriKant) > 0:
        Drag = selectRandom(FriKant)
        return Drag

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Sugen på tre i rad?")
    PrintaBräda(Bräda)

    while not(ÄrBrädanFull(Bräda)):
        if not(Vinnare(Bräda , 'O')):
            DragAvSpelare()
            PrintaBräda(Bräda)
        else:
            print("Du förlorade, synd!")
            break

        if not(Vinnare(Bräda , 'X')):
            Drag = DatorDrag()
            if Drag == 0:
                print(" ")
            else:
                VäljBokstav('O' , Drag)
                print('Datorn placerade ett o på' , Drag , ':')
                PrintaBräda(Bräda)
        else:
            print("Du vann!")
            break




    if ÄrBrädanFull(Bräda):
        print("Oavgjord runda")

while True:
    x = input("Vill du spela? Välj j för ja och n för nej (j/n)\n")
    if x.lower() == 'j':
        Bräda = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
