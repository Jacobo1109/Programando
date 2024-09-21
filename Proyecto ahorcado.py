import random
def ahorcado():
    won = 0 
    lives = 6
    guessed = []
    words = ["basketball","volleyball","futball","soccer","tennis","padel","squash","natacion","baile","ajedrez","esgrima", "equitacion","polo","clavados","atletismo","gimnasia","badminton","pingpong","boxeo","taekwondo","surf","ciclismo","criquet","patinaje","waterpolo","rugby",]

    chosen_word = random.choice(words)

    print("\nLa palabra tiene",len(chosen_word),"letras")

    for letter in chosen_word:
      guessed.append("_")

    while won == 0:
      guess = input("\nAdivina una letra: ").lower()

      for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
          guessed[position] = letter
      print(guessed)

      if "_" not in guessed:
        won = 1
        print("Ganaste!")

      if guess not in chosen_word:
        lives -= 1
        if lives == 0:
          won = 1
          print("Perdiste!")

      print(lives)

    print("La palabra era:",chosen_word,"!")
def CasoPrueba():
    won = 0 
    lives = 6
    guessed = []
    words = ["basketball","volleyball","futball","soccer","tennis","padel","squash","natacion","baile","ajedrez","esgrima", "equitacion","polo","clavados","atletismo","gimnasia","badminton","pingpong","boxeo","taekwondo","surf","ciclismo","criquet","patinaje","waterpolo","rugby",]

    chosen_word = random.choice(words)

    print("\nLa palabra tiene",len(chosen_word),"letras")

    for letter in chosen_word:
      guessed.append("_")
      
      letters = set(chosen_word)
      
      abc = list('abcdefghijklmnopqrstuvwxyz')
      
      random.shuffle(abc)

    while won == 0:
      guess = abc.pop()
      print("\n palabra addivinada:")

      for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
          guessed[position] = letter
      print("Progreso",guessed)

      if "_" not in guessed:
        won = 1
        print("Ganaste!")

      if guess not in chosen_word:
        lives -= 1
        if lives == 0:
          won = 1
          print("Perdiste!")

      print(lives)

    print("La palabra era:",chosen_word,"!")
def menu():
    print("\n1 Jugar ahorcado")
    print("2 Caso Prueba")
    print("3 Salir")
def main():
    continuar = True
    while continuar:
        menu()
        opcion = str(input("\nFavor de Introducir una opción:"))
        if opcion == '1':
            print("\nBienvenido a Ahorcado")
            ahorcado()
        elif opcion == '2':
            CasoPrueba()
        elif opcion == '3':
            print("\nGracias por jugar Ahorcado")
            continuar = False
        else:
            print("\nFavor de ingresar una opción válida")
main()
            