import numpy as np
target = 289326

vecOben   = np.array([ 0, 1])
vecUnten  = np.array([ 0,-1])
vecRechts = np.array([ 1, 0])
vecLinks  = np.array([-1, 0])
vecCursor = np.array([ 0, 0])
listOfValues = {}

richtungen = [vecRechts,vecOben,vecLinks,vecUnten]
aktuelleRichtung = 0

anzahlInLoop = 0
aktuelleStelle = 1
i = 0

while(aktuelleStelle < target): #Jeweils eine Umrundung des Feldes
    i += 1
    anzahlInLoop += 8 #Jede Umrundung kommen 8 Zahlen mehr
    min = aktuelleStelle +1
    max = aktuelleStelle + anzahlInLoop +1
    for j in range(min,max):
        vecCursor = np.add(vecCursor,richtungen[aktuelleRichtung])
        if j == target:
            print("Bei " + str(j) + ": " + str(vecCursor) + " -> " + str(abs(vecCursor.item(0)) + abs(vecCursor.item(1))))
            break
        if j != max-1 and (j== min or (j % ((anzahlInLoop)/4) == 1)): #Die Ecken damit die Richtung gewechselt werden kann.
            aktuelleRichtung = (aktuelleRichtung + 1) % 4
    aktuelleStelle = j;
