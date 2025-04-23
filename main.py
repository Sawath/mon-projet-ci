import random 
def devinette():
    choix = random.randint(0, 100)
    reponse = ""
    while True:
        nombre = int(input("Déviner ce nombre "))
        if nombre > choix :
          reponse = ("Trop grand")
          print({reponse})
        elif nombre < choix :
          reponse = ("Trop petit")
          print({reponse})
        else:
          reponse =("Exact")
          print({reponse})
          break
    
devinette()
