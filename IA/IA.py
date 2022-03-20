import random as rand # importam librariile necesare
import time
import msvcrt as m

points = int(0) # punctele reprezinta numerele
  
def wait(): # functie pentru asteptarea unei comenzi
    m.getch()

def clear(): # nu am reusit sa folosesc os.system("cls") si am folosit printarea a 100 lini
    for i in range(100):
        print("")
    print("---------Play Points = ", points , "-----------")

def menu(): # meniul in care am introdus:
    global points
    clear()
    print("Main Menu\n\n 1 -- Incepe jocul\n 2 -- Cum se joaca\n 3 -- DEBUG")  
    aleg = input("-> ")
    if aleg == "1": # start joc
        game()
    elif aleg == "2": # print la regulament
        print("Primul jucator spune numar intre 1 si 5. Cel de-al doilea jucator adauga la numarul dat un")
        print("intre 1 si 5. Primul jucator adauga la randul lui un numar intre 1 si 5 la numarul")
        print("rezultat. Jocul se continua astfel, iar castigator este jucatorul care ajunge primul la 20.")
        print("\nApasati ORICE tasta pentru a va intoarce la MENIUL PRINCIPAL!")
        wait()
        menu()
    elif aleg == "3": # debug mode unde am testat joculetul mai in amanunt, setezi punctele si userul care incepe
        clear()
        print("Bun venit in debug mode!")
        print("Setare puncte start si user start\n")
        startPoints = int(input("Puncte start -> "))
        points = startPoints
        print("Punctele au fost setate!\nAlegeti user start [ 1 == PC || 2 == USER]")
        alegDebug = input("-> ")
        if alegDebug == "1":
            pcTurn()
        elif alegDebug == "2":
            userTurn()
    else:
        print("Selectie invalida!")

def game(): # functia care alege cine incepe jocul random
    startUser = rand.randint(0,1)
    if startUser == 1:
        clear()
        print("AI-ul va incepe jocul!")
        time.sleep(1.5)
        clear()
        pcTurn()
    else:
        clear()
        print("Dvs. incepeti jocul!")
        time.sleep(1.5)
        clear()
        userTurn()

def userTurn(): # functie play PC
    global points
    print("Este randul dumneavoastra!")
    print("Adaugati puncte! Un numar de puncte intr-e 1 si 5")
    pointsAdd = int(input("-> ")) # adaugam un numar 
    while  pointsAdd > 5: # verifica ca numarul sa fie in  1 - 5
       print("Invalid, numarul de puncte trebuie sa fie intr-e 1 si 5!")
       pointsAdd = int(input("-> "))
      
    points = points + pointsAdd # aduna punctele puse
        

    print("Ati introdus ", pointsAdd, " puncte, suma punctelor este: ", points)
    if points >= 20:
        print("Ai ajuns primul la 20 si ai castigat jocul!") 
    else:
        print("\nApasati ORICE tasta pentru a CONTINUA!")
        wait()
        clear()
        pcTurn()

def pcTurn():
    """ 
    Functia PC-ului unde am incercat sa fac PC-ul mai bun decat un random

    Am incercat sa sporesc sansele de castig ale calculatorului gandind astfel:

    Daca user-ul pune 10
    PC pune maxim random 1, 4

    Daca userul pune 11
    PC pune maxim random 1, 3

    Pana la 13, unde PC pune maxim 1, lasand astfel toleranta necesara pentru a castigat la urmatoara runda

    Am facut asta pentru a lasa si user-ul sa castige
    """

    global points
    print("Este randul PC-ului!")
    if points <= 9:
        pointsAdd = rand.randint(1,5)
        points = points + pointsAdd
    elif points <= 10:
        pointsAdd = rand.randint(1,4)
        points = points + pointsAdd
    elif points <=11:
       pointsAdd = rand.randint(1,3)
       points = points + pointsAdd
    elif points <=12:
       pointsAdd = rand.randint(1,2)
       points = points + pointsAdd
    elif points <=13:
       pointsAdd = rand.randint(1,1)
       points = points + pointsAdd
    elif points > 13:
        pointsAdd = rand.randint(1,5)
        points = points + pointsAdd
    print("PC-ul a adaugat! Suma punctelor este acum: ", points)
    if points >= 20:
        print("Calculatorul a ajuns primul la 20 puncte si a castigat!")
    else:
        print("\nApasati ORICE tasta pentru a CONTINUA!")
        wait()
        clear()
        userTurn()


# main
menu()