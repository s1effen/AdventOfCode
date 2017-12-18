import numpy as np
target = 289326
vecOben   = np.array([ 0, 1])
vecUnten  = np.array([ 0,-1])
vecRechts = np.array([ 1, 0])
vecLinks  = np.array([-1, 0])
vecCursor = np.array([ 0, 0])
listOfValues = {str(vecCursor) : 1}

richtungen = [vecRechts,vecOben,vecLinks,vecUnten]
aktuelleRichtung = 0

anzahlInLoop = 0
aktuelleStelle = 1
i = 0

def add4Neighbors(vec):
    vecAsString = str(vec)
    listOfValues[vecAsString] = 0

    #Oben
    checkCoord = str(np.add(vec,vecOben))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #Oben links
    checkCoord = str(np.add(vec,np.add(vecOben,vecLinks)))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]
    #links
    checkCoord = str(np.add(vec,vecLinks))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #links unten
    checkCoord = str(np.add(vec,np.add(vecLinks,vecUnten)))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #Unten
    checkCoord = str(np.add(vec,vecUnten))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #Unten rechts
    checkCoord = str(np.add(vec,np.add(vecUnten,vecRechts)))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #Rechts
    checkCoord = str(np.add(vec,vecRechts))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    #Oben rechts
    checkCoord = str(np.add(vec,np.add(vecOben,vecRechts)))
    if checkCoord in listOfValues:
        listOfValues[vecAsString] += listOfValues[checkCoord]

    return listOfValues[vecAsString]

while(aktuelleStelle < target): #Jeweils eine Umrundung des Feldes
    i += 1
    anzahlInLoop += 8 #Jede Umrundung kommen 8 Zahlen mehr
    min = aktuelleStelle +1
    max = aktuelleStelle + anzahlInLoop +1
    for j in range(min,max):
        vecCursor = np.add(vecCursor,richtungen[aktuelleRichtung])
        add4Neighbors(vecCursor)
        #print(str(j) + " " + str(vecCursor) + " " + str(listOfValues[str(vecCursor)]))
        if listOfValues[str(vecCursor)] > target:
            print("Bei " + str(j) + ": " + str(vecCursor) + " -> " + str(listOfValues[str(vecCursor)]))
            quit()
        if j != max-1 and (j== min or (j % ((anzahlInLoop)/4) == 1)): #Die Ecken damit die Richtung gewechselt werden kann.
            aktuelleRichtung = (aktuelleRichtung + 1) % 4
    aktuelleStelle = j;

