import os

def tablica(cntr):
    os.system('clear')
    print("\033[0;37m#    1    2    3")
    print("1", "\033[1;31m", arr[0], "\033[0;37m")
    print("2", "\033[1;31m", arr[1], "\033[0;37m")
    print("3", "\033[1;31m", arr[2], "\033[0;37m")

def provjera(cntr, kraj):
    upis(cntr)
    for i in range(row):            #provjera redove
        if arr[i][0] != '#':
             a = arr[i][0]
             b = arr[i][1]
             c = arr[i][2]
             if a == b and a == c:
                  kraj = 1
    
    for j in range(col):            #provjera stupce
        if arr[0][j] != '#':
             a = arr[0][j]
             b = arr[1][j]
             c = arr[2][j]
             if a == b and a == c:
                  kraj = 1
    
    a = arr[i][i]
    for i in range(1, row):         #provjera glavne dijagonale
        if a != '#':
            if arr[i][i] != a:
                kraj = 0
            else:
                kraj = 1

    if arr[0][2] != '#' or arr[1][1] != '#' or arr[2][0] != '#':        #provjera sporedne dijagonale
        if arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0]:
            kraj = 1
    return kraj
        
def upis(cntr):                                                         #upis znaka u polja, cntr je counter koji igrac je na redu
    
    if cntr % 2 == 0:
        i = int(input("u koji red zelite staviti znak X: ")) - 1        # broj 1-3
        j = int(input("u koji stupac zelite staviti znak X: ")) - 1
        if i > 2 or j > 2 or arr[i][j] != '#':                                                      #ako u trazenom polju nije '@' trazi ponovni upis
            i = int(input("Nedozvoljen unos, u koji red zelite staviti znak X: ")) - 1
            j = int(input("Nedozvoljen unos, u koji stupac zelite staviti znak X: ")) - 1
        
        arr[i][j] = 'X'
    else:
        i = int(input("u koji red zelite staviti znak O: ")) - 1                                    # broj 1-3
        j = int(input("u koji stupac zelite staviti znak O: ")) - 1
        if i > 2 or j > 2 or arr[i][j] != '#':                                                      #ako u trazenom polju nije '@' trazi ponovni upis
            i = int(input("Nedozvoljen unos, u koji red zelite staviti znak O: ")) - 1
            j = int(input("Nedozvoljen unos, u koji stupac zelite staviti znak O: ")) - 1
        arr[i][j] = 'O'

row, col = (3, 3)
arr = [['#' for i in range(row)] for j in range(col)]
kraj = 0
cntr = 0
while kraj == 0:
    tablica(cntr)
    kraj = provjera(cntr, kraj)
    cntr = cntr + 1
    tablica(cntr)
if cntr % 2 == 0:
    print("Igrac koji je igrao sa O je pobjedio")
else:
    print("Igrac koji je igrao sa X je pobjedio")