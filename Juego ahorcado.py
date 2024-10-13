import random
def archivos():
    file = open("words.txt", "w+")
    words = ["basketball\n", "volleyball\n", "futball\n", "soccer\n", "tennis\n", "beisbol\n", "padel\n", "squash\n", "natacion\n", "baile\n", "ajedrez\n", "esgrima\n", "equitacion\n", "polo\n", "clavados\n", "atletismo\n", "gimnasia\n", "badminton\n", "pingpong\n", "boxeo\n", "taekwondo\n", "surf\n", "ciclismo\n", "criquet\n", "patinaje\n", "waterpolo\n", "kayak\n", "rugby\n", "criquet\n", "mma\n", "esqui\n", "americano\n", "balonmano\n", "netball\n", "cheerleading\n", "softball\n", "canotaje\n", "bmx\n", "parkour\n", "capoeira\n", "kickboxing\n", "bolos\n", "billar\n", "skateboarding\n", "motocross\n", "snowboard\n", "judo\n", "karate\n", "triatlon\n", "remo\n", "paracaidismo\n", "paintball\n"]
    file.writelines(words)
    file.seek(0)
    contenido = file.read()
    print(contenido)
    file.close()
def ahorcado():
    file = open("words.txt", "r")
    won = 0
    lives = 6
    guessed = []    
    ahorcado_dibujo = ['''
       +---+
       |   |
           |
           |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
           |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
       |   |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     _______
       ''']
    
    lost = ('''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     _______
       ''')

    w = ('''
       O   
      /|\  
      / \ 
     ''')
    words = file.readlines()
    chosen_word = random.choice(words).strip()
    print("\nLa palabra tiene", len(chosen_word), "letras")
    for letter in chosen_word:
        guessed.append("_")
    while won == 0:
        guess = input("\nAdivina una letra: ").lower()
        if guess not in chosen_word:
            lives -= 1
            print(ahorcado_dibujo[6 - lives - 1])
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                guessed[position] = letter        
        print("Progreso:", guessed)
        if "_" not in guessed:
            won = 1
            print("¡Ganaste!", w)
        if lives == 0:
            won = 1
            print("¡Perdiste!", lost)
            print("La palabra era:", chosen_word, "!")
        print("Vidas restantes:", lives)
    file.close()
def CasoPrueba():
    file = open("words.txt", "r")
    won = 0 
    lives = 6
    guessed = []    
    ahorcado_dibujo = ['''
       +---+
       |   |
           |
           |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
           |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
       |   |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     _______
       ''',
                       '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     _______
       ''']
    
    lost = ('''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     _______
       ''')

    w = ('''
       O   
      /|\  
      / \ 
     ''')
    words = file.readlines()
    chosen_word = random.choice(words).strip()
    print("\nLa palabra tiene", len(chosen_word), "letras")
    for letter in chosen_word:
        guessed.append("_")      
    abc = list('abcdefghijklmnopqrstuvwxyz')      
    random.shuffle(abc)
    while won == 0:
        guess = abc.pop()
        print("\nLetra adivinada:", guess)
        if guess not in chosen_word:
            lives -= 1
            print(ahorcado_dibujo[6 - lives - 1])
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                guessed[position] = letter      
        print("Progreso:", guessed)
        if "_" not in guessed:
            won = 1
            print("¡Ganaste!", w)
        if lives == 0:
            won = 1
            print("¡Perdiste!", lost)
            print("La palabra era:", chosen_word, "!")
        print("Vidas restantes:", lives)
    file.close()
def menu():
    print("\n1 Jugar ahorcado")
    print("2 Caso Prueba")
    print("3 Salir")
    print("4 Archivos")
def main():
    continuar = True
    while continuar:
        menu()
        opcion = str(input("\nFavor de Introducir una opción:"))
        if opcion == '1':
            print("\nBienvenido a Ahorcado")
            print("\n¡¡¡La temática es deportes!!!")
            ahorcado()
        elif opcion == '2':
            CasoPrueba()
        elif opcion == '3':
            print("\nGracias por jugar Ahorcado")
            continuar = False
        elif opcion == '4':
            archivos()
        else:
            print("\nFavor de ingresar una opción válida")
main()
