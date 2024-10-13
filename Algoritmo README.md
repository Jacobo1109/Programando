# Juego Ahorcado
El Juego de ahorcado consta de tratar de adivinar una palabra con el menor número de intentos que se sean posibles. Al inicio del juego únicamente apareceran rayas las cuales indican la cantidad de letras que contiene la palabra. El usuario tendrá que ir adivinando letra por letra tratando de formar la palabra; cada vez que el usuario se equivoque la horca se va a ir dibujando (Cada vez que falle el usuario se le va a dibujar una ectremidad al muñeco). El objetivo principal es adivinar la palabra antes de que se termine de dibujar al ahorcado lo cuál si se llega a acompletar significaría que perdiste.

Se le solicitará al usuario su nombre para iniciar el juego, después se le explicaran las reglas y se le presentarán los guiones enseñando la cantidad de letras que contiene la palabra y presentando únicamente la primera y última letra; a la vez que se les presenta esto también se le pedirá al usuario que trate de ir adivinando la palabra al insertar una letra por turno, si la letra se encuentra dentro de la palabra entonces ésta aparecerá, de lo contrario entonces se irá dibujando el muñeco del ahorcado. Así continuará el Usuario hasta que logre adivinar la palabra lo cuál significaría que ganó el juego o que se termine el dibujo del ahorcado lo cuál significaría que lamentablemente el jugador no pudo encontrar la palabra.

# ¿Porque?
La razón por la que decidí hacer este trabajo es debido a que este es un juego muy divertido para los usuarios y que también te puede apoyar para expandir y verificar tus conocimientos generales sobre palabras. Siento que también es una forma demasiado interesante de poder mostrarme todas las herramientas que he logrado aprender a lo largo de la programación y poner todos mis conocimientos en práctica.

# ¿Cómo funciona?
El código se conforma del uso de diferentes reglas, condiciones, etc. tal como el uso de ciclos while, ciclos for, if, funciones, strings, archivos, etc. Cada de los temas mencionados fue vital para la elaboración de este juego, 

# Instrucciones
El usuario deberá tener Python o Thonny instalado en su computadora. A la hora de correr el programa, l usuario le van a aparecer 4 opciones en el menú, la primera opción es para que el usuario juegue ahorcado, para que pase esto el jugador deberá poner el número 1 y entonces ya podrá empezar a adivinar la palabra que fue seleccionada al insertar la letra que cree que está en la palabra, a la hora de terminar sin importar si ganó o perdió se le va a poner el menú nuevamente. Si el usuario quiere un ejemplo de como funciona el juego entonces deberá poner el número 2 y con eso la computadora jugará por si sola al ahorcado, si el usuario ya terminó con el uso del programa entonces deberá insertar el número 3, y si desea ver las palabras que se están utilizando entonces deberá insertar el número 4 y se imprimirán todas las palabras del archivo. Si no tienen Thonny para poder correr el programa favor de visualizar el siguiente video: https://www.youtube.com/watch?v=JQwsIhsnoiA&pp=ygUVQ29tbyBkZXNjYXJnYXIgdGhvbm55

# Algoritmo

Entrada 1.- Opción para la función que el usuario quiera utilizar (jugar ahorcado, caso prueba, salir) 2.- Letras (Intentando adivinar la palabra)


Proceso 1.-Solicitar el nombre del usuario. 

2.-Importar la librería random para que de la lista se escojan palabras de forma aleatorio 

3.-Generar función de archivos

4.-Crear un nuevo archivo para las palabras del ahorcado

5.-Introducir en el nuevo archivo las palabras que se van a utilizar

6.-Enseñar anuncio introduciendo al usuario al juego de Ahorcado 

7.-Imprimir el mástil del ahorcado. 

8.-Imprimir la palabra de forma oculta 

9.-Solicitar al usuario que inserte letras con la finalidad de adivinar la palabra oculta. 

10.-Seguir así hasta que se complete la palabra (Ganó) o el ahorcado (Perdió). 

11.-Definir una lista con ciertas palabras y que al iniciar el juego se escoja una de esas palabras de forma aleatoria. 

12.-Para el caso prueba definir una lista con el abecedario para que de forma automática se vayan completando de forma aleatoria usando la lista del abecedario. 

13.-Utilizar herramientas para que cada vez que el usuario ponga una letra si es correcta demuestre la letra en el ahorcado y que de lo contrario aumente rallas al ahorcado.


Salida 1.-Ganar: La palabra (De haber sido descubierta) 

2.-Perder: Al ahorcado (De no haber podido descifrar la palabra)

3.-En el caso prueba las palabras que hace la computadora y el resultado de si gana o pierde

4.-Si selecciona archivos entonces imprimirá todas las palabras del archivo

# Temas
1.	Ciclo while – El ciclo while es utilizado principalmente en este código para establecer la condición que mientras que la variable won no sea igual a cero entonces se va a repetir preguntándole al usuario que adivine la palabra letra por letra, dentro de todo esto ponemos que las vidas se van a ir bajando y se seguirá repitiendo el código hasta un punto en el que se llegue a cero.


2.	Strings – Los strings en lo particular están utilizados para que el usuario adivine la palabra, están utilizados para la entrada del jugador que es la letra que está adivinando y particularmente también están siendo utilizados en los dibujos del ahorcado ya que estos son strings, también la parte de los mensajes hacia el usuario son strings.


3.	Listas – El mayor uso de las listas es para las “imágenes” o dibujos que se están utilizando del ahorcado, estos a lo largo  del código están programados para que se desplieguen cada vez que el usuario falla alguna letra, para cuando el usuario gane o pierda.


4.	Ciclos for – El uso más importante que tiene el ciclo for en el código es que esta va a comparar la letra ingresada por el usuario y las letras que están faltando en la palabra, el for también es utilizado para que se cambie la cantidad de letras por “_”, y por último el ciclo for también es utilizado para que pueda mostrar el progreso que el usuario lleva a lo largo del juego. 


5.	Archivos – Los archivos están utilizados para crear la lista de palabras que se va a utilizar a lo largo del juego, mediante este archivo podremos escoger una palabra del documento de forma aleatoria con el import random y así que si en cierto futuro se le quiera añadir palabras entonces se pueda.


6.	Funciones – El programa está desarrollado por varias funciones, tales como la del archivo, la del juego del ahorcado, la del caso prueba, la del menú y el main, cana función tiene su objetivos a cumplir y su propósito para que se ejecute a lo largo del programa.

# Espero que disfruten el juego :)
