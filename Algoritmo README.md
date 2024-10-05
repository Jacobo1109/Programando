# Juego Ahorcado
El Juego de ahorcado consta de tratar de adivinar una palabra con el menor número de intentos que se sean posibles. Al inicio del juego únicamente apareceran rayas las cuales indican la cantidad de letras que contiene la palabra. El usuario tendrá que ir adivinando letra por letra tratando de formar la palabra; cada vez que el usuario se equivoque la horca se va a ir dibujando (Cada vez que falle el usuario se le va a dibujar una ectremidad al muñeco). El objetivo principal es adivinar la palabra antes de que se termine de dibujar al ahorcado lo cuál si se llega a acompletar significaría que perdiste.

Se le solicitará al usuario su nombre para iniciar el juego, después se le explicaran las reglas y se le presentarán los guiones enseñando la cantidad de letras que contiene la palabra y presentando únicamente la primera y última letra; a la vez que se les presenta esto también se le pedirá al usuario que trate de ir adivinando la palabra al insertar una letra por turno, si la letra se encuentra dentro de la palabra entonces ésta aparecerá, de lo contrario entonces se irá dibujando el muñeco del ahorcado. Así continuará el Usuario hasta que logre adivinar la palabra lo cuál significaría que ganó el juego o que se termine el dibujo del ahorcado lo cuál significaría que lamentablemente el jugador no pudo encontrar la palabra.

# ¿Porque?
La razón por la que decidí hacer este trabajo es debido a que este es un juego muy divertido para los usuarios y que también te puede apoyar para expandir y verificar tus conocimientos generales sobre palabras. Siento que también es una forma demasiado interesante de poder mostrarme todas las herramientas que he logrado aprender a lo largo de la programación y poner todos mis conocimientos en práctica.

# Algoritmo

Entrada 1.- Opción para la función que el usuario quiera utilizar (jugar ahorcado, caso prueba, salir) 2.- Letras (Intentando adivinar la palabra)


Proceso 1.-Solicitar el nombre del usuario. 

2.-Importar la librería random para que de la lista se escojan palabras de forma aleatorio 

3.-Enseñar anuncio introduciendo al usuario al juego de Ahorcado 

4.-Imprimir el mástil del ahorcado. 

5.-Imprimir la palabra de forma oculta 

6.-Solicitar al usuario que inserte letras con la finalidad de adivinar la palabra oculta. 

7.-Seguir así hasta que se complete la palabra (Ganó) o el ahorcado (Perdió). 

8.-Definir una lista con ciertas palabras y que al iniciar el juego se escoja una de esas palabras de forma aleatoria. 

9.-Para el caso prueba definir una lista con el abecedario para que de forma automática se vayan completando de forma aleatoria usando la lista del abecedario. 

10.-Utilizar herramientas para que cada vez que el usuario ponga una letra si es correcta demuestre la letra en el ahorcado y que de lo contrario aumente rallas al ahorcado.


Salida 1.-Ganar: La palabra (De haber sido descubierta) 

2.-Perder: Al ahorcado (De no haber podido descifrar la palabra)
