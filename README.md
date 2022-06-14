# UTN-FRC-BLACKJACK1
Juego de cartas

Al inicio del juego se debe solicitar al jugador su nombre y que indique el monto que desea tener de pozo para poder
jugar al Blackjack, no pudiendo ser este monto mayor a $100000. Y luego se pide implementar un programa controlado por
#menu de opciones en el que las opciones sean:

1-Apostar
2-Jugar una Mano
3-Salir

Apostar: En esta opción del menú el jugador puede sumar dinero a su pozo. El valor a sumar no puede ser negativo ni cero.
Puede volver a esta opción del menú las veces que quiera.

Jugar una Mano: En esta opción del menú se debe realizar el juego tanto del jugador como del crupier. Inicialmente debe
definir el monto a apostar por la mano. Si el jugador no tuviera suficiente dinero para realizar una apuesta, no podrá
jugar, pero el programa no finaliza porque tiene la opción de apostar en el menú principal. La apuesta debe ser múltiplo
de 5 y menor o igual al dinero que posee en su pozo. Las reglas nuevas que aplican en este práctico son (Sin Split ni
Rendición, para quienes averiguen del juego):

El jugador recibe dos cartas inicialmente y a partir de ese momento puede seguir pidiendo cartas hasta que decida frenar
o bien logre 21 o se pase.
El valor del AS no es fijo. Cuando el jugador o el crupier lo recibe puede sumar 11 mientras no pase de 21. Si siguiera
pidiendo cartas y se pasara, el valor del AS vuelve a 1.
El crupier inicialmente recibe una carta que se muestra junto con las dos primeras cartas del jugador. Su juego continúa
cuando el jugador termina. Debe pedir cartas mientras tenga 16 o menos de puntaje y plantarse con 17 o más, siendo
indefinida la cantidad de cartas hasta lograrlo.
El blackjack natural le gana a un blackjack conseguido con 3 cartas o más.
El ganador de la partida es quien logra 21 o el valor más próximo sin pasarse. Las posibles opciones son:
Gana el jugador: Recibe el doble de su apuesta. (si tenía 10 y apostó 5, queda con 15).
Pierde el jugador: En esta ocasión no pueden perder ambos. Si el jugador pierde y el crupier también, gana el crupier.
(si tenía 10 y apostó 5, queda con 5).
Empatan: Si tanto el jugador como el crupier obtienen el mismo puntaje (21 o menos) entonces el jugador recibe su
apuesta. (si tenía 10 y apostó 5, queda con 10).

Salir: Cuando el usuario elige esta opción se debe mostrar su pozo actualizado.

