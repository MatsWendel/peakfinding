def findPeaks(_array):
    #Array in dem alle Peaks gespeichert werden.
    peaks = []
    #durchlaufen des gesammten 2D Arrays.
    for i in range(len(_array)):
        for j in range(len(_array[i])):
            #Speichern des aktuellen Wertes in einer Variable
            akt = _array[i][j]
            #initialisieren von vertPeak und horPeak und beide auf False setzen
            vertPeak = False
            horPeak = False
            #Wenn der aktuelle Wert sich ganz rechts oder ganz links befindet
            if j == 0 or j == len(_array[0])-1:
                #wenn der betrachtete Wert im Array am linken Rand ist
                if j == 0:
                    #wenn der betrachtete Wert ein horizontaler Peak ist
                    if _array[i][j] > _array[i][j+1]:
                        #hor Peak auf True setzen
                        horPeak = True
                #wenn sich der aktuelle Wert ganz rechts befindet
                elif j == len(_array[0])-1:
                    #wenn der Wert ein horPeak ist
                    if _array[i][j] > _array[i][j-1]:
                        #horPeak auf True setzen
                        horPeak = True
            #Wenn sich der aktuelle Wert nicht an einem rand befindet
            else:
                #Wenn der aktuelle Wert ein horPeak ist
                if _array[i][j] > _array[i][j+1] & _array[i][j] > _array[i][j-1]:
                    #horPeak auf True setzen
                    horPeak = True
            #Wenn der aktuelle Wert ein horPeak ist
            if horPeak == True:
                #wenn der Wert sich am oberen oder am unteren rand befindet
                if i == 0 or i == len(_array)-1:
                    #Wenn sich der Wert ganz oben befindet
                    if i == 0:
                        #Wenn der Wert ein VertPeak ist
                        if _array[i][j] > _array[i+1][j]:
                            #vertpeak auf True setzen
                            vertPeak = True
                    #Wenn der Wert ganz unten befindet
                    elif i == len(_array)-1:
                        #wenn der Wert ein vertPeak ist
                        if _array[i][j] > _array[i-1][j]:
                            #vertPeak auf True setzen
                            vertPeak = True
                #Wenn sich der Wert nicht ganz oben oder ganz unten befindet
                else:
                    #gucken, ob es sich um einen vertPeak handelt
                    if (_array[i][j] > _array[i+1][j]) & (_array[i][j] > _array[i-1][j]):
                        #vertPeak auf True setzen
                        vertPeak = True
                #Wenn es sich bei dem betrachteten Wert um einen horizontalen und vertikalen Peak handelt
                if horPeak == True & vertPeak == True:
                    #den aktuellen Wert zum Array der peaks hinzufügen
                    peaks.append(akt)

    #Alle peaks auf der Konsole ausgeben
    for x in peaks:
        print(x)

#driver code
arr = [[10, 28, 22, 10],
       [9, 13, 12, 27],
       [15, 9, 24, 30],
       [160, 17, 19, 20]]
#function call
findPeaks(arr)